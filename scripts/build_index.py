#!/usr/bin/env python3
"""Build the structured problem bank index (index.json)"""
import json, os

BASE = '/Users/andyshengruilee/Downloads/基于Trae的编程兴趣班入门百练'
GRAMMAR_DIR = os.path.join(BASE, 'source/grammar')
ALGO_DIR = os.path.join(BASE, 'source/algorithm')

# Week assignments based on curriculum plan
# Week 1-10: Grammar (Contest 271)
WEEK_GRAMMAR = {
    # Week 1: C++入门与顺序结构
    1: ['A01', 'A02', 'A03', 'A04', 'D01', 'D02'],
    # Week 2: 条件判断(1)
    2: ['A05', 'A06', 'A07', 'A03'],
    # Week 3: 条件判断(2) + 排序
    3: ['A08', 'A09', 'D03', 'D04'],
    # Week 4: 循环结构
    4: ['A01', 'A02', 'D05', 'D06', 'D12', 'D13'],
    # Week 5: 一维数组
    5: ['B01', 'D07', 'D06', 'D01', 'D02', 'D03', 'D04'],
    # Week 6: 二维数组(1)
    6: ['B02', 'B03', 'B04', 'B05', 'D08', 'D09', 'D10', 'D11'],
    # Week 7: 二维数组(2)
    7: ['B06', 'B07', 'B08'],
    # Week 8: 字符串(1)
    8: ['C01', 'C02', 'C03', 'C04', 'D14', 'D15', 'D16'],
    # Week 9: 字符串(2)
    9: ['C05', 'C06', 'C07', 'C08', 'D17', 'D18'],
    # Week 10: 字符串(3) + 综合
    10: ['C09', 'C10', 'D19', 'D20', 'D05'],
}

# Week 11-16: Algorithm (NQ100)
WEEK_ALGORITHM = {
    11: ['NQ058', 'NQ059', 'NQ060', 'NQ069', 'NQ070', 'NQ071'],
    12: ['NQ063', 'NQ064', 'NQ065', 'NQ066', 'NQ073', 'NQ075', 'NQ076'],
    13: ['NQ072', 'NQ074', 'NQ077', 'NQ078', 'NQ079', 'NQ080'],
    14: ['NQ089', 'NQ090', 'NQ091', 'NQ092'],
    15: ['NQ067', 'NQ083', 'NQ084', 'NQ085', 'NQ086', 'NQ088'],
    16: ['NQ093', 'NQ094', 'NQ099', 'NQ100'],
}

# Topic tags for each grammar problem
GRAMMAR_TOPICS = {
    'A01': ['输入输出', '浮点数', '加权平均'],
    'A02': ['输入输出', '浮点数', '加权平均'],
    'A03': ['条件判断', '区间判断'],
    'A04': ['循环', '区间统计'],
    'A05': ['条件判断', '时间计算'],
    'A06': ['条件判断', '时间计算'],
    'A07': ['条件判断', '逻辑运算'],
    'A08': ['排序', '比较'],
    'A09': ['循环', '乘法表', '格式化输出'],
    'B01': ['二维数组', '行遍历', '求和/平均'],
    'B02': ['二维数组', '对角线', '区域求和'],
    'B03': ['二维数组', '次对角线', '区域求和'],
    'B04': ['二维数组', '对角线', '区域求和'],
    'B05': ['二维数组', '对角线', '区域求和'],
    'B06': ['二维数组', '回字形', '矩阵构造'],
    'B07': ['二维数组', '矩阵构造'],
    'B08': ['二维数组', '幂次', '矩阵构造'],
    'C01': ['字符串', '模拟', '游戏'],
    'C02': ['字符串', '匹配'],
    'C03': ['字符串', '空格处理'],
    'C04': ['字符串', '连续字符', '遍历'],
    'C05': ['字符串', '单词', '最长'],
    'C06': ['字符串', '倒排', '单词'],
    'C07': ['字符串', '循环移位', '子串'],
    'C08': ['字符串', '乘方', '连接'],
    'C09': ['字符串', '最大跨距', '子串查找'],
    'C10': ['字符串', '公共后缀'],
    'D01': ['数组', '替换'],
    'D02': ['数组', '填充', '递推'],
    'D03': ['数组', '选择', '过滤'],
    'D04': ['数组', '翻转'],
    'D05': ['循环', '斐波那契', '递推'],
    'D06': ['数组', '最小值', '位置'],
    'D07': ['二维数组', '列遍历', '求和/平均'],
    'D08': ['二维数组', '主对角线', '下半部分'],
    'D09': ['二维数组', '次对角线', '下半部分'],
    'D10': ['二维数组', '对角线', '下方区域'],
    'D11': ['二维数组', '对角线', '右方区域'],
    'D12': ['字符串', '长度'],
    'D13': ['字符串', '数字统计'],
    'D14': ['字符串', '加空格'],
    'D15': ['字符串', '字符替换'],
    'D16': ['字符串', '插入', 'ASCII码'],
    'D17': ['字符串', '出现次数', '哈希'],
    'D18': ['字符串', '忽略大小写', '比较'],
    'D19': ['字符串', '加密', '循环移位'],
    'D20': ['字符串', '单词替换'],
}

