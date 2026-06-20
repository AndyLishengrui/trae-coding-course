#!/usr/bin/env python3
"""
本地验证：编译Andy.cpp/Andy.py，用OJ测试数据验证正确性

流程:
  1. 从OJ数据库获取每道题的test_case_id
  2. 导出test case文件到本地/tmp/
  3. 编译运行C++和Python代码
  4. 比对所有输入输出
  5. 报告AC/WA
"""
import json, os, sys, subprocess, tempfile, shutil
from pathlib import Path

BOOK = Path(__file__).parent.parent
TMP = Path("/tmp/nq_verify")
os.makedirs(TMP, exist_ok=True)


def get_all_test_case_ids():
    """从Docker获取所有NQ题目的test_case_id"""
    result = subprocess.run(
        ["docker", "exec", "onlinejudgedeploy-oj-backend-1", "python", "manage.py", "shell",
         "-c",
         "from problem.models import Problem; import json; "
         "probs = Problem.objects.filter(_id__startswith='NQ').values('_id','test_case_id'); "
         "print(json.dumps({p['_id']: p['test_case_id'] for p in probs if p['test_case_id']}))"],
        capture_output=True, text=True, timeout=15
    )
    # Extract JSON from output (skip Django banner)
    for line in result.stdout.split("\n"):
        line = line.strip()
        if line.startswith("{"):
            return json.loads(line)
    return {}


def export_test_cases(test_case_id: str) -> Path:
    """从容器导出测试数据"""
    dest = TMP / test_case_id
    if dest.exists():
        shutil.rmtree(dest)
    os.makedirs(dest)

    # Copy test case files from container
    subprocess.run(
        ["docker", "cp",
         f"onlinejudgedeploy-oj-backend-1:/data/test_case/{test_case_id}/.",
         str(dest)],
        capture_output=True, text=True, timeout=10
    )
    return dest


def verify_cpp(cpp_path: Path, tc_dir: Path) -> Tuple[int, int, List[str]]:
    """编译并运行C++代码，比对所有测试用例"""
    if not cpp_path.exists():
        return 0, 0, ["Missing file"]

    exe = TMP / "test_cpp.out"

    # Compile
    r = subprocess.run(
        ["g++", "-std=c++11", "-O2", str(cpp_path), "-o", str(exe)],
        capture_output=True, text=True, timeout=15
    )
    if r.returncode != 0:
        return 0, 0, [f"Compile error: {r.stderr[:100]}"]

    passed = 0
    total = 0
    errors = []

    in_files = sorted(tc_dir.glob("*.in"))
    for inf in in_files:
        tc_num = inf.stem
        out_file = tc_dir / f"{tc_num}.out"
        if not out_file.exists():
            continue
        total += 1
        try:
            r = subprocess.run([str(exe)], input=inf.read_text(encoding="utf-8"),
                             capture_output=True, text=True, timeout=5)
            expected = out_file.read_text(encoding="utf-8").strip()
            actual = r.stdout.strip()
            if actual == expected:
                passed += 1
            else:
                errors.append(f"tc{tc_num}: WA (got={actual[:50]}, exp={expected[:50]})")
        except Exception as e:
            errors.append(f"tc{tc_num}: ERR ({e})")

    # Clean up
    if exe.exists():
        exe.unlink()

    return passed, total, errors


def verify_python(py_path: Path, tc_dir: Path) -> Tuple[int, int, List[str]]:
    """运行Python代码，比对所有测试用例"""
    if not py_path.exists():
        return 0, 0, ["Missing file"]

    passed = 0
    total = 0
    errors = []

    in_files = sorted(tc_dir.glob("*.in"))
    for inf in in_files:
        tc_num = inf.stem
        out_file = tc_dir / f"{tc_num}.out"
        if not out_file.exists():
            continue
        total += 1
        try:
            r = subprocess.run(
                ["python3", str(py_path)],
                input=inf.read_text(encoding="utf-8"),
                capture_output=True, text=True, timeout=5
            )
            if r.returncode != 0:
                errors.append(f"tc{tc_num}: Python runtime error: {r.stderr[:80]}")
                continue
            expected = out_file.read_text(encoding="utf-8").strip()
            actual = r.stdout.strip()
            if actual == expected:
                passed += 1
            else:
                errors.append(f"tc{tc_num}: WA (got={actual[:50]}, exp={expected[:50]})")
        except Exception as e:
            errors.append(f"tc{tc_num}: ERR ({e})")

    return passed, total, errors


