#!/usr/bin/env python3
"""第15章 状态的艺术(角色对话版) — 动态规划"""
import json, re, os, sys
from pathlib import Path
BOOK_ROOT = Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(BOOK_ROOT / 'scripts'))

PROBLEMS = [
    {"nq":"NQ151","acw":2,"title":"01背包问题",
     "story":"小鲁终于进入了算法竞赛的巅峰领域——动态规划(DP)。\"01背包：N件物品，每件有体积和价值。背包容量V——选哪些物品使总价值最大？\"小华说，\"f[i][j]=前i件物品用j容量能获得的最大价值。每件选或不选：f[i][j]=max(f[i-1][j], f[i-1][j-v[i]]+w[i])。这就是DP的核心——用子问题的解构造原问题的解。优化：将二维压成一维，j从大到小遍历。\"",
     "input":"第一行N,V。然后N行每行v_i w_i。","output":"最大总价值。",
     "sample_in":"4 5\n1 2\n2 4\n3 4\n4 5","sample_out":"8","constraint":"0<N,V≤1000",
     "sol":"二维DP：f[i][j]=max(f[i-1][j], f[i-1][j-v]+w)。一维优化：f[j]=max(f[j], f[j-v]+w)，j从V倒序到v（防止重复使用）。时间O(NV)，空间O(V)。初始化f[0]=0（全0初值表示恰好装满？不——恰好装满需f[1..V]=-INF）。",
     "tip":"01背包的变形：完全背包(j正序)、多重背包(二进制拆分)。一维优化的关键是j倒序——保证每件物品只被选一次。DP的五步法：1)确定状态定义 2)初始化 3)转移方程 4)遍历顺序 5)答案位置。这个框架适用于所有DP问题。"},
    {"nq":"NQ152","acw":3,"title":"完全背包问题",
     "story":"\"01背包每件只能选一次——如果每件可以选无限次呢？\"小华问。\"那就是完全背包！\"小鲁推导道，\"f[i][j]=max(f[i-1][j], f[i][j-v]+w)——注意第二项是f[i]不是f[i-1]，因为选了之后i仍可选。优化到一维：j正序从v到V——正好体现'可重复选'的特点。01倒序、完全正序——两行代码的区别背后是完全不同的DP语义。\"",
     "input":"第一行N,V。然后N行每行v_i w_i。","output":"最大总价值。",
     "sample_in":"4 5\n1 2\n2 4\n3 4\n4 5","sample_out":"10","constraint":"0<N,V≤1000",
     "sol":"完全背包一维：for i: for j from v to V: f[j]=max(f[j], f[j-v]+w)。j正序遍历！因为同一件物品可以被多次选取——正序遍历时f[j-v]是已更新过的第i层状态，允许重复选。时间O(NV)，空间O(V)。",
     "tip":"完全背包正序、01背包倒序——背后是同一个转移方程在不同遍历顺序下的不同效果。理解这一点，多重背包的二进制拆分也就懂了。完全背包的初始化同样要注意是否恰好装满。"},
    {"nq":"NQ153","acw":898,"title":"数字三角形",
     "story":"\"一个三角形数塔——从顶部出发，每次可以向下走左或右，求到达底层的最大路径和。\"小华画出三角，\"这是线性DP的入门——f[i][j]=三角形第i行第j列到达底层的最大和。自底向上推：f[i][j]=max(f[i+1][j], f[i+1][j+1])+a[i][j]。顶部f[0][0]就是答案。也可以自顶向下推——但自底向上不需要处理边界。\"",
     "input":"第一行n。然后n行三角形数字。","output":"最大路径和。",
     "sample_in":"5\n7\n3 8\n8 1 0\n2 7 4 4\n4 5 2 6 5","sample_out":"30","constraint":"1 ≤ n ≤ 500, −10000 ≤ 值 ≤ 10000",
     "sol":"自底向上DP：从倒数第二行开始，f[i][j]=max(f[i+1][j],f[i+1][j+1])+a[i][j]。顶部f[0][0]为答案。时间O(n²)，空间O(n²)(滚动数组可O(n))。这是最短路径DP和三角形DP的最基本形态。",
     "tip":"自底向上避免了边界检查——每一层总有下一层。自顶向下需要处理j==0和j==i的边界。这是一个重要经验：DP的迭代方向选择直接影响代码复杂度。数字三角形也是树形DP和网格DP的简化版。"},
    {"nq":"NQ154","acw":895,"title":"最长上升子序列",
     "story":"\"LIS——最长上升子序列。给一个数组，找最长的严格递增的子序列（可以不连续）。\"小华说，\"朴素DP：f[i]=以a[i]结尾的LIS长度=max(f[j]+1) for j<i and a[j]<a[i]。O(n²)。优化版：维护一个tails数组——tails[i]=长度为i+1的IS的最小可能结尾值。二分查找更新→O(n log n)。这DP+二分的组合堪称经典。\"",
     "input":"第一行N。第二行N个整数。","output":"LIS长度。",
     "sample_in":"7\n3 1 2 1 8 5 6","sample_out":"4","constraint":"1 ≤ N ≤ 100000",
     "sol":"朴素O(n²)：对每个i遍历j<i。优化O(n log n)：tails数组——对每个x，二分找到tails中第一个≥x的位置，替换或追加。若x比所有tails大则append，否则替换。最终tails的长度=LIS。Python用bisect_left。",
     "tip":"LIS的优化是用贪心维护'最小结尾值'——保证tails数组始终是递增的，可以用二分。这个优化思路也用于LIS的变种（LNDS/带权LIS）。DP+贪心+二分=算法设计中最经典的技术融合。"},
    {"nq":"NQ155","acw":897,"title":"最长公共子序列",
     "story":"\"LCS——两个字符串的最长公共子序列。\"小华说，\"DP经典中的经典——f[i][j]=A前i个和B前j个的LCS长度。若A[i]==B[j]则f[i][j]=f[i-1][j-1]+1；否则f[i][j]=max(f[i-1][j], f[i][j-1])。二维DP的范式。LCS的应用贯穿生物信息学（DNA比对）、diff工具、拼写纠错——是字符串DP的核心模型。\"",
     "input":"第一行n,m。第二行A串，第三行B串。","output":"LCS长度。",
     "sample_in":"4 5\nacbd\nabedc","sample_out":"3","constraint":"1 ≤ n,m ≤ 1000",
     "sol":"二维DP：f[i][j]定义如上。双重循环填充：若匹配则左上+1，否则取上/左的最大值。最终答案在f[n][m]。时间O(nm)，空间O(nm)可压到O(min(n,m))滚动数组。这是编辑距离的前身——只是代价函数不同。",
     "tip":"LCS的转移图示：方向箭头——左上(匹配)、上(跳过A[i])、左(跳过B[j])。空间优化：只用两行交替(f[cur]和f[prev])。LCS可以扩展为带权版本、多串版本——理解基本模型后扩展到海量变种。"},
    {"nq":"NQ156","acw":282,"title":"石子合并",
     "story":"\"区间DP的经典——N堆石子排成一排，每次合并相邻两堆，代价为两堆石子数之和，求合并成一堆的最小总代价。\"区间DP范式：f[l][r]=合并[l,r]区间的最小代价=f[l][k]+f[k+1][r]+sum[l..r]。三重循环——len从小到大(1→n)、l从0开始、k在[l,r)分割。最终答案f[0][n-1]。区间DP是理解DP最优子结构的最佳入口。\"",
     "input":"第一行N。第二行N个整数表示每堆石子数。","output":"最小总代价。",
     "sample_in":"4\n1 3 5 2","sample_out":"22","constraint":"1 ≤ N ≤ 300",
     "sol":"区间DP模板：for len=2 to n: for l=0 to n-len: r=l+len-1; f[l][r]=INF; for k=l to r-1: f[l][r]=min(f[l][r], f[l][k]+f[k+1][r]+s[r+1]-s[l])。前缀和s[i]=前i堆的总和快速求区间和。O(n³)，n≤300时OK。",
     "tip":"区间DP三要素：len从小到大(保证子区间已算好)、l遍历起点、k遍历分割点。前缀和O(1)求区间和。这题可以用平行四边形优化到O(n²)但不在本课范围。理解这个三层循环模式，所有区间DP问题都是它的变体。"},
    {"nq":"NQ157","acw":902,"title":"最短编辑距离",
     "story":"\"把字符串A变成字符串B——每次可以增、删、改一个字符，最少操作次数？\"这是编辑距离(Levenshtein Distance)。\"f[i][j]=A前i个变B前j个的最小操作数。增：f[i][j-1]+1；删：f[i-1][j]+1；改：f[i-1][j-1]+(A[i]!=B[j])。三重min。编辑距离是所有拼写检查、DNA比对、文档diff的底层算法——LCS的泛化。\"",
     "input":"第一行n和A串。第二行m和B串。","output":"最小操作次数。",
     "sample_in":"4\nAGTCTGACGC\n3\nAGTAAGTAGGC","sample_out":"(见OJ实际输出)","constraint":"1 ≤ n,m ≤ 1000",
     "sol":"编辑距离DP：f[i][j]如上。初始化f[i][0]=i(全删), f[0][j]=j(全增)。三重min转移。时间O(nm)，空间O(nm)→滚动数组O(min(n,m))。与LCS的区别在于可以有替换操作且替换cost=1而非跳过代价。",
     "tip":"编辑距离的初始化不要忘——空串变j字符=j次增加。三个操作对应三个方向：上=删、左=增、左上=改。每个方向+1(替换是否+1取决于字符是否相同)。这个DP是所有字符串距离算法的根基。"},
    {"nq":"NQ158","acw":901,"title":"滑雪",
     "story":"\"记忆化搜索——DP和搜索的完美结合。\"华说，\"给定一个二维矩阵表示雪山高度，从某点开始滑只能从高往低滑到四个方向。求最长滑行路径。dp[i][j]=从(i,j)出发的最长路径=1+max(dp[nx][ny])对所有合法邻居(高度更低)。用DFS+备忘录——递归第一次算，后续直接查表。记忆化=Top-down DP，递推=Bottom-up DP。\"",
     "input":"第一行R,C。然后R×C矩阵。","output":"最长滑行长度。",
     "sample_in":"5 5\n1 2 3 4 5\n16 17 18 19 6\n15 24 25 20 7\n14 23 22 21 8\n13 12 11 10 9","sample_out":"25","constraint":"1 ≤ R,C ≤ 300",
     "sol":"记忆化DFS：dp[i][j]=1+max(dfs(nx,ny) for 所有高度更低的邻居)。每次dfs先检查dp[i][j]是否已算(不等于-1)，已算直接返回。每个状态算一次，O(RC)。比纯DFS快是因为避免了重复搜索——这正是DP的威力。",
     "tip":"记忆化搜索=自顶向下DP。优势：按需计算（只计算能到达的状态）。劣势：递归栈深度限制。DFS中四个方向的顺序不影响结果。Python递归可能需要sys.setrecursionlimit(1000000)。这道题展示了搜索→DP的自然过渡。"},
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
body{font-family:"PingFang SC","Hiragino Sans GB","Noto Serif CJK SC","STSong",serif;font-size:9.5pt;line-height:1.7;color:#222;string-set:chapter"第15章 状态的艺术——动态规划"}
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
    parts.append('<div class="chapter-title">状态的艺术</div>')
    parts.append('<div class="chapter-subtitle">动态规划 · 8题 · C++ &amp; Python 双语对照</div>')
    parts.append('<div class="preface">')
    parts.append('<p>小鲁进入了算法竞赛的核心——<strong>动态规划(DP)</strong>。DP不是一种算法，而是一种思想——将大问题拆成小问题，用小问题的解构造大问题的解。DP的精髓在于<strong>状态定义</strong>和<strong>转移方程</strong>。本章8题覆盖DP的四大类型：背包DP、线性DP、区间DP、记忆化搜索。学完本章，你才是一个真正的算法选手。</p>')
    parts.append('</div>')
    parts.append('<div class="knowledge-box"><div class="k-title">🧩 DP四大类型速查</div><ul>')
    parts.append('<li><strong>背包DP：</strong>01(倒序)、完全(正序)。物品选或不选→二维压一维的关键是遍历顺序</li>')
    parts.append('<li><strong>线性DP：</strong>LIS(一维)、LCS(二维)、编辑距离(二维)。字符串/序列问题的标准模型</li>')
    parts.append('<li><strong>区间DP：</strong>石子合并——len从小到大，k分割区间。O(n³)三重循环模板</li>')
    parts.append('<li><strong>记忆化搜索：</strong>DFS+备忘录=自顶向下DP。滑雪、树形DP。递归优雅但注意栈深度</li></ul></div>')

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
    parts.append('<li><strong>DP五步法：</strong>定义状态→初始化→转移方程→遍历顺序→答案位置。模板先于变种</li>')
    parts.append('<li><strong>背包进化：</strong>01倒序、完全正序——遍历顺序决定是否可以重复选</li>')
    parts.append('<li><strong>字符串DP三连：</strong>LIS(一维+二分优化)、LCS(二维+状态转移)、编辑距离(三维min)</li>')
    parts.append('<li><strong>区间DP：</strong>len从小到大、l枚举起点、k枚举分割。前缀和加速区间和查询</li>')
    parts.append('<li><strong>记忆化搜索：</strong>DFS+备忘录=优雅的Top-down。滑雪、树形DP的标准写法</li>')
    parts.append('</ul></div>')
    parts.append('<div class="chapter-end">— 第15章完 · 共8题 · 自强不息 —</div>')

    html=f"""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"><title>第15章 状态的艺术</title><style>{CSS}</style></head><body>{chr(10).join(parts)}</body></html>"""
    out=BOOK_ROOT/"textbook"/"chapter15_print.html"
    out.write_text(html,encoding='utf-8')
    print(f"✅ Ch15 dialog version: {len(html)} chars")

if __name__=="__main__":
    build_html()