# Algorithm topics for each NQ problem
ALGORITHM_TOPICS = {
    'NQ058': ['双指针', '两数之和'],
    'NQ059': ['双指针', '三数之和'],
    'NQ060': ['双指针', '四数之和', '排序'],
    'NQ063': ['动态规划', '斐波那契', '递推'],
    'NQ064': ['记忆化递归', '递推'],
    'NQ065': ['递归', '阶乘'],
    'NQ066': ['优先队列', '数学'],
    'NQ067': ['动态规划', '铺砖问题'],
    'NQ069': ['二分查找', '双指针'],
    'NQ070': ['二分查找', '最接近元素'],
    'NQ071': ['二分查找', '贪心', '最大化最小值'],
    'NQ072': ['DFS', '回溯', 'N皇后'],
    'NQ073': ['递归', '波兰表达式'],
    'NQ074': ['回溯', '八皇后', '预处理'],
    'NQ075': ['数学', '进制转换'],
    'NQ076': ['快速幂', '数学'],
    'NQ077': ['暴力枚举', '排序', '去重'],
    'NQ078': ['递归下降', '表达式求值'],
    'NQ079': ['回溯', '24点'],
    'NQ080': ['DFS', '回溯', '质数环'],
    'NQ083': ['动态规划', 'LCS', '最长公共子序列'],
    'NQ084': ['哈希', '同构字符串'],
    'NQ085': ['动态规划', '数字三角形'],
    'NQ086': ['动态规划', '背包问题'],
    'NQ088': ['动态规划', '记忆化搜索'],
    'NQ089': ['贪心', '二分', '最长子序列'],
    'NQ090': ['DFS', '记忆化搜索', '矩形切割'],
    'NQ091': ['DFS', '回溯', '骑士遍历'],
    'NQ092': ['BFS', '最短路径', '骑士移动'],
    'NQ093': ['图论', '拓扑排序'],
    'NQ094': ['图论', '拓扑排序', 'DP', '可达性'],
    'NQ099': ['图论', 'Dijkstra', '最短路'],
    'NQ100': ['BFS', '状态空间搜索'],
}

# Difficulty: 1=入门, 2=基础, 3=进阶, 4=挑战, 5=综合
GRAMMAR_DIFFICULTY = {pid: 1 for pid in [f'{c}{n:02d}' for c in 'ABCD' for n in range(1, 21)]}
# Bump difficulty for B and C series
for pid in GRAMMAR_DIFFICULTY:
    if pid.startswith('B'):
        GRAMMAR_DIFFICULTY[pid] = 2
    elif pid.startswith('C'):
        GRAMMAR_DIFFICULTY[pid] = 2
    elif pid.startswith('D') and int(pid[1:]) > 10:
        GRAMMAR_DIFFICULTY[pid] = 2

ALGORITHM_DIFFICULTY = {
    'NQ058': 2, 'NQ059': 2, 'NQ060': 3,
    'NQ063': 2, 'NQ064': 2, 'NQ065': 2, 'NQ066': 3,
    'NQ067': 3, 'NQ069': 2, 'NQ070': 2, 'NQ071': 3,
    'NQ072': 3, 'NQ073': 2, 'NQ074': 3, 'NQ075': 2,
    'NQ076': 2, 'NQ077': 3, 'NQ078': 3, 'NQ079': 3, 'NQ080': 3,
    'NQ083': 3, 'NQ084': 2, 'NQ085': 3, 'NQ086': 4, 'NQ088': 4,
    'NQ089': 3, 'NQ090': 4, 'NQ091': 3, 'NQ092': 3,
    'NQ093': 3, 'NQ094': 4, 'NQ099': 5, 'NQ100': 5,
}

