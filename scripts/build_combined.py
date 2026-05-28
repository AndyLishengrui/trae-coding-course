#!/usr/bin/env python3
"""生成合并版PDF和DOCX — 含标题页、目录、页眉页脚"""
import re, subprocess, sys, os
from pathlib import Path

BOOK_ROOT = Path(__file__).parent.parent.resolve()
TEXTBOOK = BOOK_ROOT / "textbook"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

CHAPTERS = [
    (1, "程序设计的第一个脚印", "变量、输入输出与顺序结构", 14),
    (2, "选择的艺术", "条件判断与分支结构", 14),
    (3, "循环的魔力", "for/while与嵌套循环", 14),
    (4, "数据的容器", "数组与线性存储", 12),
    (5, "矩阵的舞蹈", "多维数组与矩阵模式", 12),
    (6, "字符的世界", "字符串处理", 12),
    (7, "模块化的力量", "函数、递归与库的威力", 12),
    (8, "指针与抽象", "结构体、指针与STL容器", 10),
    (9, "分治之美", "排序与二分", 7),
    (10, "预处理的智慧", "前缀和、差分与双指针", 7),
    (11, "计算的边界", "高精度、位运算与离散化", 7),
    (12, "结构的魔力", "基础数据结构", 8),
    (13, "搜索的艺术", "搜索与回溯", 8),
    (14, "图的疆域", "图论入门", 8),
    (15, "状态的艺术", "动态规划", 8),
    (16, "终极试炼", "数学、贪心与综合实战", 8),
]
TOTAL = sum(c[3] for c in CHAPTERS)

def extract_body(html_path):
    """Extract body content from chapter HTML."""
    text = html_path.read_text(encoding='utf-8')
    m = re.search(r'<body>(.*)</body>', text, re.DOTALL)
    if m:
        body = m.group(1)
        # Remove the original chapter-title and chapter-subtitle as we'll add our own
        # But keep the rest. Actually, the chapter-title serves as the page header anchor.
        return body
    return ''

def build_combined_html():
    """Build one big HTML with title page, TOC, and all chapters."""

    # Extract common CSS from chapter01 (they're all the same)
    ch1_html = (TEXTBOOK / "chapter01_print.html").read_text(encoding='utf-8')
    css_match = re.search(r'<style>(.*?)</style>', ch1_html, re.DOTALL)
    common_css = css_match.group(1) if css_match else ""

    # Build the combined CSS — use fixed header text (Chrome doesn't support string())
    combined_css = """@page{size:A4;margin:2.2cm 2cm 2.5cm 2cm;
    @top-center{content:"基于Trae的编程兴趣班入门百练";font-size:7.5pt;color:#999;font-family:"PingFang SC","Hiragino Sans GB","Noto Serif CJK SC",sans-serif}
    @bottom-center{content:counter(page);font-size:7.5pt;color:#999;font-family:"PingFang SC",sans-serif}}
@page titlepage{@top-center{content:none}@bottom-center{content:none}}
@page tocpage{@top-center{content:none}@bottom-center{content:none}}
body{font-family:"PingFang SC","Hiragino Sans GB","Noto Serif CJK SC","STSong",serif;font-size:9.5pt;line-height:1.7;color:#222}
.title-page{page:titlepage;page-break-after:always;text-align:center;padding-top:5cm}
.title-page .main-title{font-size:28pt;font-weight:bold;letter-spacing:6pt;margin-bottom:.3em}
.title-page .sub-title{font-size:14pt;color:#555;margin-bottom:2em}
.title-page .meta{font-size:11pt;color:#888;margin-top:3em;line-height:2.2}
.toc-page{page:tocpage;page-break-after:always}
.toc-page h2{text-align:center;font-size:18pt;margin:2em 0 1.2em 0;letter-spacing:6pt;color:#333}
.toc-page .toc-entry{display:flex;margin:.55em 0;font-size:10pt;border-bottom:1px dotted #ddd;padding-bottom:.15em}
.toc-page .toc-ch{width:3.5em;font-weight:bold;color:#2563eb;text-align:right;margin-right:1em;font-size:10pt}
.toc-page .toc-title{flex:1;font-size:10pt}
.toc-page .toc-subtitle{font-size:8pt;color:#999;margin-left:.4em}
.toc-page .toc-count{width:3em;text-align:right;color:#888;font-size:8.5pt}
.chapter-start{page-break-before:always}"""

    # CSS for chapter headers and content (reuse from common_css, stripped of @page)
    content_css = re.sub(r'@page\{[^}]*\}', '', common_css)
    # Remove body string-set
    content_css = re.sub(r'string-set:chapter\s*"[^"]*"', '', content_css)
    content_css = re.sub(r'body\{[^}]*\}', 'body{font-family:"PingFang SC","Hiragino Sans GB","Noto Serif CJK SC","STSong",serif;font-size:9.5pt;line-height:1.7;color:#222}', content_css)

    combined_css += content_css

    # Start building HTML
    parts = []

    # === TITLE PAGE ===
    parts.append('<div class="title-page">')
    parts.append('<div class="main-title">基于Trae的编程兴趣班</div>')
    parts.append('<div class="main-title" style="font-size:22pt;letter-spacing:4pt;margin-top:0.3em">入门百练</div>')
    parts.append('<div class="sub-title">C++ &amp; Python 双语对照 · 四角色叙事对话</div>')
    parts.append('<div class="meta">')
    parts.append(f'<div>共16章 · {TOTAL}题</div>')
    parts.append('<div>覆盖语法基础→编程进阶→核心算法→算法进阶</div>')
    parts.append('<div style="margin-top:1em">小鲁 · 小华 · 小栋 · 小嘉</div>')
    parts.append('<div style="margin-top:0.5em;font-size:9pt">厦门大学 · 自强不息，止于至善</div>')
    parts.append('</div>')
    parts.append('</div>')

    # === TABLE OF CONTENTS ===
    parts.append('<div class="toc-page">')
    parts.append('<h2>目 录</h2>')
    # Phase headers
    phases = [
        (1, 5, "第一阶段：语法基础"),
        (6, 8, "第二阶段：编程进阶"),
        (9, 13, "第三阶段：核心算法"),
        (14, 16, "第四阶段：算法进阶"),
    ]
    phase_names = {
        (1,5): "第一阶段：语法基础（第1-5课）",
        (6,8): "第二阶段：编程进阶（第6-8课）",
        (9,13): "第三阶段：核心算法（第9-13课）",
        (14,16): "第四阶段：算法进阶（第14-16课）",
    }

    for start, end, phase_name in phases:
        parts.append(f'<div style="font-size:9pt;color:#2563eb;font-weight:bold;margin:1.2em 0 .4em 0;padding-left:4em">{phase_name}</div>')
        for ch, title, subtitle, count in CHAPTERS:
            if start <= ch <= end:
                parts.append('<div class="toc-entry">')
                parts.append(f'<span class="toc-ch">第{ch}章</span>')
                parts.append(f'<span class="toc-title">{title}<span class="toc-subtitle"> — {subtitle}</span></span>')
                parts.append(f'<span class="toc-count">{count}题</span>')
                parts.append('</div>')

    parts.append(f'<div style="text-align:right;margin-top:2em;font-size:9pt;color:#888">共计{TOTAL}题</div>')
    parts.append('</div>')

    # === ALL CHAPTERS ===
    for ch, title, subtitle, count in CHAPTERS:
        html_path = TEXTBOOK / f"chapter{ch:02d}_print.html"
        if not html_path.exists():
            print(f"  ⚠️  Ch{ch} HTML not found, skipping")
            continue

        body = extract_body(html_path)

        # Replace the chapter-title div (keep as-is, just add chapter number context)
        full_title = f"第{ch}章 {title} — {subtitle}"
        body = re.sub(
            r'<div class="chapter-title">([^<]+)</div>',
            f'<div class="chapter-title">\\1</div>',
            body, count=1
        )
        # Update subtitle to clearly show chapter number and scope
        body = re.sub(
            r'<div class="chapter-subtitle">[^<]+</div>',
            f'<div class="chapter-subtitle">第{ch}章 · {subtitle} · {count}题 · C++ &amp; Python 双语对照</div>',
            body, count=1
        )

        # Wrap chapter in a div that forces page break and sets header
        parts.append(f'<div class="chapter-start">')
        parts.append(body)
        parts.append('</div>')

    # Build final HTML
    total_body = '\n'.join(parts)

    final_html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>基于Trae的编程兴趣班入门百练</title>
