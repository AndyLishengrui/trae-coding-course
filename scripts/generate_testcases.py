#!/usr/bin/env python3
"""
生成测试数据：为所有章节的 NQ 目录补全 testcase/

策略:
  1. 从 ACW 目录复制已有 testcase/（如果 ACW 有>=10组）
  2. 如果 gen.cpp 不是 stub，编译 gen.cpp + Andy.cpp 生成
  3. 否则，用 Andy.cpp + 随机输入生成（基于样例推断输入格式）

用法:
  python3 generate_testcases.py --chapter 8    # 处理单章
  python3 generate_testcases.py --all           # 处理全部16章
  python3 generate_testcases.py --missing-only  # 只处理缺失的
"""
import json, os, sys, subprocess, random, tempfile, shutil
from pathlib import Path
from typing import List, Tuple, Optional

BOOK_ROOT = Path(__file__).parent.parent


def find_acw_dir(bank_dir: Path, acw_id: int) -> Optional[Path]:
    for d in bank_dir.iterdir():
        if d.is_dir():
            # Match "ACW001.something" pattern
            n = d.name.lower().replace("_", "")
            if f"acw{acw_id}" in n:
                return d
    return None


def copy_testcases_from_acw(nq_dir: Path, acw_dir: Path) -> bool:
    """从 ACW 目录复制测试数据到 NQ 目录"""
    acw_tc = acw_dir / "testcase"
    nq_tc = nq_dir / "testcase"
    if not acw_tc.exists():
        return False
    # Count valid test case files
    tc_files = list(acw_tc.glob("*.in"))
    if len(tc_files) < 10:
        return False
    if nq_tc.exists():
        existing = list(nq_tc.glob("*.in"))
        if len(existing) >= 10:
            return True  # Already has enough
    os.makedirs(nq_tc, exist_ok=True)
    for f in acw_tc.iterdir():
        shutil.copy2(f, nq_tc / f.name)
    return True


def is_stub_gen(gen_path: Path) -> bool:
    if not gen_path.exists():
        return True
    content = gen_path.read_text(encoding="utf-8")
    if "见原题" in content:
        return True
    lines = [l for l in content.split("\n") if l.strip() and not l.strip().startswith("//")]
    if len(lines) < 8:
        return True
    return False


def generate_with_gen_cpp(prob_dir: Path, nq_id: str) -> bool:
    """用 gen.cpp + Andy.cpp 生成10组测试数据"""
    gen_cpp = prob_dir / "gen.cpp"
    andy_cpp = prob_dir / "Andy.cpp"
    testcase_dir = prob_dir / "testcase"

    if not gen_cpp.exists() or not andy_cpp.exists():
        return False
    if is_stub_gen(gen_cpp):
        return False

    os.makedirs(testcase_dir, exist_ok=True)

    # Compile
    gen_exe = prob_dir / "gen.out"
    andy_exe = prob_dir / "andy.out"
    ok_count = 0

    # Compile gen
    r = subprocess.run(["g++", "-std=c++11", "-O2", str(gen_cpp), "-o", str(gen_exe)],
                       capture_output=True, text=True, timeout=15)
    if r.returncode != 0:
        return False

    # Compile Andy
    r = subprocess.run(["g++", "-std=c++11", "-O2", str(andy_cpp), "-o", str(andy_exe)],
                       capture_output=True, text=True, timeout=15)
    if r.returncode != 0:
        return False

    # Generate 10 test cases
    for tc in range(1, 11):
        try:
            r = subprocess.run([str(gen_exe), str(tc)], capture_output=True, text=True, timeout=5)
            if r.returncode != 0:
                continue
            inp = r.stdout
            r2 = subprocess.run([str(andy_exe)], input=inp, capture_output=True, text=True, timeout=5)
            if r2.returncode != 0:
                continue
            (testcase_dir / f"{tc}.in").write_text(inp, encoding="utf-8")
            (testcase_dir / f"{tc}.out").write_text(r2.stdout, encoding="utf-8")
            ok_count += 1
        except Exception as e:
            pass

    # Cleanup
    for exe in [gen_exe, andy_exe]:
        if exe.exists():
            exe.unlink()

    return ok_count >= 10


