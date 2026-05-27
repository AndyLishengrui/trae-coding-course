#!/usr/bin/env python3
"""第5章 矩阵的舞蹈——多维数组与矩阵模式 (增强版)"""
import json, re, os, sys
from pathlib import Path
BOOK_ROOT = Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(BOOK_ROOT / 'scripts'))

PROBLEMS = [
    {"nq":"NQ055","acw":745,"title":"数组的右上半部分",
     "desc":"计算12×12矩阵右上半部分（j>i，不含主对角线）所有元素的平均值或和。右上半部分共66个元素。理解三角区域遍历是矩阵操作的核心技能。",
     "input":"第一行操作类型(S/M)。然后144个浮点数（逐行读入）。","output":"结果保留1位小数。S输出和，M输出平均值。",
     "sample_in":"S\n(144个浮点数...)","sample_out":"(sum,1 decimal)","constraint":"矩阵元素−10⁶到10⁶",
     "sol":"右上三角：j>i。双层循环遍历矩阵，当j>i时累加。不包括对角线。66个元素。S求总和，M求平均时除以66（注意不是144）。区域遍历是矩阵题的灵魂——关键在于找到正确的行列关系表达式。",
     "tip":"右上三角条件：j>i。共有元素数=(12×12−12)/2=66。C++用double型累加，注意不要用int。Python的float是双精度。"},
    {"nq":"NQ056","acw":747,"title":"数组的左上半部分",
     "desc":"计算12×12矩阵左上半部分（j<11-i，反对角线上方）所有元素的平均值或和。共66个元素。注意与右上三角的区别——一个是主对角线(j>i)，一个是反对角线(j<11-i)。",
     "input":"操作类型(S/M)+144浮点数。","output":"保留1位小数。","sample_in":"S\n(144...)","sample_out":"(sum,1 decimal)","constraint":"同NQ055",
     "sol":"左上三角：j<11-i（反对角线以上）。反对角线条件：i+j=11。元素数量也是66。将四个三角区域的遍历条件对比理解，是掌握矩阵区域操作的关键——j>i（右上）、j<i（左下）、i+j<11（左上）、i+j>11（右下）。",
     "tip":"反对角线条件：i+j==n-1（n=12时为11）。左上三角用<。四个区域条件对称且互补，理解这一规律后所有矩阵三角题迎刃而解。"},
    {"nq":"NQ057","acw":749,"title":"数组的上方区域",
     "desc":"计算12×12矩阵上方区域（去掉左右两个三角的剩余部分）的元素和或平均值。上方区域需同时满足i<j且i+j<11，共30个元素。双重条件交集是区域遍历的进阶技能。",
     "input":"操作类型(S/M)+144浮点数。","output":"保留1位小数。","sample_in":"S\n(144...)","sample_out":"(sum,1 decimal)","constraint":"同NQ055",
     "sol":"上方区域是两个三角的交集：i<j（主对角线之上）且i+j<11（反对角线之上）。30个元素——矩阵的一半再减半。这种双重条件判断展示了用数学表达式精确描述区域的能力。","tip":"交集条件：i<j and i+j<11。从\"单一条件描述三角\"到\"两个条件交集描述更小区域\"，是逻辑思维和代码能力的双重进阶。"},
    {"nq":"NQ058","acw":751,"title":"数组的左方区域","desc":"计算12×12矩阵左方区域的元素和或平均值。条件：j<i且i+j<11。与上方区域形成左右对称。","input":"操作类型(S/M)+144浮点数。","output":"保留1位小数。","sample_in":"S\n(144...)","sample_out":"(sum,1 decimal)","constraint":"同NQ055","sol":"左方区域与上方区域对称：将j<i替换为i<j。观察NQ057和NQ058的条件——j和i的角色互换。这种对称模式是理解多维数组遍历的基础。","tip":"左右对称：互换i和j的角色。上方=去掉左右三角的上部，左方=去掉上下三角的左部。对称思维是编程中的强大工具。"},
    {"nq":"NQ059","acw":753,"title":"平方矩阵I","desc":"输入整数N（多组，0结束），输出N×N的回字形矩阵。每个位置的值=min(i+1,j+1,N-i,N-j)。这是用数学公式替代模拟填充的经典案例——一行公式替代几十行循环代码。","input":"多个整数N，以0结束。","output":"每个矩阵占N行，每个数占3字符宽度右对齐。矩阵间空行。","sample_in":"1\n2\n3\n0","sample_out":"  1\n\n  1  1\n  1  1\n\n  1  1  1\n  1  2  1\n  1  1  1","constraint":"1≤N≤100","sol":"数学公式法：val=min(i,j,n-1-i,n-1-j)+1（0-indexed）。这个公式的物理意义：每个位置的值等于它到四条边的最短距离加1。最外层距离为0→值=1，往里一层距离为1→值=2，以此类推。理解公式比手写模拟更体现编程智慧。","tip":"到四条边的距离：上i、左j、下n-1-i、右n-1-j。取最小值+1即为该位置的值。这个公式体现了\"数学建模\"的力量——用数学语言描述复杂的几何规律。"},
    {"nq":"NQ060","acw":748,"title":"数组的右下半部分","desc":"计算12×12矩阵右下半部分所有元素的平均值或和。条件：j>10-i（即i+j>10）。与左上半部分对称。","input":"操作类型(S/M)+144浮点数。","output":"保留1位小数。","sample_in":"S\n(144...)","sample_out":"(sum,1 decimal)","constraint":"同NQ055","sol":"右下三角：i+j>10。与NQ056的左上三角(i+j<11)对称。通过前6个矩阵三角题的系统训练，你应该已经掌握了区域遍历的核心技巧：找到正确的行列关系表达式。","tip":"i+j>10与11-i-1通。矩阵遍历的4个三角区域至此全部覆盖：↗(j>i)、↖(j<11-i)、↙(j<i)、↘(i+j>10)。建议画一个5×5矩阵逐格验证。"},
    {"nq":"NQ061","acw":746,"title":"数组的左下半部分","desc":"计算12×12矩阵左下半部分(j<i)元素的和或平均值。NQ060-NQ063共4题遍历矩阵的4个三角区域。","input":"操作类型(S/M)+144浮点数。","output":"保留1位小数。","sample_in":"S\n(144...)","sample_out":"(sum,1 decimal)","constraint":"同NQ055","sol":"左下三角：j<i。与右上三角(j>i)对称。遍历条件简单明了——i和j的大小关系决定位置归属。注意不包括主对角线。","tip":"四个三角区域的条件总结：右上j>i、左下j<i、左上j<11-i、右下j>10-i。掌握这4个条件，所有标准矩阵三角题都不在话下。"},
    {"nq":"NQ062","acw":750,"title":"数组的下方区域","desc":"计算12×12矩阵下方区域的元素和或平均值。条件：i>j且i+j>10。与上方区域对称，共30个元素。","input":"操作类型(S/M)+144浮点数。","output":"保留1位小数。","sample_in":"S\n(144...)","sample_out":"(sum,1 decimal)","constraint":"同NQ055","sol":"下方区域：i>j且i+j>10。与上方区域(i<j且i+j<11)对称。至此8道矩阵题全部完成——4个三角区域+2个交集区域+2个对角区域+蛇形矩阵。","tip":"对称总结：上方(i<j,i+j<11)、下方(i>j,i+j>10)、左方(j<i,i+j<11)、右方(j>i,i+j>10)。四个区域构成一个完整的\"口\"字形框架。"},
    {"nq":"NQ063","acw":752,"title":"数组的右方区域","desc":"计算12×12矩阵右方区域的元素和或平均值。条件：j>i且i+j>10。与左方区域对称。","input":"操作类型(S/M)+144浮点数。","output":"保留1位小数。","sample_in":"S\n(144...)","sample_out":"(sum,1 decimal)","constraint":"同NQ055","sol":"右方区域：j>i且i+j>10。30个元素。至此矩阵区域遍历全部完成。8道题的变化本质是条件表达式的组合。掌握了规律，任何形状的区域都能精确描述。","tip":"四个\"口\"字区域全部完成后，你的二维数组遍历能力已经达到面试水平。Key takeaway：精确的行列条件表达式=矩阵操作的全部。"},
    {"nq":"NQ064","acw":754,"title":"平方矩阵II","desc":"输入N，输出N×N矩阵。每个位置的值=|i-j|+1。这是对角线距离模型——对角线上的值最小(1)，距离对角线越远值越大。","input":"多个整数N（0结束）。","output":"N×N矩阵，每个数占3字符宽。矩阵间空行。","sample_in":"3\n0","sample_out":"  1  2  3\n  2  1  2\n  3  2  1","constraint":"1≤N≤100","sol":"|i-j|+1公式产生以主对角线为对称轴的矩阵。对角线上|i-j|=0→值=1，离对角线每远一步值增加1。这比平方矩阵I的\"四边距离\"公式更简单，展示了另一种数学建模方式。","tip":"abs(i-j)+1。C++用stdlib的abs()，Python内置abs()。注意绝对值函数对负数的处理——自动取正。这种\"距离模型\"在矩阵题中非常常见。"},
    {"nq":"NQ065","acw":755,"title":"平方矩阵III","desc":"输入N，输出N×N矩阵。每个位置的值=2^(i+j)。展示指数增长的矩阵模式。注意N≤15确保最大值2^28约2.68亿在int范围内。","input":"多个整数N（0结束）。","output":"每个数右对齐到最大数的宽度+1。矩阵间空行。","sample_in":"3\n0","sample_out":"  1  2  4\n  2  4  8\n  4  8 16","constraint":"1≤N≤15","sol":"2^(i+j)模式。C++用1<<(i+j)位运算高效计算2的幂。Python可以2**(i+j)或1<<(i+j)。右对齐宽度=最长数字的位数+1。注意N≤15的限制：N=15时2^28≈2.68×10⁸(9位数)。","tip":"C++的1<<k比pow(2,k)快得多。Python的2**k和1<<k性能相近。格式化右对齐：Python的f'{x:{w}d}'，C++的setw(w)。"},
    {"nq":"NQ066","acw":756,"title":"蛇形矩阵","desc":"输入n和m，输出n×m蛇形矩阵。从(0,0)开始向右填充，撞墙或遇到已填格子时顺时针转向。这是方向数组的经典应用——4个方向轮流执行，直到填满所有格子。","input":"一行两个整数n和m。","output":"n行m列的蛇形矩阵。","sample_in":"3 3","sample_out":"1 2 3\n8 9 4\n7 6 5","constraint":"1≤n,m≤100","sol":"方向数组+边界检测。dx=[0,1,0,-1], dy=[1,0,-1,0]依次控制→↓←↑。撞墙或已填则转向d=(d+1)%4。while循环填充所有格子。方向数组是解决螺旋/蛇形/遍历类问题的通用模板——只需改变方向顺序就能实现不同的遍历模式。","tip":"方向数组是处理网格遍历的万能钥匙。记住4个方向的顺序和dx/dy的对应关系。Python中提前分配二维数组：[[0]*m for _ in range(n)]（注意不能用[[0]*m]*n！）。"},
]

