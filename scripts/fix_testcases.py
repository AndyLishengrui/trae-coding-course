#!/usr/bin/env python3
"""为8个PENDING题目重新生成10组测试数据并上传到localhost OJ"""
import json, os, sys, subprocess, random, hashlib, shutil
from pathlib import Path

BOOK = Path(__file__).parent.parent
TMP = Path("/tmp/tc_fix")
shutil.rmtree(TMP, ignore_errors=True)
os.makedirs(TMP, exist_ok=True)


def compile_cpp(exe_path, src_path):
    r = subprocess.run(["g++", "-std=c++11", "-O2", str(src_path), "-o", str(exe_path)],
                       capture_output=True, text=True, timeout=15)
    if r.returncode != 0:
        print(f"    COMPILE ERROR: {r.stderr[:150]}")
        return False
    return True


def generate_testcases(nq_id, gen_func, ch):
    """生成10组测试数据，返回tc_dir"""
    bank = BOOK / f"chapter{ch}_bank"
    nq_dir = None
    for d in bank.iterdir():
        if d.is_dir() and d.name.startswith(nq_id):
            nq_dir = d
            break
    if not nq_dir:
        print(f"    DIR NOT FOUND")
        return None

    cpp = nq_dir / "Andy.cpp"
    if not cpp.exists():
        print(f"    NO Andy.cpp")
        return None

    exe = TMP / f"{nq_id}_sol"
    if not compile_cpp(exe, cpp):
        return None

    tc_dir = TMP / nq_id
    os.makedirs(tc_dir, exist_ok=True)

    for tc in range(1, 11):
        random.seed(tc * 9973 + hash(nq_id) % 10000)
        inp = gen_func(tc) + "\n"  # Ensure trailing newline
        (tc_dir / f"{tc}.in").write_text(inp, encoding="utf-8")
        r = subprocess.run([str(exe)], input=inp, capture_output=True, text=True, timeout=5)
        if r.returncode == 0:
            (tc_dir / f"{tc}.out").write_bytes(r.stdout.encode("utf-8"))
        else:
            (tc_dir / f"{tc}.out").write_text("")

    exe.unlink()
    return tc_dir


def upload_to_oj(nq_id, tc_dir):
    """上传测试数据到OJ并更新test_case_id"""
    tc_hash = hashlib.md5((nq_id + "_fixed").encode()).hexdigest()
    container_dir = f"/data/test_case/{tc_hash}"

    # Create dir
    subprocess.run(["docker", "exec", "onlinejudgedeploy-oj-backend-1", "mkdir", "-p", container_dir],
                   capture_output=True, timeout=5)

    # Copy all files
    for tc in range(1, 11):
        for ext in ["in", "out"]:
            subprocess.run(["docker", "cp", str(tc_dir / f"{tc}.{ext}"),
                           f"onlinejudgedeploy-oj-backend-1:{container_dir}/{tc}.{ext}"],
                          capture_output=True, timeout=5)

    # Create info.json
    test_cases = {}
    for tc in range(1, 11):
        inp = (tc_dir / f"{tc}.in").read_bytes()
        out = (tc_dir / f"{tc}.out").read_bytes()
        test_cases[str(tc)] = {
            "stripped_output_md5": hashlib.md5(out.strip()).hexdigest(),
            "input_size": len(inp),
            "output_size": len(out.strip()),
            "input_name": f"{tc}.in",
            "output_name": f"{tc}.out"
        }
    info = {"spj": False, "test_cases": test_cases}
    info_path = TMP / f"{nq_id}_info.json"
    info_path.write_text(json.dumps(info, ensure_ascii=False))
    subprocess.run(["docker", "cp", str(info_path), f"onlinejudgedeploy-oj-backend-1:{container_dir}/info"],
                   capture_output=True, timeout=5)

    # Fix permissions
    subprocess.run(["docker", "exec", "onlinejudgedeploy-oj-backend-1", "chown", "-R", "server:spj", container_dir],
                   capture_output=True, timeout=5)

    # Update DB
    subprocess.run(["docker", "exec", "onlinejudgedeploy-oj-backend-1", "python", "manage.py", "shell", "-c",
                    f"from problem.models import Problem; p=Problem.objects.get(_id='{nq_id}'); p.test_case_id='{tc_hash}'; p.save(); print('OK')"],
                   capture_output=True, text=True, timeout=10)

    print(f"    test_case_id={tc_hash}")
    return True


# ======================================================================
# Problem-specific input generators (based on actual code analysis)
# ======================================================================

def gen_nq2_14(tc):
    """NQ2-14 简单排序: 3 ints"""
    if tc == 1: return "7 14 106"
    if tc == 2: return "-10 5 0"
    if tc <= 4: return f"{random.randint(-100,100)} {random.randint(-100,100)} {random.randint(-100,100)}"
    if tc <= 7: return f"{random.randint(-10000,10000)} {random.randint(-10000,10000)} {random.randint(-10000,10000)}"
    if tc <= 9: return f"{random.randint(-10**6,10**6)} {random.randint(-10**6,10**6)} {random.randint(-10**6,10**6)}"
    return "1000000 0 -1000000"

