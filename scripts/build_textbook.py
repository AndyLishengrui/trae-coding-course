#!/usr/bin/env python3
"""Build complete 16-chapter textbook from lesson data and code files."""
import os, re, json

CHAPTERS = {
    1: {"title": "程序设计的第一个脚印", "subtitle": "变量、输入输出与顺序结构", "phase": "语法基础"},
    2: {"title": "选择的艺术", "subtitle": "条件判断与分支结构", "phase": "语法基础"},
    3: {"title": "循环的魔力", "subtitle": "for/while与嵌套循环", "phase": "语法基础"},
    4: {"title": "数据的容器", "subtitle": "数组与线性存储", "phase": "语法基础"},
    5: {"title": "矩阵的舞蹈", "subtitle": "多维数组与矩阵模式", "phase": "语法基础"},
    6: {"title": "字符的世界", "subtitle": "字符串处理", "phase": "编程进阶"},
    7: {"title": "模块化的力量", "subtitle": "函数、递归与库的威力", "phase": "编程进阶"},
    8: {"title": "指针与抽象", "subtitle": "结构体、指针与STL容器", "phase": "编程进阶"},
    9: {"title": "分治之美", "subtitle": "排序与二分", "phase": "核心算法"},
    10: {"title": "预处理的艺术", "subtitle": "前缀和、差分与双指针", "phase": "核心算法"},
    11: {"title": "数字的奥秘", "subtitle": "高精度、位运算与离散化", "phase": "核心算法"},
    12: {"title": "结构的根基", "subtitle": "基础数据结构", "phase": "核心算法"},
    13: {"title": "搜索的疆域", "subtitle": "搜索与回溯", "phase": "算法进阶"},
    14: {"title": "图的世界", "subtitle": "图论入门", "phase": "算法进阶"},
    15: {"title": "最优子结构", "subtitle": "动态规划", "phase": "算法进阶"},
    16: {"title": "智慧的策略", "subtitle": "贪心、并查集与数学", "phase": "算法进阶"},
}

def read_cpp(lnum, nq_num, pid):
    path = f'lessons_v2/lesson{lnum:02d}/codes/nq{nq_num:03d}_acw{pid}.cpp'
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return '// code not found'

def read_py(lnum, nq_num, pid):
    path = f'lessons_v2/lesson{lnum:02d}/codes/nq{nq_num:03d}_acw{pid}.py'
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return '# Python solution'

def build_chapter(ch_num, info, problems):
    """Build a single chapter."""
    lines = []
    lines.append(f"# 第{ch_num}章 {info['title']}")
    lines.append(f"> **{info['subtitle']}** | {info['phase']} | NQ{problems[0]['nq_num']:03d}-NQ{problems[-1]['nq_num']:03d}")
    lines.append("")
    lines.append(f"本章{len(problems)}题。读懂C++和Python的双语代码，在TRAE中实现，上XMUOJ提交AC。")
    lines.append("")
    lines.append("---")
    lines.append("")

    for p in problems:
        nq = f"{p['nq_num']:03d}"
        pid = p['pid']

        lines.append(f"## NQ{nq}：{p['title']}")
        lines.append(f"> 题目来源：AcWing {pid}")
        lines.append("")
        lines.append("### 描述")
        lines.append(p['desc'])
        lines.append("")
        lines.append("### 输入格式")
        lines.append(p['input_fmt'])
        lines.append("")
        lines.append("### 输出格式")
        lines.append(p['output_fmt'])
        lines.append("")
        lines.append("### 样例")
        lines.append("**输入：**")
        lines.append("```")
        lines.append(p['sample_in'])
        lines.append("```")
        lines.append("**输出：**")
        lines.append("```")
        lines.append(p['sample_out'])
        lines.append("```")
        lines.append("")
        if p.get('constraints'):
            lines.append(f"**数据范围：** {p['constraints']}")
            lines.append("")
        lines.append("### 解题思路")
        lines.append(p['solution'])
        lines.append("")
        if p.get('technique'):
            lines.append("### 编程技巧")
            lines.append(p['technique'])
            lines.append("")
        lines.append("### 参考代码")
        lines.append("")

        cpp = read_cpp(ch_num, p['nq_num'], pid)
        py = read_py(ch_num, p['nq_num'], pid)

        lines.append("**C++ Code:**")
        lines.append("```cpp")
        lines.append(cpp)
        lines.append("```")
        lines.append("")
        lines.append("**Python Code:**")
        lines.append("```python")
        lines.append(py)
        lines.append("```")
        lines.append("")
        lines.append("---")
        lines.append("")

    return '\n'.join(lines)

# Problem data for all chapters (abbreviated - full descriptions inline)
# This is a framework - full problem descriptions are in the textbook build process

# For now, let's build the first 2 chapters fully and create stubs for the rest
# The full build will happen incrementally

print("Textbook build framework ready")
print(f"Will build {len(CHAPTERS)} chapters")
