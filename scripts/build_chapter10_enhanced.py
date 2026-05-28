#!/usr/bin/env python3
"""第10章 预处理的智慧(角色对话版) — 前缀和、差分与双指针"""
import json, re, os, sys
from pathlib import Path
BOOK_ROOT = Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(BOOK_ROOT / 'scripts'))

PROBLEMS = [
    {"nq":"NQ113","acw":795,"title":"前缀和",
     "story":"小栋拿着一个巨大的数组找到小鲁：\"我要查询100000次——每次求第l到第r个元素的和。直接每次循环累加的话要100000×50000=50亿次操作，O(n×q)太慢了！\"小华接过键盘：\"前缀和——预处理一个前缀数组s[i]=前i个元素的和，查[l,r]的和只需s[r]-s[l-1]，O(1)时间。用O(n)的预处理换O(1)的查询——这就是'预处理思维'的第一课。\"",
     "input":"第一行n和m，第二行n个整数，然后m行每行l r。","output":"每行输出a[l..r]的和。",
     "sample_in":"5 3\n2 1 3 6 4\n1 2\n1 3\n2 4","sample_out":"3\n6\n10","constraint":"1 ≤ n,m ≤ 100000",
     "sol":"预处理前缀数组：s[i]=s[i-1]+a[i]（1-indexed）。查询[l,r]=s[r]-s[l-1]，O(1)。Python用accumulate。C++注意使用1-indexed数组简化边界处理。前缀和的核心思想：把重复计算变成一次计算+多次查表。",
     "tip":"用1-indexed数组避免l-1越界——s[0]=0。Python: s=list(accumulate([0]+arr))。前缀和可以扩展到异或和、乘积和、最大值/最小值（需要线段树）。理解预处理思维是算法优化的核心。"},
    {"nq":"NQ114","acw":796,"title":"子矩阵的和",
     "story":"\"前缀和能不能推广到二维？\"小鲁问。\"当然！\"小华在白板上画出矩阵，\"二维前缀和：s[i][j]=s[i-1][j]+s[i][j-1]-s[i-1][j-1]+a[i][j]——包含关系的加减。查询子矩阵(x1,y1)到(x2,y2)的和= s[x2][y2]-s[x1-1][y2]-s[x2][y1-1]+s[x1-1][y1-1]。看这个'容斥'模式——包含-排除+补回。\"",
     "input":"第一行n,m,q。然后n×m矩阵。然后q行每行x1 y1 x2 y2。","output":"每行子矩阵元素和。",
     "sample_in":"3 4 3\n1 7 2 4\n3 6 2 8\n2 1 2 3\n1 1 2 2\n2 1 3 4\n1 3 3 4","sample_out":"17\n27\n21","constraint":"1 ≤ n,m ≤ 1000, 1 ≤ q ≤ 200000",
     "sol":"二维前缀和：预处理s[i][j]包含从(1,1)到(i,j)的矩形和。公式如上述。查询子矩阵和=大矩形减两翼加回重叠部（容斥原理）。O(nm)预处理→O(1)每次查询。Python同样用accumulate思想。",
     "tip":"注意预处理和查询的加减符号——s[i][j]=s[i-1][j]+s[i][j-1]-s[i-1][j-1]+a[i][j]（包含关系）。查询时=大矩形-上矩形-左矩形+左上矩形（容斥）。1-indexed简化边界。理解这个模式后三维前缀和也是同样的加减法。"},
    {"nq":"NQ115","acw":797,"title":"差分",
     "story":"\"前缀和是前缀→查询。那它的逆运算是什么？\"小华问。\"如果我需要对数组的[l,r]区间每个元素都加c，怎么最快？\"小鲁想了想：\"差分！构造b数组使a是b的前缀和。对[l,r]加c只需b[l]+=c, b[r+1]-=c——两次操作！对整个区间每个元素加同一个值——这是差分最经典的用法。O(1)修改，O(n)还原。\"",
     "input":"第一行n,m。第二行n个整数。然后m行每行l r c。","output":"所有操作后的数组。",
     "sample_in":"6 3\n1 2 2 1 2 1\n1 3 1\n3 5 1\n1 6 1","sample_out":"3 4 5 3 4 2","constraint":"1 ≤ n,m ≤ 100000",
     "sol":"差分数组b：b[i]=a[i]-a[i-1]（用a[i]的差分量），则a[i]=b[1]+...+b[i]。区间[l,r]加c：b[l]+=c, b[r+1]-=c。最后做前缀和还原。这是'区间修改→点查询'的最优方案——O(1)修改O(n)还原。",
     "tip":"差分=前缀和的逆运算。核心操作：b[l]+=c, b[r+1]-=c。Python实现可直接用数组操作。理解差分的妙处：两次修改影响整个区间。竞赛中差分和前缀和是黄金搭档——90%的区间问题都可以用这俩之一解决。"},
    {"nq":"NQ116","acw":798,"title":"差分矩阵",
     "story":"\"一维差分搞定了——二维呢？\"小栋继续追问。小华画出矩阵：\"二维差分——对子矩阵(x1,y1)到(x2,y2)加c只需四步：b[x1][y1]+=c, b[x2+1][y1]-=c, b[x1][y2+1]-=c, b[x2+1][y2+1]+=c。注意四个角——加主对角减副对角。最后做二维前缀和还原。两次操作，影响整个子矩阵——这就是数学建模的优雅。\"",
     "input":"第一行n,m,q。然后n×m矩阵。然后q行每行x1 y1 x2 y2 c。","output":"所有操作后的矩阵。",
     "sample_in":"3 4 3\n1 2 2 1\n3 2 2 1\n1 1 1 1\n1 1 2 2 1\n1 3 2 3 2\n3 1 3 4 1","sample_out":"2 3 4 1\n4 3 4 1\n2 2 2 2","constraint":"1 ≤ n,m ≤ 1000, 1 ≤ q ≤ 100000",
     "sol":"二维差分：b[i][j]使a[i][j]=b[1..i][1..j]的和。子矩阵加c的四步操作如上述——两个正角（x1,y1和x2+1,y2+1）两个负角（x2+1,y1和x1,y2+1）。最后二维前缀和还原。O(1)修改→O(nm)还原。",
     "tip":"记忆四角公式：正正负负。左上角(x1,y1)+c，右上角(x1,y2+1)-c，左下角(x2+1,y1)-c，右下角(x2+1,y2+1)+c。二维差分比一维多了一对操作。这是图像处理中滤镜效果的基础——用极少操作影响大区域。"},
    {"nq":"NQ117","acw":799,"title":"最长连续不重复子序列",
     "story":"\"给一个数组，找最长的一段，里面的数都不重复。\"小华说，\"暴力三重循环O(n³)太慢。优化——用双指针！维护窗口[l,r]，用计数数组记录窗口内每个数出现多少次。当a[r]重复时，不断l++直到消除重复。双指针的复杂度是O(2n)=O(n)——每个元素最多进窗口一次，出窗口一次。\"",
     "input":"第一行n，第二行n个整数。","output":"最长连续不重复子序列的长度。",
     "sample_in":"5\n1 2 2 3 5","sample_out":"3","constraint":"1 ≤ n ≤ 100000",
     "sol":"双指针滑动窗口：维护[l,r]区间无重复。遍历r，每次cnt[a[r]]++。若cnt[a[r]]>1说明有重复，while(cnt[a[r]]>1) cnt[a[l]]--, l++。答案=max(ans, r-l+1)。时间复杂度O(n)——每个元素最多入窗一次离开一次。",
     "tip":"双指针核心：两指针都只向前移动，从不后退——保证O(n)。重复检测用计数数组作哈希（值域小时）。Python用字典记录上次出现位置可优化到只移一次。双指针是处理'连续子数组'类问题的常用武器。"},
    {"nq":"NQ118","acw":800,"title":"数组元素的目标和",
     "story":"\"两个升序数组A和B，找一对a[i]+b[j]=x。\"\"如果暴力双循环O(n×m)太慢——但既然两个数组都是升序的……\"小鲁已经有了思路，\"用双指针！i从A的开头开始向右走，j从B的末尾开始向左走。a[i]+b[j]比x大就j--，比x小就i++。对撞双指针——各自走一遍，O(n+m)。\"",
     "input":"第一行n,m,x。第二行n个升序整数(A)。第三行m个升序整数(B)。","output":"i和j（0-indexed）。",
     "sample_in":"4 5 6\n1 2 4 7\n3 4 6 8 9","sample_out":"1 1","constraint":"1 ≤ n,m ≤ 100000。保证有唯一解。",
     "sol":"对撞双指针：i=0从左，j=m-1从右。当a[i]+b[j]>x则j--（太大，缩右边的），当a[i]+b[j]<x则i++（太小，扩左边的）。相等时输出。O(n+m)因为i只增不减，j只减不增。利用了有序性的经典双指针模式。",
     "tip":"双指针三种模式：滑动窗口（同向）、对撞指针（反向）、快慢指针。本题是对撞指针——从两端向中间逼近。抓住while循环的两个关键：条件(a[i]+b[j] vs x)和移动方向(谁移动)。"},
    {"nq":"NQ119","acw":2816,"title":"判断子序列",
     "story":"\"最后一个双指针问题：判断a是不是b的子序列——即a的元素按相同顺序出现在b中（不一定连续）。\"小华说，\"双指针i指a、j指b。遍历b的每个元素，如果b[j]==a[i]就i++。最后如果i==n说明a的所有元素都按顺序找到了。这个'匹配式'双指针——j不停走，i只在匹配时走——O(n+m)。\"",
     "input":"第一行n,m。第二行n个整数(a)。第三行m个整数(b)。","output":"是子序列输出Yes，否则No。",
     "sample_in":"3 5\n1 3 5\n1 2 3 4 5","sample_out":"Yes","constraint":"1 ≤ n ≤ m ≤ 100000",
     "sol":"匹配双指针：i=0指a，j=0指b。遍历j，if b[j]==a[i]: i++。最后i==n则匹配完成。j一直移动，i只在匹配成功时前移。O(n+m)时间O(1)空间。此模式适用于有序序列的判断和验证问题。",
     "tip":"判断子序列是双指针的经典入門题——理解'只有匹配时才移动i'的节奏。这个模式也是KMP算法的前身——都是字符串/序列匹配，但双指针版更简单直白。竞赛中大量'验证是否满足某约束'的题都在用这个思路。"},
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
body{font-family:"PingFang SC","Hiragino Sans GB","Noto Serif CJK SC","STSong",serif;font-size:9.5pt;line-height:1.7;color:#222;string-set:chapter"第10章 预处理的智慧——前缀和、差分与双指针"}
.chapter-title{text-align:center;font-size:20pt;font-weight:bold;margin:1.5em 0 .1em 0;letter-spacing:3pt}
.chapter-subtitle{text-align:center;font-size:10pt;color:#777;margin-bottom:1.5em;padding-bottom:.8em;border-bottom:1px solid #bbb}
.preface{font-size:10pt;margin-bottom:1.5em;color:#444}.preface p{margin:.3em 0;text-indent:2em}
.preface h3{font-size:11pt;color:#2563eb;margin:1em 0 .3em 0}
.knowledge-box{background:#f0f6ff;border:1pt solid #bdd;border-radius:4px;padding:.7em 1em;margin:.8em 0;font-size:9pt}
.knowledge-box .k-title{font-weight:bold;color:#2563eb;margin-bottom:.3em;font-size:9.5pt}.knowledge-box p{margin:.2em 0}.knowledge-box ul{margin:.2em 0;padding-left:1.5em}
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
    parts.append('<div class="chapter-title">预处理的智慧</div>')
    parts.append('<div class="chapter-subtitle">前缀和、差分与双指针 · 7题 · C++ &amp; Python 双语对照</div>')
    parts.append('<div class="preface">')
    parts.append('<p>小鲁上节课学会了排序——把混乱变有序。这节课要学的是：<strong>有了有序性或预处理之后，如何以光速回答问题</strong>。小华说：\"排序之后数组有序了，二分查找O(log n)；但如果你经常要查区间和呢？每次都要O(n)累加还是太慢——所以有了前缀和，O(1)回答。有了前缀和就有差分——修改一个区间只需两次操作。有了滑动窗口就有双指针——两个指针各走一遍解决O(n²)的问题。这些技巧的核心思想都是：<strong>预处理</strong>和<strong>挖掘有序结构</strong>。\"</p>')
    parts.append('<h3>本章角色</h3>')
    parts.append('<p>🧑‍🎓 <strong>小鲁</strong>（进阶者）· 学习用预处理换取查询速度——\"计算一次，查询千次\"</p>')
    parts.append('<p>🧠 <strong>小华</strong>（算法队长）· 画图解释二维前缀和的容斥原理、差分矩阵的四角操作</p>')
    parts.append('<p>🏗️ <strong>小栋</strong>（工程师）· 带真实场景来问：大数据量的区间查询和快速修改</p>')
    parts.append('</div>')
    parts.append('<div class="knowledge-box"><div class="k-title">🔢 前缀和·差分·双指针 核心模板</div><ul>')
    parts.append('<li><strong>一维前缀和：</strong>s[i]=s[i-1]+a[i], 查询[l,r]=s[r]-s[l-1]</li>')
    parts.append('<li><strong>二维前缀和：</strong>s[i][j]=s[i-1][j]+s[i][j-1]-s[i-1][j-1]+a[i][j]（容斥模式）</li>')
    parts.append('<li><strong>一维差分：</strong>b[l]+=c, b[r+1]-=c（区间修改O(1)）</li>')
    parts.append('<li><strong>二维差分：</strong>正角(x1,y1)+c, (x2+1,y2+1)+c；负角(x1,y2+1)-c, (x2+1,y1)-c</li>')
    parts.append('<li><strong>滑动窗口：</strong>维护[l,r]区间，while条件移动l，答案不断更新</li>')
    parts.append('<li><strong>对撞指针：</strong>i从左向右，j从右向左，根据条件判断移动哪个</li></ul></div>')

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
    parts.append('<li><strong>前缀和（1D/2D）：</strong>O(n)预处理→O(1)查询。"重复查询→预处理"思维的典型应用</li>')
    parts.append('<li><strong>差分（1D/2D）：</strong>O(1)区间修改→O(n)还原。"修改操作远多于查询"场景的最优方案</li>')
    parts.append('<li><strong>双指针三模式：</strong>滑动窗口、对撞指针、匹配指针——核心是不回溯，O(n)解决O(n²)问题</li>')
    parts.append('<li><strong>厦大精神：</strong>自强不息。这些预处理技巧，在真实工程中（大数据、图像处理）同样大放异彩</li>')
    parts.append('</ul></div>')
    parts.append('<div class="chapter-end">— 第10章完 · 共7题 · 自强不息 —</div>')

    html=f"""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"><title>第10章 预处理的智慧</title><style>{CSS}</style></head><body>{chr(10).join(parts)}</body></html>"""
    out=BOOK_ROOT/"textbook"/"chapter10_print.html"
    out.write_text(html,encoding='utf-8')
    print(f"✅ Ch10 dialog version: {len(html)} chars")

if __name__=="__main__":
    build_html()
