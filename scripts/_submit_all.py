#!/usr/bin/env python3
"""批量提交所有NQ题目的C++和Python代码到localhost OJ，验证AC"""
import json, time, requests, os
from pathlib import Path

BOOK = Path(__file__).parent.parent
nq_map = json.loads((BOOK / "scripts/nq_mapping.json").read_text())
oj_ids = json.loads(Path("/tmp/nq_oj_ids.json").read_text())

s = requests.Session()
s.headers.update({"Content-Type": "application/json"})

# Collect all problems to submit
tasks = []
for nq_id, info in sorted(nq_map.items(), key=lambda x: (x[1]["ch"], x[1]["idx"])):
    ch = info["ch"]
    if nq_id not in oj_ids:
        continue
    bank = BOOK / f"chapter{ch}_bank"
    # Find NQ dir
    nq_dir = None
    for d in bank.iterdir():
        if d.is_dir() and d.name.startswith(nq_id):
            nq_dir = d
            break
    if not nq_dir:
        continue
    cpp_file = nq_dir / "Andy.cpp"
    py_file = nq_dir / "Andy.py"
    if cpp_file.exists() and py_file.exists():
        tasks.append({
            "nq_id": nq_id,
            "ch": ch,
            "oj_id": oj_ids[nq_id],
            "cpp": cpp_file.read_text(encoding="utf-8"),
            "py": py_file.read_text(encoding="utf-8"),
        })

print(f"准备提交 {len(tasks)} 题")

# Submit C++ first
print("\n--- 提交 C++ ---")
subs = {}  # sub_id -> {"nq_id": ..., "lang": ...}
for t in tasks:
    try:
        r = s.post("http://localhost/api/submission", json={
            "problem_id": t["oj_id"],
            "code": t["cpp"],
            "language": "C++",
            "contest_id": 356,
        }, timeout=10)
        d = r.json()
        if not d.get("error"):
            sub_id = d.get("data", {}).get("submission_id", "")
            if sub_id:
                subs[sub_id] = {"nq_id": t["nq_id"], "lang": "C++", "ch": t["ch"]}
                print(f"  C++ {t['nq_id']} -> {sub_id}")
    except Exception as e:
        print(f"  ❌ C++ {t['nq_id']}: {e}")

print(f"Submitted {len(subs)} C++")

# Poll C++ results
print("\n--- 等待 C++ 判题 ---")
cpp_results = {}
for attempt in range(30):
    pending = [sid for sid, info in subs.items() if sid not in cpp_results]
    if not pending:
        break
    time.sleep(3)
    for sub_id in pending[:20]:  # Check 20 per batch
        try:
            r = s.get(f"http://localhost/api/submission?id={sub_id}", timeout=5)
            d = r.json()
            result = d.get("data", {}).get("result", -2)
            if result != -1:
                info = subs[sub_id]
                status = "AC" if result == 0 else f"err={result}"
                cpp_results[sub_id] = status
                print(f"  C++ {info['nq_id']}: {status}")
        except:
            pass

# Check remaining
for sub_id in pending:
    info = subs[sub_id]
    cpp_results[sub_id] = "timeout"
    print(f"  C++ {info['nq_id']}: TIMEOUT")

# Submit Python
print("\n--- 提交 Python ---")
py_subs = {}
for t in tasks:
    try:
        r = s.post("http://localhost/api/submission", json={
            "problem_id": t["oj_id"],
            "code": t["py"],
            "language": "Python3",
            "contest_id": 356,
        }, timeout=10)
        d = r.json()
        if not d.get("error"):
            sub_id = d.get("data", {}).get("submission_id", "")
            if sub_id:
                py_subs[sub_id] = {"nq_id": t["nq_id"], "lang": "Python3", "ch": t["ch"]}
                print(f"  Py {t['nq_id']} -> {sub_id}")
    except Exception as e:
        print(f"  ❌ Py {t['nq_id']}: {e}")

print(f"Submitted {len(py_subs)} Python")

# Poll Python results
print("\n--- 等待 Python 判题 ---")
py_results = {}
for attempt in range(30):
    pending = [sid for sid, info in py_subs.items() if sid not in py_results]
    if not pending:
        break
    time.sleep(3)
    for sub_id in pending[:20]:
        try:
            r = s.get(f"http://localhost/api/submission?id={sub_id}", timeout=5)
            d = r.json()
            result = d.get("data", {}).get("result", -2)
            if result != -1:
                info = py_subs[sub_id]
                status = "AC" if result == 0 else f"err={result}"
                py_results[sub_id] = status
                print(f"  Py {info['nq_id']}: {status}")
        except:
            pass

# Final report
print(f"\n{'='*60}")
print(f"📊 验证报告")
print(f"{'='*60}")

nq_status = {}
for sub_id, info in subs.items():
    nq_status[info["nq_id"]] = {"cpp": cpp_results.get(sub_id, "?")}
for sub_id, info in py_subs.items():
    if info["nq_id"] not in nq_status:
        nq_status[info["nq_id"]] = {}
    nq_status[info["nq_id"]]["py"] = py_results.get(sub_id, "?")

ac_both = 0
ac_cpp = 0
ac_py = 0
failed = []

for nq_id in sorted(nq_status.keys()):
    s = nq_status[nq_id]
    cpp = s.get("cpp", "?")
    py = s.get("py", "?")
    if cpp == "AC":
        ac_cpp += 1
    if py == "AC":
        ac_py += 1
    if cpp == "AC" and py == "AC":
        ac_both += 1
    else:
        failed.append((nq_id, cpp, py))

total = len(nq_status)
print(f"总题数: {total}")
print(f"C++ AC: {ac_cpp}/{total}")
print(f"Python AC: {ac_py}/{total}")
print(f"双AC: {ac_both}/{total}")

if failed:
    print(f"\n❌ 未通过 ({len(failed)}题):")
    for nq_id, cpp, py in failed:
        print(f"  {nq_id}: C++={cpp} Py={py}")
else:
    print(f"\n🎉 全部通过！")

# Save report
report = {"total": total, "ac_both": ac_both, "ac_cpp": ac_cpp, "ac_py": ac_py, "failed": failed}
with open(BOOK / "scripts/submission_report.json", "w") as f:
    json.dump(report, f, ensure_ascii=False, indent=2)
print(f"\n报告: scripts/submission_report.json")
