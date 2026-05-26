#!/usr/bin/env python3
"""Rebuild chapters 5-16 with real OJ descriptions."""
import json, re, os, sys
from pathlib import Path

BOOK_ROOT = Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(Path(__file__).parent))

with open(Path(__file__).parent / 'chapter5_16_data.json', 'r', encoding='utf-8') as f:
    REAL_DATA = json.load(f)

CODE_CACHE = {}
PY_CACHE = {}
for d in ['acwing_codes', 'algorithm_basic_codes']:
    for root, dirs, files in os.walk(str(BOOK_ROOT/d)):
        for f in files:
            if f.endswith('.cpp'):
                m = re.search(r'AcWing\s+(\d+)', f)
                if m:
                    with open(os.path.join(root, f)) as fh:
                        CODE_CACHE[int(m.group(1))] = fh.read().strip()

# Also read Python from chapter banks and NQ100 source
for ch in range(1, 17):
    bank_dir = BOOK_ROOT / f'chapter{ch}_bank'
    if bank_dir.exists():
        for d in bank_dir.iterdir():
            if d.is_dir():
                py_file = d / 'Andy.py'
                if py_file.exists():
                    py_content = py_file.read_text().strip()
                    if len(py_content) > 20 and not py_content.startswith('# AcWing') and not py_content.startswith('# Python'):
                        # Extract PID from dirname like "ACW745.xxx"
                        m = re.search(r'ACW(\d+)', d.name)
                        if m:
                            PY_CACHE[int(m.group(1))] = py_content
# NQ100 source Python
nq_src = BOOK_ROOT / 'source' / 'algorithm'
if nq_src.exists():
    for d in nq_src.iterdir():
        if d.is_dir():
            py_files = list(d.glob('*improved.py'))
            if py_files:
                py_content = py_files[0].read_text().strip()
                if len(py_content) > 50:
                    PY_CACHE[d.name] = py_content  # key is NQxxx

from xmuoj_cli.constants import V2_PLAN, CHAPTER_TITLES
from pygments import highlight
from pygments.lexers import CppLexer, PythonLexer
from pygments.formatters import HtmlFormatter

CPP_FMT = HtmlFormatter(style='vs', noclasses=True)
PY_FMT = HtmlFormatter(style='vs', noclasses=True)

def hl(code, lexer, fmt):
    if not code: return '// no code'
    h = highlight(code, lexer, fmt)
    m = re.search(r'<pre[^>]*>(.*)</pre>', h, re.DOTALL)
    return re.sub(r'<span></span>\n?', '', m.group(1)) if m else code

CSS = r"""@page{size:A4;margin:2.2cm 2cm 2.2cm 2cm;@top-center{content:string(chapter);font-size:7.5pt;color:#999;font-family:"PingFang SC",sans-serif}@bottom-center{content:counter(page);font-size:7.5pt;color:#999}}
body{font-family:"PingFang SC","Hiragino Sans GB","Noto Serif CJK SC","STSong",serif;font-size:9.5pt;line-height:1.7;color:#222}
.chapter-title{text-align:center;font-size:20pt;font-weight:bold;margin:1.5em 0 .1em 0;letter-spacing:3pt}
.chapter-subtitle{text-align:center;font-size:10pt;color:#777;margin-bottom:1.5em;padding-bottom:.8em;border-bottom:1px solid #bbb}
.problem-title{font-size:12pt;font-weight:bold;margin:1.5em 0 .4em 0;padding-bottom:.15em;border-bottom:1pt solid #444}
.problem-title .nq{color:#2563eb;margin-right:.6em;font-size:11pt}.problem-title .acw{font-size:7.5pt;color:#aaa;font-weight:normal;margin-left:1em}
.problem-desc{margin:.6em 0 1em 0;text-indent:2em;line-height:1.85}
.spec-table{width:100%;border-collapse:collapse;margin:.3em 0 .5em 0;font-size:9pt}
.spec-table td{padding:.3em .8em;vertical-align:top;border:none}
.spec-table .spec-label{width:4em;font-size:8pt;font-weight:bold;text-align:right;padding-right:1em;white-space:nowrap}
.spec-table .spec-label .tag{display:inline-block;padding:.15em .5em;border-radius:2px;color:#fff;font-size:7.5pt;letter-spacing:.5pt}
.spec-table .spec-label .tag.in{background:#2563eb}.spec-table .spec-label .tag.out{background:#059669}.spec-table .spec-label .tag.lim{background:#d97706}
.spec-table .spec-value{color:#333;font-size:9pt}
.sample-box{background:#f7f8fa;border:.5pt solid #dde;border-radius:4px;padding:.5em 1em;margin:.8em 0 1em 0}
.sample-grid{display:flex;gap:1.5em}.sample-col{min-width:0}.sample-col:first-child{flex:1}.sample-col:last-child{flex:1}
.sample-col .col-label{font-size:7.5pt;color:#888;margin-bottom:0;font-weight:bold}
.sample-col pre{background:none;border:none;padding:.2em 0;margin:0;font-family:"SF Mono","Menlo","Consolas",monospace;font-size:8.5pt;line-height:1.3;white-space:pre-wrap;color:#333}
.insight-block{margin:.8em 0;padding:.5em .8em;border-left:3px solid #2563eb;background:#f8faff}
.insight-block .insight-label{font-size:8pt;font-weight:bold;color:#2563eb;margin-right:.5em}
.code-dual{display:flex;gap:1.2em;margin:1.2em 0;page-break-inside:avoid}.code-col{min-width:0}.code-col:first-child{flex:3}.code-col:last-child{flex:2}
.code-col .lang-badge{display:inline-block;font-size:7.5pt;font-weight:bold;color:#fff;background:#2563eb;padding:.2em .7em;border-radius:3px;margin-bottom:.4em}
.code-col pre{background:#f8f8f0;border:.5pt solid #e0e0e0;border-radius:4px;padding:.7em .9em;font-family:"SF Mono","Menlo","Consolas","Courier New",monospace;font-size:7.5pt;line-height:1.45;overflow-x:auto;margin:0;white-space:pre-wrap;word-break:break-all}
.section-divider{border:none;border-top:.3pt solid #e0e0e0;margin:1em 0 0 0}.chapter-end{text-align:center;margin-top:3em;font-size:8pt;color:#999}"""

