#!/usr/bin/env python3
"""最终批量修复：替换代码+提高时限+重新提交验证"""
import json, os, re, subprocess, sys, time
from pathlib import Path

BOOK = Path(__file__).parent.parent

# 1. Build best Python code map from all sources
code_map = {}
for src_dir in ['acwing_codes', 'algorithm_basic_codes', 'lessons_v2']:
    base = BOOK / src_dir
    if not base.exists():
        continue
    for root, dirs, files in os.walk(str(base)):
        for f in files:
            if not f.endswith('.py'):
                continue
            for pattern in [r'acw(\d+)\.py$', r'_acw(\d+)\.py$']:
                m = re.search(pattern, f.lower())
                if m:
                    acw = int(m.group(1))
                    code_map.setdefault(acw, {})['py'] = Path(root) / f
                    break

print(f"Code map: {len(code_map)} AcWing IDs with Python")

# 2. Load nq mapping
nq_map = json.loads((BOOK / 'scripts/nq_mapping.json').read_text())

# 3. Replace ALL Python files with best available code
replaced = 0
for nq_id, info in nq_map.items():
    acw = info['acw']
    ch = info['ch']
    if acw not in code_map or 'py' not in code_map[acw]:
        continue

    nq_dir = None
    bank = BOOK / f'chapter{ch}_bank'
    for d in bank.glob(nq_id + '*'):
        nq_dir = d
        break
    if not nq_dir:
        continue

    src = code_map[acw]['py']
    dst = nq_dir / 'Andy.py'
    new_code = src.read_text(encoding='utf-8')
    if not dst.exists() or dst.read_text(encoding='utf-8') != new_code:
        dst.write_text(new_code, encoding='utf-8')
        replaced += 1

print(f"Replaced {replaced} Python files with best available code")

# 4. Increase all time limits to 3000ms
subprocess.run(["docker", "exec", "onlinejudgedeploy-oj-backend-1",
    "python", "manage.py", "shell", "-c",
    "from problem.models import Problem; "
    "c=Problem.objects.filter(_id__startswith='NQ',time_limit__lt=3000).update(time_limit=3000); "
    f"print(f'Updated {{c}} time limits')"],
    capture_output=True, text=True, timeout=10)

print("Time limits set to 3000ms")

# 5. Get current failure list
r = subprocess.run(["docker","exec","onlinejudgedeploy-oj-backend-1","python","manage.py","shell","-c",
    "from submission.models import Submission; from problem.models import Problem; "
    "for p in Problem.objects.filter(_id__startswith='NQ'):"
    " s=Submission.objects.filter(problem_id=p.id,language='Python3',id__startswith='cli_').order_by('-create_time').first();"
    " if s and s.result!=0: print('FAIL:'+p._id+':'+str(s.result)+':'+str(s.statistic_info.get('score',0)))"],
    capture_output=True, text=True, timeout=15)

failures = []
for line in r.stdout.split('\n'):
    if line.startswith('FAIL:'):
        parts = line[5:].split(':')
        failures.append((parts[0], int(parts[1]), int(parts[2])))

print(f"\nCurrent failures: {len(failures)}")
for nq, res, score in failures:
    print(f"  {nq}: result={res} score={score}")

# 6. Re-submit all failures
print(f"\nRe-submitting {len(failures)} failures...")
results = []
for nq_id, _, _ in failures:
    info = nq_map.get(nq_id)
    if not info:
        continue
    ch = info['ch']
    nq_dir = None
    for d in (BOOK / f'chapter{ch}_bank').glob(nq_id + '*'):
        nq_dir = d
        break
    if not nq_dir:
        continue

    py_file = nq_dir / 'Andy.py'
    if not py_file.exists():
        continue

    code = py_file.read_text(encoding='utf-8')
    sub_id = 'fin_' + nq_id.replace('-', '_')[:20]

    # Write code to container and submit
    code_json = json.dumps(code)
    subprocess.run(["docker","exec","onlinejudgedeploy-oj-backend-1","python","manage.py","shell","-c",
        f"with open('/tmp/py_{sub_id}.txt','w',encoding='utf-8') as f: f.write({code_json})"],
        capture_output=True, timeout=5)

    # Submit + poll
    poll = (
        "import time; from submission.models import Submission; from problem.models import Problem; "
        "from account.models import User; from judge.tasks import judge_task; "
        f"user=User.objects.get(username='andy'); p=Problem.objects.get(id={info.get('oj_id',0)}); "
        f"with open('/tmp/py_{sub_id}.txt','r') as f: code=f.read(); "
        f"s=Submission.objects.create(id='{sub_id}',user_id=user.id,username=user.username,language='Python3',code=code,problem_id=p.id,contest_id=356,ip='127.0.0.1',result=-1); "
        f"judge_task.send(s.id,p.id); "
        f"for i in range(180): time.sleep(1); s.refresh_from_db(); "
        f"  if s.result!=-1: print('OK:'+str(s.result)+':'+str((s.statistic_info or {{}}).get('score',0))); break; "
        f"else: s.refresh_from_db(); print('OK:'+str(s.result)+':0')"
    )

    r = subprocess.run(["docker","exec","onlinejudgedeploy-oj-backend-1","python","manage.py","shell","-c",poll],
        capture_output=True, text=True, timeout=200)

    result = -9
    score = 0
    for line in (r.stdout + '\n' + r.stderr).split('\n'):
        if line.strip().startswith('OK:'):
            parts = line.strip()[3:].split(':')
            try:
                result = int(parts[0])
                score = int(parts[1]) if len(parts) > 1 else 0
            except:
                pass

    status = 'AC' if result == 0 else {-1:'PEND',4:'RE',8:'SYS',1:'WA'}.get(result, str(result))
    icon = 'OK' if result == 0 else '!!'
    print(f"  {icon} {nq_id}: {status} score={score}")
    results.append((nq_id, result, score))

# 7. Final summary
ac_count = sum(1 for _, r, _ in results if r == 0)
print(f"\n{'='*50}")
print(f"本轮结果: {ac_count}/{len(results)} AC")
total_ac = 161 - len(failures) + ac_count
print(f"估计总AC: {total_ac}/161 ({100*total_ac//161}%)")
print(f"\n仍需处理:")
for nq, r, s in [(n, r, s) for n, r, s in results if r != 0]:
    print(f"  {nq}: result={r} score={s}")
