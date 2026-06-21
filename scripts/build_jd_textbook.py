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
    """Token-based syntax highlighting — no nested span corruption."""
    code = html_mod.escape(code)
    placeholders = []

    def placeholder(html_span):
        """Replace a span with a numbered placeholder to prevent re-matching."""
        idx = len(placeholders)
        token = f'\x00PH{idx}\x00'
        placeholders.append(html_span)
        return token

    def restore(text):
        for i, html in enumerate(placeholders):
            text = text.replace(f'\x00PH{i}\x00', html)
        return text

    if lang in ('cpp', 'c'):
        # Order matters: comments first, strings, numbers, keywords
        # 1. Comments (// to end of line)
        code = re.sub(r'(//[^\n]*)', lambda m: placeholder(f'<span class="comment">{m.group(1)}</span>'), code)
        # 2. Strings
        code = re.sub(r'("(?:[^"\\]|\\.)*")', lambda m: placeholder(f'<span class="string">{m.group(1)}</span>'), code)
        # 3. Numbers
        code = re.sub(r'\b(\d+\.?\d*[fFlLuU]*)\b', lambda m: placeholder(f'<span class="number">{m.group(1)}</span>'), code)
        # 4. Keywords
        kw = r'\b(int|long|float|double|char|void|bool|string|auto|const|static|return|if|else|for|while|do|switch|case|break|continue|default|class|struct|public|private|protected|virtual|new|delete|this|true|false|nullptr|include|using|namespace|std|template|typename|sizeof|typedef|enum|union|extern|register|volatile|inline|constexpr|NULL)\b'
        code = re.sub(kw, lambda m: placeholder(f'<span class="keyword">{m.group(1)}</span>'), code)

    elif lang == 'python':
        # 1. Comments
        code = re.sub(r'(#[^\n]*)', lambda m: placeholder(f'<span class="comment">{m.group(1)}</span>'), code)
        # 2. Triple-quoted strings
        code = re.sub(r'(""".*?"""|\'\'\'.*?\'\'\')', lambda m: placeholder(f'<span class="string">{m.group(1)}</span>'), code, flags=re.DOTALL)
        # 3. Single/double quoted strings
        code = re.sub(r'("(?:[^"\\]|\\.)*"|\'(?:[^\'\\]|\\.)*\')', lambda m: placeholder(f'<span class="string">{m.group(1)}</span>'), code)
        # 4. Numbers
        code = re.sub(r'\b(\d+\.?\d*)\b', lambda m: placeholder(f'<span class="number">{m.group(1)}</span>'), code)
        # 5. Keywords
        kw = r'\b(def|class|return|if|elif|else|for|while|break|continue|pass|import|from|as|try|except|finally|raise|with|yield|lambda|and|or|not|in|is|True|False|None|print|range|len|int|float|str|list|dict|set|tuple|input|map|sorted|enumerate|zip|reversed|sum|min|max|abs|all|any|open|super|self)\b'
        code = re.sub(kw, lambda m: placeholder(f'<span class="keyword">{m.group(1)}</span>'), code)

    code = restore(code)
    return f'<pre><code class="language-{lang}">{code}</code></pre>'


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