for ch in range(5, 17):
    title = CHAPTER_TITLES[ch]
    chapter_name = title.split("——")[0] if "——" in title else title[:10]
    pids = V2_PLAN[ch]
    n = len(pids)
    nq_base = sum(len(V2_PLAN[c]) for c in range(1, ch)) + 1

    parts = []
    for i, pid in enumerate(pids):
        nq = f"NQ{nq_base + i:03d}"
        data = REAL_DATA.get(str(ch), {}).get(str(pid), {})
        desc = data.get('description', f'AcWing {pid}')
        input_fmt = data.get('input_description', '见原题')
        output_fmt = data.get('output_description', '见原题')
        samples = data.get('samples', [])
        hint = data.get('hint', '')
        acw_title = data.get('title', f'AcWing {pid}')
        sample_in = samples[0].get('input', '') if samples else ''
        sample_out = samples[0].get('output', '') if samples else ''
        cpp = CODE_CACHE.get(pid, f'// AcWing {pid}')
        py = PY_CACHE.get(pid) or PY_CACHE.get(f'NQ{pid:03d}') or '# Python solution pending'

        pb = ['<div class="problem-block">']
        pb.append(f'<div class="problem-title"><span class="nq">{nq}</span>{acw_title}<span class="acw">AcWing {pid}</span></div>')
        pb.append(f'<div class="problem-desc">{desc}</div>')
        pb.append('<table class="spec-table">')
        pb.append(f'<tr><td class="spec-label"><span class="tag in">输入</span></td><td class="spec-value">{input_fmt}</td></tr>')
        pb.append(f'<tr><td class="spec-label"><span class="tag out">输出</span></td><td class="spec-value">{output_fmt}</td></tr>')
        pb.append(f'<tr><td class="spec-label"><span class="tag lim">来源</span></td><td class="spec-value">AcWing {pid}</td></tr>')
        pb.append('</table>')
        if sample_in:
            pb.append('<div class="sample-box"><div class="sample-grid">')
            pb.append(f'<div class="sample-col"><div class="col-label">输入</div><pre>{sample_in}</pre></div>')
            pb.append(f'<div class="sample-col"><div class="col-label">输出</div><pre>{sample_out}</pre></div>')
            pb.append('</div></div>')
        if hint:
            pb.append(f'<div class="insight-block"><span class="insight-label">提示</span><span>{hint[:500]}</span></div>')
        pb.append('<div class="code-dual">')
        pb.append(f'<div class="code-col"><div class="lang-badge">C++</div><pre>{hl(cpp, CppLexer(), CPP_FMT)}</pre></div>')
        pb.append(f'<div class="code-col"><div class="lang-badge">Python</div><pre>{hl(py, PythonLexer(), PY_FMT)}</pre></div>')
        pb.append('</div></div><hr class="section-divider">')
        parts.append('\n'.join(pb))

    subtitle = title.split('——')[1] if '——' in title else ''
    html = f"""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"><title>第{ch}章 {chapter_name}</title><style>{CSS}
body{{string-set:chapter "第{ch}章 {title}"}}</style></head><body>
<div class="chapter-title">{chapter_name}</div><div class="chapter-subtitle">{subtitle} · {n}题 · C++ &amp; Python 双语对照</div>
{chr(10).join(parts)}<div class="chapter-end">— 第{ch}章完 · 共{n}题 —</div></body></html>"""

    html_path = BOOK_ROOT / "textbook" / f"chapter{ch:02d}_print.html"
    html_path.write_text(html, encoding="utf-8")
    print(f"  ✅ Ch{ch}: {chapter_name} ({n} problems, {len(html)} chars)")

print(f"\n✅ Chapters 5-16 rebuilt!")