def main():
    print("📊 获取 test_case_id 映射...")
    tc_map = get_all_test_case_ids()
    print(f"   共 {len(tc_map)} 个NQ题目有test_case_id")

    nq_map = json.loads((BOOK / "scripts/nq_mapping.json").read_text())

    results = []
    total_pass = 0
    total_fail = 0

    # Process in chapter order
    for ch in range(1, 17):
        ch_probs = [(nq_id, info) for nq_id, info in nq_map.items() if info["ch"] == ch]
        if not ch_probs:
            continue
        print(f"\n--- 第{ch}章 ({len(ch_probs)}题) ---")

        for nq_id, info in sorted(ch_probs, key=lambda x: x[1]["idx"]):
            bank = BOOK / f"chapter{ch}_bank"
            nq_dir = None
            for d in bank.iterdir():
                if d.is_dir() and d.name.startswith(nq_id):
                    nq_dir = d
                    break
            if not nq_dir:
                print(f"  ⚠️  {nq_id}: 目录不存在")
                continue

            cpp_file = nq_dir / "Andy.cpp"
            py_file = nq_dir / "Andy.py"

            if nq_id not in tc_map:
                print(f"  ⚠️  {nq_id}: 无test_case_id")
                continue

            tc_id = tc_map[nq_id]

            # Export test cases
            try:
                tc_dir = export_test_cases(tc_id)
            except Exception as e:
                print(f"  ❌ {nq_id}: 导出测试数据失败: {e}")
                continue

            # Verify C++
            cpp_pass, cpp_total, cpp_errs = verify_cpp(cpp_file, tc_dir)
            # Verify Python
            py_pass, py_total, py_errs = verify_python(py_file, tc_dir)

            cpp_ok = cpp_pass == cpp_total and cpp_total > 0
            py_ok = py_pass == py_total and py_total > 0

            if cpp_ok and py_ok:
                total_pass += 1
                print(f"  ✅ {nq_id}: C++ {cpp_pass}/{cpp_total} Py {py_pass}/{py_total}")
            else:
                total_fail += 1
                print(f"  ❌ {nq_id}: C++ {cpp_pass}/{cpp_total} Py {py_pass}/{py_total}")
                for e in cpp_errs[:2]:
                    print(f"      C++ {e}")
                for e in py_errs[:2]:
                    print(f"      Py {e}")

            results.append({
                "nq_id": nq_id,
                "ch": ch,
                "cpp_pass": cpp_pass, "cpp_total": cpp_total,
                "py_pass": py_pass, "py_total": py_total,
                "cpp_ok": cpp_ok, "py_ok": py_ok,
                "cpp_errs": cpp_errs[:3], "py_errs": py_errs[:3],
            })

    # Final report
    print(f"\n{'='*60}")
    print(f"📊 总报告: {len(results)}题验证")
    print(f"  通过: {total_pass}")
    print(f"  失败: {total_fail}")

    failed = [r for r in results if not (r["cpp_ok"] and r["py_ok"])]
    if failed:
        print(f"\n❌ 失败题目:")
        for r in failed:
            print(f"  {r['nq_id']}: C++={r['cpp_pass']}/{r['cpp_total']} Py={r['py_pass']}/{r['py_total']}")
    else:
        print(f"\n🎉 全部通过！")

    # Save report
    report_path = BOOK / "scripts/verify_report.json"
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\n报告: {report_path}")


if __name__ == "__main__":
    main()
