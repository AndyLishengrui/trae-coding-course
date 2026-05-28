#!/usr/bin/env python3
"""第9章 分治之美(角色对话版) — 排序与二分"""
import json, re, os, sys
from pathlib import Path
BOOK_ROOT = Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(BOOK_ROOT / 'scripts'))

PROBLEMS = [
    {"nq":"NQ106","acw":785,"title":"快速排序",
     "story":"\"排序——这是计算机科学里研究得最透彻的问题之一。\"小华郑重地说，\"给你n个乱序的整数，用快速排序把它们排好。快排的核心思想是'分治'——选一个基准数，把比它小的放左边，大的放右边，然后左右分别递归排序。这个模板你会写100遍——背下来，默出来，成为肌肉记忆。\"小鲁试了试：\"do-while循环和指针的配合确实巧妙，不小心就会无限循环……\"",
     "input":"第一行整数n，第二行n个整数。","output":"升序排列的n个整数，空格分隔。",
     "sample_in":"5\n3 1 2 4 5","sample_out":"1 2 3 4 5","constraint":"1 ≤ n ≤ 100000，所有整数在1~10⁹范围内",
     "sol":"快排模板：选基准x=arr[l+r>>1]，i=l-1,j=r+1双指针向中间移动，i找≥x的，j找≤x的，交换，直到i≥j，然后递归[l,j]和[j+1,r]。时间O(n log n)平均，最坏O(n²)。注意边界：用do-while避免死循环，用j而非i-1防止无限递归。",
     "tip":"快排背板要点：1)取中间值作基准避免最坏情况；2)i和j初始为l-1和r+1配合do-while；3)递归用j和j+1（不用i）。Python版sorted()内部用Timsort，实践中永远比手写快排好。但手写快排是理解分治思想的必修课。"},
    {"nq":"NQ107","acw":786,"title":"第k个数",
     "story":"\"如果是找第k小的数——而不是排序整个数组呢？\"小栋问。小华说：\"用快排的变种——快速选择算法。每次划分后，看第k个数落在左半边还是右半边，只递归那一边。平均O(n)时间找到第k小，比先排序O(n log n)再取第k个快。这就是'不需要的信息就不处理'的思维——算法优化的本质就是只做必要的工作。\"",
     "input":"第一行n和k，第二行n个整数。","output":"第k小的数。",
     "sample_in":"5 3\n2 4 1 5 3","sample_out":"3","constraint":"1 ≤ n ≤ 100000，1 ≤ k ≤ n",
     "sol":"快速选择：在快排划分基础上，设左半长度为sl=j-l+1。若k≤sl则在左半递归找第k小；否则在右半递归找第k-sl小。平均O(n)，最坏O(n²)（可通过随机选基准优化）。Python直接用nth_element或排序后取arr[k-1]。",
     "tip":"快速选择的核心是partition后的决策——只递归一边。这和二分查找的思想一样：每一步排除一半候选。最坏O(n²)可以用随机化基准数来规避——C++的nth_element就是这个算法。"},
    {"nq":"NQ108","acw":787,"title":"归并排序",
     "story":"\"除了快排，还有一种经典排序——归并排序。\"小华画出一个分叉图，\"先把数组不断对半分，分到只有一个元素（自然有序），然后从下往上两两合并有序子数组。归并排序的优点是稳定且时间复杂度始终O(n log n)，缺点是需要额外O(n)空间。快排vs归并——这是算法课永恒的话题。\"",
     "input":"第一行n，第二行n个整数。","output":"升序排列的n个整数。",
     "sample_in":"5\n3 1 2 4 5","sample_out":"1 2 3 4 5","constraint":"1 ≤ n ≤ 100000",
     "sol":"归并三步骤：1)递归划分mid=l+r>>1，merge_sort(l,mid)和merge_sort(mid+1,r)；2)双指针合并两个有序子数组到tmp；3)复制tmp回原数组。稳定排序，时间O(n log n)，空间O(n)。逆序对问题可以天然嵌入归并过程。",
     "tip":"归并是稳定排序——相等元素的相对位置不变。快排不稳定。Python用sorted()（稳定），C++用stable_sort（归并）和sort（快排）。理解归并对后续学习逆序对、CDQ分治至关重要。"},
    {"nq":"NQ109","acw":788,"title":"逆序对的数量",
     "story":"\"统计数组中逆序对的数量——即i<j但a[i]>a[j]的对数。\"小华说，\"暴力两重循环O(n²)太慢。巧妙的方法？在归并排序的合并过程中统计！当左半的a[i]大于右半的a[j]时，左半从i到mid的所有数都大于a[j]，逆序对增加mid-i+1个。排序+统计一气呵成。注意答案可能超过int范围——用long long！\"",
     "input":"第一行n，第二行n个整数。","output":"逆序对总数。",
     "sample_in":"6\n2 3 4 5 6 1","sample_out":"5","constraint":"1 ≤ n ≤ 100000，答案可能超int",
     "sol":"归并排序嵌入计数：当a[i]>a[j]时，cnt+=mid-i+1（左半剩余元素全部形成逆序对）。归并过程中自然完成了逆序对统计。时间复杂度O(n log n)，比暴力O(n²)快4个数量级（n=10⁵时）。逆序对数量是衡量数组\"混乱程度\"的指标。",
     "tip":"C++必须用long long存储cnt——n=10⁵时逆序对最多约5×10⁹超过int。Python自带大整数。这道题是归并排序最重要的应用之一——理解'在归并过程中顺便统计'是分治算法的精髓。"},
    {"nq":"NQ110","acw":789,"title":"数的范围",
     "story":"\"在一个升序数组里，某个数出现了多次——请找出它第一次和最后一次出现的位置。\"小栋出题。小鲁说：\"遍历一遍就行！\"小华摇头：\"数组有10⁵个元素，查询10⁴次——O(n×q)要10⁹次操作，超时。需要用二分——O(log n)每次查询。二分的精髓：用mid+1或mid不停缩小范围，直到找到边界。整数二分的边界处理是90%的人都会写错的地方。\"",
     "input":"第一行n和q，第二行n个升序整数，然后q行每行一个查询k。","output":"每个查询输出k的起始和终止位置，不存在输出-1 -1。",
     "sample_in":"6 3\n1 2 2 3 3 4\n3\n2\n5","sample_out":"3 4\n1 2\n-1 -1","constraint":"1 ≤ n ≤ 100000，1 ≤ q ≤ 10000",
     "sol":"二分查找左右边界：左边界→while(l<r):mid=l+r>>1; if(a[mid]>=k) r=mid else l=mid+1。右边界→while(l<r):mid=l+r+1>>1; if(a[mid]<=k) l=mid else r=mid-1。注意右边界二分的mid要+1避免死循环。Python可用bisect_left和bisect_right。",
     "tip":"整数二分最关键的差异：左边界mid=l+r>>1，右边界mid=l+r+1>>1（不+1会死循环）。记住：l=mid时mid要+1，r=mid时不用。二分是OI/ACM中最基础也是最容易写错的算法——花时间理解透彻值得。"},
    {"nq":"NQ111","acw":790,"title":"数的三次方根",
     "story":"\"整数二分搞定了，那实数二分呢？\"小鲁问。\"比如计算n的三次方根，精确到10⁻⁶。\"小华说，\"实数二分比整数二分简单——不需要处理+1/-1的边界。设定精度阈值（如1e-8），while(r-l>1e-8)不断对半分。浮点二分的优势：不需要纠结mid的取值，收敛极快——log₂(10⁸)≈27步即可到目标精度。\"",
     "input":"一个浮点数n。","output":"n的三次方根，保留6位小数。",
     "sample_in":"1000.00","sample_out":"10.000000","constraint":"−10000 ≤ n ≤ 10000",
     "sol":"实数二分：设l=-10000,r=10000（范围包含答案），while(r-l>1e-8): mid=(l+r)/2; if(mid³≥n) r=mid else l=mid。输出r保留6位小数（printf(\"%.6lf\",r)）。收敛步数=log₂(范围/精度)≈log₂(20000/1e-8)≈41步——非常快。",
     "tip":"实数二分不需要处理整数二分的mid+1问题。直接mid=(l+r)/2即可。精度通常比要求多两位（要求1e-6则迭代到1e-8）。C++用double，Python用float。注意n为负数时三次方根也为负。"},
    {"nq":"NQ112","acw":727,"title":"菱形",
     "story":"\"最后来一道'画图题'放松一下——打印一个菱形！\"小华说，\"看起来简单，但其实考察的是曼哈顿距离的几何直觉。菱形中心到四边的曼哈顿距离是n/2，每个位置如果到中心距离≤n/2就填*否则填空格。这道题把几何和格式化输出结合起来——是算法竞赛中'观察规律→数学建模→代码实现'的完美微型案例。\"",
     "input":"一个奇数n。","output":"n行菱形图案，中心行有n个*。",
     "sample_in":"5","sample_out":"  *\n ***\n*****\n ***\n  *","constraint":"1 ≤ n ≤ 100，n为奇数",
     "sol":"曼哈顿距离模型：设中心cx=cy=n/2。对于每个位置(i,j)，如果abs(i-cx)+abs(j-cy)≤n/2则填*否则空格。这种'距离阈值'的判断方式在心形、沙漏等图案题中都通用。时间复杂度O(n²)。",
     "tip":"曼哈顿距离=|x1-x2|+|y1-y2|。菱形就是曼哈顿距离≤阈值的点集。换欧几里得距离就是圆形。理解这种几何距离与图形形状的关系，是计算机图形学的基础。"},
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
body{font-family:"PingFang SC","Hiragino Sans GB","Noto Serif CJK SC","STSong",serif;font-size:9.5pt;line-height:1.7;color:#222;string-set:chapter"第9章 分治之美——排序与二分"}
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
    parts.append('<div class="chapter-title">分治之美</div>')
    parts.append('<div class="chapter-subtitle">排序与二分 · 7题 · C++ &amp; Python 双语对照</div>')
    parts.append('<div class="preface">')
    parts.append('<p>从本章开始，小鲁正式进入<strong>算法</strong>的世界。前面的语法和数据结构是工具，算法才是让程序\"聪明\"起来的灵魂。\"排序——把混乱变成有序——是计算机科学中最基础也最深刻的主题。快排、归并、二分……这些经典算法经过几十年的打磨，至今仍是每个程序员的基本功。\"小华严肃地说。</p>')
    parts.append('<p>本章7道题分三个板块：<strong>排序模板</strong>（快排+归并）——理解分治思想并将模板变成肌肉记忆；<strong>排序应用</strong>（快速选择+逆序对）——在排序过程中顺便解决更复杂的问题；<strong>二分查找</strong>（整数+实数）——利用有序性将搜索从O(n)降到O(log n)，这是算法优化的第一思维。</p>')
    parts.append('<h3>本章角色</h3>')
    parts.append('<p>🧑‍🎓 <strong>小鲁</strong>（进阶者）· 从语法期毕业，进入算法训练营——分治、排序、二分</p>')
    parts.append('<p>🧠 <strong>小华</strong>（算法队长）· \"快排模板写100遍——背下来、默出来、成为肌肉记忆\"</p>')
    parts.append('<p>🏗️ <strong>小栋</strong>（工程师）· \"为什么不能直接调用sort()?\"——理解算法原理和工程实践的关系</p>')
    parts.append('</div>')
    parts.append('<div class="knowledge-box"><div class="k-title">⚡ 排序与二分核心模板</div><ul>')
    parts.append('<li><strong>快排模板：</strong>取中值基准→do-while双指针→交换→递归[l,j]和[j+1,r]</li>')
    parts.append('<li><strong>归并模板：</strong>二分递归→双指针合并→复制回原数组。稳定O(n log n)</li>')
    parts.append('<li><strong>整数二分：</strong>左边界mid=l+r>>1, r=mid。右边界mid=l+r+1>>1, l=mid</li>')
    parts.append('<li><strong>实数二分：</strong>while(r-l>eps) mid=(l+r)/2。比整数二分简单——不需处理+1/-1</li>')
    parts.append('<li><strong>Python：</strong>sort()/sorted()快速排序，bisect_left/right二分。标准库是工程首选</li></ul></div>')

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
    parts.append('<li><strong>快排模板：</strong>O(n log n)平均。do-while+双指针+分治递归。非稳定排序</li>')
    parts.append('<li><strong>归并模板：</strong>O(n log n)保证。稳定排序。额外O(n)空间。可在合并过程统计逆序对</li>')
    parts.append('<li><strong>快速选择：</strong>基于快排划分，O(n)平均找第k小。只递归一边——\"不需要的信息就不处理\"</li>')
    parts.append('<li><strong>整数二分：</strong>左边界和右边界模板不同——注意mid是否需要+1避免死循环</li>')
    parts.append('<li><strong>实数二分：</strong>无需处理+1/-1边界。迭代到目标精度+2位即可</li>')
    parts.append('<li><strong>厦大精神：</strong>自强不息。把这些模板练成肌肉记忆——它们是你算法之路的基石</li>')
    parts.append('</ul></div>')
    parts.append('<div class="chapter-end">— 第9章完 · 共7题 · 自强不息 —</div>')

    html=f"""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"><title>第9章 分治之美</title><style>{CSS}</style></head><body>{chr(10).join(parts)}</body></html>"""
    out=BOOK_ROOT/"textbook"/"chapter09_print.html"
    out.write_text(html,encoding='utf-8')
    print(f"✅ Ch9 dialog version: {len(html)} chars")

if __name__=="__main__":
    build_html()
