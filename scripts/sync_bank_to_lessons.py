#!/usr/bin/env python3
"""Sync verified AC code from chapterN_bank to lessons_v2 and acwing_codes."""

import json, re, os, shutil, subprocess
from pathlib import Path

BOOK_ROOT = Path(__file__).parent.parent.resolve()

def load_mapping():
    with open(BOOK_ROOT / "scripts" / "nq_mapping.json") as f:
        return json.load(f)

def find_bank_dir(ch, acw):
    """Find the bank directory for a given chapter and ACW number."""
    bank_dir = BOOK_ROOT / f"chapter{ch}_bank"
    if not bank_dir.exists():
        return None
    for entry in bank_dir.iterdir():
        if entry.is_dir():
            # Match "ACW001.Something" pattern
            m = re.match(r'ACW0*(\d+)', entry.name)
            if m and int(m.group(1)) == acw:
                return entry
    return None

def compute_nq_num(nq_id):
    """Compute the cumulative NQ number from NQ ID like 'NQ1-01'."""
    # Load mapping to compute cumulative index
    with open(BOOK_ROOT / "scripts" / "nq_mapping.json") as f:
        mapping = json.load(f)

    # Count all entries before this one
    ch_num = int(nq_id.split('-')[0][2:])  # e.g., NQ1 -> 1
    idx = int(nq_id.split('-')[1])  # e.g., 01

    # Count cumulative: sum of all entries from previous chapters + idx
    cumulative = 0
    for ch in range(1, ch_num):
        cumulative += sum(1 for k, v in mapping.items() if v['ch'] == ch)
    cumulative += idx
    return cumulative

def find_acwing_code_file(acw):
    """Find the C++ file in acwing_codes/ that matches a given ACW number."""
    acwing_dir = BOOK_ROOT / "acwing_codes"
    for root, dirs, files in os.walk(str(acwing_dir)):
        for f in files:
            if f.endswith('.cpp'):
                # Match "AcWing 123. Title.cpp" pattern
                m = re.search(r'AcWing\s+(\d+)', f)
                if m and int(m.group(1)) == acw:
                    return Path(root) / f
    return None

def main():
    mapping = load_mapping()

    # Filter chapters 1-8
    chapters_1_8 = {}
    for nq_id, info in mapping.items():
        ch = info['ch']
        if 1 <= ch <= 8:
            chapters_1_8[nq_id] = info

    print(f"Found {len(chapters_1_8)} problems in chapters 1-8")

    updates_lesson = 0
    updates_acwing = 0
    errors = []

    for nq_id, info in sorted(chapters_1_8.items(), key=lambda x: (x[1]['ch'], x[1]['idx'])):
        ch = info['ch']
        acw = info['acw']
        nq_cumulative = compute_nq_num(nq_id)
        lesson_num = f"lesson{ch:02d}"

        # Find bank directory
        bank_dir = find_bank_dir(ch, acw)
        if not bank_dir:
            errors.append(f"[{nq_id}] Bank dir not found for ACW{acw} in chapter{ch}_bank")
            continue

        # Source files
        src_py = bank_dir / "Andy.py"
        src_cpp = bank_dir / "Andy.cpp"

        # Target files in lessons_v2
        target_dir = BOOK_ROOT / "lessons_v2" / lesson_num / "codes"
        target_py = target_dir / f"nq{nq_cumulative:03d}_acw{acw}.py"
        target_cpp = target_dir / f"nq{nq_cumulative:03d}_acw{acw}.cpp"

        lesson_updated = False

        # Copy Andy.py
        if src_py.exists():
            content_py = src_py.read_bytes()
            if not target_py.exists() or target_py.read_bytes() != content_py:
                target_py.parent.mkdir(parents=True, exist_ok=True)
                target_py.write_bytes(content_py)
                print(f"  [PY] {nq_id} ACW{acw}: {target_py.name} UPDATED")
                updates_lesson += 1
                lesson_updated = True
        else:
            errors.append(f"[{nq_id}] Andy.py not found in {bank_dir}")

        # Copy Andy.cpp
        if src_cpp.exists():
            content_cpp = src_cpp.read_bytes()
            if not target_cpp.exists() or target_cpp.read_bytes() != content_cpp:
                target_cpp.parent.mkdir(parents=True, exist_ok=True)
                target_cpp.write_bytes(content_cpp)
                print(f"  [CPP] {nq_id} ACW{acw}: {target_cpp.name} UPDATED")
                updates_lesson += 1
                lesson_updated = True
        else:
            errors.append(f"[{nq_id}] Andy.cpp not found in {bank_dir}")

        if not lesson_updated:
            print(f"  [OK] {nq_id} ACW{acw}: already synced")

        # Update acwing_codes/ with verified C++ code
        acwing_file = find_acwing_code_file(acw)
        if acwing_file and src_cpp.exists():
            cpp_content = src_cpp.read_bytes()
            if acwing_file.read_bytes() != cpp_content:
                acwing_file.write_bytes(cpp_content)
                print(f"  [ACW] {nq_id} ACW{acw}: {acwing_file.name} UPDATED in acwing_codes")
                updates_acwing += 1

    print(f"\n{'='*60}")
    print(f"SUMMARY: {updates_lesson} lesson files updated, {updates_acwing} acwing_codes files updated")
    if errors:
        print(f"\nERRORS ({len(errors)}):")
        for e in errors:
            print(f"  {e}")
    return errors

if __name__ == "__main__":
    errors = main()
    if errors:
        exit(1)
