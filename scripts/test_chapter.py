#!/usr/bin/env python3
"""
标准化章节AC测试脚本
=====================
用法:
  python3 test_chapter.py 2              # 测试第2章 (Python)
  python3 test_chapter.py 3 --both       # 测试第3章 (Python + C++)
  python3 test_chapter.py 1 --fix-only   # 仅修复测试数据，不提交
  python3 test_chapter.py --all          # 测试全部16章

流程:
  1. 扫描 chapterN_bank 获取解决方案
  2. 从数据库获取题目ID和测试数据ID
  3. 检查测试数据完整性，对比bank原始数据，自动修复损坏的测试用例
  4. 本地运行代码验证输出格式是否匹配期望
  5. 提交代码 → 轮询评测 → 汇总报告
"""
import json, os, sys, time, hashlib, subprocess, argparse, glob, shutil

BASE = "http://localhost"
TOKEN = "63310cdaec0bc93b08f856568e125e75"
CONTEST_ID = 356
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BANK_ROOT = os.path.dirname(SCRIPT_DIR)
HOST_TC = "/Users/andyshengruilee/Downloads/OpenJudgeFE/OnlineJudgeDeploy/data/backend/test_case"

# ===================== 数据加载 =====================

def load_nq_mapping():
    with open(os.path.join(SCRIPT_DIR, "nq_mapping.json"), "r") as f:
        raw = json.load(f)
    chapters = {}
    for nq_id, info in raw.items():
        ch = info["ch"]
        chapters.setdefault(ch, []).append((nq_id, info["idx"], info["acw"], info["pid"]))
    for ch in chapters:
        chapters[ch].sort(key=lambda x: x[1])
    return chapters

def load_acw_dir_mapping():
    """扫描所有 chapterN_bank，建立 acw_id -> 目录路径 的映射"""
    mapping = {}
    for ch in range(1, 17):
        bank_dir = os.path.join(BANK_ROOT, f"chapter{ch}_bank")
        if not os.path.isdir(bank_dir):
            continue
        for d in os.listdir(bank_dir):
            dpath = os.path.join(bank_dir, d)
            if not os.path.isdir(dpath):
                continue
            parts = d.split(".", 1)
            if parts[0].startswith("ACW"):
                try:
                    mapping[int(parts[0][3:])] = dpath
                except ValueError:
                    continue
    return mapping

def get_db_problems(chapter):
    result = subprocess.run([
        "docker", "exec", "-i", "onlinejudgedeploy-oj-postgres-1",
        "psql", "-U", "onlinejudge", "-d", "onlinejudge", "-t", "-A",
        "-c", f"SELECT id, _id, test_case_id FROM problem WHERE _id LIKE 'NQ{chapter}-%' ORDER BY _id;"
    ], capture_output=True, text=True)
    problems = {}
    for line in result.stdout.strip().split("\n"):
        if not line.strip(): continue
        parts = line.split("|")
        if len(parts) >= 3:
            problems[parts[1]] = {"db_id": int(parts[0]), "test_case_id": parts[2]}
    return problems

# ===================== 测试数据检查与修复 =====================

def check_test_cases(test_case_id):
    tc_dir = os.path.join(HOST_TC, test_case_id)
    if not os.path.isdir(tc_dir):
        return {"status": "MISSING_DIR", "in_count": 0, "out_count": 0, "has_info": False}
    in_files = sorted(glob.glob(os.path.join(tc_dir, "*.in")))
    out_files = sorted(glob.glob(os.path.join(tc_dir, "*.out")))
    has_info = os.path.exists(os.path.join(tc_dir, "info"))
    return {
        "status": "OK" if (len(in_files) == len(out_files) >= 1) else "INCOMPLETE",
        "in_count": len(in_files), "out_count": len(out_files), "has_info": has_info,
    }

