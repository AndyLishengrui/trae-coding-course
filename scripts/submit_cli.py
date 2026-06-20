#!/usr/bin/env python3
"""
本地OJ提交验证CLI — 通过 docker exec + Django ORM 直接提交判题

用法:
  python3 submit_cli.py --nq NQ1-01 --lang cpp   # 单题C++
  python3 submit_cli.py --chapter 1               # 第1章全部
  python3 submit_cli.py --all --lang cpp          # 全部161题C++
"""
import json, sys, time, subprocess, uuid
from pathlib import Path

BOOK = Path(__file__).parent.parent
SCRIPTS = Path(__file__).parent


def load_json(name):
    return json.loads((SCRIPTS / name).read_text())


def get_oj_ids() -> dict:
    r = subprocess.run(
        ["docker", "exec", "onlinejudgedeploy-oj-backend-1",
         "python", "manage.py", "shell", "-c",
         "from problem.models import Problem; import json; "
         "probs = Problem.objects.filter(_id__startswith='NQ'); "
         "print(json.dumps({p._id: p.id for p in probs}))"],
        capture_output=True, text=True, timeout=15
    )
    for line in r.stdout.strip().split("\n"):
        if line.startswith("{"):
            return json.loads(line)
    return {}


def submit_one(nq_id: str, oj_id: int, code_text: str, lang: str) -> dict:
    """提交代码并等判题结果。先把代码写入容器文件，再读文件提交，避免转义问题。"""
    sub_id = "cli_" + uuid.uuid4().hex[:12]
    code_file = "/tmp/submit_{}.txt".format(sub_id)

    # Step 1: Write code to file in container using Python
    code_json = json.dumps(code_text)
    write_cmd = (
        "with open('{}','w',encoding='utf-8') as f: f.write({})".format(code_file, code_json)
    )
    subprocess.run(
        ["docker", "exec", "onlinejudgedeploy-oj-backend-1",
         "python", "manage.py", "shell", "-c", write_cmd],
        capture_output=True, text=True, timeout=10
    )

    # Step 2: Submit via Django ORM (create + trigger judge)
    dj = """\
from submission.models import Submission
from problem.models import Problem
from account.models import User
from judge.tasks import judge_task

user = User.objects.get(username='andy')
p = Problem.objects.get(id={oj_id})

with open('{code_file}', 'r', encoding='utf-8') as f:
    code = f.read()

sub = Submission.objects.create(
    id='{sub_id}',
    user_id=user.id, username=user.username,
    language='{lang}', code=code,
    problem_id=p.id, contest_id=356,
    ip='127.0.0.1', result=-1
)
judge_task.send(sub.id, p.id)
""".format(oj_id=oj_id, code_file=code_file, sub_id=sub_id, lang=lang)

    subprocess.run(
        ["docker", "exec", "-i", "onlinejudgedeploy-oj-backend-1",
         "sh", "-c", "cd /app && python manage.py shell"],
        input=dj, capture_output=True, text=True, timeout=30
    )

    # Clean up code file
    subprocess.run(
        ["docker", "exec", "onlinejudgedeploy-oj-backend-1",
         "python", "manage.py", "shell", "-c",
         "import os; os.remove('{}') if os.path.exists('{}') else None".format(code_file, code_file)],
        capture_output=True, text=True, timeout=5
    )

    # Step 3: Poll database directly for result (no stdout parsing)
    poll = (
        "from submission.models import Submission; import time;"
        "s=Submission.objects.get(id='{sub_id}');"
        "for i in range(120):"
        "    time.sleep(1); s.refresh_from_db();"
        "    if s.result != -1:"
        "        print('OK:' + str(s.result) + ':' + str((s.statistic_info or {{}}).get('time_cost',0)));"
        "        break;"
        "else:"
        "    s.refresh_from_db();"
        "    print('OK:' + str(s.result) + ':0')"
    ).format(sub_id=sub_id)

    r = subprocess.run(
        ["docker", "exec", "onlinejudgedeploy-oj-backend-1",
         "python", "manage.py", "shell", "-c", poll],
        capture_output=True, text=True, timeout=180
    )

    result = -9
    time_cost = 0
    for line in (r.stdout + "\n" + r.stderr).split("\n"):
        line = line.strip()
        if line.startswith("OK:"):
            parts = line[3:].split(":")
            try:
                result = int(parts[0])
                time_cost = int(parts[1]) if len(parts) > 1 else 0
            except ValueError:
                pass

    if result == -9:
        # Fallback: direct DB query
        r2 = subprocess.run(
            ["docker", "exec", "onlinejudgedeploy-oj-backend-1",
             "python", "manage.py", "shell", "-c",
             "from submission.models import Submission; s=Submission.objects.get(id='{}'); print(s.result)".format(sub_id)],
            capture_output=True, text=True, timeout=10
        )
        for line in r2.stdout.split("\n"):
            line = line.strip()
            if line.lstrip("-").isdigit():
                result = int(line)
                break

    status_map = {0: "AC", -1: "PENDING", 1: "WA", 2: "TLE", 3: "MLE", 4: "RE", 5: "SE", 6: "CE", 7: "OLE"}
    status = status_map.get(result, "ERR({})".format(result))

    return {"nq_id": nq_id, "lang": lang, "result": status, "time_ms": time_cost}