from pygments import highlight; from pygments.lexers import CppLexer, PythonLexer; from pygments.formatters import HtmlFormatter
CPP_FMT=HtmlFormatter(style='vs',noclasses=True); PY_FMT=HtmlFormatter(style='vs',noclasses=True)
def hl(code,lexer,fmt):
    if not code:return''
    h=highlight(code,lexer,fmt);m=re.search(r'<pre[^>]*>(.*)</pre>',h,re.DOTALL)
    return re.sub(r'<span></span>\n?','',m.group(1))if m else code

CODE_CACHE={}
for d in['acwing_codes','algorithm_basic_codes']:
    for root,dirs,files in os.walk(str(BOOK_ROOT/d)):
        for f in files:
            if f.endswith('.cpp'):
                m=re.search(r'AcWing\s+(\d+)',f)
                if m:CODE_CACHE[int(m.group(1))]=open(os.path.join(root,f)).read().strip()
PY_CACHE={}
for ch in range(1,17):
    bank_dir=BOOK_ROOT/f'chapter{ch}_bank'
    if bank_dir.exists():
        for d in bank_dir.iterdir():
            if d.is_dir():
                py_file=d/'Andy.py'
                if py_file.exists():
                    c=py_file.read_text().strip()
                    if len(c)>20 and not c.startswith('# AcWing'):
                        m=re.search(r'ACW(\d+)',d.name)
                        if m:PY_CACHE[int(m.group(1))]=c

