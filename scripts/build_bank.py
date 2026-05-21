#!/usr/bin/env python3
"""Build unified problem bank from all sources."""
import json, os, re

BASE = '/Users/andyshengruilee/Downloads/基于Trae的编程兴趣班入门百练'
BANK_DIR = os.path.join(BASE, 'problem_bank/problems')
os.makedirs(BANK_DIR, exist_ok=True)

# ── Tag inference rules ──────────────────────────────────────────
def infer_tags(title, desc, acw_id, section=''):
    """Infer topic tags from title and description."""
    tags = set()
    text = (title + ' ' + desc).lower()

    # Input/Output basics
    if any(kw in text for kw in ['输入', '输出', '读取', '打印', 'a+b', '差', '面积', '体积', '距离', '工资', '油耗', '燃料']):
        tags.add('输入输出')
    if any(kw in text for kw in ['整数', '浮点', '实数', 'double', 'float']):
        tags.add('变量与数据类型')

    # Conditionals
    if any(kw in text for kw in ['判断', '区间', '条件', '选择', '如果', '大于', '小于', '三角形', '倍数']):
        tags.add('条件判断')

    # Loops
    if any(kw in text for kw in ['循环', '连续', '序列', '乘法表', '斐波那契', '阶乘', 'for', 'while']):
        tags.add('循环')
    if any(kw in text for kw in ['菱形', '矩阵', '二维']):
        tags.add('嵌套循环')

    # Arrays
    if any(kw in text for kw in ['数组', '矩阵', '替换', '填充', '选择', '翻转', '变换']):
        tags.add('一维数组')
    if any(kw in text for kw in ['二维', '矩阵', '对角线', '上半', '下半', '区域', '蛇形']):
        tags.add('二维数组')

    # Strings
    if any(kw in text for kw in ['字符串', '字符', '单词', '空格', '字母', '子串', '回文', '加密', '密码']):
        tags.add('字符串')

    # Functions
    if any(kw in text for kw in ['函数', '递归', '交换', '最大公约数', '最小公倍数', '排列']):
        tags.add('函数')
    if any(kw in text for kw in ['递归']):
        tags.add('递归')

    # Structs/Pointers
    if any(kw in text for kw in ['链表', '结点', '指针', '引用', '结构体', '删除节点', '合并', '反转']):
        tags.add('链表')
    if any(kw in text for kw in ['结构体', '类', '指针', '引用']):
        tags.add('指针与引用')

    # STL/Bit operations
    if any(kw in text for kw in ['排序', '去重', '队列', '栈', 'stl', 'sort']):
        tags.add('STL容器')
    if any(kw in text for kw in ['位运算', '二进制', '1的个数', '奇数位于偶数']):
        tags.add('位运算')

    # Algorithm tags
    if any(kw in text for kw in ['排序', '升序']):
        tags.add('排序')
    if any(kw in text for kw in ['二分', '查找', '搜索']):
        tags.add('二分查找')
    if any(kw in text for kw in ['双指针', '两数之和', '三数之和', '四数之和']):
        tags.add('双指针')
    if any(kw in text for kw in ['贪心']):
        tags.add('贪心')
    if any(kw in text for kw in ['深度优先', 'dfs', '回溯', '皇后', '24点', '质数环']):
        tags.add('深度优先搜索')
    if any(kw in text for kw in ['广度优先', 'bfs', '最短路径', '迷宫']):
        tags.add('广度优先搜索')
    if any(kw in text for kw in ['动态规划', 'dp', '背包', '最长公共子序列', '最长上升']):
        tags.add('动态规划')
    if any(kw in text for kw in ['拓扑排序', '有向图']):
        tags.add('拓扑排序')
    if any(kw in text for kw in ['dijkstra', '最短路径', '最省赛']):
        tags.add('最短路径')
    if any(kw in text for kw in ['数论', '质数', '约数', '公约', '公倍', '幂']):
        tags.add('数学')

    return sorted(tags)

def infer_difficulty(title, desc, section=''):
    """Infer difficulty 1-5."""
    text = (title + ' ' + desc).lower()
    if any(kw in text for kw in ['最长公共', '背包', '状态空间', '数独', 'dijkstra']):
        return 4
    if any(kw in text for kw in ['dfs', 'bfs', '动态规划', '回溯', '皇后', '拓扑', '记忆化']):
        return 3
    if any(kw in text for kw in ['二维', '矩阵', '递归', '二分', '链表', '指针']):
        return 2
    return 1