def validate_test_case_output(tc_dir, bank_dir):
    """
    对比 OJ 测试数据与 bank 原始数据。
    如果 OJ 数据缺失或与 bank 不一致，从 bank 复制并重建 info.json。
    返回修复数量。
    """
    if not os.path.isdir(bank_dir):
        return 0
    bank_tc = os.path.join(bank_dir, "testcase")
    if not os.path.isdir(bank_tc):
        return 0

    fixed = 0
    needs_rebuild = False

    for fname in sorted(os.listdir(bank_tc)):
        if not (fname.endswith(".in") or fname.endswith(".out")):
            continue
        bank_path = os.path.join(bank_tc, fname)
        oj_path = os.path.join(tc_dir, fname)

        if not os.path.exists(oj_path):
            # OJ 缺失这个文件
            shutil.copy2(bank_path, oj_path)
            fixed += 1
            needs_rebuild = True
        elif fname.endswith(".out"):
            # 对比内容
            with open(bank_path, "rb") as f:
                bank_content = f.read()
            with open(oj_path, "rb") as f:
                oj_content = f.read()
            if bank_content != oj_content:
                shutil.copy2(bank_path, oj_path)
                fixed += 1
                needs_rebuild = True

    # 重建 info.json
    if needs_rebuild or not os.path.exists(os.path.join(tc_dir, "info")):
        rebuild_info_json(tc_dir)
        fixed += 1

    return fixed

def rebuild_info_json(tc_dir):
    """重建测试数据的 info.json"""
    info = {"spj": False, "test_cases": {}}
    in_files = sorted(glob.glob(os.path.join(tc_dir, "*.in")))
    for idx, in_path in enumerate(in_files, 1):
        fname = os.path.basename(in_path)
        base = fname.rsplit(".", 1)[0]
        out_path = os.path.join(tc_dir, f"{base}.out")
        if not os.path.exists(out_path):
            continue
        in_size = os.path.getsize(in_path)
        out_size = os.path.getsize(out_path)
        with open(out_path, "rb") as f:
            stripped_md5 = hashlib.md5(f.read().rstrip()).hexdigest()
        info["test_cases"][str(idx)] = {
            "stripped_output_md5": stripped_md5,
            "input_size": in_size, "output_size": out_size,
            "input_name": fname, "output_name": f"{base}.out",
        }
    with open(os.path.join(tc_dir, "info"), "w") as f:
        json.dump(info, f, indent=4)

# ===================== 代码验证 =====================

def run_code_locally(code, language, input_data):
    """本地运行代码获取输出"""
    import tempfile
    try:
        if language in ("Python3", "Python"):
            result = subprocess.run(
                ["python3", "-c", code], input=input_data,
                capture_output=True, text=True, timeout=5
            )
            return result.stdout, result.stderr
        elif language in ("C", "C++"):
            ext = "cpp" if language == "C++" else "c"
            compiler = "g++" if language == "C++" else "gcc"
            with tempfile.NamedTemporaryFile(suffix=f".{ext}", delete=False, mode="w") as f:
                f.write(code); tmp_path = f.name
            r = subprocess.run([compiler, "-o", tmp_path + ".out", tmp_path], capture_output=True, text=True, timeout=10)
            if r.returncode != 0:
                os.unlink(tmp_path)
                return "", f"Compile error: {r.stderr[:200]}"
            result = subprocess.run([tmp_path + ".out"], input=input_data, capture_output=True, text=True, timeout=5)
            os.unlink(tmp_path)
            if os.path.exists(tmp_path + ".out"): os.unlink(tmp_path + ".out")
            return result.stdout, result.stderr
        return "", f"Unsupported language: {language}"
    except Exception as e:
        return "", str(e)

