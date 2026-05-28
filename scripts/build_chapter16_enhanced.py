#!/usr/bin/env python3
"""第16章 终极试炼(角色对话版) — 数学、贪心与综合实战"""
import json, re, os, sys
from pathlib import Path
BOOK_ROOT = Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(BOOK_ROOT / 'scripts'))

PROBLEMS = [
    {"nq":"NQ159","acw":905,"title":"区间选点",
     "story":"\"在数轴上有N个区间，选出最少的点，使每个区间至少包含一个点。\"小华说，\"贪心经典题——按右端点排序，每次选当前未覆盖区间中最小的右端点作为新点。因为右端点排序后，选右端点覆盖最多后续区间。贪心的核心：'每次做当前看起来最好的选择'——但关键是证明贪心策略的正确性。排序+遍历=O(n log n)。\"",
     "input":"第一行N。然后N行每行l r表示区间。","output":"最少点数。",
     "sample_in":"3\n-1 1\n2 4\n3 5","sample_out":"2","constraint":"1 ≤ N ≤ 10⁵, −10⁹ ≤ l ≤ r ≤ 10⁹",
     "sol":"贪心策略：按右端点升序排序。ans=0, last=-INF。遍历每个区间[l,r]：若l>last则需新点ans++, last=r。证明：按右端点排序后，每次选最小的右端点保证了对后续区间的最大覆盖能力。",
     "tip":"贪心的正确性证明通常用'交换论证'或'归纳法'。区间问题的通用解法：先排序再贪心——排序确定处理的顺序，贪心确定每一步的选择。Python: intervals.sort(key=lambda x: x[1])按右端点排序。"},
    {"nq":"NQ160","acw":148,"title":"合并果子",
     "story":"\"N堆果子，每次合并任意两堆，代价为两堆之和。求合并成一堆的最小总代价。\"这就是Huffman编码！\"每次选最小的两堆合并——用小根堆维护。贪心+Huffman=O(n log n)。\"小华说，\"Huffman树的每个内部节点对应一次合并，叶子是原始堆。最优性证明：最小的两堆一定在Huffman树的最深层——交换论证。\"",
     "input":"第一行n。第二行n个整数。","output":"最小总代价。",
     "sample_in":"3\n1 2 9","sample_out":"15","constraint":"1 ≤ n ≤ 10000",
     "sol":"小根堆(优先队列)：每次pop两个最小值，合并(=和)，将和push回堆，ans+=和。重复直到堆中只剩一个元素。时间O(n log n)。Python用heapq: heapify(arr); while len>1: a,b=heappop,heappop; heappush(a+b); ans+=a+b。",
     "tip":"Huffman编码=最优二叉树构造。堆的选择：小根堆取最小值最快(O(log n))。这是优先队列最重要、最经典的应用——Dijkstra、Prim都用到了堆。Python的heapq模块简单高效——记住heappush+heappop组合。"},
    {"nq":"NQ161","acw":836,"title":"合并集合",
     "story":"\"并查集(Disjoint Set Union)——处理集合的合并和查询。\"小华画出带箭头的图，\"每个集合用一个树表示，根节点是集合代表。find(x)：找x的根。union(x,y)：将x根连到y根。两种优化：路径压缩(find时把所有路径节点直接连根)和按秩合并(小树连到大树)。均摊复杂度近乎O(1)——这是数据结构设计中最精妙的成就之一。\"",
     "input":"第一行n,m。然后m行：M a b(合并)或Q a b(查询是否同集)。","output":"对Q操作输出Yes/No。",
     "sample_in":"4 5\nM 1 2\nM 3 4\nQ 1 2\nQ 1 3\nQ 3 4","sample_out":"Yes\nNo\nYes","constraint":"1 ≤ n,m ≤ 10⁵",
     "sol":"并查集：p[x]存父节点(初始p[x]=x)。find(x): if p[x]!=x: p[x]=find(p[x]); return p[x]——路径压缩。union(x,y): p[find(x)]=find(y)。所有操作均摊O(α(n))≈O(1)。这是数据结构课程上最简洁又最高效的设计之一。",
     "tip":"并查集是竞赛中使用频率最高的数据结构。路径压缩(find中的p[x]=find(p[x]))是将树扁平化的关键。按秩合并：若两个集合秩相同则根秩+1。Python递归find可能超深度——用while迭代或sys.setrecursionlimit。并查集在Kruskal、连通性、动态图问题中是核心工具。"},
    {"nq":"NQ162","acw":837,"title":"连通块数量",
     "story":"\"上一题的扩展——除了查询连通性，还要知道每个连通块的大小。\"小华说，\"在并查集中额外维护一个size数组——初始size[i]=1。合并时size[新根]+=size[被合并的根]。查询某个节点所在连通块大小只需size[find(x)]。如果在合并时重复合并同一集合，size不变——避免重复累加。这是并查集的自然扩展。\"",
     "input":"第一行n,m。然后m行：C a b(合并,若已连通忽略) / Q1 a b(查询连通) / Q2 a(查询a所在连通块大小)。","output":"按要求输出。",
     "sample_in":"5 5\nC 1 2\nQ1 1 2\nQ2 1\nC 2 3\nQ2 1","sample_out":"Yes\n2\n3","constraint":"1 ≤ n,m ≤ 10⁵",
     "sol":"维护size的并查集：初始化size[i]=1。union时：if a_root!=b_root: p[a_root]=b_root; size[b_root]+=size[a_root]。注意必须先判连通再合并——避免重复size。find不变。",
     "tip":"并查集可以维护更多信息：size、距离到根(带权并查集)、最小值/最大值等。关键是理解'合并时如何更新附加信息'。食物链(240)是带权并查集的经典应用——每个节点维护与父节点的关系。"},
    {"nq":"NQ163","acw":240,"title":"食物链",
     "story":"\"动物王国三种关系：A吃B、B吃C、C吃A——循环克制。\"这是带权并查集的巅峰应用！\"每个节点维护到根的距离d[x]：d[x]%3=0与根同类，=1吃根，=2被根吃。合并集合时根据两个节点的关系计算出它们根之间的距离关系。路径压缩时同步更新d[x]。这是竞赛中最精彩的并查集应用！\"",
     "input":"第一行N,K。然后K行：D X Y（D=1同类,2表示X吃Y）。","output":"假话数量。",
     "sample_in":"100 7\n1 101 1\n2 1 2\n2 2 3\n2 3 3\n1 1 3\n2 3 1\n1 5 5","sample_out":"3","constraint":"1 ≤ N ≤ 50000, 0 ≤ K ≤ 100000",
     "sol":"带权并查集：p[x]存父，d[x]存与父的关系(0同类/1吃父/2被父吃)。find时路径压缩：root=find(p[x]); d[x]+=d[p[x]]; p[x]=root。合并X和Y：根据D=1/2计算X根和Y根的距离关系。判断假话：X/Y超范围、已连通但与关系不符。",
     "tip":"食物链是并查集+模3运算的智力巅峰。d[x]%3是与根的关系：0同类、1吃根、2被根吃。路径压缩时d[x]+=d[p[x]]保证距离累加正确。理解这道题后，所有带权并查集问题都不在话下。这是OI/ACM金牌选手的基本功。"},
    {"nq":"NQ164","acw":875,"title":"快速幂",
     "story":"\"计算a^b mod p ——b可能大到10⁹。\"小华在黑板上写下算法，\"朴素循环O(b)超时。快速幂：利用a^b=a^(b/2)×a^(b/2) ——分治+二进制分解。while(b): if(b&1) res=res*a%p; a=a*a%p; b>>=1。核心：将指数按二进制位拆开计算——时间O(log b)。这个模板出现在RSA加密、矩阵快速幂、模逆元等场景中。\"",
     "input":"第一行n。然后n行每行a b p。","output":"每行a^b mod p。",
     "sample_in":"2\n2 3 5\n3 2 7","sample_out":"3\n2","constraint":"1 ≤ n ≤ 10⁵, 1 ≤ a,b,p ≤ 2×10⁹",
     "sol":"快速幂while循环：a^b mod p。while b>0: if b&1: res=res*a%p; a=a*a%p; b>>=1。每步b减半→O(log b)。Python: pow(a,b,p)一行内置(支持三参数取模)——底层用快速幂实现。但手写理解原理是必须的。",
     "tip":"Python pow(a,b,p)三步参数：a^b mod p——内置最高效。快速幂是数论算法的基础——之后模逆元、快速幂+矩阵乘法(矩阵快速幂)、米勒-拉宾素性检测都依赖于此。位运算b&1判断奇偶比b%2更快。"},
    {"nq":"NQ165","acw":868,"title":"筛质数",
     "story":"\"找出1到n中的所有质数。\"小华说，\"埃氏筛法(Eratosthenes)：从2开始，依次划掉2的倍数、3的倍数……未被划掉的就是质数。优化：每个数只被它最小的质因子划掉——这就是线性筛。线性筛保证每个合数只被标记一次，O(n)。理解线性筛是理解数论算法的关键——最小质因子是数论中最核心的概念之一。\"",
     "input":"一个整数n。","output":"1到n中质数的个数。",
     "sample_in":"8","sample_out":"4","constraint":"1 ≤ n ≤ 10⁶",
     "sol":"埃氏筛：bool数组标记合数，for i from 2: if !st[i]: primes.push(i); for j=i*i到n步长i: st[j]=true。O(n log log n)。线性筛：每个数只被最小质因子筛——for p in primes: if i*p>n break; st[i*p]=true; if i%p==0 break。O(n)。",
     "tip":"筛法不仅是求质数——还可以同时记录最小质因子、欧拉函数、约数个数等。线性筛复杂度O(n)所以可以处理n=10⁷。Python的筛法比C++慢几倍但n=10⁶仍可。关键优化：只用≤√n的质数来筛。"},
    {"nq":"NQ166","acw":104,"title":"货仓选址",
     "story":"\"最后一个问题——在数轴上选一个位置建仓库，使到N个商店的总距离最小。\"小华笑道，\"答案是中位数！将商店坐标排序，最优位置=中位数位置。证明：如果把仓库往任意方向移dx，离一半商店近了dx但离另一半远了dx——中位数处达到平衡。这展示了数学思维在算法优化中的力量——有时候最优解不需要代码搜索，数学定理直接给出答案。\"",
     "input":"第一行N。第二行N个整数。","output":"最小总距离。",
     "sample_in":"4\n6 2 9 1","sample_out":"12","constraint":"1 ≤ N ≤ 100000",
     "sol":"排序取中位数：sort(arr); median=arr[n//2]; ans=sum(abs(a-median))。O(n log n)。进阶：如果N是偶数，任何在中间两个数之间的位置都是最优的。中位数距离和是最小绝对偏差问题的标准答案——不需要搜索，理解定理就完成了。",
     "tip":"中位数vs平均数：最小化绝对偏差和用中位数，最小化平方偏差和用平均数。这是统计学的基础结论。Python一行：median=sorted(arr)[n//2]; print(sum(abs(x-median) for x in arr))。16章到此结束——从A+B到货仓选址，你已经完成了算法竞赛入门的所有基础训练。",
     "tip2":"这16章的征程，小鲁从第一个Hello World起航，穿越了语法、算法、数据结构——最终抵达了数学和贪心的彼岸。下一站就是真正的算法竞赛实战。自强不息，止于至善——编程之路永无止境。"},
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
body{font-family:"PingFang SC","Hiragino Sans GB","Noto Serif CJK SC","STSong",serif;font-size:9.5pt;line-height:1.7;color:#222;string-set:chapter"第16章 终极试炼——数学、贪心与综合实战"}
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
    parts.append('<div class="chapter-title">终极试炼</div>')
    parts.append('<div class="chapter-subtitle">数学、贪心与综合实战 · 8题 · C++ &amp; Python 双语对照</div>')
    parts.append('<div class="preface">')
    parts.append('<p>最后一章！小鲁回顾了这一路的风景——从第一个A+B，到循环、数组、字符串、函数、STL、排序、二分、前缀和、差分、双指针、高精度、位运算、离散化、数据结构、搜索、图论、动态规划……16章的征程即将画上句号。最后一章，我们用数学和贪心来收尾——有时候最优解不需要复杂算法，一个定理就够了。\"编程的最高境界——不是写最多的代码，而是用最少的代码解决最难的问题。\"</p>')
    parts.append('</div>')
    parts.append('<div class="knowledge-box"><div class="k-title">🏆 终极速查</div><ul>')
    parts.append('<li><strong>贪心：</strong>区间选点(排序右端点)、合并果子(Huffman+堆)——每次局部最优</li>')
    parts.append('<li><strong>并查集：</strong>路径压缩+按秩合并——近乎O(1)的集合操作</li>')
    parts.append('<li><strong>带权并查集：</strong>食物链——维护到根的距离，模运算分类关系</li>')
    parts.append('<li><strong>数论：</strong>快速幂O(log b)、筛质数(线性筛O(n))、中位数选址——数学直接给答案</li></ul></div>')

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
        if "tip2" in p:
            pb.append(f'<div class="insight-block"><span class="insight-label">技巧</span><span>{p["tip"]}</span></div>')
        else:
            pb.append(f'<div class="insight-block"><span class="insight-label">技巧</span><span>{p["tip"]}</span></div>')
        cpp=CODE_CACHE.get(p['acw'],f'// AcWing {p["acw"]}')
        py=PY_CACHE.get(p['acw'],'# Python solution')
        pb.append('<div class="code-dual">')
        pb.append(f'<div class="code-col"><div class="lang-badge">C++</div><pre>{hl(cpp,CppLexer(),CPP_FMT)}</pre></div>')
        pb.append(f'<div class="code-col"><div class="lang-badge">Python</div><pre>{hl(py,PythonLexer(),PY_FMT)}</pre></div>')
        pb.append('</div></div><hr class="section-divider">')
        parts.append('\n'.join(pb))

    parts.append('<div class="chapter-summary"><h3>📋 全书总结</h3><ul>')
    parts.append('<li><strong>16章·161题·C++/Python双语：</strong>从A+B到货仓选址——完整覆盖算法竞赛入门的全部知识点</li>')
    parts.append('<li><strong>四大阶段：</strong>语法基础(L1-5)→编程进阶(L6-8)→核心算法(L9-13)→算法进阶(L14-16)</li>')
    parts.append('<li><strong>两语言并行：</strong>C++让你理解底层，Python让你快速验证——两种视角互补</li>')
    parts.append('<li><strong>厦大校训：</strong>自强不息，止于至善。16章的征程结束，但算法之路刚刚开始。</li>')
    parts.append('</ul></div>')
    parts.append('<div class="chapter-end">— 全16章完 · 共161题 · 自强不息，止于至善 —</div>')

    html=f"""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"><title>第16章 终极试炼</title><style>{CSS}</style></head><body>{chr(10).join(parts)}</body></html>"""
    out=BOOK_ROOT/"textbook"/"chapter16_print.html"
    out.write_text(html,encoding='utf-8')
    print(f"✅ Ch16 dialog version: {len(html)} chars")

if __name__=="__main__":
    build_html()
