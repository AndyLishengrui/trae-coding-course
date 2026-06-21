#!/usr/bin/env python3
"""
剑道试炼教材构建脚本
====================
从 剑道试炼/ 题库读取 problem.md + Andy.cpp + Andy.py，生成各章 HTML 教材。

用法：
  python build_jd_textbook.py              # 生成全部章节 HTML
  python build_jd_textbook.py --ch 7       # 只生成第7章
  python build_jd_textbook.py --pdf        # 生成后转 PDF
  python build_jd_textbook.py --docx       # 生成后转 DOCX
"""
import json, re, os, sys, subprocess, html as html_mod
from pathlib import Path

BOOK_ROOT = Path(__file__).parent.parent.resolve()
BANK = BOOK_ROOT / "剑道试炼"
TEXTBOOK = BOOK_ROOT / "textbook"
TEXTBOOK.mkdir(exist_ok=True)

# Chapter metadata: (dir_prefix, title, subtitle)
CHAPTERS = {
    1:  ("第1章_持剑叩门——变量与输入输出",   "持剑叩门", "变量与输入输出"),
    2:  ("第2章_歧路逢生——条件判断与分支",   "歧路逢生", "条件判断与分支"),
    3:  ("第3章_千回百转——for与while",       "千回百转", "for与while"),
    4:  ("第4章_排兵布阵——数组",             "排兵布阵", "数组"),
    5:  ("第5章_十二宫剑阵——二维数组",       "十二宫剑阵", "二维数组"),
    6:  ("第6章_古卷密文——字符串处理",       "古卷密文", "字符串处理"),
    7:  ("第7章_以招创招——函数与递归",       "以招创招", "函数与递归"),
    8:  ("第8章_百器图谱——容器与内置算法",   "百器图谱", "容器与内置算法"),
    9:  ("第9章_快剑如风——排序与二分",       "快剑如风", "排序与二分"),
    10: ("第10章_千锤百炼——高精度与位运算",  "千锤百炼", "高精度与位运算"),
    11: ("第11章_蓄势待发——前缀和、差分与双指针", "蓄势待发", "前缀和、差分与双指针"),
    12: ("第12章_利器出鞘——进阶数据结构",   "利器出鞘", "进阶数据结构"),
    13: ("第13章_迷雾寻踪——搜索与回溯",     "迷雾寻踪", "搜索与回溯"),
    14: ("第14章_千里奔袭——最短路与生成树",  "千里奔袭", "最短路与生成树"),
    15: ("第15章_华山论剑——动态规划",       "华山论剑", "动态规划"),
}


def load_problem(prob_dir):
    """Load problem data from a JD directory."""
    md_path = prob_dir / "problem.md"
    json_path = prob_dir / "problem.json"
    cpp_path = prob_dir / "Andy.cpp"
    py_path = prob_dir / "Andy.py"

    data = {}

    # Read problem.md
    if md_path.exists():
        content = md_path.read_text(encoding='utf-8')
        # Extract title
        m = re.search(r'^# (JD\d+：.+)$', content, re.MULTILINE)
        data['title'] = m.group(1) if m else prob_dir.name
        # Extract description (between 题目描述 and 输入格式)
        m = re.search(r'## 题目描述\s*\n(.*?)(?=\n## )', content, re.DOTALL)
        data['description'] = m.group(1).strip() if m else ''
        # Extract input format
        m = re.search(r'## 输入格式\s*\n(.*?)(?=\n## )', content, re.DOTALL)
        data['input_format'] = m.group(1).strip() if m else ''
        # Extract output format
        m = re.search(r'## 输出格式\s*\n(.*?)(?=\n## )', content, re.DOTALL)
        data['output_format'] = m.group(1).strip() if m else ''
        # Extract sample
        m = re.search(r'## 样例\s*\n.*?输入：\s*\n```text\n(.*?)\n```.*?输出：\s*\n```text\n(.*?)\n```', content, re.DOTALL)
        if m:
            data['sample_in'] = m.group(1).strip()
            data['sample_out'] = m.group(2).strip()
        # Extract hint
        m = re.search(r'## 解题思路\s*\n(.*?)(?=\n## |\Z)', content, re.DOTALL)
        data['hint'] = m.group(1).strip() if m else ''

    # Read problem.json for metadata
    if json_path.exists():
        with open(json_path, encoding='utf-8') as f:
            jdata = json.load(f)
        data['acw'] = jdata.get('source', '').split('|')[0].strip().replace('AcWing ', '')
        data['tags'] = jdata.get('tags', [])
        data['samples'] = jdata.get('samples', [])

    # Read Andy.cpp
    if cpp_path.exists():
        data['cpp'] = cpp_path.read_text(encoding='utf-8').strip()

    # Read Andy.py
    if py_path.exists():
        data['py'] = py_path.read_text(encoding='utf-8').strip()

    return data