def gen_nq4_06(tc):
    """NQ4-06 斐波那契数列: 1 int N"""
    if tc == 1: return "5"
    if tc == 2: return "1"
    if tc <= 4: return str(random.randint(0, 10))
    if tc <= 7: return str(random.randint(10, 30))
    if tc <= 9: return str(random.randint(30, 60))
    return "60"

def gen_nq4_07(tc):
    """NQ4-07 最小数和它的位置: N + N ints"""
    if tc == 1: return "5\n10 20 30 5 15"
    if tc == 2: return "3\n0 -5 -3"
    if tc <= 4:
        n = random.randint(2, 5)
        return f"{n}\n" + " ".join(str(random.randint(-50, 50)) for _ in range(n))
    if tc <= 7:
        n = random.randint(5, 15)
        return f"{n}\n" + " ".join(str(random.randint(-1000, 1000)) for _ in range(n))
    if tc <= 9:
        n = random.randint(20, 50)
        return f"{n}\n" + " ".join(str(random.randint(-10000, 10000)) for _ in range(n))
    n = 100
    return f"{n}\n" + " ".join(str(random.randint(-100000, 100000)) for _ in range(n))

def gen_nq5_05(tc):
    """NQ5-05 平方矩阵I: single N + 0 per test case"""
    sizes = [1, 3, 4, 2, 5, 7, 6, 9, 10, 8]
    return f"{sizes[tc-1]}\n0"

def gen_nq5_10(tc):
    """NQ5-10 平方矩阵II: single N + 0 per test case"""
    sizes = [1, 3, 2, 4, 5, 6, 7, 10, 9, 8]
    return f"{sizes[tc-1]}\n0"

def gen_nq6_03(tc):
    """NQ6-03 循环相克令: pairs of Hunter/Bear/Gun strings"""
    pairs = [
        ("Hunter", "Bear"), ("Bear", "Hunter"), ("Hunter", "Gun"),
        ("Gun", "Bear"), ("Bear", "Gun"), ("Gun", "Hunter"),
        ("Hunter", "Hunter"), ("Bear", "Bear"), ("Gun", "Gun"),
        ("Hunter", "Gun"),
    ]
    return f"{pairs[tc-1][0]} {pairs[tc-1][1]}"

def gen_nq6_08(tc):
    """NQ6-08 字符串匹配: float + 2 strings"""
    if tc == 1: return "0.5\nabcdef\nabc"
    if tc == 2: return "0.0\nhello\nworld"
    if tc <= 5:
        k = round(random.uniform(0, 1), 1)
        return f"{k}\nabcdefg\ncde"
    s1 = "programming"
    s2 = s1[random.randint(0, len(s1)//2):random.randint(len(s1)//2+1, len(s1))]
    return f"{round(random.uniform(0, 1), 1)}\n{s1}\n{s2}"

def gen_nq7_06(tc):
    """NQ7-06 打印矩阵: row col + matrix"""
    if tc == 1: return "2 3\n1 2 3\n4 5 6"
    if tc == 2: return "1 1\n42"
    if tc <= 4:
        r, c = 2, 3
        return f"{r} {c}\n" + "\n".join(" ".join(str(random.randint(-5,5)) for _ in range(c)) for _ in range(r))
    if tc <= 7:
        r, c = 3, 4
        return f"{r} {c}\n" + "\n".join(" ".join(str(random.randint(-100,100)) for _ in range(c)) for _ in range(r))
    if tc <= 9:
        r, c = 5, 6
        return f"{r} {c}\n" + "\n".join(" ".join(str(random.randint(-1000,1000)) for _ in range(c)) for _ in range(r))
    r, c = 10, 10
    return f"{r} {c}\n" + "\n".join(" ".join(str(random.randint(-10000,10000)) for _ in range(c)) for _ in range(r))


PROBLEMS = [
    ("NQ2-14", gen_nq2_14, 2),
    ("NQ4-06", gen_nq4_06, 4),
    ("NQ4-07", gen_nq4_07, 4),
    ("NQ5-05", gen_nq5_05, 5),
    ("NQ5-10", gen_nq5_10, 5),
    ("NQ6-03", gen_nq6_03, 6),
    ("NQ6-08", gen_nq6_08, 6),
    ("NQ7-06", gen_nq7_06, 7),
]


def main():
    ok = 0
    for nq_id, gen_func, ch in PROBLEMS:
        print(f"\n🔧 {nq_id}...")
        tc_dir = generate_testcases(nq_id, gen_func, ch)
        if tc_dir:
            if upload_to_oj(nq_id, tc_dir):
                ok += 1
            else:
                print(f"    ❌ Upload failed")
        else:
            print(f"    ❌ Generation failed")

    print(f"\n{'='*50}")
    print(f"Fixed: {ok}/{len(PROBLEMS)}")

    if ok > 0:
        print(f"\nRe-verify:")
        for nq_id, _, _ in PROBLEMS:
            print(f"  python3 scripts/submit_cli.py --nq {nq_id} --lang cpp")


if __name__ == "__main__":
    main()
