#!/usr/bin/env python3
"""第14章 图的疆域(角色对话版) — 图论入门"""
import json, re, os, sys
from pathlib import Path
BOOK_ROOT = Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(BOOK_ROOT / 'scripts'))

PROBLEMS = [
    {"nq":"NQ143","acw":848,"title":"拓扑序列",
     "story":"小鲁在整理课程先修关系：\"高数→线代→概率论——这些课有先后依赖关系。\"小华说：\"这就是有向图的拓扑排序！Kahn算法：每次选一个入度为0的节点输出，删除它所有出边。用队列维护当前入度为0的节点集合。如果最终输出的节点数小于n，说明图中有环——拓扑排序同时也是判环算法。\"",
     "input":"第一行n,m。然后m行每行x y表示边x→y。","output":"一个拓扑序列，不存在输出-1。",
     "sample_in":"4 3\n1 2\n2 3\n4 3","sample_out":"1 2 4 3","constraint":"1 ≤ n,m ≤ 10⁵",
     "sol":"Kahn算法(BFS拓扑排序)：1)统计所有节点入度；2)入度为0的节点入队；3)while队列非空：弹出队头t输出，遍历t的所有邻居，邻居入度-1，若入度变为0则入队；4)输出数<n则有环。O(n+m)。另外DFS也能做拓扑排序。",
     "tip":"拓扑排序=有向无环图(DAG)的线性排列。应用：课程安排、编译依赖、任务调度。Python: 邻接表+deque+入度数组。拓扑排序是算法竞赛中最基础的图论算法之一——必须熟练掌握。"},
    {"nq":"NQ144","acw":849,"title":"Dijkstra I",
     "story":"\"求图中从1号点到n号点的最短路径——每条边有正权重。\"小华说，\"Dijkstra算法——贪心法。每次从未确定最短距离的点中选距离最小的，用它去松弛(relax)它的邻居。朴素版每次O(n)找最小值，n次循环→O(n²)。适合稠密图(n不大但边多)。Python的heapq优化版更适合稀疏图，O(m log n)。\"",
     "input":"第一行n,m。然后m行每行x y z表示边x→y权重z。","output":"1到n的最短距离。",
     "sample_in":"3 3\n1 2 2\n2 3 1\n1 3 4","sample_out":"3","constraint":"1 ≤ n ≤ 500, 1 ≤ m ≤ 10⁵",
     "sol":"Dijkstra朴素版：dist[1]=0, 其余INF。n次循环：每次找未被标记的最近节点t，标记t，用t松弛所有邻居v: dist[v]=min(dist[v],dist[t]+w[t][v])。O(n²+m)。证明：贪心选择正确性基于边权非负（边权为负时应用Bellman-Ford/SPFA）。",
     "tip":"Dijkstra只适用于非负权图。找最近节点的O(n)可以用堆优化降到O(log n)。Python: heap=(dist[i],i)入堆，弹堆时检查是否过期。朴素版n≤500时O(n²)≈250K——完全够用。"},
    {"nq":"NQ145","acw":850,"title":"Dijkstra II",
     "story":"\"上一题n=500，O(n²)没问题。但如果n=10⁵呢？\"小华说，\"需要用堆优化——优先队列每次O(log n)找最近节点。总复杂度O(m log n)。注意堆中可能有过期的旧值——弹堆时检查dist是否已更新。STL的priority_queue不支持修改键值，所以有重复入堆的策略。\"",
     "input":"第一行n,m。然后m行每行x y z。","output":"1到n的最短距离，不可达输出-1。",
     "sample_in":"3 3\n1 2 2\n2 3 1\n1 3 4","sample_out":"3","constraint":"1 ≤ n,m ≤ 1.5×10⁵，边权≤10000",
     "sol":"堆优化Dijkstra：dist[1]=0, heap.push({0,1})。while heap非空：弹出{d,u}(若d>dist[u]则skip过期)，标记st[u]，遍历所有邻居v: if(dist[v]>dist[u]+w): dist[v]=dist[u]+w; heap.push({dist[v],v})。O(m log n)。",
     "tip":"Python用heapq：heappush(heap,(dist[v],v))。过期检测：if d>dist[u]: continue。这是C++和Python都通用的堆优化模板——配上邻接表就是标准的Dijkstra优化版。背下这个模板，面试/竞赛都够用。"},
    {"nq":"NQ146","acw":851,"title":"spfa求最短路",
     "story":"\"Dijkstra不能处理负权边——Bellman-Ford可以但O(n×m)太慢。SPFA是Bellman-Ford的队列优化版——只有被松弛过的节点才入队去松弛别人。平均O(m)，最坏O(n×m)可能被卡。\"小华补充，\"SPFA还能判断负环——如果一个节点入队超过n次，存在负环。虽然竞赛中经常被卡，但实现简单、思路巧妙。\"",
     "input":"第一行n,m。然后m行每行x y z（可能有负权）。","output":"1到n最短路，有负环输出impossible。",
     "sample_in":"3 3\n1 2 1\n2 3 2\n1 3 4","sample_out":"3","constraint":"1 ≤ n,m ≤ 10⁵",
     "sol":"SPFA：dist[1]=0, q.push(1), st[1]=true。while q非空：t=q.front(); q.pop(); st[t]=false。遍历t的邻居v: if(dist[v]>dist[t]+w): dist[v]=dist[t]+w; if(!st[v]) q.push(v), st[v]=true。复杂度：平均O(m)最坏O(nm)。",
     "tip":"st数组记录节点是否在队列中——避免重复入队。负环检测：维护cnt[v]=到v的最短路边数，若cnt[v]≥n则有负环。SPFA容易被构造数据卡掉——正权图用Dijkstra更安全。但理解SPFA的松弛传播思想对理解更多图论算法有帮助。"},
    {"nq":"NQ147","acw":854,"title":"Floyd求最短路",
     "story":"\"如果要查询任意两点之间的最短距离——多源最短路径——怎么办？\"小华说，\"Floyd-Warshall算法！三重循环——for k,i,j: dist[i][j]=min(dist[i][j], dist[i][k]+dist[k][j])。这个简洁的三行代码本质是动态规划——dp[k][i][j]表示只经过前k个节点作中间节点时i到j的最短距离，压缩掉k维就是最终的三重循环。O(n³)但n≤200时完全OK。\"",
     "input":"第一行n,m,q。然后m行每行x y z。然后q行每行a b查询。","output":"每行查询结果，不可达输出impossible。",
     "sample_in":"3 3 2\n1 2 1\n2 3 2\n1 3 4\n2 1\n1 3","sample_out":"impossible\n3","constraint":"1 ≤ n ≤ 200, 1 ≤ q ≤ 10⁵",
     "sol":"Floyd模板：初始化dist[i][i]=0，dist[i][j]=INF。读入边权(注意去重——可能有多条边取min)。三重循环：for k: for i: for j: d[i][j]=min(d[i][j], d[i][k]+d[k][j])。时间O(n³)=8×10⁶(n=200)，空间O(n²)。注意INF不要用0x3f3f3f3f以免溢出。",
     "tip":"Floyd是n≤200的多源最短路首选。它能同时处理正负权边（不能有负环）。k循环必须在最外层——这是理解Floyd为DP的直接体现。Python三重循环可能较慢，n=200时约需0.5秒。INF设为10⁹避免溢出。"},
    {"nq":"NQ148","acw":858,"title":"Prim",
     "story":"\"最小生成树——连接所有节点的最小总权重。\"Prim算法——从一个点开始，每次选距离当前集合最近的节点加入。这和Dijkstra几乎一模一样！区别只在于dist的定义：Dijkstra是到起点的距离，Prim是到当前集合的距离。代码只差一行。\"小华总结道，\"Prim适合稠密图O(n²)，Kruskal适合稀疏图O(m log m)。\"",
     "input":"第一行n,m。然后m行每行u v w（无向边）。","output":"最小生成树的总权重，不连通输出impossible。",
     "sample_in":"4 5\n1 2 1\n1 3 2\n1 4 3\n2 3 2\n3 4 4","sample_out":"6","constraint":"1 ≤ n ≤ 500, 1 ≤ m ≤ 10⁵",
     "sol":"Prim朴素版：dist[i]=到当前生成树的最近距离。n次循环：每次找未标记的最近点t，标记t，ans+=dist[t]。用t更新所有邻居v的dist[v]=min(dist[v], w[t][v])。O(n²+m)。与Dijkstra的唯一区别：dist的更新公式是w[t][v]而非dist[t]+w[t][v]。",
     "tip":"Prim=Dijkstra改一行。Dijkstra: dist[v]=min(dist[v], dist[t]+w)。Prim: dist[v]=min(dist[v], w)。这个区别体现了两者的本质差异——一个求路径累积最短，一个求集合距离最近。稠密图(n≤500)用Prim O(n²)，稀疏图用Kruskal。"},
    {"nq":"NQ149","acw":859,"title":"Kruskal",
     "story":"\"Kruskal——另一种MST算法。把所有边按权重排序，从小到大尝试每条边——如果边的两端不在同一集合中（并查集判断），就加入这条边。贪心法！因为排序后轻边优先加入，保证了树的总权重最小。需要并查集维护连通性——find+union操作。Kruskal=排序+并查集——两个简单工具组合出强大算法。\"",
     "input":"第一行n,m。然后m行每行u v w。","output":"MST总权重，不连通输出impossible。",
     "sample_in":"4 5\n1 2 1\n1 3 2\n1 4 3\n2 3 2\n3 4 4","sample_out":"6","constraint":"1 ≤ n ≤ 10⁵, 1 ≤ m ≤ 2×10⁵",
     "sol":"Kruskal：1)所有边按w升序排序；2)初始化并查集(p[i]=i)；3)遍历每条边(u,v,w)：若find(u)!=find(v)则union(u,v), ans+=w, cnt++；4)若cnt==n-1则连通输出ans，否则impossible。时间O(m log m)（排序主导）。",
     "tip":"Kruskal=排序+并查集。并查集：p[x]存父节点，find(x)路径压缩返回根，union(a,b)将a根连到b根。排序O(m log m)是Kruskal的瓶颈——稀疏图(m≈n)时log m小因此Kruskal快于Prim O(n²)。稠密图反之。"},
    {"nq":"NQ150","acw":860,"title":"染色法判定二分图",
     "story":"\"二分图——能把所有节点分成两组，使所有边的两端都在不同组中。用染色法判断：从一个未染色节点出发，染成1，它的所有邻居染成2，邻居的邻居染成1……如果发现一条边的两端同色——不是二分图。这就是二染色判定——本质是BFS/DFS遍历中检查冲突。是匈牙利算法(最大匹配)的前置知识。\"",
     "input":"第一行n,m。然后m行每行u v表示无向边。","output":"是二分图输出Yes否则No。",
     "sample_in":"4 4\n1 2\n2 3\n3 4\n4 1","sample_out":"Yes","constraint":"1 ≤ n,m ≤ 10⁵",
     "sol":"二染色判定：color数组初始0(未染色)。遍历每个节点，若未染色则BFS/DFS：染色1，邻居染色-1(或2)，邻居的邻居染色1……若遇到已染色且颜色与期望不符→冲突→不是二分图。O(n+m)。BFS和DFS都行——DFS递归简单但深度大时需注意栈溢出。",
     "tip":"二分图=不包含奇环。染色过程本质是BFS涂色——涂色冲突=奇环存在。Python的DFS递归可能栈溢出→用BFS或迭代DFS。二分图判定是图论中的基础算法——后续最大匹配、最小点覆盖都依赖于此。"},
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
body{font-family:"PingFang SC","Hiragino Sans GB","Noto Serif CJK SC","STSong",serif;font-size:9.5pt;line-height:1.7;color:#222;string-set:chapter"第14章 图的疆域——图论入门"}
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
    parts.append('<div class="chapter-title">图的疆域</div>')
    parts.append('<div class="chapter-subtitle">图论入门 · 8题 · C++ &amp; Python 双语对照</div>')
    parts.append('<div class="preface">')
    parts.append('<p>小鲁终于进入了算法竞赛中最大的领域——<strong>图论</strong>。\"图可以描述世间万物——交通网络、社交关系、课程依赖、电路连接……理解图论算法就像获得了一个新的视角。\"本章8道题覆盖图论四大基石：拓扑排序(DAG)、最短路(Dijkstra/SPFA/Floyd)、最小生成树(Prim/Kruskal)、二分图判定。\"这些算法是竞赛和面试的高频考点——背下来、理解透。\"</p>')
    parts.append('</div>')
    parts.append('<div class="knowledge-box"><div class="k-title">🗺️ 图论五大算法速查</div><ul>')
    parts.append('<li><strong>拓扑排序：</strong>Kahn BFS。入度为0节点入队→删除出边。O(n+m)。判环</li>')
    parts.append('<li><strong>Dijkstra：</strong>贪心+松弛。朴素O(n²)稠密/堆优化O(m log n)稀疏。非负权</li>')
    parts.append('<li><strong>SPFA：</strong>队列优化Bellman-Ford。支持负权、判负环。平均O(m)最坏O(nm)</li>')
    parts.append('<li><strong>Floyd：</strong>三重循环dp[k][i][j]。O(n³)。n≤200多源最短路首选</li>')
    parts.append('<li><strong>MST：</strong>Prim O(n²)稠密，Kruskal O(m log m)稀疏（排序+并查集）</li></ul></div>')

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
    parts.append('<li><strong>图论四大基石：</strong>拓扑排序、最短路、最小生成树、二分图——背下模板终身受用</li>')
    parts.append('<li><strong>Dijkstra vs SPFA vs Floyd：</strong>正权选Dijkstra(堆)，负权选SPFA(慎用)，多源n≤200选Floyd</li>')
    parts.append('<li><strong>Prim vs Kruskal：</strong>Prim=改一行Dijkstra，稠密O(n²)。Kruskal=排序+并查集，稀疏O(m log m)</li>')
    parts.append('</ul></div>')
    parts.append('<div class="chapter-end">— 第14章完 · 共8题 · 自强不息 —</div>')

    html=f"""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"><title>第14章 图的疆域</title><style>{CSS}</style></head><body>{chr(10).join(parts)}</body></html>"""
    out=BOOK_ROOT/"textbook"/"chapter14_print.html"
    out.write_text(html,encoding='utf-8')
    print(f"✅ Ch14 dialog version: {len(html)} chars")

if __name__=="__main__":
    build_html()