def find_best_cpp(dpath, dname):
    """Find the best CPP file in a source directory."""
    # Check for _improved variant first
    improved = os.path.join(dpath, dname + '_improved.cpp')
    if os.path.exists(improved):
        return improved
    # Check for _improved_improved variant
    imp2 = os.path.join(dpath, dname + '_improved_improved.cpp')
    if os.path.exists(imp2):
        return imp2
    # Any .cpp file with 'improved' in name
    for f in sorted(os.listdir(dpath)):
        if f.endswith('.cpp') and 'improved' in f.lower():
            return os.path.join(dpath, f)
    # Fallback to any .cpp file
    for f in sorted(os.listdir(dpath)):
        if f.endswith('.cpp'):
            return os.path.join(dpath, f)
    return None

def find_best_py(dpath, dname):
    """Find the best Python file in a source directory."""
    improved = os.path.join(dpath, dname + '_improved.py')
    if os.path.exists(improved):
        return improved
    imp2 = os.path.join(dpath, dname + '_improved_improved.py')
    if os.path.exists(imp2):
        return imp2
    for f in sorted(os.listdir(dpath)):
        if f.endswith('.py') and 'improved' in f.lower() and f != '__init__.py':
            return os.path.join(dpath, f)
    for f in sorted(os.listdir(dpath)):
        if f.endswith('.py') and f != '__init__.py':
            return os.path.join(dpath, f)
    return None

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def extract_code_from_readme(readme_path):
    """Extract C++ and Python code blocks from a README.md."""
    cpp_code = None
    py_code = None
    if not os.path.exists(readme_path):
        return cpp_code, py_code
    content = read_file(readme_path)
    in_cpp = False
    in_py = False
    cpp_lines = []
    py_lines = []
    for line in content.split('\n'):
        stripped = line.strip()
        if stripped.startswith('```cpp') or stripped.startswith('```c++'):
            in_cpp = True
            cpp_lines = []
            continue
        elif stripped.startswith('```python'):
            in_py = True
            py_lines = []
            continue
        elif stripped == '```':
            if in_cpp:
                cpp_code = '\n'.join(cpp_lines).strip()
                in_cpp = False
            elif in_py:
                py_code = '\n'.join(py_lines).strip()
                in_py = False
            continue
        if in_cpp:
            cpp_lines.append(line)
        elif in_py:
            py_lines.append(line)
    return cpp_code, py_code

def clean_html(html):
    text = html.replace('<br>', '\n').replace('<br/>', '\n').replace('<br />', '\n')
    text = re.sub(r'<[^>]+>', '', text)
    text = text.replace('&quot;', '"').replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>')
    return text.strip()

def format_samples(samples_raw):
    try:
        samples = json.loads(samples_raw) if isinstance(samples_raw, str) else samples_raw
    except:
        return ''
    if not samples:
        return ''
    lines = []
    for i, s in enumerate(samples):
        lines.append('**样例 {}：**'.format(i + 1))
        lines.append('')
        lines.append('输入：')
        lines.append((s.get('input', '') or '').strip())
        lines.append('输出：')
        lines.append((s.get('output', '') or '').strip())
        lines.append('')
    return '\n'.join(lines)


# ── Load sources ──────────────────────────────────────────────────

all_problems = []
pb_counter = [0]  # mutable counter

# 1. AcWing problems from xmuoj
acw_path = '/tmp/acw_all.json'
if os.path.exists(acw_path):
    with open(acw_path) as f:
        acw_data = json.load(f)
    for d in acw_data:
        pb_counter[0] += 1
        pid = 'PB_{:03d}'.format(pb_counter[0])
        title = d['title']
        desc = clean_html(d['description'])
        input_desc = clean_html(d['input_description'])
        output_desc = clean_html(d['output_description'])
        hint = clean_html(d.get('hint', ''))
        samples_md = format_samples(d.get('samples', '[]'))
        tags = infer_tags(title, desc, d['acw_id'])
        diff = infer_difficulty(title, desc)

        all_problems.append({
            'id': pid, 'title': title, 'source': 'AcWing ' + d['acw_id'][3:],
            'source_url': 'https://www.xmuoj.com/problem/' + d['acw_id'],
            'topics': tags, 'difficulty': diff,
            'description': desc, 'input_description': input_desc,
            'output_description': output_desc, 'hint': hint,
            'samples': samples_md, 'oj_problem_id': d['acw_id'],
            'time_limit': d['time_limit'], 'memory_limit': d['memory_limit'],
            'origin_section': 'acwing',
        })
    print('Loaded {} AcWing problems'.format(len(acw_data)))
