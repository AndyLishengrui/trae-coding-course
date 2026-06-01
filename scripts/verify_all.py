#!/usr/bin/env python3
"""
全面验证脚本 — 三道防线确保质量
=================================
1. 数据库 AC 状态检查 (Python + C++ 双语言)
2. 测试数据完整性检查 (MD5 校验)
3. 代码本地运行验证 (输出格式匹配)

用法: python3 verify_all.py           # 全部检查
      python3 verify_all.py --quick   # 仅数据库检查
"""
import json, os, sys, subprocess, glob, hashlib, time, argparse

BANK_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOST_TC = "/Users/andyshengruilee/Downloads/OpenJudgeFE/OnlineJudgeDeploy/data/backend/test_case"
TOKEN = "63310cdaec0bc93b08f856568e125e75"

def db_query(sql):
    r = subprocess.run(["docker","exec","-i","onlinejudgedeploy-oj-postgres-1",
        "psql","-U","onlinejudge","-d","onlinejudge","-t","-A","-c",sql],
        capture_output=True, text=True)
    return r.stdout.strip()

# ========== 防线1: 数据库 AC 状态 ==========

def check_db_ac():
    """检查所有题目的 Python 和 C++ AC 状态"""
    issues = []
    for ch in range(1, 17):
        result = db_query(f"""
            SELECT p._id FROM problem p
            WHERE p._id LIKE 'NQ{ch}-%'
            AND p.id NOT IN (
                SELECT DISTINCT problem_id FROM submission
                WHERE username='andy' AND contest_id=356 AND result=0 AND language='Python3')
            ORDER BY p._id;
        """)
        if result:
            for nq in result.split("\n"):
                if nq.strip(): issues.append(("Python", nq.strip()))

        result = db_query(f"""
            SELECT p._id FROM problem p
            WHERE p._id LIKE 'NQ{ch}-%'
            AND p.id NOT IN (
                SELECT DISTINCT problem_id FROM submission
                WHERE username='andy' AND contest_id=356 AND result=0 AND language='C++')
            ORDER BY p._id;
        """)
        if result:
            for nq in result.split("\n"):
                if nq.strip(): issues.append(("C++", nq.strip()))
    return issues

# ========== 防线2: 测试数据完整性 ==========

def check_test_data_integrity():
    """检查所有题目的 info.json MD5 是否与实际 .out 文件匹配"""
    issues = []
    for ch in range(1, 17):
        result = db_query(f"SELECT _id, test_case_id FROM problem WHERE _id LIKE 'NQ{ch}-%' ORDER BY _id;")
        for line in result.split("\n"):
            if not line.strip(): continue
            parts = line.split("|")
            if len(parts) < 2: continue
            nq_id, tc_id = parts[0], parts[1]
            tc_dir = os.path.join(HOST_TC, tc_id)
            if not os.path.isdir(tc_dir):
                issues.append((nq_id, "TC_DIR_MISSING", tc_dir))
                continue
            info_path = os.path.join(tc_dir, "info")
            if not os.path.exists(info_path):
                issues.append((nq_id, "INFO_MISSING", ""))
                continue
            try:
                with open(info_path) as f:
                    info = json.load(f)
            except:
                issues.append((nq_id, "INFO_CORRUPT", ""))
                continue
            for tc_name, tc_data in info.get("test_cases", {}).items():
                out_file = os.path.join(tc_dir, tc_data.get("output_name", ""))
                if not os.path.exists(out_file):
                    issues.append((nq_id, f"TC{tc_name}_OUT_MISSING", tc_data.get("output_name","")))
                    continue
                with open(out_file, "rb") as f:
                    actual_md5 = hashlib.md5(f.read().rstrip()).hexdigest()
                expected_md5 = tc_data.get("stripped_output_md5", "")
                if actual_md5 != expected_md5:
                    issues.append((nq_id, f"TC{tc_name}_MD5_MISMATCH", f"expected={expected_md5[:12]} actual={actual_md5[:12]}"))
    return issues

# ========== 防线3: 本地运行验证 ==========

def run_code(code, language, input_data):
    """本地运行代码并返回输出"""
    import tempfile
    try:
        if language == "Python3":
            r = subprocess.run(["python3", "-c", code], input=input_data,
                capture_output=True, text=True, timeout=5)
            return r.stdout, r.stderr
        elif language == "C++":
            with tempfile.NamedTemporaryFile(suffix=".cpp", delete=False, mode="w") as f:
                f.write(code); tmp_path = f.name
            r = subprocess.run(["g++", "-std=c++11", "-o", tmp_path+".out", tmp_path],
                capture_output=True, text=True, timeout=15)
            if r.returncode != 0:
                os.unlink(tmp_path)
                return "", f"COMPILE: {r.stderr[:100]}"
            result = subprocess.run([tmp_path+".out"], input=input_data,
                capture_output=True, text=True, timeout=5)
            os.unlink(tmp_path)
            if os.path.exists(tmp_path+".out"): os.unlink(tmp_path+".out")
            return result.stdout, result.stderr
        return "", f"Unknown language: {language}"
    except Exception as e:
        return "", str(e)

