#!/usr/bin/env python3
"""批量修复剩余Python失败题目并重新验证"""
import subprocess, json, sys
from pathlib import Path

BOOK = Path(__file__).parent.parent

# 获取当前所有失败题目
r = subprocess.run(
    ["docker", "exec", "onlinejudgedeploy-oj-backend-1", "python", "manage.py", "shell", "-c",
     "from submission.models import Submission; from problem.models import Problem; import json; r={}; "
     "for p in Problem.objects.filter(_id__startswith='NQ'): "
     " s=Submission.objects.filter(problem_id=p.id,language='Python3',id__startswith='cli_').order_by('-create_time').first(); "
     " if s and s.result!=0: r[p._id]=s.result; "
     "print(json.dumps(r))"],
    capture_output=True, text=True, timeout=15
)
failures = {}
for line in r.stdout.split('\n'):
    if line.strip().startswith('{'):
        failures = json.loads(line)
        break

print(f"当前失败: {len(failures)} 题")
print(f"列表: {sorted(failures.keys())}")

# Check each and fix if possible
import re
for nq_id, result in sorted(failures.items()):
    nq_dir = None
    for bank in BOOK.glob("chapter*_bank"):
        for d in bank.glob(nq_id + "*"):
            nq_dir = d
            break
    if not nq_dir:
        continue

    py = nq_dir / "Andy.py"
    cpp = nq_dir / "Andy.cpp"
    if not py.exists():
        continue

    code = py.read_text(encoding="utf-8")
    modified = False

    # Rule 1: binary stdin → text stdin
    if "sys.stdin.buffer" in code:
        code = code.replace("sys.stdin.buffer.read()", "sys.stdin.read()")
        modified = True
        print(f"  {nq_id}: buffer→text")

    # Rule 2: input() → sys.stdin for problems with multiple inputs
    if code.count("input()") >= 2 and "import sys" not in code:
        code = "import sys\ndata = sys.stdin.read().split()\n" + code
        # Don't auto-replace - too risky. Just convert single-value reads
        code = re.sub(r'(\w+)\s*=\s*int\(input\(\)\)', r'\1 = int(data.pop(0))', code)
        code = re.sub(r'(\w+)\s*=\s*float\(input\(\)\)', r'\1 = float(data.pop(0))', code)
        code = re.sub(r'(\w+)\s*=\s*input\(\)', r'\1 = data.pop(0)', code)
        if "data.pop" in code:
            code = code.replace("import sys\n", "import sys\nif 'data' not in dir(): data = sys.stdin.read().split()\n")
            modified = True
            print(f"  {nq_id}: input→sys.stdin")

    # Rule 3: Infinite while loop fix (add n=0 termination check)
    if "while True:" in code and "n:" not in code[:200]:
        code = code.replace("while True:", "while True:\n    if not data: break\n    ", 1)
        modified = True
        print(f"  {nq_id}: while-loop guard")

    if modified:
        py.write_text(code, encoding="utf-8")

print("\n修复完成。运行以下命令验证：")
for nq_id in sorted(failures.keys()):
    print(f"  python3 scripts/submit_cli.py --nq {nq_id} --lang py")
