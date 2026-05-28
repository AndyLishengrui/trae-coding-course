#!/usr/bin/env python3
"""批量验证Python代码在localhost上的AC状态"""
import sys, os, time, json, subprocess, re
from pathlib import Path

BOOK_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(BOOK_ROOT / 'scripts' / 'xmuoj_cli'))
from client import XmuojClient

TOKEN = '63310cdaec0bc93b08f856568e125e75'
BASE = 'http://localhost'

# Chapter problem lists (AcWing IDs)
CHAPTERS = {
    1: [1, 608, 604, 606, 609, 615, 616, 653, 654, 605, 611, 612, 613, 614],
    2: [665, 660, 659, 664, 667, 669, 670, 657, 671, 662, 666, 668, 672, 663],
    3: [708, 709, 712, 714, 716, 721, 720, 724, 723, 710, 711, 718, 715, 713],
}

def find_py_file(acw_id):
    """Find Python file by AcWing ID in chapter banks."""
    for ch in range(1, 17):
        bank = BOOK_ROOT / f"chapter{ch}_bank"
        for d in bank.iterdir():
            if d.is_dir() and f"ACW{acw_id}" in d.name:
                py = d / "Andy.py"
                if py.exists():
                    return str(py)
    return None

def check_result(sub_id, max_wait=20):
    """Poll for submission result."""
    for _ in range(max_wait):
        time.sleep(2)
        resp = subprocess.run(
            ['curl', '-s', f'{BASE}/api/submission?id={sub_id}',
             '-H', f'Authorization: Bearer {TOKEN}'],
            capture_output=True, text=True
        ).stdout
        try:
            d = json.loads(resp)
            data = d.get('data', d)
            r = data.get('result', -2)
            if r != -2:  # -2 = pending, -1 = judging
                label = data.get('result_label', str(r))
                info = data.get('info', {})
                err_info = data.get('statistic_info', {}).get('err_info', '')
                return r, label, err_info, info
        except:
            pass
    return -2, "timeout", "", {}

def main():
    client = XmuojClient(token=TOKEN, base_url=BASE)

    total_ac = 0
    total_all = 0

    for ch in sorted(CHAPTERS.keys()):
        pids = CHAPTERS[ch]
        print(f"\n{'='*60}")
        print(f"第{ch}章 Python AC验证 ({len(pids)}题)")
        print(f"{'='*60}")

        ch_ac = 0
        for pid in pids:
            total_all += 1
            display_id = f"ACW{pid}"

            # Find problem on OJ
            try:
                prob = client.get_problem(display_id=display_id)
                if not prob or not isinstance(prob, dict):
                    print(f"  ⚠️  {display_id}: 题目不存在")
                    continue
                pid_int = prob.get('id')
            except Exception as e:
                print(f"  ⚠️  {display_id}: 查询失败 ({e})")
                continue

            # Find Python file
            py_file = find_py_file(pid)
            if not py_file:
                print(f"  ⚠️  {display_id}: 本地无Python代码")
                continue

            code = Path(py_file).read_text(encoding='utf-8').strip()
            if not code or code.startswith('# AcWing') and len(code) < 50:
                print(f"  ⚠️  {display_id}: Python代码为空")
                continue

            # Submit
            try:
                result = client.submit(pid_int, code, 'Python3')
                sub_id = result.get('submission_id', result.get('id'))
                if not sub_id:
                    print(f"  ❌ {display_id}: 提交失败")
                    continue
            except Exception as e:
                print(f"  ❌ {display_id}: 提交异常 ({e})")
                continue

            # Check result
            verdict, label, err_info, info = check_result(sub_id)

            if verdict == 0:
                print(f"  ✅ {display_id}: AC")
                ch_ac += 1
                total_ac += 1
            elif verdict == -2:
                print(f"  ⏰ {display_id}: 超时未出结果")
            else:
                print(f"  ❌ {display_id}: {label} (verdict={verdict})")
                if err_info:
                    print(f"       {err_info[:150]}")

        print(f"\n  第{ch}章: {ch_ac}/{len(pids)} AC")

    print(f"\n{'='*60}")
    print(f"总计: {total_ac}/{total_all} AC")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
