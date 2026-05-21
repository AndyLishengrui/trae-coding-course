#!/usr/bin/env python3
"""Migrate NQ100 algorithm problems to source/algorithm/"""
import os, re, shutil

NQ100_DIR = '/Users/andyshengruilee/Downloads/基于Trae的编程兴趣班入门百练/兴趣班入门百练讲义/NQ100'
TARGET_DIR = '/Users/andyshengruilee/Downloads/基于Trae的编程兴趣班入门百练/source/algorithm'

os.makedirs(TARGET_DIR, exist_ok=True)

stats = {'total': 0, 'has_md': 0, 'has_docx': 0, 'has_cpp': 0, 'has_py': 0}

# Scan all NQ dirs
dirs = sorted([d for d in os.listdir(NQ100_DIR) if d.startswith('NQ') and os.path.isdir(os.path.join(NQ100_DIR, d))])

for dname in dirs:
    dpath = os.path.join(NQ100_DIR, dname)
    files = os.listdir(dpath)

    stats['total'] += 1

    # Find key files
    sldoc_file = None  # 思路.md
    docx_file = None
    cpp_file = None
    py_file = None
    other_cpp = []

    for f in files:
        full = os.path.join(dpath, f)
        if f == '思路.md':
            sldoc_file = full
        elif f.startswith('~$'):
            continue
        elif f.endswith('.docx') and f.startswith('NQ'):
            docx_file = full
        elif '_improved.cpp' in f:
            cpp_file = full
        elif '_improved.py' in f:
            py_file = full

    if sldoc_file:
        stats['has_md'] += 1
    if docx_file:
        stats['has_docx'] += 1
    if cpp_file:
        stats['has_cpp'] += 1
    if py_file:
        stats['has_py'] += 1

    # Create target directory
    target = os.path.join(TARGET_DIR, dname)
    os.makedirs(target, exist_ok=True)

    # Copy 思路.md
    if sldoc_file:
        with open(sldoc_file, 'r', encoding='utf-8') as f:
            md_content = f.read()
        with open(os.path.join(target, 'README.md'), 'w', encoding='utf-8') as f:
            f.write(md_content)

    # Copy code files
    if cpp_file:
        shutil.copy2(cpp_file, os.path.join(target, os.path.basename(cpp_file)))
    if py_file:
        shutil.copy2(py_file, os.path.join(target, os.path.basename(py_file)))

print('Migration complete!')
print('Total: {}'.format(stats['total']))
print('  思路.md: {}'.format(stats['has_md']))
print('  docx: {}'.format(stats['has_docx']))
print('  C++: {}'.format(stats['has_cpp']))
print('  Python: {}'.format(stats['has_py']))

# Report missing
missing_md = [d for d in dirs if not os.path.exists(os.path.join(TARGET_DIR, d, 'README.md'))]
if missing_md:
    print('\nMissing 思路.md:')
    for m in missing_md:
        print('  ' + m)