def md_to_html(text):
    """Simple markdown to HTML conversion for problem descriptions."""
    # Bold
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    # Inline code
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    # Paragraphs
    paragraphs = text.split('\n\n')
    html = ''
    for p in paragraphs:
        p = p.strip()
        if p:
            # Check if it's a list
            if p.startswith('- ') or p.startswith('* '):
                items = p.split('\n')
                html += '<ul>\n'
                for item in items:
                    item = re.sub(r'^[-*]\s*', '', item.strip())
                    if item:
                        html += f'  <li>{item}</li>\n'
                html += '</ul>\n'
            else:
                html += f'<p>{p}</p>\n'
    return html


def syntax_highlight(code, lang='cpp'):
    """Token-based syntax highlighting — HTML-escape AFTER wrapping spans."""
    placeholders = []

    def ph(html_span):
        idx = len(placeholders)
        placeholders.append(html_span)
        return '\x00PH%d\x00' % idx

    def restore(text):
        for i, html in enumerate(placeholders):
            text = text.replace('\x00PH%d\x00' % i, html)
        return text

    if lang in ('cpp', 'c'):
        code = re.sub(r'(//[^\n]*)', lambda m: ph('<span class="comment">%s</span>' % html_mod.escape(m.group(1))), code)
        code = re.sub(r'("(?:[^"\\]|\\.)*")', lambda m: ph('<span class="string">%s</span>' % html_mod.escape(m.group(1))), code)
        code = re.sub(r'\b(\d+\.?\d*[fFlLuU]*)\b', lambda m: ph('<span class="number">%s</span>' % m.group(1)), code)
        kw = r'\b(int|long|float|double|char|void|bool|string|auto|const|static|return|if|else|for|while|do|switch|case|break|continue|default|class|struct|public|private|protected|virtual|new|delete|this|true|false|nullptr|include|using|namespace|std|template|typename|sizeof|typedef|enum|union|extern|register|volatile|inline|constexpr|NULL)\b'
        code = re.sub(kw, lambda m: ph('<span class="keyword">%s</span>' % m.group(1)), code)
    elif lang == 'python':
        code = re.sub(r'(#[^\n]*)', lambda m: ph('<span class="comment">%s</span>' % html_mod.escape(m.group(1))), code)
        code = re.sub(r'(""".*?"""|\'\'\'.*?\'\'\')', lambda m: ph('<span class="string">%s</span>' % html_mod.escape(m.group(1))), code, flags=re.DOTALL)
        code = re.sub(r'("(?:[^"\\]|\\.)*"|\'(?:[^\'\\]|\\.)*\')', lambda m: ph('<span class="string">%s</span>' % html_mod.escape(m.group(1))), code)
        code = re.sub(r'\b(\d+\.?\d*)\b', lambda m: ph('<span class="number">%s</span>' % m.group(1)), code)
        kw = r'\b(def|class|return|if|elif|else|for|while|break|continue|pass|import|from|as|try|except|finally|raise|with|yield|lambda|and|or|not|in|is|True|False|None|print|range|len|int|float|str|list|dict|set|tuple|input|map|sorted|enumerate|zip|reversed|sum|min|max|abs|all|any|open|super|self)\b'
        code = re.sub(kw, lambda m: ph('<span class="keyword">%s</span>' % m.group(1)), code)

    # HTML-escape everything that's NOT a placeholder
    code = restore(code)
    return '<pre><code class="language-%s">%s</code></pre>' % (lang, code)