else:
    print('AcWing data not found at {}'.format(acw_path))


# 2. Contest 271 grammar problems (A01-D20)
grammar_dir = os.path.join(BASE, 'source/grammar')
if os.path.exists(grammar_dir):
    grammar_count = 0
    for dname in sorted(os.listdir(grammar_dir)):
        dpath = os.path.join(grammar_dir, dname)
        readme = os.path.join(dpath, 'README.md')
        if os.path.isdir(dpath) and os.path.exists(readme):
            with open(readme) as f:
                content = f.read()
            # Extract title
            title_match = re.match(r'^#\s*\w+\s+(.+)', content)
            title = title_match.group(1) if title_match else dname

            # Extract sections
            sections = re.split(r'^## ', content, flags=re.MULTILINE)
            desc = ''; input_desc = ''; output_desc = ''; samples_md = ''; hint = ''
            for sec in sections:
                if sec.startswith('题目描述'):
                    desc = sec.replace('题目描述\n', '').strip()
                elif sec.startswith('输入格式'):
                    input_desc = sec.replace('输入格式\n', '').strip()
                elif sec.startswith('输出格式'):
                    output_desc = sec.replace('输出格式\n', '').strip()
                elif sec.startswith('输入输出样例'):
                    samples_md = sec.replace('输入输出样例\n', '').strip()
                elif sec.startswith('提示'):
                    hint = sec.replace('提示\n', '').strip()

            pb_counter[0] += 1
            pid = 'PB_{:03d}'.format(pb_counter[0])
            # Use section prefix to infer tags
            section = dname[0]  # A, B, C, D
            if section == 'A':
                default_tags = ['输入输出', '条件判断', '循环']
            elif section == 'B':
                default_tags = ['二维数组']
            elif section == 'C':
                default_tags = ['字符串']
            elif section == 'D':
                default_tags = ['一维数组', '字符串']
            else:
                default_tags = []

            tags = infer_tags(title, desc, '', section)
            if not tags:
                tags = default_tags
            diff = infer_difficulty(title, desc, section)

            all_problems.append({
                'id': pid, 'title': title, 'source': 'Contest 271',
                'source_url': 'https://www.xmuoj.com/contest/271',
                'topics': tags, 'difficulty': diff if diff > 1 else (2 if section in 'BC' else 1),
                'description': desc, 'input_description': input_desc,
                'output_description': output_desc, 'hint': hint,
                'samples': samples_md, 'oj_problem_id': dname,
                'time_limit': 1000, 'memory_limit': 256,
                'origin_section': 'grammar_' + section,
            })
            grammar_count += 1
    print('Loaded {} Contest 271 problems'.format(grammar_count))


