#!/usr/bin/env python3
"""第8章 指针与抽象(角色对话版) — 结构体、指针与STL容器"""
import json, re, os, sys
from pathlib import Path
BOOK_ROOT = Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(BOOK_ROOT / 'scripts'))

PROBLEMS = [
    {"nq":"NQ096","acw":16,"title":"替换空格",
     "story":"小鲁在写一个URL编码程序：\"网络请求中的空格必须转成%20……\"他在循环里逐个字符检查。小华走过来说：\"这道题看似简单，但考察的是字符串构建的思维。C++中逐字符拼接用+='\\%20\\'，Python直接用replace(' ','%20')一行搞定。注意——不是打印，而是构建一个新字符串返回。理解'构建新对象'和'原地修改'的区别，是进阶编程的重要分水岭。\"",
     "input":"一个字符串（可能含空格）。","output":"空格替换为%20后的字符串。",
     "sample_in":"We are happy.","sample_out":"We%20are%20happy.","constraint":"0 ≤ 字符串长度 ≤ 1000",
     "sol":"字符串构建：遍历每个字符，是空格就追加%20，否则追原字符。Python: s.replace(' ', '%20')一行。C++: for(char c:str) res+=(c==' '?\"%20\":string(1,c))。注意构建新字符串而非原地修改。",
     "tip":"Python的replace()返回新字符串（不可变性）。C++的std::string支持+=拼接。这道题也是理解Python字符串不可变性的好例子——所有的'修改'其实都是'创建新版'。"},
    {"nq":"NQ097","acw":17,"title":"从尾到头打印链表",
     "story":"小鲁第一次接触链表：\"这些节点通过next指针连在一起——只能从头沿着指针走到尾，不能反向走。那怎么才能从尾到头打印呢？\"小华说：\"聪明的做法——先遍历链表把值存到数组里，然后翻转数组输出。Python一行arr[::-1]翻转。栈的LIFO（后进先出）特性天然适合'反向输出'——这个思维后续会用在表达式求值、括号匹配等场景。\"",
     "input":"链表节点值序列，以-1结束。","output":"从尾到头的节点值，每行一个。",
     "sample_in":"1 2 3 -1","sample_out":"3\n2\n1","constraint":"链表长度 ≤ 1000",
     "sol":"先遍历链表收集值→翻转数组→输出。本质是用数组模拟栈（先入后出）。Python: arr[::-1]翻转。C++: reverse(res.begin(),res.end())。如果面试要求不用额外空间，可以递归（利用函数调用栈天然的后进先出）。",
     "tip":"Python翻转：arr[::-1]（切片）或arr.reverse()（原地）。链表是基础数据结构中最重要的一种——理解指针/引用的跳转模型是理解所有链式结构（树、图）的前提。"},
    {"nq":"NQ098","acw":20,"title":"用两个栈实现队列",
     "story":"\"栈是后进先出（LIFO），队列是先进先出（FIFO）——怎么用两个栈模拟一个队列？\"小栋把这个经典面试题抛给了小鲁。小华在纸上画起来：\"第一个栈负责push（入队），第二个栈负责pop（出队）。当需要pop时，如果第二个栈为空，就把第一个栈的所有元素倒进第二个栈——顺序自然就反过来了。这就是计算机科学中最巧妙的设计模式之一。\"",
     "input":"一系列操作指令（push x / pop / empty）。","output":"对pop操作输出弹出的值。",
     "sample_in":"push 1\npush 2\npop\npush 3\npop\npop\nempty","sample_out":"1\n2\n3\nempty!","constraint":"操作数 ≤ 100",
     "sol":"双栈模拟队列：stack1负责push，stack2负责pop。pop时若stack2为空则将stack1全部倒入stack2（翻转顺序）。时间复杂度：每个元素最多入栈2次出栈2次，均摊O(1)。这是理解\"均摊分析\"的经典案例。",
     "tip":"Python用list作栈：append()=push, pop()=pop。两个list分别模拟两个栈。虽然Python有collections.deque，但理解手写实现比调用库更重要——面试常考题。"},
    {"nq":"NQ099","acw":21,"title":"斐波那契数列(类)",
     "story":"\"这次我们用面向对象的方式实现斐波那契！\"小华说，\"定义一个类/结构体，用成员变量存储状态。C++的class或struct都可以——区别是struct默认public，class默认private。Python的class简单直观。注意N=39时斐波那契数已经超过6千万，C++要用long long存储。\"",
     "input":"一个整数n。","output":"第n项斐波那契数。",
     "sample_in":"5","sample_out":"5","constraint":"0 ≤ n ≤ 39",
     "sol":"用类封装：C++ class Solution { public: int Fibonacci(int n) {...} }。递推法O(n)，a,b=b,a+b模式。n≤39时int够用（F(39)≈6.3×10⁷＜2³¹）。n≥40需long long。",
     "tip":"Python的类不需要声明成员变量类型——构造函数__init__中直接赋值。C++的struct和class唯一区别是默认访问权限。此题的核心是理解\"将算法封装成类的方法\"——OO思想的萌芽。"},
    {"nq":"NQ100","acw":35,"title":"反转链表",
     "story":"\"把链表反转——1→2→3→null变成3→2→1→null。\"小华在白板上画箭头，\"关键操作：把每个节点的next指针指向前一个节点。你需要三个指针——prev（前一个）、curr（当前）、next（下一个，暂存防止断链）。每次迭代：保存下一个→当前指向prev→prev和curr前移。\"小鲁试了三遍才理解——\"原来指针重新定向这么容易出错，一步顺序都不能乱！\"",
     "input":"链表节点值序列，以-1结束。","output":"反转后的链表节点值，每行一个。",
     "sample_in":"1 2 3 -1","sample_out":"3\n2\n1","constraint":"链表长度 ≤ 1000",
     "sol":"迭代反转：prev=null, curr=head; while(curr): next=curr->next; curr->next=prev; prev=curr; curr=next。三指针法——prev(已反转部分)、curr(当前)、next(暂存)。注意顺序：必须先保存next再改curr->next，否则链表就断了。",
     "tip":"反转链表是所有链表操作的基础——合并链表、回文链表、环形链表……都建立在对指针重定向的理解之上。Python虽然没有指针，但用list模拟链表时理解原理同样重要。"},
    {"nq":"NQ101","acw":36,"title":"合并两个排序链表",
     "story":"\"现在有两个已经从小到大排好序的链表——把它们合并成一个排好序的链表。\"小华说，\"这就是归并排序中的'归并'步骤。用一个虚拟头节点dummy简化边界处理，然后比较l1和l2的当前值，较小的接入新链表。\"小鲁恍然：\"这就像两叠从小到大排好的扑克牌——每次比较各自最上面那张，小的拿出来放到新牌堆。\"",
     "input":"两行，每行链表节点值序列（以-1结束）。","output":"合并后链表节点值，空格分隔。",
     "sample_in":"1 3 5 -1\n2 4 6 -1","sample_out":"1 2 3 4 5 6","constraint":"链表长度 ≤ 1000",
     "sol":"双指针归并：dummy头简化逻辑，tail跟随。每次比较l1->val和l2->val，较小的接入tail->next，tail后移。最后把剩余链表接入。时间O(n+m)，空间O(1)。Python用list模拟：while i<len(a) and j<len(b)比较a[i]和b[j]。",
     "tip":"用dummy头节点是链表题的常用技巧——避免处理空链表这种边界情况。合并是归并排序(merge sort)的核心操作——后续会学到完整的归并模板。"},
    {"nq":"NQ102","acw":862,"title":"三元组排序",
     "story":"\"给你N个三元组(x,y,z)，按x从小到大排序——这就是结构体排序的经典题。\"小华说，\"C++中定义一个struct Triple{int x; double y; string z;}，然后sort+自定义比较函数。Python更优雅——用list of tuples，sorted(arr, key=lambda t: t[0])一行排序。这就是为什么Python在数据处理领域如此流行——一行lambda替代C++十几行代码。\"",
     "input":"第一行N，然后N行每行三个值。","output":"按x升序输出三元组（y保留2位小数）。",
     "sample_in":"3\n1 3.5 abc\n2 1.2 def\n1 2.8 ghi","sample_out":"1 3.50 abc\n1 2.80 ghi\n2 1.20 def","constraint":"1 ≤ N ≤ 100",
     "sol":"结构体/元组排序。C++: struct+sort+cmp；Python: sorted(arr, key=lambda x: x[0])。Python的lambda是匿名函数——快速定义比较逻辑而不需要单独定义函数。理解排序的稳定性（x相同时保持原序）。",
     "tip":"Python: sorted(arr, key=lambda t: t[0])。lambda是Python函数式编程的利器——它就是一个只能写一行表达式的匿名函数。C++可用lambda: [](auto &a, auto &b){return a.x<b.x;}。"},
    {"nq":"NQ103","acw":810,"title":"绝对值",
     "story":"\"定义一个abs函数——但有一个要求：支持int和double两种类型的参数。\"小华说，\"这就是函数重载（Overloading）。C++可以写两个同名的abs函数——C++根据参数类型自动选择正确的版本。Python不需要重载——它是动态类型，同一个函数可以接收任何支持<0和-操作的类型。两种语言的设计哲学差异在这里体现得淋漓尽致。\"",
     "input":"一个整数或浮点数。","output":"其绝对值。",
     "sample_in":"-5","sample_out":"5","constraint":"−10⁹ ≤ x ≤ 10⁹",
     "sol":"C++函数重载：int abs(int x)和double abs(double x)可以共存。编译器根据参数类型自动选择。Python不需要——def abs(x): return -x if x<0 else x就行（鸭子类型）。Python内置abs()已经是多态的。",
     "tip":"C++函数重载的核心：同名不同参。编译器根据参数类型/数量自动匹配。Python通过鸭子类型（duck typing）实现类似效果——只要对象支持所需操作就行。"},
    {"nq":"NQ104","acw":814,"title":"复制数组",
     "story":"\"写个函数把数组a的内容复制到数组b——但要求用函数封装，且复制后b的内容是a的完全副本。\"小华强调，\"C++中数组传参会退化为指针——void copy(int a[], int b[], int size)。Python的list直接b=a[:]或b=a.copy()。但注意Python的浅拷贝陷阱——如果list里嵌套了list，需要用copy.deepcopy。\"",
     "input":"第一行n和size，第二行n个数。","output":"复制后的数组（空格分隔）。",
     "sample_in":"5 3\n1 2 3 4 5","sample_out":"1 2 3","constraint":"1 ≤ size ≤ n ≤ 1000",
     "sol":"数组复制函数：遍历赋值b[i]=a[i]。C++用for循环或memcpy，Python用切片a[:]（浅拷贝）。理解浅拷贝vs深拷贝——对于int这种不可变对象，浅拷贝安全；对于嵌套list需要用copy.deepcopy。",
     "tip":"Python切片a[:]创建新列表——最常用的复制方式。list.copy()和list(a)也创建浅拷贝。C++的memcpy是原始内存复制——对非POD类型不安全，现代C++推荐std::copy。"},
    {"nq":"NQ105","acw":816,"title":"数组翻转",
     "story":"\"最后一道——把数组的前size个元素翻转。\"小栋说。小华点头：\"这可以验证你对数组操作、函数传参和对称交换的理解。标准做法是从两端向中间交换——arr[0]和arr[size-1]交换，arr[1]和arr[size-2]交换……直到中间相遇。Python用arr[:size][::-1]切片翻转，C++用reverse或手写交换循环。\"",
     "input":"第一行n和size，第二行n个数。","output":"翻转前size个元素后的数组。",
     "sample_in":"5 3\n1 2 3 4 5","sample_out":"3 2 1 4 5","constraint":"1 ≤ size ≤ n ≤ 1000",
     "sol":"部分翻转：for i in range(size//2): swap(arr[i], arr[size-1-i])。只交换前size个元素，后面的不动。时间O(size/2)，空间O(1)。Python用arr[:size]=arr[size-1::-1]结合切片赋值。",
     "tip":"Python切片翻转arr[::-1]最简洁但创建新列表。原地翻转用reverse()或手写交换。理解'对称交换'是理解更多高级翻转（旋转、循环移位）的基础。"},
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
body{font-family:"PingFang SC","Hiragino Sans GB","Noto Serif CJK SC","STSong",serif;font-size:9.5pt;line-height:1.7;color:#222;string-set:chapter"第8章 指针与抽象——结构体、指针与STL容器"}
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
    parts.append('<div class="chapter-title">指针与抽象</div>')
    parts.append('<div class="chapter-subtitle">结构体、指针与STL容器 · 10题 · C++ &amp; Python 双语对照</div>')
    parts.append('<div class="preface">')
    parts.append('<p>小鲁已经掌握了函数和递归。但小华告诉他：\"真正的工程代码很少只有简单的int和数组——你需要<strong>结构体</strong>把多个数据捆在一起，需要<strong>指针</strong>让数据之间产生链接，需要<strong>标准容器</strong>处理复杂的数据组织需求。\"小鲁深吸一口气：\"所以……编程世界才刚刚开始展开？\"</p>')
    parts.append('<p>本章10道题从三个角度切入：<strong>链表基础操作</strong>（NQ096-101）——替换空格到链表合并，学会用指针/引用操作链式结构；<strong>结构体与排序</strong>（NQ102）——C++ struct vs Python tuple，lambda vs 比较函数；<strong>函数重载与数组操作</strong>（NQ103-105）——多态思维和大数组处理。学完本章，你将从\"会写代码\"升级到\"理解编程语言的设计哲学\"。</p>')
    parts.append('<h3>本章角色</h3>')
    parts.append('<p>🧑‍🎓 <strong>小鲁</strong>（初学者）· 第一次接触指针和链表，从\"为什么需要这个\"到\"原来如此巧妙\"</p>')
    parts.append('<p>🧠 <strong>小华</strong>（算法高手）· 用两个栈实现队列、反转链表三指针——经典面试题的活字典</p>')
    parts.append('<p>🏗️ <strong>小栋</strong>（工程师）· 用\"合并两叠排序好的扑克牌\"把归并思想讲得生动易懂</p>')
    parts.append('<p>🏛️ <strong>小嘉</strong>（校主精神）· 阐释抽象的力量：\"抽象不是复杂度，抽象是管理的艺术\"</p>')
    parts.append('</div>')
    parts.append('<div class="knowledge-box"><div class="k-title">🔗 C++ vs Python 结构体/容器对比</div><ul>')
    parts.append('<li><strong>结构体/类：</strong>C++ struct/class → Python class/namedtuple/dataclass</li>')
    parts.append('<li><strong>链表：</strong>C++指针操作 → Python用list模拟（重在学习原理）</li>')
    parts.append('<li><strong>栈/队列：</strong>C++ stack/queue → Python list/deque</li>')
    parts.append('<li><strong>函数重载：</strong>C++同名不同参 → Python鸭子类型天然多态</li>')
    parts.append('<li><strong>排序：</strong>C++ sort+cmp → Python sorted+lambda</li></ul></div>')

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
    parts.append('<li><strong>链表五操作：</strong>遍历、反向输出、反转、合并、两栈模拟队列——每个都是面试高频题</li>')
    parts.append('<li><strong>三指针法：</strong>prev/curr/next——反转链表的标准模板，一步顺序都不能乱</li>')
    parts.append('<li><strong>dummy头节点：</strong>合并链表时用虚拟头简化边界——链表题的通用技巧</li>')
    parts.append('<li><strong>结构体排序：</strong>C++ struct+sort+cmp vs Python tuple+lambda——一行lambda替代十几行C++</li>')
    parts.append('<li><strong>函数重载vs鸭子类型：</strong>C++编译期多态 vs Python运行期多态——两种语言哲学的核心差异</li>')
    parts.append('<li><strong>厦大精神：</strong>自强不息。指针和链表是CS专业的标志——突破这道坎，你就真正进入了计算机科学的世界</li>')
    parts.append('</ul></div>')
    parts.append('<div class="chapter-end">— 第8章完 · 共10题 · 自强不息</div>')

    html=f"""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"><title>第8章 指针与抽象</title><style>{CSS}</style></head><body>{chr(10).join(parts)}</body></html>"""
    out=BOOK_ROOT/"textbook"/"chapter08_print.html"
    out.write_text(html,encoding='utf-8')
    print(f"✅ Ch8 dialog version: {len(html)} chars")

if __name__=="__main__":
    build_html()