CSS="""@page{size:A4;margin:2.2cm 2cm 2.2cm 2cm;@top-center{content:string(chapter);font-size:7.5pt;color:#999}@bottom-center{content:counter(page);font-size:7.5pt;color:#999}}
body{font-family:"PingFang SC","Hiragino Sans GB","Noto Serif CJK SC","STSong",serif;font-size:9.5pt;line-height:1.7;color:#222;string-set:chapter"第5章 矩阵的舞蹈——多维数组与矩阵模式"}
.chapter-title{text-align:center;font-size:20pt;font-weight:bold;margin:1.5em 0 .1em 0;letter-spacing:3pt}
.chapter-subtitle{text-align:center;font-size:10pt;color:#777;margin-bottom:1.5em;padding-bottom:.8em;border-bottom:1px solid #bbb}
.preface{font-size:10pt;margin-bottom:1.5em;color:#444}.preface p{margin:.3em 0;text-indent:2em}
.preface h3{font-size:11pt;color:#2563eb;margin:1em 0 .3em 0}
.knowledge-box{background:#f0f6ff;border:1pt solid #bdd;border-radius:4px;padding:.7em 1em;margin:.8em 0;font-size:9pt}
.knowledge-box .k-title{font-weight:bold;color:#2563eb;margin-bottom:.3em;font-size:9.5pt}
.knowledge-box p{margin:.2em 0}.knowledge-box ul{margin:.2em 0;padding-left:1.5em}
.problem-title{font-size:12pt;font-weight:bold;margin:1.5em 0 .4em 0;padding-bottom:.15em;border-bottom:1pt solid #444}
.problem-title .nq{color:#2563eb;margin-right:.6em;font-size:11pt}.problem-title .acw{font-size:7.5pt;color:#aaa;font-weight:normal;margin-left:1em}
.problem-desc{margin:.6em 0 1em 0;text-indent:2em;line-height:1.85}
.spec-table{width:100%;border-collapse:collapse;margin:.3em 0 .5em 0;font-size:9pt}
.spec-table td{padding:.3em .8em;vertical-align:top;border:none}
.spec-table .spec-label{width:4em;font-size:8pt;font-weight:bold;text-align:right;padding-right:1em;white-space:nowrap}
.spec-table .spec-label .tag{display:inline-block;padding:.15em .5em;border-radius:2px;color:#fff;font-size:7.5pt;letter-spacing:.5pt}
.spec-table .spec-label .tag.in{background:#2563eb}.spec-table .spec-label .tag.out{background:#059669}.spec-table .spec-label .tag.lim{background:#d97706}
.spec-table .spec-value{color:#333;font-size:9pt}
.sample-box{background:#f7f8fa;border:.5pt solid #dde;border-radius:4px;padding:.7em 1em;margin:1em 0 1.2em 0}
.sample-grid{display:flex;gap:2em}.sample-col{flex:1}
.sample-col .col-label{font-size:7.5pt;color:#888;margin-bottom:.2em;font-weight:bold}
.sample-col pre{background:none;border:none;padding:.3em 0;margin:0;font-family:"SF Mono","Menlo","Consolas",monospace;font-size:9pt;line-height:1.4;white-space:pre-wrap;color:#333}
.insight-block{margin:.8em 0;padding:.5em .8em;border-left:3px solid #2563eb;background:#f8faff}
.insight-block .insight-label{font-size:8pt;font-weight:bold;color:#2563eb;margin-right:.5em}
.code-dual{display:flex;gap:1.2em;margin:1.2em 0;page-break-inside:avoid}.code-col{min-width:0}.code-col:first-child{flex:3}.code-col:last-child{flex:2}
.code-col .lang-badge{display:inline-block;font-size:7.5pt;font-weight:bold;color:#fff;background:#2563eb;padding:.2em .7em;border-radius:3px;margin-bottom:.4em}
.code-col pre{background:#f8f8f0;border:.5pt solid #e0e0e0;border-radius:4px;padding:.7em .9em;font-family:"SF Mono","Menlo","Consolas","Courier New",monospace;font-size:7.5pt;line-height:1.45;overflow-x:auto;margin:0;white-space:pre-wrap;word-break:break-all}
.section-divider{border:none;border-top:.3pt solid #e0e0e0;margin:1em 0 0 0}
.chapter-summary{background:#f8fafc;border:1pt solid #ddd;border-radius:4px;padding:1em 1.5em;margin:2em 0;font-size:9pt}
.chapter-summary h3{font-size:11pt;color:#2563eb;margin:0 0 .5em 0}.chapter-summary ul{margin:.3em 0;padding-left:1.5em}
.chapter-end{text-align:center;margin-top:3em;font-size:8pt;color:#999}"""