# 3. NQ100 problems (grammar NQ001-057 + algorithm NQ058+)
algo_dir = os.path.join(BASE, 'source/algorithm')
if os.path.exists(algo_dir):
    algo_count = 0
    grammar_nq_count = 0
    # Full NQ100 difficulty mapping
    algo_diff = {
        # Grammar NQ001-NQ057
        'NQ001': 1, 'NQ002': 1, 'NQ003': 1, 'NQ004': 1, 'NQ005': 1,
        'NQ006': 1, 'NQ007': 1, 'NQ008': 1, 'NQ009': 1, 'NQ010': 1,
        'NQ011': 1, 'NQ012': 1, 'NQ013': 1, 'NQ014': 1, 'NQ015': 1,
        'NQ016': 2, 'NQ017': 2, 'NQ018': 2, 'NQ019': 2, 'NQ020': 2,
        'NQ021': 2, 'NQ022': 2, 'NQ023': 2, 'NQ024': 2, 'NQ025': 2,
        'NQ026': 2, 'NQ027': 2, 'NQ028': 2, 'NQ029': 2, 'NQ030': 2,
        'NQ031': 2, 'NQ032': 2, 'NQ033': 2, 'NQ034': 2, 'NQ035': 2,
        'NQ036': 2, 'NQ037': 2, 'NQ038': 2, 'NQ039': 2, 'NQ040': 2,
        'NQ041': 2, 'NQ042': 2, 'NQ043': 2, 'NQ044': 2, 'NQ045': 2,
        'NQ046': 2, 'NQ047': 2, 'NQ048': 2, 'NQ049': 2, 'NQ050': 2,
        'NQ051': 2, 'NQ053': 2, 'NQ054': 2, 'NQ055': 2, 'NQ056': 2,
        'NQ057': 2,
        # Algorithm NQ058+
        'NQ058': 2, 'NQ059': 2, 'NQ060': 3, 'NQ061': 2, 'NQ062': 2,
        'NQ063': 2, 'NQ064': 2, 'NQ065': 2, 'NQ066': 3, 'NQ068': 3,
        'NQ069': 2, 'NQ070': 2, 'NQ071': 3, 'NQ072': 3, 'NQ073': 2,
        'NQ074': 3, 'NQ075': 2, 'NQ076': 2, 'NQ077': 3, 'NQ078': 3,
        'NQ079': 3, 'NQ080': 3, 'NQ081': 3, 'NQ082': 3, 'NQ083': 3,
        'NQ084': 2, 'NQ085': 3, 'NQ086': 4, 'NQ087': 3, 'NQ088': 4,
        'NQ090': 4, 'NQ091': 3, 'NQ092': 3, 'NQ093': 3, 'NQ094': 4,
        'NQ095': 3, 'NQ096': 3, 'NQ097': 4, 'NQ098': 5, 'NQ099': 5,
        'NQ100': 5,
    }
    algo_tags_manual = {
        # Grammar NQ001-NQ057
        'NQ001': ['循环', '输入输出'],
        'NQ002': ['条件判断', '字符处理'],
        'NQ003': ['输入输出', '数学'],
        'NQ004': ['输入输出', '数学'],
        'NQ005': ['条件判断', '数学'],
        'NQ006': ['条件判断'],
        'NQ007': ['条件判断', '循环'],
        'NQ008': ['循环', '输入输出'],
        'NQ009': ['循环'],
        'NQ010': ['循环', '输入输出'],
        'NQ011': ['循环'],
        'NQ012': ['循环', '数学'],
        'NQ013': ['循环'],
        'NQ014': ['循环', '条件判断'],
        'NQ015': ['排序', '一维数组'],
        'NQ016': ['字符串', '数学'],
        'NQ017': ['条件判断'],
        'NQ018': ['数学', '循环'],
        'NQ019': ['数学', '循环'],
        'NQ020': ['数学', '条件判断'],
        'NQ021': ['条件判断', '循环'],
        'NQ022': ['一维数组', '条件判断'],
        'NQ023': ['条件判断'],
        'NQ024': ['数学', '循环'],
        'NQ025': ['数学', '输入输出'],
        'NQ026': ['数学'],
        'NQ027': ['数学', '循环'],
        'NQ028': ['二维数组'],
        'NQ029': ['循环', '字符串'],
        'NQ030': ['数学', '条件判断'],
        'NQ031': ['字符串'],
        'NQ032': ['字符串'],
        'NQ033': ['字符串'],
        'NQ034': ['字符串', '数学'],
        'NQ035': ['字符串', '位运算'],
        'NQ036': ['字符串'],
        'NQ037': ['排序', '一维数组'],
        'NQ038': ['字符串', '字符处理'],
        'NQ039': ['字符串', '条件判断'],
        'NQ040': ['字符串', '字符处理'],
        'NQ041': ['字符串', '字符处理'],
        'NQ042': ['字符串', '双指针'],
        'NQ043': ['一维数组'],
        'NQ044': ['字符串'],
        'NQ045': ['字符串', '位运算'],
        'NQ046': ['字符串'],
        'NQ047': ['一维数组', '条件判断'],
        'NQ048': ['一维数组', '条件判断'],
        'NQ049': ['一维数组', '循环'],
        'NQ050': ['排序', '一维数组'],
        'NQ051': ['一维数组'],
        'NQ053': ['字符串', '双指针'],
        'NQ054': ['条件判断', '循环'],
        'NQ055': ['数学'],
        'NQ056': ['条件判断', '数学'],
        'NQ057': ['循环', '一维数组'],
        # Algorithm NQ058+
        'NQ058': ['双指针', '两数之和'],
        'NQ059': ['双指针', '三数之和'],
        'NQ060': ['双指针', '四数之和'],
        'NQ061': ['数学', '几何'],
        'NQ062': ['位运算', '二进制'],
        'NQ063': ['动态规划', '斐波那契'],
        'NQ064': ['记忆化搜索', '递推'],
        'NQ065': ['递归', '阶乘'],
        'NQ066': ['优先队列', '数学'],
        'NQ068': ['数学', '二分查找'],
        'NQ069': ['二分查找', '双指针'],
        'NQ070': ['二分查找'],
        'NQ071': ['二分查找', '贪心'],
        'NQ072': ['深度优先搜索', '回溯', 'N皇后'],
        'NQ073': ['递归', '波兰表达式'],
        'NQ074': ['回溯', '八皇后'],
        'NQ075': ['数学', '进制转换'],
        'NQ076': ['快速幂', '数学'],
        'NQ077': ['暴力枚举', '排序'],
        'NQ078': ['递归下降', '表达式求值'],
        'NQ079': ['回溯', '24点'],
        'NQ080': ['深度优先搜索', '回溯', '质数环'],
        'NQ081': ['深度优先搜索', '回溯'],
        'NQ082': ['贪心', '排序'],
        'NQ083': ['动态规划', '最长公共子序列'],
        'NQ084': ['哈希', '同构字符串'],
        'NQ085': ['动态规划', '数字三角形'],
        'NQ086': ['动态规划', '背包问题'],
        'NQ087': ['广度优先搜索', '图论'],
        'NQ088': ['动态规划', '记忆化搜索'],
        'NQ090': ['深度优先搜索', '记忆化搜索'],
        'NQ091': ['深度优先搜索', '回溯'],
        'NQ092': ['广度优先搜索', '最短路径'],
        'NQ093': ['拓扑排序', '图论'],
        'NQ094': ['拓扑排序', '动态规划', '图论'],
        'NQ095': ['深度优先搜索', '记忆化搜索'],
        'NQ096': ['深度优先搜索', '图论'],
        'NQ097': ['深度优先搜索', '图论'],
        'NQ098': ['深度优先搜索', '回溯', '数独'],
        'NQ099': ['最短路径', 'Dijkstra'],
        'NQ100': ['广度优先搜索', '状态空间搜索'],
    }

    for dname in sorted(os.listdir(algo_dir)):
        dpath = os.path.join(algo_dir, dname)
        readme = os.path.join(dpath, 'README.md')
        if not (os.path.isdir(dpath) and os.path.exists(readme)):
            continue
        if 'X' in dname:  # Skip NQ006X etc variants
            continue

        num_match = re.match(r'NQ(\d+)', dname)
        num = int(num_match.group(1)) if num_match else 0

        with open(readme) as f:
            content = f.read()

        title_match = re.match(r'^#\s*\w+\s*(.+)', content)
        title = title_match.group(1).strip() if title_match else dname
        if not title:
            title = dname
        # Clean "解题思路" / "思路" suffix from title
        title = re.sub(r'(解题)?思路$', '', title).strip()

        desc = content.strip()

        pb_counter[0] += 1
        pid = 'PB_{:03d}'.format(pb_counter[0])
        tags = algo_tags_manual.get(dname, ['算法'])
        diff = algo_diff.get(dname, 3)

        all_problems.append({
            'id': pid, 'title': title, 'source': 'NQ100',
            'source_url': 'https://www.xmuoj.com/problem/' + dname,
            'topics': tags, 'difficulty': diff,
            'description': desc, 'input_description': '',
            'output_description': '', 'hint': '',
            'samples': '', 'oj_problem_id': dname,
            'time_limit': 1000, 'memory_limit': 256,
            'origin_section': 'algorithm',
        })
        if num < 58:
            grammar_nq_count += 1
        else:
            algo_count += 1
    print('Loaded {} NQ100 problems ({} grammar + {} algorithm)'.format(
        grammar_nq_count + algo_count, grammar_nq_count, algo_count))