def main():
    import argparse
    parser = argparse.ArgumentParser(description="本地OJ提交验证CLI")
    parser.add_argument("--chapter", "-c", type=int)
    parser.add_argument("--nq")
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--lang", choices=["cpp", "py", "both"], default="both")
    args = parser.parse_args()

    langs = []
    if args.lang in ("cpp", "both"):
        langs.append("C++")
    if args.lang in ("py", "both"):
        langs.append("Python3")

    nq_map = load_json("nq_mapping.json")
    oj_ids = get_oj_ids()
    print("OJ: {} NQ problems".format(len(oj_ids)))

    tasks = []

    def add_chapter(ch):
        bank = BOOK / "chapter{}_bank".format(ch)
        for nq_id, info in sorted(nq_map.items(), key=lambda x: (x[1]["ch"], x[1]["idx"])):
            if info["ch"] != ch:
                continue
            nq_dir = None
            for d in bank.iterdir():
                if d.is_dir() and d.name.startswith(nq_id):
                    nq_dir = d
                    break
            if not nq_dir:
                continue
            oj_id = oj_ids.get(nq_id, 0)
            if not oj_id:
                continue
            for lang in langs:
                ext = "cpp" if lang == "C++" else "py"
                fpath = nq_dir / "Andy.{}".format(ext)
                if fpath.exists():
                    tasks.append({"nq_id": nq_id, "ch": ch, "lang": lang,
                                  "oj_id": oj_id, "code": fpath.read_text(encoding="utf-8")})

    if args.nq:
        info = nq_map.get(args.nq)
        if not info:
            print("Unknown NQ:", args.nq)
            return
        add_chapter(info["ch"])
        tasks = [t for t in tasks if t["nq_id"] == args.nq]
    elif args.chapter:
        add_chapter(args.chapter)
    elif args.all:
        for ch in range(1, 17):
            add_chapter(ch)
    else:
        parser.print_help()
        return

    print("Tasks:", len(tasks))

    results = []
    for i, t in enumerate(tasks, 1):
        print("[{}/{}] {} {} ...".format(i, len(tasks), t["nq_id"], t["lang"]), end=" ", flush=True)
        r = submit_one(t["nq_id"], t["oj_id"], t["code"], t["lang"])
        icon = "OK" if r["result"] == "AC" else "!!"
        print("{} {}".format(icon, r["result"]))
        results.append(r)

    total = len(results)
    ac = sum(1 for r in results if r["result"] == "AC")
    cpp_ac = sum(1 for r in results if "C++" in r["lang"] and r["result"] == "AC")
    py_ac = sum(1 for r in results if "Python" in r["lang"] and r["result"] == "AC")
    cpp_total = sum(1 for r in results if "C++" in r["lang"])
    py_total = sum(1 for r in results if "Python" in r["lang"])

    print("\n" + "="*50)
    print("C++ AC: {}/{} | Py AC: {}/{}\nTotal: {}/{}".format(cpp_ac, cpp_total or 1, py_ac, py_total or 1, ac, total))

    failed = [r for r in results if r["result"] != "AC"]
    if failed:
        print("\nFailed ({}):".format(len(failed)))
        for r in failed[:20]:
            print("  {} {}: {}".format(r["nq_id"], r["lang"], r["result"]))
    else:
        print("\nAll AC!")

    (SCRIPTS / "submission_report.json").write_text(json.dumps(results, ensure_ascii=False, indent=2))
    print("\nReport: scripts/submission_report.json")


if __name__ == "__main__":
    main()