def validate_output(code, language, test_case_dir):
    """用第一个测试用例验证代码输出格式是否匹配期望"""
    first_in = os.path.join(test_case_dir, "1.in")
    first_out = os.path.join(test_case_dir, "1.out")
    if not os.path.exists(first_in) or not os.path.exists(first_out):
        return {"match": None, "reason": "no test case files"}
    sample_input = open(first_in).read()
    expected = open(first_out).read()
    actual, err = run_code_locally(code, language, sample_input)
    if err:
        return {"match": False, "reason": f"run error: {err[:80]}"}
    # 比较时去除末尾空白
    actual_trimmed = actual.rstrip()
    expected_trimmed = expected.rstrip()
    return {
        "match": actual_trimmed == expected_trimmed,
        "actual": actual_trimmed.replace("\n", "\\n")[:100],
        "expected": expected_trimmed.replace("\n", "\\n")[:100],
    }

# ===================== 提交与评测 =====================

def submit_and_wait(db_id, language, code, timeout=120):
    import requests
    s = requests.Session()
    s.headers.update({"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"})
    r = s.post(f"{BASE}/api/submission", json={
        "problem_id": db_id, "contest_id": CONTEST_ID,
        "language": language, "code": code
    })
    data = r.json()
    if data.get("error"):
        return {"error": f"Submit: {data.get('data','?')[:60]}"}
    sid = data["data"]["submission_id"]
    for _ in range(timeout):
        time.sleep(1)
        r = s.get(f"{BASE}/api/submission", params={"id": sid})
        rd = r.json().get("data", {})
        result = rd.get("result", -99)
        if result not in (-1, -2):
            return {
                "submission_id": sid, "result": result,
                "score": rd.get("statistic_info", {}).get("score", 0),
                "time_cost": rd.get("statistic_info", {}).get("time_cost", 0),
            }
    return {"submission_id": sid, "result": -1, "error": "TIMEOUT"}

# ===================== 主流程 =====================

def test_chapter(chapter, languages=("Python3",), fix_only=False):
    print(f"\n{'='*60}")
    print(f"  第 {chapter} 章 AC 标准化测试")
    print(f"{'='*60}\n")

    chapters = load_nq_mapping()
    acw_dirs = load_acw_dir_mapping()
    db_problems = get_db_problems(chapter)
    nq_list = chapters.get(chapter, [])

    if not nq_list:
        print(f"❌ 第{chapter}章无数据")
        return False

    print(f"共 {len(nq_list)} 题，语言: {', '.join(languages)}\n")
    results = []

    for nq_id, idx, acw_id, pid in nq_list:
        db = db_problems.get(nq_id, {})
        db_id = db.get("db_id")
        test_case_id = db.get("test_case_id", "")
        acw_dir = acw_dirs.get(acw_id, "")
        tc_dir = os.path.join(HOST_TC, test_case_id) if test_case_id else ""
        bank_tc_dir = os.path.join(acw_dir, "testcase") if acw_dir else ""

        print(f"  {nq_id} (ACW{acw_id})")

        if not db_id:
            print(f"    ❌ 数据库中无此题目")
            results.append((nq_id, "NO_DB"))
            continue

        # 1. 检查并修复测试数据
        if tc_dir and os.path.isdir(tc_dir) and os.path.isdir(bank_tc_dir):
            fixed = validate_test_case_output(tc_dir, bank_tc_dir)
            if fixed > 0:
                print(f"    🔧 修复了 {fixed} 个测试数据文件")
            tc = check_test_cases(test_case_id)
            if tc["status"] != "OK":
                print(f"    ⚠️ 测试数据不完整: {tc['in_count']}in/{tc['out_count']}out")
        else:
            print(f"    ⚠️ 测试数据目录缺失")

        if fix_only:
            continue

        # 2. 验证并提交解决方案
        for lang in languages:
            ext = "py" if lang in ("Python3", "Python") else "cpp"
            sol_file = os.path.join(acw_dir, f"Andy.{ext}") if acw_dir else ""
            if not sol_file or not os.path.exists(sol_file):
                print(f"    ⚠️ {lang} 方案缺失")
                results.append((nq_id, lang, "NO_FILE"))
                continue

            with open(sol_file, "r") as f:
                code = f.read()

            # 本地验证输出格式
            validation = validate_output(code, lang, tc_dir) if tc_dir else {"match": None}
            if validation["match"] is False:
                actual = validation.get("actual", validation.get("reason", "?"))
                expected = validation.get("expected", "?")
                print(f"    ❌ {lang}: 输出不匹配 → 实际={actual}")
                print(f"                       期望={expected}")
                results.append((nq_id, lang, "FORMAT_MISMATCH"))
                continue
            elif validation["match"] is True:
                print(f"    ✅ {lang}: 输出格式匹配")

            # 提交
            print(f"    提交 {lang}...", end="", flush=True)
            result = submit_and_wait(db_id, lang, code, timeout=120)

            if result.get("error"):
                print(f" ❌ {result['error']}")
                results.append((nq_id, lang, "ERR"))
            elif result["result"] == 0:
                print(f" ✅ AC score={result['score']} time={result['time_cost']}ms")
                results.append((nq_id, lang, "AC"))
            else:
                print(f" ❌ result={result['result']} score={result.get('score',0)}")
                results.append((nq_id, lang, f"FAIL({result['result']})"))

    # 汇总
    if fix_only:
        print(f"\n  📋 仅修复模式，未提交代码")
        return True

    ac_count = sum(1 for r in results if r[-1] == "AC")
    total = len(results)

    print(f"\n{'='*60}")
    print(f"  第 {chapter} 章结果: {ac_count}/{total} AC")
    print(f"{'='*60}")
    for r in results:
        nq, *rest = r
        if len(rest) == 2:
            lang, status = rest
            icon = "✅" if status == "AC" else "❌"
            print(f"  {icon} {nq} [{lang}]: {status}")
        else:
            print(f"  ❌ {nq}: {rest[0]}")

    return ac_count == total