# ── Deduplication ────────────────────────────────────────────────
# Remove duplicates: prefer Contest 271 over AcWing, prefer AcWing L6-L8 over L4-L5
# Keep the first occurrence (AcWing loaded first, then Contest 271)
# Strategy: Contest 271 > AcWing (same titles), keep unique NQ100

seen_titles = {}
deduped = []
for p in all_problems:
    title = p['title'].strip()
    src = p['source']

    if title in seen_titles:
        existing = seen_titles[title]
        exist_src = existing['source']

        # Contest 271 wins over AcWing
        if src == 'Contest 271' and exist_src.startswith('AcWing'):
            # Replace the AcWing one with Contest 271 version
            deduped = [x for x in deduped if x['title'].strip() != title]
            deduped.append(p)
            seen_titles[title] = p
            continue
        elif exist_src == 'Contest 271' and src.startswith('AcWing'):
            # Skip this AcWing version, keep existing Contest 271
            continue
        # NQ100 duplicates with itself? Skip
        elif src == 'NQ100' and exist_src == 'NQ100':
            continue
        else:
            # Keep first one
            continue
    else:
        seen_titles[title] = p
        deduped.append(p)

dup_removed = len(all_problems) - len(deduped)
print('Removed {} duplicates'.format(dup_removed))
all_problems = deduped