<style>{combined_css}</style>
</head>
<body>
{total_body}
</body>
</html>"""

    out_path = TEXTBOOK / "combined_print.html"
    out_path.write_text(final_html, encoding='utf-8')
    return out_path

def build_combined_pdf(html_path):
    """Generate combined PDF from HTML using Chrome headless."""
    pdf_path = TEXTBOOK / "基于Trae的编程兴趣班入门百练.pdf"
    file_url = html_path.as_uri()
    result = subprocess.run([
        CHROME, "--headless", "--disable-gpu",
        f"--print-to-pdf={pdf_path}",
        "--no-pdf-header-footer",
        file_url
    ], capture_output=True, text=True, timeout=120)
    if pdf_path.exists():
        size_kb = pdf_path.stat().st_size // 1024
        print(f"✅ Combined PDF: {size_kb}KB → {pdf_path.name}")
        return pdf_path
    else:
        print(f"❌ Combined PDF FAILED: {result.stderr[:300]}")
        return None

def build_combined_docx(html_path):
    """Generate combined DOCX from HTML using pandoc."""
    docx_path = TEXTBOOK / "基于Trae的编程兴趣班入门百练.docx"
    result = subprocess.run([
        "pandoc", str(html_path), "-f", "html", "-t", "docx",
        "-o", str(docx_path),
        "--resource-path", str(TEXTBOOK),
        "--metadata", "title=基于Trae的编程兴趣班入门百练"
    ], capture_output=True, text=True, timeout=180)
    if docx_path.exists():
        size_kb = docx_path.stat().st_size // 1024
        print(f"✅ Combined DOCX: {size_kb}KB → {docx_path.name}")
        return docx_path
    else:
        print(f"❌ Combined DOCX FAILED: {result.stderr[:300]}")
        return None

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf", action="store_true", default=True)
    parser.add_argument("--docx", action="store_true", default=True)
    parser.add_argument("--no-pdf", action="store_true")
    parser.add_argument("--no-docx", action="store_true")
    args = parser.parse_args()

    print("Building combined HTML...")
    html_path = build_combined_html()
    print(f"  ✅ Combined HTML: {html_path.stat().st_size//1024}KB")

    if args.no_pdf:
        args.pdf = False
    if args.no_docx:
        args.docx = False

    if args.pdf:
        print("\nGenerating combined PDF...")
        build_combined_pdf(html_path)

    if args.docx:
        print("\nGenerating combined DOCX...")
        build_combined_docx(html_path)

    print("\nDone!")
