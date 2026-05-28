#!/usr/bin/env python3
"""
南强百练题库 三一致同步工具链
==============================
1. 根据 nq_mapping.json 找到原ACW题目
2. 克隆测试数据 → 创建NQ题目（题面来自教材chapter_print.html）
3. C++/Python 双重验证
4. 加入"南强百练题库"实验(Contest #354)

用法:
  python scripts/sync_nq_bank.py                    # 全部161题
  python scripts/sync_nq_bank.py --chapter 1         # 只同步第1章
  python scripts/sync_nq_bank.py --dry-run           # 预览
  python scripts/sync_nq_bank.py --validate-only     # 只验证不创建
  python scripts/sync_nq_bank.py --force             # 强制覆盖
"""
import sys, os, re, json, time, subprocess, requests
from pathlib import Path

BOOK = Path(__file__).parent.parent.resolve()
TEXTBOOK = BOOK / "textbook"
CONTEST_ID = 354
TOKEN = "63310cdaec0bc93b08f856568e125e75"

# ---- OJ Client ----
class OJ:
    def __init__(self):
        self.s = requests.Session()
        self.s.headers.update({"Authorization": f"Bearer {TOKEN}"})

    def _api(self, method, path, **kw):
        if "?" not in path:
            url = f"http://localhost/api/admin/{path}/"
        else:
            url = f"http://localhost/api/admin/{path}"
        r = self.s.request(method, url, **kw)
        d = r.json()
        if d.get("error"):
            raise Exception(str(d.get("data", "unknown"))[:200])
        return d.get("data", d)

    def get_problem(self, pid):
        return self._api("GET", f"problem?id={pid}")

    def find_nq(self, nq_id):
        """Check if NQ problem already exists (uses DB query for accuracy)."""
        import subprocess
        q = f"SELECT id, _id, title FROM problem WHERE _id = '{nq_id}' AND contest_id IS NULL LIMIT 1;"
        r = subprocess.run(['docker','exec','onlinejudgedeploy-oj-postgres-1','psql','-U','onlinejudge','-d','onlinejudge','-t','-A','-F','|','-c',q],
            capture_output=True, text=True)
        line = r.stdout.strip()
        if line and '|' in line:
            parts = line.split('|')
            if len(parts) >= 2 and parts[1] == nq_id:
                return {"id": int(parts[0]), "_id": parts[1], "title": parts[2] if len(parts)>2 else ""}
        return None

    def create_problem(self, data):
        return self._api("POST", "problem", json=data)

    def update_problem(self, data):
        return self._api("PUT", "problem", json=data)

    def download_tc(self, pid):
        r = self.s.get(f"http://localhost/api/admin/test_case/?problem_id={pid}", stream=True)
        if r.status_code == 200:
            return r.content
        raise Exception(f"HTTP {r.status_code}")

    def upload_tc(self, zip_bytes):
        r = self.s.post("http://localhost/api/admin/test_case/",
            data={"spj": "false"},
            files={"file": ("tc.zip", zip_bytes, "application/zip")})
        d = r.json()
        if d.get("error"):
            raise Exception(str(d.get("data", ""))[:200])
        return d["data"]["id"]

    def add_to_contest(self, problem_id, display_id):
        return self._api("POST", "contest/problem", json={
            "contest_id": CONTEST_ID,
            "problem_id": problem_id,
            "display_id": display_id,
        })

    def submit(self, problem_id, code, language):
        return self._api("POST", "submission", json={
            "problem_id": problem_id, "code": code, "language": language
        })

# ---- Textbook Description Extractor ----
def get_desc(html_path, acw_id):
    if not html_path.exists():
        return None
    html = html_path.read_text(encoding='utf-8')
    # Find problem block for this ACW
    pat = rf'AcWing {acw_id}.*?</div>\s*<div class="problem-desc">(.*?)</div>'
    m = re.search(pat, html, re.DOTALL)
    if not m: return None
    rest = html[m.start():]
    story = m.group(1).strip()
    def _extract(label, rest_text):
        p = rf'<span class="tag {label}">[^<]+</span></td><td class="spec-value">(.*?)</td>'
        mm = re.search(p, rest_text, re.DOTALL)
        return mm.group(1).strip() if mm else ""
    inp = _extract("in", rest)
    out = _extract("out", rest)
    lim = _extract("lim", rest)
    sin = re.search(r'<div class="col-label">输入</div><pre>(.*?)</pre>', rest, re.DOTALL)
    sout = re.search(r'<div class="col-label">输出</div><pre>(.*?)</pre>', rest, re.DOTALL)
    sample_in = sin.group(1).strip() if sin else ""
    sample_out = sout.group(1).strip() if sout else ""
    return {
        "description": story,
        "input_description": inp,
        "output_description": out,
        "hint": lim,
        "samples": [{"input": sample_in, "output": sample_out}],
    }

# ---- Code Finder ----
def find_code(acw_id, lang):
    fname = "Andy.cpp" if lang == "cpp" else "Andy.py"
    for ch in range(1, 17):
        bank = BOOK / f"chapter{ch}_bank"
        for d in bank.iterdir():
            if d.is_dir():
                for fmt in [f'ACW{acw_id:03d}', f'ACW{acw_id}.', f'ACW{acw_id}_']:
                    if fmt in d.name:
                        f = d / fname
                        if f.exists(): return f.read_text().strip()
    return None