# Re-assign sequential IDs
for i, p in enumerate(all_problems):
    old_id = p['id']
    new_id = 'PB_{:03d}'.format(i + 1)
    p['id'] = new_id


# ── Write bank files ─────────────────────────────────────────────

def format_frontmatter(p):
    """Format YAML frontmatter for a problem."""
    lines = ['---']
    lines.append('id: ' + p['id'])
    lines.append('title: "' + p['title'] + '"')
    lines.append('source: "' + p['source'] + '"')
    lines.append('source_url: "' + p['source_url'] + '"')
    lines.append('topics: [' + ', '.join(p['topics']) + ']')
    lines.append('difficulty: ' + str(p['difficulty']))
    oj_id = p.get('oj_problem_id', '')
    lines.append('oj_problem_id: "' + oj_id + '"')
    lines.append('---')
    return '\n'.join(lines)

def format_problem_md(p):
    """Format a complete problem markdown file."""
    fm = format_frontmatter(p)
    md = fm + '\n\n'
    md += '# ' + p['title'] + '\n\n'
    md += '## 题目描述\n\n' + p['description'] + '\n\n'

    if p['input_description']:
        md += '## 输入格式\n\n' + p['input_description'] + '\n\n'
    if p['output_description']:
        md += '## 输出格式\n\n' + p['output_description'] + '\n\n'
    if p['samples']:
        md += '## 样例\n\n' + p['samples'] + '\n\n'
    if p['hint']:
        md += '## 提示\n\n' + p['hint'] + '\n\n'

    md += '## 题目信息\n\n'
    md += '- 时间限制：{}ms\n'.format(p.get('time_limit', 1000))
    md += '- 内存限制：{}MB\n'.format(p.get('memory_limit', 256))
    md += '- 来源：{}\n\n'.format(p['source'])

    md += '## C++ 参考代码\n\n```cpp\n// TODO: 待补充\n```\n\n'
    md += '## Python 参考代码\n\n```python\n# TODO: 待补充\n```\n'
    return md

# Write all problems
for p in all_problems:
    filepath = os.path.join(BANK_DIR, p['id'] + '.md')
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(format_problem_md(p))

print('\n=== Bank built! ===')
print('Total problems: {}'.format(len(all_problems)))
print('Written to: {}'.format(BANK_DIR))

# Quick stats
acw_count = sum(1 for p in all_problems if p['source'].startswith('AcWing'))
grammar_count = sum(1 for p in all_problems if p['source'] == 'Contest 271')
algo_count = sum(1 for p in all_problems if p['source'] == 'NQ100')
print('  AcWing: {}'.format(acw_count))
print('  Contest 271: {}'.format(grammar_count))
print('  NQ100: {}'.format(algo_count))

# Difficulty distribution
diffs = {}
for p in all_problems:
    d = p['difficulty']
    diffs[d] = diffs.get(d, 0) + 1
print('  Difficulty: ' + ', '.join('L{}={}'.format(k, v) for k, v in sorted(diffs.items())))

# Topic distribution (top 10)
topic_count = {}
for p in all_problems:
    for t in p['topics']:
        topic_count[t] = topic_count.get(t, 0) + 1
top_topics = sorted(topic_count.items(), key=lambda x: -x[1])[:15]
print('  Top topics: ' + ', '.join('{}={}'.format(t, c) for t, c in top_topics))