def generate_with_andy(prob_dir: Path, nq_id: str, samples: List[dict]) -> bool:
    """用 Andy.cpp + 随机输入生成测试数据（当 gen.cpp 不可用时）"""
    andy_cpp = prob_dir / "Andy.cpp"
    testcase_dir = prob_dir / "testcase"

    if not andy_cpp.exists():
        return False

    os.makedirs(testcase_dir, exist_ok=True)

    # Compile Andy
    andy_exe = prob_dir / "andy.out"
    r = subprocess.run(["g++", "-std=c++11", "-O2", str(andy_cpp), "-o", str(andy_exe)],
                       capture_output=True, text=True, timeout=15)
    if r.returncode != 0:
        return False

    ok_count = 0

    # Parse sample to infer input format
    sample_inputs = [s["input"] for s in samples[:3] if s.get("input")]

    def gen_random_input(tc: int) -> str:
        """根据样例推断输入格式，生成随机变体"""
        if tc == 1 and sample_inputs:
            return sample_inputs[0]  # tc=1 always sample
        if tc <= min(3, len(sample_inputs)) and sample_inputs:
            return sample_inputs[tc - 1]

        # Parse the first sample to infer format
        if sample_inputs:
            lines = sample_inputs[0].strip().split("\n")
        else:
            lines = ["1"]

        result = []
        for line in lines:
            tokens = line.split()
            new_tokens = []
            for tok in tokens:
                try:
                    v = float(tok)
                    if v == int(v) and "." not in tok:
                        # Integer
                        v = int(v)
                        if abs(v) <= 1:
                            new_tokens.append(str(random.randint(2, 100)))
                        else:
                            delta = random.randint(-v//2, v//2) if v != 0 else random.randint(1, 100)
                            new_tokens.append(str(v + delta))
                    else:
                        # Float
                        delta = random.uniform(-v, v) if v != 0 else random.uniform(1, 10)
                        new_tokens.append(f"{v + delta:.2f}")
                except ValueError:
                    # String
                    new_tokens.append(tok)
            result.append(" ".join(new_tokens))

        return "\n".join(result)

    for tc in range(1, 11):
        try:
            inp = gen_random_input(tc)
            r = subprocess.run([str(andy_exe)], input=inp, capture_output=True, text=True, timeout=5)
            if r.returncode != 0:
                continue
            (testcase_dir / f"{tc}.in").write_text(inp, encoding="utf-8")
            (testcase_dir / f"{tc}.out").write_text(r.stdout, encoding="utf-8")
            ok_count += 1
        except Exception:
            pass

    # Cleanup
    if andy_exe.exists():
        andy_exe.unlink()

    return ok_count >= 10


def generate_for_chapter(ch: int, missing_only: bool = True):
    """为单章生成测试数据"""
    bank_dir = BOOK_ROOT / f"chapter{ch}_bank"
    if not bank_dir.exists():
        print(f"  ch{ch}: bank dir not found")
        return 0, 0, 0

    copied = 0
    generated = 0
    failed = 0

    # Find NQ directories
    nq_dirs = sorted([d for d in bank_dir.iterdir() if d.is_dir() and d.name.startswith("NQ")])

    for nq_dir in nq_dirs:
        nq_id = nq_dir.name.split(".")[0] if "." in nq_dir.name else nq_dir.name

        # Check if already has test cases
        tc_dir = nq_dir / "testcase"
        existing = len(list(tc_dir.glob("*.in"))) if tc_dir.exists() else 0
        if missing_only and existing >= 10:
            continue

        # Load problem.json for metadata
        pj_file = nq_dir / "problem.json"
        samples = []
        acw_id = 0
        if pj_file.exists():
            pj = json.loads(pj_file.read_text(encoding="utf-8"))
            samples = pj.get("samples", [])
            # Extract AcWing ID from source field: "AcWing 905 | NQ16-01 | 第16章"
            source = pj.get("source", "")
            import re
            m = re.search(r'AcWing (\d+)', source)
            if m:
                acw_id = int(m.group(1))

        # Strategy 1: Find matching ACW dir and copy test cases
        acw_dir = None
        for d in bank_dir.iterdir():
            if d.is_dir() and not d.name.startswith("NQ"):
                n = d.name.lower().replace("_", "")
                if f"acw{acw_id}" in n:
                    acw_dir = d
                    break
        if acw_dir:
            acw_tc = acw_dir / "testcase"
            if acw_tc.exists() and len(list(acw_tc.glob("*.in"))) >= 10:
                os.makedirs(tc_dir, exist_ok=True)
                for f in acw_tc.iterdir():
                    shutil.copy2(f, tc_dir / f.name)
                copied += 1
                print(f"    copied from {acw_dir.name}")
                continue

        # Strategy 2: Try gen.cpp generation
        if generate_with_gen_cpp(nq_dir, nq_id):
            generated += 1
            print(f"    generated via gen.cpp")
            continue

        # Strategy 3: Generate from Andy.cpp
        if generate_with_andy(nq_dir, nq_id, samples):
            generated += 1
            print(f"    generated via Andy.cpp")
            continue

        failed += 1
        print(f"    FAILED: no test case source")

    return copied, generated, failed


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--chapter", "-c", type=int, help="单章")
    parser.add_argument("--all", action="store_true", help="全部16章")
    parser.add_argument("--missing-only", action="store_true", default=True, help="只处理缺失的")
    args = parser.parse_args()

    if args.chapter:
        chapters = [args.chapter]
    elif args.all:
        chapters = list(range(1, 17))
    else:
        chapters = list(range(1, 17))

    total_copied = 0
    total_gen = 0
    total_fail = 0

    for ch in chapters:
        print(f"\nch{ch}:")
        copied, gen, fail = generate_for_chapter(ch, args.missing_only)
        total_copied += copied
        total_gen += gen
        total_fail += fail
        print(f"  copied: {copied}, gen: {gen}, fail: {fail}")

    print(f"\n{'='*40}")
    print(f"总计: copied {total_copied}, gen {total_gen}, fail {total_fail}")


if __name__ == "__main__":
    main()