# Determine role: which problems are 例题 (demonstration) vs 练习 (practice)
# Each week has 2-3 例题 and the rest are 练习
def assign_role(pid, week_data):
    for wk, pids in week_data.items():
        if pid in pids:
            idx = pids.index(pid)
            if idx < 3:
                return '例题'
            return '练习'
    return '未知'

# Build index
index = {'problems': {}, 'weeks': {}, 'topics': []}

# Grammar problems
for pid in [d for d in os.listdir(GRAMMAR_DIR) if os.path.isdir(os.path.join(GRAMMAR_DIR, d))]:
    readme = os.path.join(GRAMMAR_DIR, pid, 'README.md')
    title = ''
    if os.path.exists(readme):
        with open(readme) as f:
            first = f.readline()
            title = first.replace('#', '').strip().replace(pid, '').strip()

    topics = GRAMMAR_TOPICS.get(pid, ['语法'])
    difficulty = GRAMMAR_DIFFICULTY.get(pid, 1)
    role = assign_role(pid, WEEK_GRAMMAR)

    index['problems'][pid] = {
        'id': pid,
        'title': title,
        'section': 'grammar',
        'topics': topics,
        'difficulty': difficulty,
        'algorithms': ['模拟'],
        'weeks': [wk for wk, pids in WEEK_GRAMMAR.items() if pid in pids],
        'role': role,
        'source': 'Contest 271',
        'cpp': 'source/grammar/{}/{}_improved.cpp'.format(pid, pid),
        'python': 'source/grammar/{}/{}_improved.py'.format(pid, pid),
        'markdown': 'source/grammar/{}/README.md'.format(pid),
    }

# Algorithm problems
for pid in [d for d in os.listdir(ALGO_DIR) if d.startswith('NQ') and os.path.isdir(os.path.join(ALGO_DIR, d))]:
    # Skip X variants
    if 'X' in pid:
        continue

    if pid not in sum(WEEK_ALGORITHM.values(), []):
        continue  # Skip unassigned problems

    readme = os.path.join(ALGO_DIR, pid, 'README.md')
    title = ''
    if os.path.exists(readme):
        with open(readme) as f:
            first = f.readline()
            title = first.replace('#', '').strip().replace(pid, '').strip()

    topics = ALGORITHM_TOPICS.get(pid, ['算法'])
    difficulty = ALGORITHM_DIFFICULTY.get(pid, 3)
    role = assign_role(pid, WEEK_ALGORITHM)

    algos = ALGORITHM_TOPICS.get(pid, [])
    algorithms = [t for t in algos if t not in topics[:2]]

    index['problems'][pid] = {
        'id': pid,
        'title': title,
        'section': 'algorithm',
        'topics': topics,
        'difficulty': difficulty,
        'algorithms': algorithms,
        'weeks': [wk for wk, pids in WEEK_ALGORITHM.items() if pid in pids],
        'role': role,
        'source': 'NQ100',
        'cpp': 'source/algorithm/{}/{}_improved.cpp'.format(pid, pid),
        'python': 'source/algorithm/{}/{}_improved.py'.format(pid, pid),
        'markdown': 'source/algorithm/{}/README.md'.format(pid),
    }

# Build week summaries
for wk in range(1, 17):
    grammar_pids = WEEK_GRAMMAR.get(wk, [])
    algo_pids = WEEK_ALGORITHM.get(wk, [])
    all_pids = grammar_pids + algo_pids
    index['weeks'][str(wk)] = {
        'problems': all_pids,
        'count': len(all_pids),
    }

# Collect all unique topics
all_topics = set()
for p in index['problems'].values():
    all_topics.update(p['topics'])
    all_topics.update(p['algorithms'])
index['topics'] = sorted(all_topics)

# Write index.json
out_path = os.path.join(BASE, '02_题库/index.json')
os.makedirs(os.path.join(BASE, '02_题库'), exist_ok=True)
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(index, f, ensure_ascii=False, indent=2)

print('Index built!')
print('Total problems: {}'.format(len(index['problems'])))
print('Grammar: {}'.format(sum(1 for p in index['problems'].values() if p['section'] == 'grammar')))
print('Algorithm: {}'.format(sum(1 for p in index['problems'].values() if p['section'] == 'algorithm')))
print('Unique topics: {}'.format(len(index['topics'])))
for wk in sorted(index['weeks'].keys(), key=int):
    w = index['weeks'][wk]
    print('Week {}: {} problems'.format(wk, w['count']))
print('Output: {}'.format(out_path))
