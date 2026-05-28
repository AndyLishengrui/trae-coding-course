#!/usr/bin/env python3
"""第11章 计算的边界(角色对话版) — 高精度、位运算与离散化"""
import json, re, os, sys
from pathlib import Path
BOOK_ROOT = Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(BOOK_ROOT / 'scripts'))

PROBLEMS = [
    {"nq":"NQ120","acw":791,"title":"高精度加法",
     "story":"\"C++的int最大21亿，long long最大9×10¹⁸——但如果你要算10²⁰⁰+10²⁰⁰呢？\"小华严肃地说。\"这就是高精度计算。C++需要手写大整数——用字符串读入，按位加，处理进位。\"小鲁很惊讶：\"这么基础的操作还要手写？！\"小华笑道：\"对。但这正是Python最震撼的地方——Python的int无精度上限，直接a+b就行。C++手写30行，Python一行。这就是'用对语言'的力量。\"",
     "input":"两行，每行一个正整数（长度≤100000位）。","output":"两数之和。",
     "sample_in":"123456789\n987654321","sample_out":"1111111110","constraint":"数字长度 ≤ 100000",
     "sol":"C++高精度加法：字符串读入→倒序存入vector<int>→按位相加处理进位→倒序输出。核心代码：for i from 0 to max(len): t+=A[i]+B[i]; C.push_back(t%10); t/=10。Python: print(int(input())+int(input()))——震撼教育时刻。",
     "tip":"Python的int底层用30-bit数组存储，自动扩展——可以处理任意大的整数（只受内存限制）。这是Python在算法竞赛中的最大优势之一——高精度计算零负担。C++手写高精度是理解数字表示和进位机制的好练习。"},
    {"nq":"NQ121","acw":792,"title":"高精度减法",
     "story":"\"加法有进位，减法有借位——高精度减法的核心是借位处理。\"小华说，\"首先判断A和B谁大，保证大减小。然后逐位减——如果不够减就向高位借1（当前位+10）。最后去掉前导0。C++手写减法比加法多一步：处理借位+前导0。Python——print(int(input())-int(input()))，又是零负担。\"",
     "input":"两行，每行一个正整数。","output":"A-B的结果。",
     "sample_in":"1000\n1","sample_out":"999","constraint":"数字长度 ≤ 100000",
     "sol":"C++高精度减法：先判断A≥B，若A<B则输出负号并交换。逐位相减：若A[i]<B[i]则借位(A[i]+=10, A[i+1]--)。去掉结果中的前导0。Python: print(int(input())-int(input()))。",
     "tip":"借位处理：if A[i]<B[i]: A[i]+=10; A[i+1]--。前导0如'00123'应输出'123'（但保留最后一个0——结果为0时输出0）。Python的int自动处理所有这些问题。这就是为什么Python在数据处理和AI领域如此流行。"},
    {"nq":"NQ122","acw":801,"title":"二进制中1的个数",
     "story":"\"给你一个整数，求它的二进制表示中1的个数。\"小华说，\"这就是'汉明重量'——编译器优化和密码学中常用的操作。C++用__builtin_popcount()或while(x) cnt+=x&1, x>>=1。Python 3.8+用x.bit_count()。还有lowbit技巧：x&-x取最低位的1，while(x) x-=x&-x, cnt++——比逐位检查更快。\"",
     "input":"一个整数n。","output":"n的二进制表示中1的个数。",
     "sample_in":"5","sample_out":"2","constraint":"0 ≤ n ≤ 10⁹",
     "sol":"三种方法：1)逐位检查while(n): cnt+=n&1; n>>=1；2)lowbit法while(n): n-=n&-n; cnt++——复杂度=1的个数而非位数；3)__builtin_popcount/Python bit_count()一行搞定。lowbit=n&-n是位运算中最精妙的trick之一。",
     "tip":"x&-x取x的最低位的1——证明：负数用补码表示，-x=~x+1，x&~x+1就是最低位1的位置。这个trick在树状数组（Fenwick Tree）中是核心操作。bit_count()是Python 3.8+新特性，C++20有std::popcount。"},
    {"nq":"NQ123","acw":793,"title":"高精度乘法",
     "story":"\"高精度乘高精度——C++手写要三重循环：A的每一位乘B的每一位，结果加到对应位置。\"小华在黑板上演示。小鲁问：\"那乘法是不是比加减法难很多？\"\"对——加减O(n)，朴素乘法O(n²)。还有更快的Karatsuba和FFT算法可以在O(n log n)内完成，但那已经是大数运算的科研前沿了。Python——print(int(input())*int(input()))。\"",
     "input":"两行，每行一个正整数。","output":"乘积。",
     "sample_in":"12\n34","sample_out":"408","constraint":"数字长度 ≤ 100000",
     "sol":"C++高精度乘法：两重循环 C[i+j]+=A[i]*B[j]; C[i+j+1]+=C[i+j]/10; C[i+j]%=10; 最后去前导0。时间复杂度O(len(A)×len(B))。Python的int乘法底层用Karatsuba算法优化——对超长整数自动切换，比手写快得多。",
     "tip":"Python int乘法内部根据数字大小自动选择算法：小数字用基础乘法，大数字切到Karatsuba(O(n^1.585))，超大数字用Toom-Cook。这就是为什么Python数据处理生态如此强大——底层的数学运算经过极致优化。"},
    {"nq":"NQ124","acw":794,"title":"高精度除法",
     "story":"\"除法是四则运算中最复杂的——需要从高位到低位逐位试商。\"小华说。高精度除以低精度相对简单（逐位除）；高精度除以高精度则需要二分法试商。\"好消息是——Python print(int(input())//int(input()))一行搞定，还能同时得到商和余数用divmod(a,b)。高精度四则运算到此全部覆盖——C++手写超越100行，Python四行收工。\"",
     "input":"两行，每行一个正整数。","output":"第一行商，第二行余数。",
     "sample_in":"10\n3","sample_out":"3\n1","constraint":"数字长度 ≤ 100000",
     "sol":"C++高精度除以低精度：从高位到低位，r=r*10+A[i]; C.push_back(r/B); r%=B。高精度除以高精度需二分或减法模拟。Python: divmod(a,b)返回(商,余数)元组。",
     "tip":"Python高精度总结：input(),int(),四则运算——零负担。C++手写高精度的意义在于理解底层运算原理——数字如何存储、进位借位如何处理。两种路径都有价值——但竞赛时用Python省下的时间可以做更多题。"},
    {"nq":"NQ125","acw":802,"title":"区间和",
     "story":"\"有一个无限长的数轴，在几个坐标上加了值。现在要查询若干区间和。\"小华说，\"但坐标范围是−10⁹到10⁹——不能开10⁹大小的数组。怎么办？\"离散化！把所有用到的坐标收集起来，排序去重，映射成0,1,2,...的连续下标。然后用前缀和——问题变成熟悉的区间查询。离散化就是'压缩稀疏坐标'的技术——只存储和处理用得到的数据。\"",
     "input":"第一行n,m。然后n行每行x c（位置加值）。然后m行每行l r（查询区间和）。","output":"每行查询结果。",
     "sample_in":"3 3\n1 2\n3 6\n7 5\n1 3\n4 6\n7 8","sample_out":"8\n0\n5","constraint":"−10⁹ ≤ x ≤ 10⁹, n,m ≤ 100000",
     "sol":"离散化三步骤：1)收集所有坐标(x, l, r)；2)排序去重→映射为0..k-1；3)在压缩后的数组上做前缀和+查询。用二分查找原坐标对应的压缩下标。Python用bisect_left。时间O((n+2m)log(n+2m))。",
     "tip":"离散化是处理稀疏大范围数据的标准手段——坐标0和10⁹之间的空间不需要全部存储。Python: all_x=sorted(set(coords)); idx={v:i+1 for i,v in enumerate(all_x)}（1-indexed）。结合前缀和，大范围区间查询轻松解决。"},
    {"nq":"NQ126","acw":803,"title":"区间合并",
     "story":"\"最后一题——把重叠的区间合并。\"比如[1,3]和[2,6]重叠→合并成[1,6]。\"小华说，\"贪心法：按左端点排序，然后遍历。维护当前合并区间[st,ed]——如果新区间的左端点≤ed说明重叠，更新ed=max(ed, new_ed)；否则当前区间完成，开启新区间。一次排序O(n log n)+一次遍历O(n)——总共O(n log n)。\"",
     "input":"第一行n。然后n行每行l r表示区间。","output":"第一行合并后区间数。然后每行一个区间。",
     "sample_in":"5\n1 2\n2 4\n5 6\n7 8\n7 9","sample_out":"3\n1 4\n5 6\n7 9","constraint":"−10⁹ ≤ l ≤ r ≤ 10⁹, n ≤ 100000",
     "sol":"区间合并：1)按左端点升序排序；2)初始化st,ed为第一个区间；3)遍历剩余：如果l≤ed则ed=max(ed,r)（合并）；否则输出[st,ed]并开始新区间。注意输入区间可能不完全排序——必须先排序。时间O(n log n)。",
     "tip":"贪心的核心：按左端点排序后，重叠区间一定连续出现。边界条件ed<l才断开（注意不含等于）。区间合并是贪心入门的经典题——理解'排序→贪心遍历'的模式后，更多的区间问题（区间选点、最大不相交区间数）也是类似思路。"},
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
body{font-family:"PingFang SC","Hiragino Sans GB","Noto Serif CJK SC","STSong",serif;font-size:9.5pt;line-height:1.7;color:#222;string-set:chapter"第11章 计算的边界——高精度、位运算与离散化"}
.preface{font-size:10pt;margin-bottom:1.5em;color:#444}.preface p{margin:.3em 0;text-indent:2em}
.preface h3{font-size:11pt;color:#2563eb;margin:1em 0 .3em 0}
.knowledge-box{background:#f0f6ff;border:1pt solid #bdd;border-radius:4px;padding:.7em 1em;margin:.8em 0;font-size:9pt}
.knowledge-box .k-title{font-weight:bold;color:#2563eb;margin-bottom:.3em;font-size:9.5pt}.knowledge-box p{margin:.2em 0}.knowledge-box ul{margin:.2em 0;padding-left:1.5em}
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
    parts.append('<div class="chapter-title">计算的边界</div>')
    parts.append('<div class="chapter-subtitle">高精度、位运算与离散化 · 7题 · C++ &amp; Python 双语对照</div>')
    parts.append('<div class="preface">')
    parts.append('<p>小鲁在上个月的语法训练中，抱怨过\"C++的int不够大\"。小华说：\"今天你终于遇到了C++的短板——高精度计算。但先别急——这也正是Python最闪耀的时刻：int无精度上限，四则运算零负担。\"本章的位运算部分教二进制思维——取最低位、计数、快速幂——底层优化与竞赛高频考点。离散化和区间合并则是空间压缩和贪心的经典案例。</p>')
    parts.append('<h3>本章角色</h3>')
    parts.append('<p>🧑‍🎓 <strong>小鲁</strong>（进阶者）· 第一次深刻感受Python的震撼——高精度四题C++手写100行，Python四行</p>')
    parts.append('<p>🧠 <strong>小华</strong>（算法队长）· 讲解lowbit(x&-x)的二进制原理和补码证明</p>')
    parts.append('</div>')
    parts.append('<div class="knowledge-box"><div class="k-title">🔢 Python震撼教育：高精度与位运算</div><ul>')
    parts.append('<li><strong>高精度加/减/乘/除：</strong>C++手写30-50行 → Python: int(input()) (+ - * //) 一行</li>')
    parts.append('<li><strong>lowbit：</strong>x & -x 取最低位的1。树状数组的核心操作</li>')
    parts.append('<li><strong>bit_count：</strong>Python int.bit_count() / C++ __builtin_popcount()</li>')
    parts.append('<li><strong>离散化：</strong>收集坐标→排序去重→二分映射→前缀和。处理稀疏大范围的标准手段</li>')
    parts.append('<li><strong>区间合并：</strong>按左端点排序→贪心遍历→合并重叠。O(n log n)</li></ul></div>')

    for p in PROBLEMS:
        pb=['<div class="problem-block">']
        pb.append(f'<div class="problem-title"><span class="nq">{p["nq"]}</span>{p["title"]}<span class="acw">AcWing {p["acw"]}</span></div>')
        pb.append(f'<div class="problem-desc">{p["story"]}</div>')
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
    parts.append('<li><strong>高精度四则运算：</strong>C++手写理解底层（进位/借位/试商），Python直接用——选对语言事半功倍</li>')
    parts.append('<li><strong>位运算核心：</strong>lowbit=x&-x, bit_count, 左移右移——底层优化的利器</li>')
    parts.append('<li><strong>离散化：</strong>稀疏空间→压缩→常规操作——大数据+稀疏坐标的标准处理流程</li>')
    parts.append('<li><strong>区间合并：</strong>排序+贪心遍历——O(n log n)解决最小区间覆盖问题</li>')
    parts.append('</ul></div>')
    parts.append('<div class="chapter-end">— 第11章完 · 共7题 · 自强不息 —</div>')

    html=f"""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"><title>第11章 计算的边界</title><style>{CSS}</style></head><body>{chr(10).join(parts)}</body></html>"""
    out=BOOK_ROOT/"textbook"/"chapter11_print.html"
    out.write_text(html,encoding='utf-8')
    print(f"✅ Ch11 dialog version: {len(html)} chars")

if __name__=="__main__":
    build_html()
