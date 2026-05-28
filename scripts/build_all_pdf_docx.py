#!/usr/bin/env python3
"""批量生成16章的PDF和DOCX — 从_print.html通过Chrome headless + pandoc"""
import subprocess, os, sys, time
from pathlib import Path

BOOK_ROOT = Path(__file__).parent.parent.resolve()
TEXTBOOK = BOOK_ROOT / "textbook"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

CHAPTERS = [
    (1, "第1章 程序设计的第一个脚印"),
    (2, "第2章 选择的艺术"),
    (3, "第3章 循环的魔力"),
    (4, "第4章 数据的容器"),
    (5, "第5章 矩阵的舞蹈"),
    (6, "第6章 字符的世界"),
    (7, "第7章 模块化的力量"),
    (8, "第8章 指针与抽象"),
    (9, "第9章 分治之美"),
    (10, "第10章 预处理的智慧"),
    (11, "第11章 计算的边界"),
    (12, "第12章 结构的魔力"),
    (13, "第13章 搜索的艺术"),
    (14, "第14章 图的疆域"),
    (15, "第15章 状态的艺术"),
    (16, "第16章 终极试炼"),
]

def build_pdf(ch, title):
    html_path = TEXTBOOK / f"chapter{ch:02d}_print.html"
    pdf_path = TEXTBOOK / f"chapter{ch:02d}.pdf"
    if not html_path.exists():
        print(f"  ❌ Ch{ch}: HTML not found: {html_path}")
        return False
    file_url = html_path.as_uri()
    result = subprocess.run([
        CHROME, "--headless", "--disable-gpu",
        f"--print-to-pdf={pdf_path}",
        "--no-pdf-header-footer",
        file_url
    ], capture_output=True, text=True, timeout=60)
    if pdf_path.exists():
        size_kb = pdf_path.stat().st_size // 1024
        print(f"  ✅ Ch{ch} PDF: {size_kb}KB — {title}")
        return True
    else:
        print(f"  ❌ Ch{ch} PDF FAILED: {result.stderr[:200]}")
        return False

def build_docx(ch, title):
    html_path = TEXTBOOK / f"chapter{ch:02d}_print.html"
    docx_path = TEXTBOOK / f"chapter{ch:02d}.docx"
    if not html_path.exists():
        print(f"  ❌ Ch{ch}: HTML not found: {html_path}")
        return False
    result = subprocess.run([
        "pandoc", str(html_path), "-f", "html", "-t", "docx",
        "-o", str(docx_path),
        "--resource-path", str(TEXTBOOK)
    ], capture_output=True, text=True, timeout=120)
    if docx_path.exists():
        size_kb = docx_path.stat().st_size // 1024
        print(f"  ✅ Ch{ch} DOCX: {size_kb}KB — {title}")
        return True
    else:
        print(f"  ❌ Ch{ch} DOCX FAILED: {result.stderr[:200]}")
        return False

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf", action="store_true", default=True, help="Generate PDF (default)")
    parser.add_argument("--docx", action="store_true", default=True, help="Generate DOCX (default)")
    parser.add_argument("--ch", type=int, help="Build single chapter")
    args = parser.parse_args()

    chapters = CHAPTERS
    if args.ch:
        chapters = [c for c in CHAPTERS if c[0] == args.ch]

    print(f"\n{'='*60}")
    print(f"Building {len(chapters)} chapter(s)...")
    print(f"{'='*60}\n")

    pdf_ok = docx_ok = 0
    for ch, title in chapters:
        if args.pdf:
            if build_pdf(ch, title):
                pdf_ok += 1
        if args.docx:
            if build_docx(ch, title):
                docx_ok += 1
        time.sleep(0.3)  # prevent Chrome from being overwhelmed

    print(f"\n{'='*60}")
    if args.pdf:
        print(f"PDF: {pdf_ok}/{len(chapters)} OK")
    if args.docx:
        print(f"DOCX: {docx_ok}/{len(chapters)} OK")
    print(f"{'='*60}")