# ---- Sync One Problem ----
def sync_one(oj, nq_id, info, html_path, force=False):
    ch, idx, acw, src_pid = info["ch"], info["idx"], info["acw"], info["pid"]

    # Get source problem for metadata
    src = oj.get_problem(src_pid)
    if not src: return {"status": "no_source"}

    # Get textbook description
    desc = get_desc(html_path, acw)
    if not desc: return {"status": "no_desc"}

    result = {"nq": nq_id, "acw": acw}

    # Download & re-upload test data
    try:
        tc_zip = oj.download_tc(src_pid)
        new_tc = oj.upload_tc(tc_zip)
    except Exception as e:
        result["status"] = f"tc_error: {e}"
        return result

    # Build problem data
    data = {
        "_id": nq_id,
        "title": src.get("title", f"Problem {acw}"),
        "description": desc["description"],
        "input_description": desc["input_description"],
        "output_description": desc["output_description"],
        "samples": desc["samples"],
        "hint": desc["hint"],
        "test_case_id": new_tc,
        "test_case_score": [{"input_name": f"{i}.in", "output_name": f"{i}.out", "score": 10} for i in range(1, 11)],
        "languages": ["C", "C++", "Python3"],
        "time_limit": max(src.get("time_limit", 1000), 2000),
        "memory_limit": src.get("memory_limit", 256),
        "difficulty": src.get("difficulty", "Low"),
        "visible": True,
        "rule_type": "OI",
        "total_score": 100,
        "source": "南强百练题库",
        "spj": False,
        "spj_language": "",
        "spj_code": "",
        "spj_version": "",
        "spj_compile_ok": False,
        "template": {},
        "io_mode": {"input": "input.txt", "output": "output.txt", "io_mode": "Standard IO"},
        "share_submission": False,
        "is_public": True,
        "tags": src.get("tags", ["基础语法"]),
    }

    # Create or update
    try:
        # Check if already exists
        existing = oj.find_nq(nq_id)

        if existing and not force:
            result["status"] = "skipped"
            result["problem_id"] = existing["id"]
            return result

        if existing:
            data["id"] = existing["id"]
            oj.update_problem(data)
            result["status"] = "updated"
        else:
            created = oj.create_problem(data)
            existing = created
            result["status"] = "created"

        pid = existing["id"]
        result["problem_id"] = pid

        # Add to contest
        try:
            oj.add_to_contest(pid, nq_id)
            result["contest"] = "ok"
        except Exception as e:
            if "already" in str(e).lower():
                result["contest"] = "already"
            else:
                result["contest"] = str(e)[:40]

    except Exception as e:
        result["status"] = f"error: {e}"
        return result

    return result

# ---- Validate Codes ----
def validate(oj, nq_id, acw, problem_id):
    v = {"nq": nq_id}
    for lang, oj_lang in [("cpp", "C++"), ("python", "Python3")]:
        code = find_code(acw, lang)
        if not code:
            v[lang] = "no_code"
            continue
        try:
            sub = oj.submit(problem_id, code, oj_lang)
            sid = sub.get("submission_id", sub.get("id"))
            for _ in range(20):
                time.sleep(1.5)
                st = oj.s.get(f"http://localhost/api/submission?id={sid}").json()
                st = st.get("data", st)
                r = st.get("result", -2)
                if r not in (-1, -2):
                    v[lang] = "AC" if r == 0 else f"F{r}"
                    break
            else:
                v[lang] = "timeout"
        except Exception as e:
            v[lang] = f"err:{str(e)[:20]}"
    return v

# ---- Main ----
def main():
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--chapter", "-c", type=int)
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--validate-only", action="store_true")
    p.add_argument("--force", action="store_true")
    p.add_argument("--validate-after", action="store_true", help="同步后验证C++/Python")
    args = p.parse_args()

    with open(BOOK / "scripts/nq_mapping.json") as f:
        all_map = json.load(f)

    oj = OJ()
    chapters = [args.chapter] if args.chapter else range(1, 17)
    summary = []

    for ch in chapters:
        html = TEXTBOOK / f"chapter{ch:02d}_print.html"
        items = [(nq, info) for nq, info in all_map.items() if info["ch"] == ch]
        items.sort(key=lambda x: x[1]["idx"])
        print(f"\n{'='*50}\n第{ch}章 ({len(items)}题)\n{'='*50}")

        for nq, info in items:
            if args.dry_run:
                print(f"  🔍 {nq} (ACW{info['acw']})")
                continue

            if args.validate_only:
                acw = info["acw"]
                pid = info.get("_oj_pid") or info["pid"]
                if not pid: continue
                v = validate(oj, nq, acw, pid)
                summary.append(v)
                icon = "✅" if v.get("cpp")=="AC" and v.get("python")=="AC" else "⚠️"
                print(f"  {icon} {nq}: C++={v.get('cpp')} Python={v.get('python')}")
                continue

            r = sync_one(oj, nq, info, html, force=args.force)
            summary.append(r)
            icon = {"created":"🆕","updated":"✏️","skipped":"⏭️"}.get(r["status"],"❌")
            print(f"  {icon} {nq} (ACW{info['acw']}): {r['status']}")

            time.sleep(0.2)

    created = sum(1 for r in summary if r.get("status") in ("created","updated"))
    print(f"\n同步: {created}/{len(summary)} 题 (Contest #{CONTEST_ID})")

    # Validation after sync
    if args.validate_after:
        print(f"\n{'='*50}\nC++ / Python 验证\n{'='*50}")
        cpp_ok = py_ok = 0
        for r in summary:
            pid = r.get("problem_id")
            if not pid: continue
            v = validate(oj, r["nq"], r["acw"], pid)
            cpp = v.get("cpp","?"); py = v.get("python","?")
            icon = "✅" if (cpp=="AC" and py=="AC") else "⚠️"
            print(f"  {icon} {r['nq']}: C++={cpp} Python={py}")
            if cpp == "AC": cpp_ok += 1
            if py == "AC": py_ok += 1
        print(f"\nC++ AC: {cpp_ok}/{len(summary)}  Python AC: {py_ok}/{len(summary)}")

if __name__ == "__main__":
    main()