# Chapter introductions - wuxia scene-setting
CHAPTER_INTROS = {
    1: '<p>李少白第一次来到剑道宗山门前。梁嘉峰递给他两枚铁令："学会输入输出，才能踏入剑道的第一步。"</p><p>本章将学习变量、数据类型和输入输出——这是所有程序的基础。掌握如何读入数据、计算、输出结果，你就能写出人生中第一个程序了。</p>',
    2: '<p>山道分岔，石碑指路。赵晴儿说："条件判断让程序学会了选择——根据不同的条件，走不同的路。"</p><p>本章学习 if/else 条件判断——让程序根据不同的输入做出不同的反应。这是编程从"计算"走向"决策"的关键一步。</p>',
    3: '<p>千层塔中，梁嘉峰指着重复的石阶："循环——让代码自动重复执行。掌握它，你就能用一行代码完成一百次操作。"</p><p>本章学习 for 循环和 while 循环——让程序自动重复执行任务。嵌套循环处理更复杂的问题。</p>',
    4: '<p>赵晴儿在沙盘上排了一列石块："数组——用一个名字管理一整排数据。"</p><p>本章学习数组——存储和管理一组有序数据。遍历、求和、排序，这些操作将伴随你整个编程生涯。</p>',
    5: '<p>十二宫剑阵展开，光幕上浮现一个12×12的方格。"二维数组——矩阵。行与列交织，每个格子都是一个数据点。"</p><p>本章学习二维数组——矩阵的存储、遍历和方向数组。掌握这些，你就能操控任何网格结构。</p>',
    6: '<p>古卷展开，密文横陈。赵晴儿说："字符串——字符的序列。古人的智慧，藏在文字之间。"</p><p>本章学习字符串处理——文本数据的查找、替换、分割等操作。剑道传承，始于文字。</p>',
    7: '<p>丹房之中，赵晴儿演示炼丹之术："重复的操作，封装成函数。复杂的计算，用递归层层解开。"</p><p>本章学习函数封装和递归——将重复逻辑封装成可复用的函数，用递归解决分治类问题。这是从"写代码"到"设计程序"的飞跃。</p>',
    8: '<p>兵器阁深处，梁嘉峰指着各种容器："栈如叠盘，队如列阵，链如铁环——每种容器都有独特的用途。"</p><p>本章学习 STL 容器——栈、队列、链表等数据结构的实际应用。掌握容器，你的代码将更加优雅高效。</p>',
    9: '<p>试炼场上，梁嘉峰演示一剑分两路之术："排序——让混乱变得有序。二分——在有序中快速定位。"</p><p>本章学习快速排序、归并排序和二分查找——这是算法世界的基石，掌握它们，你将拥有处理海量数据的能力。</p>',
    10: '<p>精铸阁中，匠人在铁板上刻下巨大的数字。"高精度——用数组模拟大数运算。位运算——在二进制世界中游刃有余。"</p><p>本章学习高精度运算和位运算——当普通数据类型不够用时，这些技巧能让你突破极限。</p>',
    11: '<p>蓄势阁中，赵晴儿盘膝而坐："前缀和——记住历史，快速回答。差分——记录变化，高效更新。双指针——两路并进，一击即中。"</p><p>本章学习前缀和、差分和双指针——这些技巧让你用 O(1) 或 O(n) 的时间处理看似需要 O(n²) 的问题。</p>',
    12: '<p>兵器阁深处，梁嘉峰打开一个布满机关的箱子："单调栈、单调队列、KMP、堆、并查集——每一种都是利器。"</p><p>本章学习进阶数据结构——它们是解决复杂问题的利器，掌握它们，你将能应对更高级的算法挑战。</p>',
    13: '<p>迷雾弥漫的林间小径上，赵晴儿指着分叉的路口："DFS 深入探索每一条路，BFS 逐层推进找最短。回溯——选了不行就回头。"</p><p>本章学习搜索和回溯——DFS 和 BFS 是图搜索的基础，回溯是枚举所有可能的利器。</p>',
    14: '<p>城际连横，梁嘉峰展开地图："从一座城到另一座城，最短的路在哪里？Dijkstra、Floyd、Kruskal——每一种算法都是战场上的利器。"</p><p>本章学习最短路和最小生成树——图论的核心算法，掌握它们，你将能解决任何网络优化问题。</p>',
    15: '<p>华山之巅，风雷激荡。四面八方的高手齐聚于此——华山论剑，一决高下。"动态规划——记住过去，优化未来。背包、区间、状态压缩、树形——每一种DP都是一门绝技。"</p><p>本章学习动态规划——算法世界中最精妙的技巧。掌握DP，你将拥有解决任何复杂问题的能力。这一战之后，你便可以出师了。</p>',
}