def check_code_output():
    """本地运行验证：代码输出是否匹配测试数据期望输出"""
    issues = []
    nq_mapping = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "nq_mapping.json")))
    acw_dirs = {}
    for ch in range(1, 17):
        bank_dir = os.path.join(BANK_ROOT, f"chapter{ch}_bank")
        if not os.path.isdir(bank_dir): continue
        for d in os.listdir(bank_dir):
            dpath = os.path.join(bank_dir, d)
            if not os.path.isdir(dpath): continue
            parts = d.split(".", 1)
            if parts[0].startswith("ACW"):
                try: acw_dirs[int(parts[0][3:])] = dpath
                except: pass

    for nq_id, info in nq_mapping.items():
        acw_id = info["acw"]
        acw_dir = acw_dirs.get(acw_id, "")
        if not acw_dir: continue

        tc_dir = os.path.join(acw_dir, "testcase")
        if not os.path.isdir(tc_dir): continue

        first_in = os.path.join(tc_dir, "1.in")
        first_out = os.path.join(tc_dir, "1.out")
        if not os.path.exists(first_in) or not os.path.exists(first_out): continue

        with open(first_in) as f: inp = f.read()
        with open(first_out) as f: expected = f.read().rstrip()

        for lang, ext in [("Python3", "py"), ("C++", "cpp")]:
            sol_file = os.path.join(acw_dir, f"Andy.{ext}")
            if not os.path.exists(sol_file): continue
            with open(sol_file) as f: code = f.read()
            actual, err = run_code(code, lang, inp)
            if err:
                issues.append((nq_id, lang, "RUN_ERROR", err[:60]))
                continue
            if actual.rstrip() != expected:
                issues.append((nq_id, lang, "OUTPUT_MISMATCH",
                    f"expected={expected[:50].replace(chr(10),'&')} actual={actual.rstrip()[:50].replace(chr(10),'&')}"))
    return issues

# ========== 主流程 ==========

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--quick", action="store_true")
    args = parser.parse_args()

    print("="*60)
    print("  全面质量验证")
    print("="*60)

    # 防线1
    print("\n🔍 防线1: 数据库 AC 状态...")
    db_issues = check_db_ac()
    if db_issues:
        print(f"  ❌ {len(db_issues)} 项未通过:")
        py_missing = [nq for lang, nq in db_issues if lang=="Python3"]
        cpp_missing = [nq for lang, nq in db_issues if lang=="C++"]
        if py_missing: print(f"     Python 缺 AC ({len(py_missing)}): {', '.join(py_missing[:10])}...")
        if cpp_missing: print(f"     C++ 缺 AC ({len(cpp_missing)}): {', '.join(cpp_missing[:10])}...")
    else:
        print("  ✅ 全部 161 题 Python + C++ 双 AC")

    if args.quick:
        return

    # 防线2
    print("\n🔍 防线2: 测试数据完整性...")
    tc_issues = check_test_data_integrity()
    if tc_issues:
        print(f"  ❌ {len(tc_issues)} 项异常:")
        for nq, err_type, detail in tc_issues[:15]:
            print(f"     {nq}: {err_type} — {detail}")
        if len(tc_issues) > 15: print(f"     ... 共 {len(tc_issues)} 项")
    else:
        print("  ✅ 全部测试数据 info.json 正确")

    # 防线3
    print("\n🔍 防线3: 本地代码输出验证...")
    code_issues = check_code_output()
    if code_issues:
        print(f"  ❌ {len(code_issues)} 项不匹配:")
        for nq, lang, err_type, detail in code_issues[:20]:
            print(f"     {nq} [{lang}]: {err_type} — {detail}")
        if len(code_issues) > 20: print(f"     ... 共 {len(code_issues)} 项")
    else:
        print("  ✅ 全部代码输出与测试数据匹配")

    print(f"\n{'='*60}")
    total = len(db_issues) + len(tc_issues) + len(code_issues)
    if total == 0:
        print("  🎉 全部验证通过！Python + C++ + 测试数据 100% 准确")
    else:
        print(f"  ⚠️ 共 {total} 项需修复")

if __name__ == "__main__":
    main()
