#!/usr/bin/env python3
"""Generate human-readable index.md from index.json"""
import json, os

BASE = '/Users/andyshengruilee/Downloads/基于Trae的编程兴趣班入门百练'
idx_path = os.path.join(BASE, '02_题库/index.json')

with open(idx_path) as f:
    idx = json.load(f)

# Week theme names
WEEK_THEMES = {
    1: 'C++入门与顺序结构', 2: '条件判断(1)', 3: '条件判断(2) + 排序',
    4: '循环结构', 5: '一维数组', 6: '二维数组(1)', 7: '二维数组(2)',
    8: '字符串(1)', 9: '字符串(2)', 10: '字符串(3) + 综合',
    11: '二分查找与双指针', 12: '递归与分治', 13: 'DFS与回溯',
    14: 'BFS与贪心', 15: '动态规划', 16: '图论与综合',
}

lines = []
lines.append('# 编程兴趣班入门百练 — 题库索引')
lines.append('')
lines.append('共 {} 题（语法 {} 题 + 算法 {} 题），16周课程。'.format(
    len(idx['problems']),
    sum(1 for p in idx['problems'].values() if p['section'] == 'grammar'),
    sum(1 for p in idx['problems'].values() if p['section'] == 'algorithm'),
))
lines.append('')

for wk in sorted(idx['weeks'].keys(), key=int):
    theme = WEEK_THEMES.get(int(wk), '')
    w = idx['weeks'][wk]
    lines.append('## Week {}: {}'.format(wk, theme))
    lines.append('')
    lines.append('| 编号 | 题目 | 类型 | 难度 | 知识点 |')
    lines.append('|------|------|------|------|--------|')

    for pid in w['problems']:
        p = idx['problems'].get(pid)
        if not p:
            continue
        diff = '★' * p['difficulty']
        tags = ', '.join(p['topics'][:3])
        role = '讲' if p['role'] == '例题' else '练'
        lines.append('| {} | {} | {} | {} | {} |'.format(
            pid, p['title'], role, diff, tags))

    lines.append('')

# Topic index
lines.append('---')
lines.append('')
lines.append('## 知识点索引')
lines.append('')
for topic in idx['topics'][:50]:  # Top 50
    probs = [pid for pid, p in idx['problems'].items() if topic in p['topics'] or topic in p['algorithms']]
    if probs:
        lines.append('- **{}**：{}'.format(topic, ', '.join(probs[:6])))
        if len(probs) > 6:
            lines.append('  (+ {} more)'.format(len(probs) - 6))

out = os.path.join(BASE, '02_题库/index.md')
with open(out, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print('Written: {}'.format(out))
print('{} lines'.format(len(lines)))
