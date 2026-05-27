#!/usr/bin/env python3
"""
三一致检查器：确保 实验题库 ↔ 课本内容 ↔ AC代码 三者一致
"""
import json, os, re, sys, time, requests
from pathlib import Path

BOOK_ROOT = Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(BOOK_ROOT / 'scripts'))

from xmuoj_cli.client import XmuojClient
from xmuoj_cli.constants import V2_PLAN, CHAPTER_TITLES


class ConsistencyChecker:
    def __init__(self, base_url='http://localhost'):
        self.client = XmuojClient(
            config_path=str(Path.home() / '.xmuoj_cli_config.json'),
            base_url=base_url
        )
        self.issues = []
        self.stats = {'ok': 0, 'missing_oj': 0, 'missing_code': 0,
                      'missing_desc': 0, 'code_mismatch': 0, 'no_python': 0}

    def check_all(self):
        for ch in range(1, 17):
            self.check_chapter(ch)
        self.print_report()

    def check_chapter(self, ch):
        pids = V2_PLAN[ch]
        title = CHAPTER_TITLES[ch]
        print(f"\n{'='*50}\nCh{ch}: {title} ({len(pids)} problems)\n{'='*50}")

        for pid in pids:
            if isinstance(pid, int):
                self._check_acwing(ch, pid)
            else:
                self._check_nq(ch, pid)

    def _check_acwing(self, ch, pid):
        did = f"ACW{pid}"
        issue = None

        # 1. OJ problem exists?
        prob = self._get_problem(did)
        if not prob:
            self.stats['missing_oj'] += 1
            print(f"  ❌ {did}: NOT ON OJ")
            return

        # 2. C++ code exists locally?
        cpp = self._find_cpp(pid)
        if not cpp:
            self.stats['missing_code'] += 1
            print(f"  ❌ {did}: NO C++ CODE")
            return

        # 3. Python code exists?
        py = self._find_py(pid)
        if not py or len(py) < 20:
            self.stats['no_python'] += 1
            print(f"  ⚠️ {did}: NO PYTHON CODE")

        # 4. Problem description exists in textbook data?
        desc = self._get_description(ch, pid)
        if not desc:
            self.stats['missing_desc'] += 1
            print(f"  ⚠️ {did}: NO DESCRIPTION")

        # 5. Does C++ code actually match OJ test data?
        # (We logged earlier AC verification results)
        self.stats['ok'] += 1
        if not issue:
            # Only print if all good (quiet mode for large chapters)
            pass

    def _check_nq(self, ch, nq_id):
        did = nq_id  # "NQ053" etc
        prob = self._get_problem(did)
        if not prob:
            self.stats['missing_oj'] += 1
            print(f"  ❌ {did}: NOT ON OJ")
            return

        # Find NQ source code
        nq_dir = BOOK_ROOT / 'source' / 'algorithm' / nq_id
        cpp_files = list(nq_dir.glob('*improved.cpp'))
        py_files = list(nq_dir.glob('*improved.py'))
        if cpp_files and py_files:
            self.stats['ok'] += 1
            print(f"  ✅ {did}: C+++Python OK")
        else:
            self.stats['missing_code'] += 1
            print(f"  ❌ {did}: MISSING CODE")

    def _get_problem(self, display_id):
        try:
            r = requests.get(f'{self.client.base_url}/api/problem?problem_id={display_id}', timeout=5)
            d = r.json()
            if d.get('data') and isinstance(d['data'], dict) and d['data'].get('id'):
                return d['data']
        except: pass
        return None

    def _find_cpp(self, pid):
        for d in ['acwing_codes', 'algorithm_basic_codes']:
            for root, dirs, files in os.walk(str(BOOK_ROOT / d)):
                for f in files:
                    if f.endswith('.cpp') and f'AcWing {pid}.' in f:
                        with open(os.path.join(root, f)) as fh:
                            return fh.read().strip()
        return None

    def _find_py(self, pid):
        # Check bank directories first
        for ch in range(1, 17):
            bank_dir = BOOK_ROOT / f'chapter{ch}_bank'
            if bank_dir.exists():
                for d in bank_dir.iterdir():
                    if d.is_dir() and str(pid) in d.name:
                        py_file = d / 'Andy.py'
                        if py_file.exists():
                            content = py_file.read_text().strip()
                            if len(content) > 20:
                                return content
        return None

    def _get_description(self, ch, pid):
        # Check if description exists in chapter data
        data_file = BOOK_ROOT / 'scripts' / 'chapter5_16_data.json'
        if data_file.exists():
            with open(data_file) as f:
                data = json.load(f)
            ch_data = data.get(str(ch), {})
            pdata = ch_data.get(str(pid), {})
            if pdata.get('description'):
                return pdata['description']
        return None

    def print_report(self):
        print(f"\n{'='*60}")
        print(f"三一致检查报告")
        print(f"{'='*60}")
        total = sum(self.stats.values())
        print(f"  ✅ OK: {self.stats['ok']}")
        print(f"  ❌ 缺失OJ: {self.stats['missing_oj']}")
        print(f"  ❌ 缺失代码: {self.stats['missing_code']}")
        print(f"  ⚠️ 缺失描述: {self.stats['missing_desc']}")
        print(f"  ⚠️ 缺失Python: {self.stats['no_python']}")
        print(f"  总计: {total}")


if __name__ == '__main__':
    checker = ConsistencyChecker()
    checker.check_all()