def test_all_chapters(languages=("Python3",)):
    """测试全部16章"""
    total_ac = 0
    total_all = 0
    failed_chapters = []
    for ch in range(1, 17):
        chapters = load_nq_mapping()
        if ch not in chapters:
            continue
        success = test_chapter(ch, languages)
        if not success:
            failed_chapters.append(ch)

        # 统计
        import requests
        s = requests.Session()
        s.headers.update({"Authorization": f"Bearer {TOKEN}"})
        for nq_id, _, _, _ in chapters[ch]:
            db = get_db_problems(ch).get(nq_id, {})
            db_id = db.get("db_id")
            if not db_id:
                continue
            r = s.get(f"{BASE}/api/submissions", params={"problem_id": db_id, "limit": 1, "myself": 1})
            results = r.json().get("data", {}).get("results", [])
            total_all += 1
            if results and results[0].get("result") == 0:
                total_ac += 1

    print(f"\n{'='*60}")
    print(f"  全部16章总结果: {total_ac}/{total_all} AC")
    print(f"{'='*60}")
    if failed_chapters:
        print(f"  未完全通过: 第{','.join(map(str, failed_chapters))}章")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="标准化章节AC测试")
    parser.add_argument("chapter", nargs="?", type=int, help="章节号 (1-16)")
    parser.add_argument("--python", action="store_true")
    parser.add_argument("--cpp", action="store_true")
    parser.add_argument("--both", action="store_true")
    parser.add_argument("--fix-only", action="store_true", help="仅修复测试数据，不提交")
    parser.add_argument("--all", action="store_true", help="测试全部16章")
    args = parser.parse_args()

    if args.cpp:
        langs = ("C++",)
    elif args.both:
        langs = ("Python3", "C")
    else:
        langs = ("Python3",)

    if args.all:
        test_all_chapters(langs)
    elif args.chapter:
        test_chapter(args.chapter, langs, fix_only=args.fix_only)
    else:
        parser.print_help()