def build_html():
    parts=[]
    parts.append('<div class="chapter-title">矩阵的舞蹈</div>')
    parts.append('<div class="chapter-subtitle">多维数组与矩阵模式 · 12题 · C++ &amp; Python 双语对照</div>')
    parts.append('<div class="preface">')
    parts.append('<p>上一章我们认识了一维数组——数据排成一排。这一章，我们将数据排成<strong>行和列</strong>，进入二维数组的世界。矩阵（Matrix）是科学计算、图像处理、游戏开发中最常用的数据结构之一——从像素网格到电子表格，从棋盘游戏到线性代数，矩阵无处不在。</p>')
    parts.append('<p>本章12道题分为三个板块：<strong>区域遍历</strong>（NQ055-063）——精确地遍历矩阵的三角区域、<strong>模式填充</strong>（NQ059,064,065）——用数学公式生成漂亮的数字图案、<strong>蛇形遍历</strong>（NQ066）——方向数组的经典实战。每一题都在训练你用<strong>数学表达式精确描述二维区域</strong>的能力。</p>')
    parts.append('<h3>本章学习目标</h3>')
    parts.append('<p>① 理解二维数组的行优先存储和索引规则</p><p>② 掌握用行列关系表达式描述任意几何区域</p><p>③ 学会用数学公式替代模拟填充——编程智慧的体现</p><p>④ 入门方向数组——网格遍历的万能钥匙</p>')
    parts.append('</div>')
    parts.append('<div class="knowledge-box"><div class="k-title">🧭 矩阵三角区域速查表（12×12矩阵）</div>')
    parts.append('<ul><li>↗ <strong>右上三角</strong>：j > i（不含对角线，66个元素）</li><li>↖ <strong>左上三角</strong>：j < 11-i（不含反对角线，66个元素）</li>')
    parts.append('<li>↙ <strong>左下三角</strong>：j < i（不含对角线，66个元素）</li><li>↘ <strong>右下三角</strong>：i+j > 10（66个元素）</li>')
    parts.append('<li>⬆ <strong>上方区域</strong>：i < j 且 i+j < 11（30个元素）</li><li>⬇ <strong>下方区域</strong>：i > j 且 i+j > 10（30个元素）</li>')
    parts.append('<li>⬅ <strong>左方区域</strong>：j < i 且 i+j < 11（30个元素）</li><li>➡ <strong>右方区域</strong>：j > i 且 i+j > 10（30个元素）</li></ul>')
    parts.append('<p><strong>总览：</strong>矩阵可分4个三角区域（各66元素）和4个\"口\"字侧边区域（各30元素）。记住条件表达式=掌握所有矩阵区域遍历。</p></div>')

    for p in PROBLEMS:
        pb=['<div class="problem-block">']
        pb.append(f'<div class="problem-title"><span class="nq">{p["nq"]}</span>{p["title"]}<span class="acw">AcWing {p["acw"]}</span></div>')
        pb.append(f'<div class="problem-desc">{p["desc"]}</div>')
        pb.append('<table class="spec-table">')
        pb.append(f'<tr><td class="spec-label"><span class="tag in">输入</span></td><td class="spec-value">{p["input"]}</td></tr>')
        pb.append(f'<tr><td class="spec-label"><span class="tag out">输出</span></td><td class="spec-value">{p["output"]}</td></tr>')
        pb.append(f'<tr><td class="spec-label"><span class="tag lim">范围</span></td><td class="spec-value">{p["constraint"]}</td></tr>')
        pb.append('</table>')
        pb.append('<div class="sample-box"><div class="sample-grid">')
        pb.append(f'<div class="sample-col"><div class="col-label">输入</div><pre>{p["sample_in"]}</pre></div>')
        pb.append(f'<div class="sample-col"><div class="col-label">输出</div><pre>{p["sample_out"]}</pre></div>')
        pb.append('</div></div>')
        pb.append(f'<div class="insight-block"><span class="insight-label">思路</span><span>{p["sol"]}</span></div>')
        pb.append(f'<div class="insight-block"><span class="insight-label">技巧</span><span>{p["tip"]}</span></div>')
        cpp=CODE_CACHE.get(p['acw'],f'// AcWing {p["acw"]}')
        py=PY_CACHE.get(p['acw'],'# Python solution')
        pb.append('<div class="code-dual">')
        pb.append(f'<div class="code-col"><div class="lang-badge">C++</div><pre>{hl(cpp,CppLexer(),CPP_FMT)}</pre></div>')
        pb.append(f'<div class="code-col"><div class="lang-badge">Python</div><pre>{hl(py,PythonLexer(),PY_FMT)}</pre></div>')
        pb.append('</div></div><hr class="section-divider">')
        parts.append('\n'.join(pb))

    parts.append('<div class="chapter-summary"><h3>📋 本章知识点总结</h3><ul>')
    parts.append('<li><strong>8种矩阵区域</strong>：4个三角（各66元素）+ 4个\"口\"字边（各30元素）= 精确遍历矩阵任意形状</li>')
    parts.append('<li><strong>3种填充模式</strong>：四边距离min公式、对角线距离abs公式、2的指数幂模式——用数学替代模拟</li>')
    parts.append('<li><strong>方向数组</strong>：dx=[0,1,0,-1], dy=[1,0,-1,0] → 控制四个方向旋转，蛇形/螺旋/遍历通用模板</li>')
    parts.append('<li><strong>关键技巧</strong>：Python二维列表[[0]*m for _ in range(n)]（注意不能用*操作符浅拷贝！）</li>')
    parts.append('<li><strong>对称思维</strong>：上下、左右区域的行列条件只是i和j角色的互换——理解对称性可举一反三</li>')
    parts.append('</ul></div>')
    parts.append('<div class="chapter-end">— 第5章完 · 共12题 —</div>')

    html=f"""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"><title>第5章 矩阵的舞蹈</title><style>{CSS}</style></head><body>{chr(10).join(parts)}</body></html>"""
    out=BOOK_ROOT/"textbook"/"chapter05_print.html"
    out.write_text(html,encoding='utf-8')
    print(f"✅ Ch5 enhanced: {len(html)} chars")

if __name__=="__main__":
    build_html()
