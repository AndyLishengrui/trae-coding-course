#!/usr/bin/env python3
"""第12章 结构的魔力(角色对话版) — 基础数据结构"""
import json, re, os, sys
from pathlib import Path
BOOK_ROOT = Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(BOOK_ROOT / 'scripts'))

PROBLEMS = [
    {"nq":"NQ127","acw":826,"title":"单链表",
     "story":"小鲁第一次实现链表：\"每个节点有一个next指针指向下一个节点。但反复new/delete太慢了——竞赛中用的是数组模拟链表！\"小华解释道：\"e[i]存节点i的值，ne[i]存节点i的下一个节点下标。头节点head指向第一个节点，空闲链表管理未用节点。三个数组+一个整数idx（当前可用下标）就搭建了完整的内存池。这就是为什么OIer的代码里满是数组——不是不会用指针，而是数组更快。\"",
     "input":"第一行M。然后M行操作：H x(头插)、D k(删第k后)、I k x(在第k后插入)。","output":"链表从头到尾的值。",
     "sample_in":"10\nH 9\nI 1 1\nD 1\nD 0\nH 6\nI 3 6\nI 4 5\nI 4 5\nI 3 4\nD 6","sample_out":"6 4 6 5","constraint":"1 ≤ M ≤ 100000",
     "sol":"数组模拟链表：e[]存值, ne[]存next下标, head=头节点下标, idx=当前可用下标。头插法：e[idx]=x; ne[idx]=head; head=idx++。第k个后插入：e[idx]=x; ne[idx]=ne[k]; ne[k]=idx++。删除第k个之后：ne[k]=ne[ne[k]]。",
     "tip":"数组模拟链表=静态链表。每个操作O(1)。Python用list同样高效（append/pop=O(1)）。理解这种'用数组下标替代指针'的思想——后续Trie、并查集、堆都是用数组模拟各种结构。"},
    {"nq":"NQ128","acw":828,"title":"模拟栈",
     "story":"\"栈——后进先出(LIFO)。就像叠盘子，最后放上去的最先拿下来。\"小华说，\"实现一个栈支持push和pop操作。C++有std::stack，Python用list的append()和pop()天然就是栈。但手写一个数组模拟理解底层更透彻——用一个数组stk和指针tt，push时stk[++tt]=x，pop时tt--只移动指针，O(1)时间。\"",
     "input":"第一行M。然后M行：push x / pop / empty / query。","output":"按操作输出。",
     "sample_in":"6\npush 5\nquery\npush 6\npop\nquery\nempty","sample_out":"5\n5\nNO","constraint":"1 ≤ M ≤ 100000",
     "sol":"数组模拟栈：stk[N]和tt（栈顶指针，初始0）。push: stk[++tt]=x；pop: tt--；query: stk[tt]；empty: tt>0?'NO':'YES'。指针只是整数下标，极其高效。Python: list.append()=push, list.pop()=pop, list[-1]=query。",
     "tip":"单调栈就是在普通栈的基础上加一条约束——栈内元素保持单调。这是后续处理'下一个更大元素'等问题的核心数据结构。理解栈+单调性=>O(n)解决看似O(n²)的问题。"},
    {"nq":"NQ129","acw":829,"title":"模拟队列",
     "story":"\"队列——先进先出(FIFO)。就像排队买饭，先到的先服务。\"小华画出示意图，\"用数组模拟队列需要两个指针：hh(队头)和tt(队尾)。push时q[++tt]=x，pop时hh++——两个指针都只进不退。这就是'同时移动双端'的模式。Python的deque是双端队列，from collections import deque——比list的pop(0)快(O(1) vs O(n))。\"",
     "input":"第一行M。然后M行：push x / pop / empty / query。","output":"按操作输出。",
     "sample_in":"6\npush 5\nquery\npush 6\npop\nquery\nempty","sample_out":"5\n6\nNO","constraint":"1 ≤ M ≤ 100000",
     "sol":"数组模拟队列：q[N], hh=0队头, tt=-1队尾。push: q[++tt]=x；pop: hh++；query: q[hh]；empty: hh>tt。注意hh>tt表示空。Python: deque.append()=push, deque.popleft()=pop。list的pop(0)是O(n)——不要用！",
     "tip":"Python中list.pop(0)是O(n)因为要移动所有元素。一定要用collections.deque！单调队列=单调性+双端队列——滑动窗口最值问题的核心数据结构。"},
    {"nq":"NQ130","acw":3302,"title":"表达式求值",
     "story":"\"计算'(2+3)×5'——用栈！\"小华说，\"两个栈：一个存数字，一个存运算符。遇到数字压数字栈；遇到(压运算符栈；遇到)计算直到(被弹出；遇到运算符——如果栈顶优先级≥当前，先算栈顶。核心：维护运算优先级。这是编译原理和计算器的核心。\"小鲁试了试：\"确实巧妙——中缀表达式转后缀求值的经典算法！\"",
     "input":"一个中缀表达式（含+-*/和括号，数字非负）。","output":"表达式结果（整数除法向零截断）。",
     "sample_in":"(2+3)*5","sample_out":"25","constraint":"表达式长度 ≤ 100000",
     "sol":"双栈法求中缀表达式：数字栈+运算符栈。优先级映射：+-为1，*/为2。遇到)弹栈直到(。每次弹出一个运算符和两个数字，计算结果压回数字栈。Python的eval()能直接算但OJ比赛中禁止。理解手写栈求值是数据结构综合应用的经典案例。",
     "tip":"符号优先级存入字典：pri={'+':1,'-':1,'*':2,'/':2}。从左到右扫描。eval()在安全环境下可用但不适用于OJ——学会手写才是目的。注意除法向零截断——Python的//对负数向下取整，需要用int(a/b)。"},
    {"nq":"NQ131","acw":830,"title":"单调栈",
     "story":"\"找每个数左边第一个比它小的数——暴力O(n²)太慢。\"小华说，\"单调栈——维护一个单调递增的栈。遍历每个数时，把栈中≥它的数都弹掉（因为它们不会再成为任何后续数的答案）。弹完之后栈顶就是答案，然后当前数入栈。每个数最多入栈一次出栈一次——均摊O(n)。单调性把O(n²)降到O(n)！\"",
     "input":"第一行N。第二行N个整数。","output":"每个数左边第一个比它小的数（没有输出-1）。",
     "sample_in":"5\n3 4 2 7 5","sample_out":"-1 3 -1 2 2","constraint":"1 ≤ N ≤ 100000",
     "sol":"维护单调递增栈：遍历每个数，while栈非空且栈顶≥当前数则pop()。弹出结束后栈顶就是答案。当前数入栈。每个数入栈1次出栈1次——均摊O(n)。单调栈利用'大数再也不会被需要'的洞察来去掉无用信息。",
     "tip":"单调栈的变种：找右边第一个大的（从右往左+单调递减），找左边第一个大的（从左到右+单调递减）。记模板不如理解核心：'弹出永远不会用到的元素'。Python: while stack and stack[-1]>=x: stack.pop()。"},
    {"nq":"NQ132","acw":154,"title":"滑动窗口",
     "story":"\"长度为k的窗口在数组上从左滑到右——输出每个窗口的最小值和最大值。\"小栋说，\"暴力每个窗口O(k)总O(n×k)太慢。\"小华回答：\"单调队列！用双端队列维护窗口内的最小值候选。队头是当前窗口的最小值下标，当队头滑出窗口时弹出，当新元素比队尾更小时——队尾永无翻身之日，弹掉。O(n)时间解决。这是单调队列最经典的应用！\"",
     "input":"第一行n,k。第二行n个整数。","output":"第一行所有窗口最小值。第二行所有窗口最大值。",
     "sample_in":"8 3\n1 3 -1 -3 5 3 6 7","sample_out":"-1 -3 -3 -3 3 3\n3 3 5 5 6 7","constraint":"1 ≤ n ≤ 10⁶, 1 ≤ k ≤ n",
     "sol":"单调队列维护窗口最值。最小值：维护递增队列，队头存窗口最小值下标。每次新元素x到来：while队尾值≥x则pop_back（队尾不会再成为最小值），然后push_back当前下标。if队头下标<窗口左边界则pop_front。队头=当前窗口最小值。最大值类似（维护递减队列）。O(n)。",
     "tip":"Python用collections.deque——O(1)的popleft()和pop()。队尾弹出while q and arr[q[-1]]>=x: q.pop()。理解单调队列的本质：维护一个'永远单调'的双端候选集。这是滑动窗口问题的终极答案。"},
    {"nq":"NQ133","acw":831,"title":"KMP字符串",
     "story":"\"字符串匹配——模式串P在文本串T中找所有出现位置。暴力匹配O(n×m)太慢。\"小华打开白板，\"KMP算法——预处理next数组，利用已经匹配的信息避免重复比较。next[i]=P[0..i-1]的最长公共前后缀长度。匹配时如果失配，j跳到next[j]——不需要回到最初的i+1。时间O(n+m)。这是算法课上最优雅的设计之一。\"",
     "input":"第一行n和模式串P，第二行m和文本串T。","output":"所有匹配位置的起始下标（0-indexed）。",
     "sample_in":"3\naba\n5\nababa","sample_out":"0 2","constraint":"1 ≤ n ≤ 10⁵, 1 ≤ m ≤ 10⁶",
     "sol":"KMP两步骤：1)求next数组——i从1开始，j=next[i-1]；while j>0且P[i]!=P[j]则j=next[j-1]；若P[i]==P[j]则j++；next[i]=j。2)匹配——i遍历T,j跟踪P；while j>0且T[i]!=P[j]则j=next[j-1]；若T[i]==P[j]则j++；若j==n则找到匹配。Python的P in T或find()底层用高效算法但理解KMP原理是理解字符串算法的基石。",
     "tip":"next数组=失配时跳转的'记忆'——利用模式串自身的前后缀重复避免回溯。KMP保证了每个字符最多被比较两次。Python: T.find(P)一行，但手写KMP理解'失配跳转'的智慧是进阶算法的必修课。"},
    {"nq":"NQ134","acw":839,"title":"模拟堆",
     "story":"\"最后一个数据结构——堆。\"小华说，\"小根堆：父节点≤子节点。插入：放在末尾然后向上冒泡(up)。删除堆顶：把最后一个元素移到堆顶然后向下沉降(down)。用数组模拟完全二叉树：节点i的父节点=i/2，左子=2i，右子=2i+1。堆是优先队列的底层——Dijkstra、Huffman编码、堆排序都离不开它。\"",
     "input":"第一行n。然后n行：I x(插入)、PM(输出最小)、DM(删除最小)、D k(删除第k个插入)、C k x(修改第k个插入为x)。","output":"按操作输出。",
     "sample_in":"8\nI 2\nI 1\nPM\nDM\nD 1\nC 2 8\nI 3\nPM","sample_out":"1\n3","constraint":"1 ≤ n ≤ 100000",
     "sol":"数组模拟小根堆：h[i]存值，size存当前堆大小。down(u): 找u和两子中最小的，若子更小则交换并递归down。up(u): 若u<父节点则交换并递归up。插入：h[++size]=x; up(size)。删除堆顶：h[1]=h[size--]; down(1)。支持随机删除需额外维护ph[k]（第k个插入在堆中位置）和hp[i]（堆位置i对应的插入编号）。",
     "tip":"Python用heapq：heappush/ heappop/ heapify。但竞赛中常需要支持随机删除修改——需要手写堆+位置映射。理解堆的up/down操作是理解所有优先队列变种（d-ary堆、fib堆、配对堆）的基础。数组下标从1开始方便计算父子。"},
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
body{font-family:"PingFang SC","Hiragino Sans GB","Noto Serif CJK SC","STSong",serif;font-size:9.5pt;line-height:1.7;color:#222;string-set:chapter"第12章 结构的魔力——基础数据结构"}
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
    parts.append('<div class="chapter-title">结构的魔力</div>')
    parts.append('<div class="chapter-subtitle">基础数据结构 · 8题 · C++ &amp; Python 双语对照</div>')
    parts.append('<div class="preface">')
    parts.append('<p>小鲁已经学会了不少算法技巧——排序、二分、前缀和、双指针。但小华告诉他：\"真正的程序性能瓶颈往往不在算法，而在<strong>数据结构</strong>。选对数据结构——你的代码可以快100倍。栈来处理后进先出，队列来处理先进先出，单调栈来找下一个更大元素，滑动窗口用单调队列，字符串匹配用KMP，优先队列用堆……本章8道题，每一题都是一个数据结构选择的经典案例。</p>')
    parts.append('<h3>本章角色</h3>')
    parts.append('<p>🧑‍🎓 <strong>小鲁</strong>（进阶者）· 从数组迈入抽象数据结构——栈/队列/堆/KMP</p>')
    parts.append('<p>🧠 <strong>小华</strong>（算法队长）· 白板上画出KMP的next数组跳转、堆的up/down操作</p>')
    parts.append('<p>🏗️ <strong>小栋</strong>（工程师）· \"单调队列求滑动窗口最值\"——真实大数据场景的最优解</p>')
    parts.append('</div>')
    parts.append('<div class="knowledge-box"><div class="k-title">🏗️ 八大基础数据结构速查</div><ul>')
    parts.append('<li><strong>单链表：</strong>数组模拟——e[],ne[],head,idx。全部操作O(1)</li>')
    parts.append('<li><strong>栈/队列：</strong>数组+指针。Python: list=栈, deque=队列</li>')
    parts.append('<li><strong>单调栈：</strong>维护单调性的栈——找左右第一个更小/大值。均摊O(n)</li>')
    parts.append('<li><strong>单调队列：</strong>维护单调性的双端队列——滑动窗口最值。O(n)</li>')
    parts.append('<li><strong>KMP：</strong>next数组+失配跳转——字符串匹配O(n+m)</li>')
    parts.append('<li><strong>堆：</strong>完全二叉树+up/down——优先队列O(log n)插入删除</li></ul></div>')

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
    parts.append('<li><strong>数组模拟数据结构：</strong>链表/栈/队列/堆都可以用数组+下标模拟——O(1)操作且更缓存友好</li>')
    parts.append('<li><strong>单调栈/单调队列：</strong>利用单调性排除无用元素——O(n²)→O(n)的关键技术</li>')
    parts.append('<li><strong>KMP：</strong>利用自身前后缀重复——字符串匹配O(n+m)。理解失配跳转的智慧</li>')
    parts.append('<li><strong>堆：</strong>完全二叉树+up/down——优先队列O(log n)。是Dijkstra/Huffman/堆排序的基础</li>')
    parts.append('</ul></div>')
    parts.append('<div class="chapter-end">— 第12章完 · 共8题 · 自强不息 —</div>')

    html=f"""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"><title>第12章 结构的魔力</title><style>{CSS}</style></head><body>{chr(10).join(parts)}</body></html>"""
    out=BOOK_ROOT/"textbook"/"chapter12_print.html"
    out.write_text(html,encoding='utf-8')
    print(f"✅ Ch12 dialog version: {len(html)} chars")

if __name__=="__main__":
    build_html()
