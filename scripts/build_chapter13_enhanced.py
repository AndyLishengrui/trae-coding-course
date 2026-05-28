#!/usr/bin/env python3
"""第13章 搜索的艺术(角色对话版) — 搜索与回溯"""
import json, re, os, sys
from pathlib import Path
BOOK_ROOT = Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(BOOK_ROOT / 'scripts'))

PROBLEMS = [
    {"nq":"NQ135","acw":842,"title":"排列数字",
     "story":"小鲁开始学习搜索算法：\"全排列——1到n的所有排列方式。用DFS深度优先搜索，像走迷宫一样一条路走到底再回头。每次选一个没用过的数放入路径，递归进入下一层，然后撤销选择(回溯)。\"小华点头：\"DFS+回溯是搜索算法的灵魂框架。三个要素：路径(已经选了什么)、选择列表(还能选什么)、结束条件(选满了就输出)。这个框架将贯穿你的算法生涯。\"",
     "input":"一个整数n。","output":"1~n所有排列，每行一个，按字典序。",
     "sample_in":"3","sample_out":"1 2 3\n1 3 2\n2 1 3\n2 3 1\n3 1 2\n3 2 1","constraint":"1 ≤ n ≤ 7",
     "sol":"DFS回溯：path存当前路径，used标记已用数字。dfs(u): 若u==n则输出path；否则遍历1..n，若未used则标记used→加入path→dfs(u+1)→撤销标记→弹出path。复杂度O(n!)。注意递归树的深度=n，叶子数=n!。",
     "tip":"Python: itertools.permutations一行。手写DFS重点理解回溯的'撤销'操作——进入递归前做的修改，返回后必须完全复原。回溯=尝试→失败→回退→再尝试。排列问题是回溯第一课，也是理解'搜索状态空间'的钥匙。"},
    {"nq":"NQ136","acw":843,"title":"n-皇后问题",
     "story":"\"N皇后——在N×N棋盘上放N个皇后，使它们互不攻击（同行、同列、同对角线只有一个）。\"小华画出棋盘，\"回溯搜索的经典题。按行搜索——每行必放一个皇后，只需决定放在哪一列。用三个布尔数组标记：col[j](列是否被占)、dg[i+j](主对角线)、udg[i-j+n](反对角线)。回溯的剪枝的力量——不满足约束的分支直接跳过。\"",
     "input":"一个整数n。","output":"所有方案，每个方案n行，每行n个字符(.Q)表示棋盘。",
     "sample_in":"4","sample_out":".Q..\n...Q\nQ...\n..Q.\n\n..Q.\nQ...\n...Q\n.Q..","constraint":"1 ≤ n ≤ 9",
     "sol":"按行DFS：dfs(r)——在第r行选一列放皇后。对每列，检查col[j], dg[r+j], udg[r-j+n]是否未占。若可放则标记→递归r+1→撤销标记。对角线坐标映射：主对角线r+j为定值([0,2n-2])，反对角线r-j+n为定值。O(n!)但剪枝后实际更快。",
     "tip":"对角线编号技巧：主对角线r+c=常数(0到2n-2)，反对角线r-c+n=常数(n到2n+n)。用三个bool数组O(1)判断冲突——比每次遍历O(n)快得多。回溯+剪枝=搜索的效率保证——剪得越早，省得越多。"},
    {"nq":"NQ137","acw":844,"title":"走迷宫",
     "story":"\"从迷宫起点走到终点——每次只能上下左右走一步。\"小华说，\"DFS会找到一条路径，但不一定最短；BFS广度优先——层层扩展，像水的波纹——第一次遇到终点时走的一定是最短路径！BFS用队列：起点入队→弹出一个位置→扩展四个方向→合法的入队。每个位置只访问一次。BFS是求无权图最短路径的标准算法。\"",
     "input":"第一行n,m。然后n×m的迷宫(0可走1墙)。","output":"从(0,0)到(n-1,m-1)的最少步数。",
     "sample_in":"5 5\n0 1 0 0 0\n0 1 0 1 0\n0 0 0 0 0\n0 1 1 1 0\n0 0 0 1 0","sample_out":"8","constraint":"1 ≤ n,m ≤ 100",
     "sol":"BFS模板：queue存(x,y,dist)；vis数组标记访问过。四个方向：dx=[-1,0,1,0],dy=[0,1,0,-1]。每次while queue非空：弹出队头，判断是否终点，否则扩展四个方向，合法且未访问则标记入队。每个位置最多访问一次，O(nm)。",
     "tip":"BFS层序遍历——队列保证先访问近的点。dist不需要额外存储，直接存在队列元素或距离数组中。DFS和BFS的选择：DFS找一条路径(不保证最短)，BFS找最短路径。Python用deque作BFS队列——popleft() O(1)。"},
    {"nq":"NQ138","acw":845,"title":"八数码",
     "story":"\"3×3的格子，8个数+1个空格——通过滑动空格，把乱序排列恢复成123/456/78x。\"小华说，\"BFS的状态空间搜索！每个状态是一个3×3排列→看成一个字符串。从初始状态开始BFS，每次空格和相邻数字交换生成新状态。用字典记录每个状态到初始状态的距离。终止状态固定为'12345678x'。BFS第一次遇到终止状态时的距离就是最少步数。\"",
     "input":"一行9个字符，表示初始状态（x代表空格）。","output":"最少移动步数，无解输出-1。",
     "sample_in":"2 3 4 1 5 x 7 6 8","sample_out":"19","constraint":"3×3网格",
     "sol":"BFS状态空间搜索：状态编码为字符串(9字符)。从初始状态开始BFS，用unordered_map/dict记录距离。每次找到'x'的位置，和上下左右(若合法)交换，生成新状态。复杂度O(9!)=362880状态——BFS完全可以。注意逆序对奇偶性判断无解。",
     "tip":"BFS的队列保证层层扩展——第一次遇到目标状态时步数最少。状态总数=9!/2=181440（一半无解）。Python用字典作距离映射+deque作BFS队列。把3×3网格编码成一维字符串是简化状态的关键。"},
    {"nq":"NQ139","acw":846,"title":"树的重心",
     "story":"\"找树的重心——删除重心后剩余各连通块中最大块的最小值。\"小华画出树，\"DFS遍历树，统计每个节点的子树大小。删除节点u后，连通块有三部分：u的各子树、u的父节点所在的整棵树减去u的子树。取这些中的最大值，然后所有u的这个最大值中的最小值就是答案。树形DP+DFS——理解'树遍历+状态统计'的模式。\"",
     "input":"第一行n。然后n-1行每行a b表示边。","output":"重心对应的最大连通块最小值。",
     "sample_in":"9\n1 2\n1 7\n1 4\n2 8\n2 5\n4 3\n3 9\n4 6","sample_out":"4","constraint":"1 ≤ n ≤ 10⁵",
     "sol":"DFS统计子树大小：dfs(u,fa)——遍历u的邻居v(排除fa)，dfs(v,u)，s[u]+=s[v]累加子树大小。删除u后最大块=max(s[v](各子树), n-s[u](上方树))。取所有u的max的最小值。O(n)一次DFS。",
     "tip":"树形DFS的关键：用fa参数避免回头，用邻接表存图。Python递归可能超深度——用sys.setrecursionlimit(200000)或手写栈。重心在点分治(CDQ)中起关键作用——保证递归深度为log n。这是树形DP的入门。"},
    {"nq":"NQ140","acw":847,"title":"图中点的层次",
     "story":"\"给一个有向图，求从1号点到n号点的最短距离（每条边长度为1）。\"BFS天然适合！因为边权相同，BFS第一层是距离1的点，第二层距离2……第一次遇到n号点时的距离就是最短距离。小鲁说：\"这和迷宫BFS本质上是一样的——只是图的连接关系用邻接表存储，而不是四方向规则。\"",
     "input":"第一行n,m。然后m行每行a b表示有向边。","output":"1到n的最短距离，不可达输出-1。",
     "sample_in":"4 5\n1 2\n2 3\n3 4\n1 3\n1 4","sample_out":"1","constraint":"1 ≤ n,m ≤ 10⁵",
     "sol":"BFS模板：queue存(node, dist)，vis数组标记访问。邻接表存图：vector<int> adj[N]或list of lists。从1号出发BFS，遇到n时输出dist。每个节点最多访问一次，O(n+m)。BFS是边权相同的单源最短路径标准算法。",
     "tip":"邻接表：Python用列表嵌套——adj=[[] for _ in range(n+1)]。BFS的queue用deque。dist数组初始化为-1表示未访问，dist[1]=0。BFS层层扩展的性质保证第一次遇到终点时的距离就是最短的。无权图的最短路=BFS。"},
    {"nq":"NQ141","acw":777,"title":"字符串乘方",
     "story":"\"求一个字符串的最小循环节——即最小的k使得s等于某个字符串重复k次。\"小华说，\"方法1：枚举子串长度len（必须是n的约数），检查所有对应位置字符是否相同。方法2：KMP的next数组——最小循环节=n-next[n]（当n%(n-next[n])==0时）。前者O(n×约数个数)，后者O(n)。两种方法从不同角度展示了'周期性判断'的思维。\"",
     "input":"多行，每行一个字符串，以'.'结束。","output":"每行输出最大k值。",
     "sample_in":"abcd\naaaa\nababab\n.","sample_out":"1\n4\n3","constraint":"字符串长度 ≤ 10⁶",
     "sol":"KMP法：next[n]是n的最长公共前后缀长度。若n%(n-next[n])==0，则最小循环节len=n-next[n]，k=n/len。否则整个串是最大循环节(k=1)。验证：aaaa中next[4]=3, n-next[n]=1, k=4。枚举法：检查len为n的约数，验证所有s[i]==s[i%len]。",
     "tip":"KMP的next数组不仅用于匹配，还揭示了字符串的周期结构——len=n-next[n]是最小可能的循环节长度。这个性质在字符串周期分析和压缩中非常有用。"},
    {"nq":"NQ142","acw":778,"title":"字符串最大跨距",
     "story":"\"找字符串S中三个子串S1,S2,S3的位置——S1在最左，S2在最右，S3在S1和S2之间——求S1最右位置到S2最左位置的距离。\"小鲁说：\"用find()从左往右找S1的最左出现，用rfind()从右往左找S2的最右出现。然后检查S3是否在它们之间合法存在。Python的str.find/rfind让这题行云流水。\"",
     "input":"一行字符串S，以及S1,S2,S3（用逗号隔开）。","output":"最右跨距，若无合法方案输出-1。",
     "sample_in":"abcd123ab888efghij45ef67kl,ab,ef,45","sample_out":"18","constraint":"S长度≤300",
     "sol":"1)S.find(S1)→左边界L。2)S.rfind(S2)→右边界R。3)检查S[L+len1:R]中是否有S3且位置合法。4)R-(L+len1)就是跨距。若L==-1或R==-1或R<L+len1则无解。注意跨距计算不含S1和S2本身。",
     "tip":"Python的find()返回第一次出现，rfind()返回最后一次出现。这是字符串操作的经典组合——左找+右找+中间检查。逗号分割输入：s=input().split(',')。本题训练的是对字符串多种查找操作的组合运用能力。"},
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
body{font-family:"PingFang SC","Hiragino Sans GB","Noto Serif CJK SC","STSong",serif;font-size:9.5pt;line-height:1.7;color:#222;string-set:chapter"第13章 搜索的艺术——搜索与回溯"}
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
    parts.append('<div class="chapter-title">搜索的艺术</div>')
    parts.append('<div class="chapter-subtitle">搜索与回溯 · 8题 · C++ &amp; Python 双语对照</div>')
    parts.append('<div class="preface">')
    parts.append('<p>小鲁开始学习人工智能最基础的算法——<strong>搜索</strong>。\"搜索就是穷举所有可能性——但穷举不等于蛮力。DFS回溯像走迷宫一条路走到黑，BFS像水的波纹层层扩散。加上剪枝——提前砍掉不可能的分支——搜索可以从指数级变成多项式级。理解搜索，是理解所有AI和优化算法的基石。\"</p>')
    parts.append('</div>')
    parts.append('<div class="knowledge-box"><div class="k-title">🔍 DFS vs BFS 速查</div><ul>')
    parts.append('<li><strong>DFS：</strong>深度优先——回溯探索。适合：全排列、N皇后、树遍历。空间O(深度)</li>')
    parts.append('<li><strong>BFS：</strong>广度优先——层层扩散。适合：最短路径、八数码、无权图最短路。空间O(宽度)</li>')
    parts.append('<li><strong>剪枝：</strong>提前排除不可能的分支——N皇后的col/dg/udg标记</li>')
    parts.append('<li><strong>状态编码：</strong>将棋盘/网格编码成字符串作哈希key——八数码的关键技术</li></ul></div>')

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
    parts.append('<li><strong>DFS回溯：</strong>路径+选择列表+结束条件。回溯撤销操作是理解搜索的关键</li>')
    parts.append('<li><strong>BFS：</strong>队列+距离数组。层层扩展保证最短路径（边权相同）</li>')
    parts.append('<li><strong>状态搜索：</strong>八数码——将棋盘编码为字符串做状态BFS</li>')
    parts.append('<li><strong>树形DFS：</strong>重心问题——理解树遍历+子树统计的DP模式</li>')
    parts.append('</ul></div>')
    parts.append('<div class="chapter-end">— 第13章完 · 共8题 · 自强不息 —</div>')

    html=f"""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"><title>第13章 搜索的艺术</title><style>{CSS}</style></head><body>{chr(10).join(parts)}</body></html>"""
    out=BOOK_ROOT/"textbook"/"chapter13_print.html"
    out.write_text(html,encoding='utf-8')
    print(f"✅ Ch13 dialog version: {len(html)} chars")

if __name__=="__main__":
    build_html()