def build_chapter_html(ch_num):
    """Generate HTML for a single chapter."""
    ch_dir_name, ch_title, ch_subtitle = CHAPTERS[ch_num]
    ch_path = BANK / ch_dir_name

    if not ch_path.exists():
        print(f"  ❌ Chapter {ch_num}: directory not found: {ch_path}")
        return None

    # Get all JD problem directories
    prob_dirs = sorted([d for d in ch_path.iterdir() if d.is_dir() and d.name.startswith('JD')])

    if not prob_dirs:
        print(f"  ❌ Chapter {ch_num}: no JD problems found")
        return None

    # Load all problems
    problems = []
    for pd in prob_dirs:
        prob = load_problem(pd)
        prob['dir_name'] = pd.name
        prob['jd_id'] = pd.name.split('_')[0]
        problems.append(prob)

    # Generate HTML
    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>第{ch_num}章 {ch_title}——{ch_subtitle}</title>
    <style>
        body {{ font-family: "Noto Serif SC", "Source Han Serif CN", serif; max-width: 800px; margin: 0 auto; padding: 20px; line-height: 1.8; color: #333; }}
        h1 {{ text-align: center; color: #8B0000; border-bottom: 2px solid #8B0000; padding-bottom: 10px; }}
        h2 {{ color: #4A0080; margin-top: 2em; }}
        h3 {{ color: #2E5090; }}
        .chapter-subtitle {{ text-align: center; color: #666; font-size: 1.1em; margin-bottom: 2em; }}
        .problem {{ border: 1px solid #ddd; border-radius: 8px; padding: 20px; margin: 20px 0; background: #fafafa; }}
        .problem-title {{ color: #8B0000; font-size: 1.3em; font-weight: bold; margin-bottom: 10px; }}
        .problem-meta {{ color: #666; font-size: 0.9em; margin-bottom: 15px; }}
        .description {{ margin: 15px 0; }}
        .description p {{ margin: 8px 0; }}
        .io-section {{ background: #f0f0f0; padding: 12px; border-radius: 4px; margin: 10px 0; }}
        .io-section h4 {{ margin: 0 0 8px 0; color: #555; font-size: 0.95em; }}
        .sample {{ background: #1e1e1e; color: #d4d4d4; padding: 15px; border-radius: 4px; margin: 10px 0; font-family: "Consolas", "Courier New", monospace; white-space: pre-wrap; }}
        .sample-label {{ color: #569cd6; font-weight: bold; margin-bottom: 5px; }}
        .hint {{ background: #fff8e1; border-left: 4px solid #ffc107; padding: 12px; margin: 15px 0; }}
        .code-section {{ margin: 15px 0; }}
        .code-section summary {{ cursor: pointer; color: #2E5090; font-weight: bold; }}
        pre {{ background: #1e1e1e; color: #d4d4d4; padding: 15px; border-radius: 4px; overflow-x: auto; font-size: 0.9em; }}
        code {{ font-family: "Consolas", "Courier New", monospace; }}
        .lang-tabs {{ display: flex; gap: 10px; margin: 10px 0; }}
        .lang-tab {{ padding: 5px 15px; cursor: pointer; border: 1px solid #ddd; border-radius: 4px 4px 0 0; }}
        .lang-tab.active {{ background: #1e1e1e; color: #d4d4d4; border-color: #1e1e1e; }}
    </style>
</head>
<body>
    <h1>第{ch_num}章 {ch_title}</h1>
    <div class="chapter-subtitle">{ch_subtitle}</div>
    <div class="chapter-intro" style="margin: 1.5em 0; padding: 1em; background: #f8f4e8; border-left: 4px solid #b8860b; border-radius: 0 8px 8px 0;">
        {CHAPTER_INTROS.get(ch_num, '')}
    </div>
"""

    for i, prob in enumerate(problems, 1):
        jd_id = prob.get('jd_id', f'JD{i:03d}')
        title = prob.get('title', prob['dir_name'])
        desc = prob.get('description', '')
        input_fmt = prob.get('input_format', '')
        output_fmt = prob.get('output_format', '')
        sample_in = prob.get('sample_in', '')
        sample_out = prob.get('sample_out', '')
        hint = prob.get('hint', '')
        cpp_code = prob.get('cpp', '')
        py_code = prob.get('py', '')
        acw = prob.get('acw', '')

        html += f"""
    <div class="problem" id="{jd_id}">
        <div class="problem-title">{title}</div>
        <div class="problem-meta">AcWing {acw} | {jd_id}</div>

        <div class="description">
            {md_to_html(desc)}
        </div>

        <div class="io-section">
            <h4>输入格式</h4>
            {md_to_html(input_fmt)}
        </div>

        <div class="io-section">
            <h4>输出格式</h4>
            {md_to_html(output_fmt)}
        </div>
"""

        if sample_in or sample_out:
            html += f"""
        <div class="sample">
            <div class="sample-label">输入样例</div>
{sample_in}
        </div>
        <div class="sample">
            <div class="sample-label">输出样例</div>
{sample_out}
        </div>
"""

        if hint:
            html += f"""
        <div class="hint">
            <strong>解题思路：</strong>{md_to_html(hint)}
        </div>
"""

        if cpp_code or py_code:
            html += '        <div class="code-section">\n'
            html += '            <details><summary>参考代码</summary>\n'
            if cpp_code:
                html += '            <h4>C++</h4>\n'
                html += f'            {syntax_highlight(cpp_code, "cpp")}\n'
            if py_code:
                html += '            <h4>Python</h4>\n'
                html += f'            {syntax_highlight(py_code, "python")}\n'
            html += '            </details>\n'
            html += '        </div>\n'

        html += '    </div>\n'

    html += """
</body>
</html>
"""

    # Write HTML
    html_path = TEXTBOOK / f"chapter{ch_num:02d}_jd_print.html"
    html_path.write_text(html, encoding='utf-8')
    print(f"  ✅ Ch{ch_num:02d} HTML: {len(html)} bytes — {ch_title} ({len(problems)} problems)")
    return html_path


def build_all():
    """Build all chapters."""
    print("=== Building 剑道试炼 Textbook ===\n")
    for ch_num in sorted(CHAPTERS.keys()):
        build_chapter_html(ch_num)
    print("\nDone!")


def build_pdf(ch_num):
    """Convert HTML to PDF using Chrome headless."""
    html_path = TEXTBOOK / f"chapter{ch_num:02d}_jd_print.html"
    pdf_path = TEXTBOOK / f"chapter{ch_num:02d}_jd.pdf"
    chrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

    if not html_path.exists():
        print(f"  ❌ Ch{ch_num}: HTML not found")
        return False

    result = subprocess.run([
        chrome, "--headless", "--disable-gpu",
        f"--print-to-pdf={pdf_path}",
        "--no-pdf-header-footer",
        html_path.as_uri()
    ], capture_output=True, text=True, timeout=60)

    if pdf_path.exists():
        size_kb = pdf_path.stat().st_size // 1024
        print(f"  ✅ Ch{ch_num:02d} PDF: {size_kb}KB")
        return True
    else:
        print(f"  ❌ Ch{ch_num:02d} PDF FAILED")
        return False


def build_docx(ch_num):
    """Convert HTML to DOCX using pandoc."""
    html_path = TEXTBOOK / f"chapter{ch_num:02d}_jd_print.html"
    docx_path = TEXTBOOK / f"chapter{ch_num:02d}_jd.docx"

    if not html_path.exists():
        print(f"  ❌ Ch{ch_num}: HTML not found")
        return False

    result = subprocess.run([
        "pandoc", str(html_path), "-f", "html", "-t", "docx",
        "-o", str(docx_path),
        "--resource-path", str(TEXTBOOK)
    ], capture_output=True, text=True, timeout=120)

    if docx_path.exists():
        size_kb = docx_path.stat().st_size // 1024
        print(f"  ✅ Ch{ch_num:02d} DOCX: {size_kb}KB")
        return True
    else:
        print(f"  ❌ Ch{ch_num:02d} DOCX FAILED")
        return False


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Build 剑道试炼 textbook")
    parser.add_argument("--ch", type=int, help="Build single chapter")
    parser.add_argument("--pdf", action="store_true", help="Generate PDF")
    parser.add_argument("--docx", action="store_true", help="Generate DOCX")
    args = parser.parse_args()

    if args.ch:
        build_chapter_html(args.ch)
        if args.pdf:
            build_pdf(args.ch)
        if args.docx:
            build_docx(args.ch)
    else:
        build_all()
        if args.pdf:
            print("\n=== Generating PDFs ===")
            for ch in CHAPTERS:
                build_pdf(ch)
        if args.docx:
            print("\n=== Generating DOCXs ===")
            for ch in CHAPTERS:
                build_docx(ch)
