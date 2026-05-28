#!/usr/bin/env python3
"""第7章 模块化的力量(角色对话版) — 函数、递归与库的威力"""
import json, re, os, sys
from pathlib import Path
BOOK_ROOT = Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(BOOK_ROOT / 'scripts'))

PROBLEMS = [
    {"nq":"NQ083","acw":804,"title":"n的阶乘",
     "story":"小鲁正对着一道数学题发愁：\"5! = 5×4×3×2×1 = 120，这个我还能手算……但是如果要算10!怎么办？\"小华拉过键盘：\"函数就是做这个的！你把'计算阶乘'封装成一个fact(n)函数——每次需要算阶乘的时候调用它就行。这就叫'封装'。Python直接import math; math.factorial(10)一行搞定，但理解函数定义与调用的关系，比直接用库更重要。\"",
     "input":"共一行，包含一个整数n。","output":"共一行，包含一个整数表示n的阶乘的值。",
     "sample_in":"3","sample_out":"6","constraint":"1 ≤ n ≤ 10",
     "sol":"阶乘n! = 1×2×...×n。用for循环累乘。C++需定义int fact(int n)函数，Python可以def fact(n)或直接用math.factorial()。int在n≤10范围内安全（最大10! = 3,628,800）。",
     "tip":"Python的math.factorial()使用高效的C实现。手写版关键是用result=1初始化然后for i in range(1,n+1):result*=i。初始化是初学者最常犯的bug——用0而不是1会导致结果永远是0。"},
    {"nq":"NQ084","acw":805,"title":"x和y的最大值",
     "story":"\"写个函数，输入两个数，返回较大的那个。\"小栋对小鲁说。\"这还用函数？直接if判断不就行了。\"小鲁反驳。小华摇摇头：\"在大的程序里，你可能要在几十个地方都用max——每次都写if多麻烦，而且如果max逻辑改了（比如要支持更多参数），你要改几十处。有了max(x,y)函数，改一次，处处生效。这就是函数的第二个价值：代码复用。\"",
     "input":"一行，两个整数x和y。","output":"一个整数，较大者。",
     "sample_in":"3 5","sample_out":"5","constraint":"−100 ≤ x,y ≤ 100",
     "sol":"函数封装max逻辑：if x>y return x else return y。C++用int max(int x,int y)，Python用def my_max(x,y): return x if x>y else y。理解函数签名（参数名+类型+返回值）是设计函数的第一步。",
     "tip":"C++的三元运算符：return x>y?x:y。Python: return x if x>y else y。两种语法看似不同，语义完全一样——条件→值1→值2。"},
    {"nq":"NQ085","acw":808,"title":"最大公约数",
     "story":"小嘉从南洋经商归来，带回了一道古老的问题：\"两个正整数，找到能同时整除它们的最大数——这就是《九章算术》里的'更相减损术'，也就是欧几里得算法。\"小华在屏幕上写道：\"gcd(a,b)=gcd(b,a%b)，一直递归到b=0时返回a。这是两千年前的算法，至今仍然是求GCD最高效的方法。Python的math.gcd()内部用的就是它。\"",
     "input":"一行，两个整数a和b。","output":"一个整数，a和b的最大公约数。",
     "sample_in":"12 18","sample_out":"6","constraint":"1 ≤ a,b ≤ 10⁹",
     "sol":"欧几里得算法：while b: a,b = b,a%b; return a。Python的a,b=b,a%b一行完成交换和取余。C++用while(b){int t=a%b;a=b;b=t;}。时间复杂度O(log min(a,b))——对10⁹只需约30次运算。",
     "tip":"Python一行gcd：while b: a,b = b, a%b。这个\"元组解包+赋值\"的写法是Python递推算法的标志性代码。math.gcd()底层是C实现，更快但手写更理解原理。"},
    {"nq":"NQ086","acw":811,"title":"交换数值",
     "story":"\"交换两个变量的值——这是编程的'hello world'动作。\"小华说，\"C++需要传引用（&）或者用指针，否则函数内的交换不会影响外部变量。Python的函数参数是'传对象引用'——列表可变会受影响，整数不可变不会。但Python有更优雅的方式：a,b = b,a——直接元组解包交换，不需要函数！\"",
     "input":"一行，两个整数x和y。","output":"一行，交换后的两个整数（用空格分开）。",
     "sample_in":"3 5","sample_out":"5 3","constraint":"−10⁹ ≤ x,y ≤ 10⁹",
     "sol":"C++的难点：值传递vs引用传递。void swap(int &a,int &b){int t=a;a=b;b=t;}中的&是关键——没有&则函数内的交换不影响调用处。Python直接用x,y=y,x一行交换，无需定义函数。理解这个差异是理解两种语言参数传递模型的关键。",
     "tip":"Python的a,b=b,a是元组解包——等式右边先创建元组(b,a)，然后解包赋值给a和b。这是Python最优雅的语法糖之一。C++用std::swap(a,b)最简单。"},
    {"nq":"NQ087","acw":812,"title":"打印数字",
     "story":"\"我想写一个函数print_array(arr, size)，传入一个数组和它的大小，自动打印所有元素。\"小鲁跃跃欲试。小华说：\"C++中数组作为参数时退化为指针，必须显式传size。Python的list自带长度信息，不需要额外参数。这个差异体现了两种语言的设计哲学：C追求零开销，Python追求方便安全。\"",
     "input":"第一行n和size，第二行n个数。","output":"打印前size个元素，空格分隔。",
     "sample_in":"5 3\n1 2 3 4 5","sample_out":"1 2 3","constraint":"1 ≤ size ≤ n ≤ 1000",
     "sol":"C++数组参数退化为指针——void print(int a[], int size)。必须传size。Python的list自带__len__，for x in arr自动遍历。数组传参是理解C指针与Python引用差异的典型案例。",
     "tip":"C++中int a[]作参数等同于int* a——丢失了长度信息。这就是为什么C风格的数组操作几乎都带size参数。Python没有这个问题——每个list都知道自己的长度。"},
    {"nq":"NQ088","acw":813,"title":"打印矩阵",
     "story":"\"升级了！现在要打印一个二维矩阵。\"小栋把题目升级。小华说：\"C++需要指定第二维的大小——void print(int a[][100], int row, int col)。注意：只有第一维可以省略，第二维必须指定（编译器需要知道每行的大小来做地址计算）。Python就简单多了——list of lists，遍历即打印。\"",
     "input":"第一行row和col，然后row行col列。","output":"按行列格式打印矩阵。",
     "sample_in":"2 3\n1 2 3\n4 5 6","sample_out":"1 2 3\n4 5 6","constraint":"1 ≤ row,col ≤ 100",
     "sol":"C++二维数组参数：void print(int a[][100], int r, int c)。第二维必须指定大小。Python: def print_matrix(mat): for row in mat: print(*row)一键解包输出。",
     "tip":"Python的print(*row)用*解包列表——等价于print(row[0],row[1],row[2])。这是Python打印列表最优雅的写法。C++的二维数组参数中第二维大小是编译期常量限制——动态大小的矩阵需要用vector或动态数组。"},
    {"nq":"NQ089","acw":819,"title":"递归求阶乘",
     "story":"\"之前我们用循环写阶乘——现在用递归！\"小华说，\"递归就是函数自己调用自己。fact(n)=n×fact(n-1)，fact(0)=1。代码只有3行，但理解它需要'递归思维'——假设fact(n-1)已知，你只需要乘上n。\"小鲁试着在纸上展开fact(4)→4×fact(3)→4×3×fact(2)→...→24。\"确实优雅！但感觉比循环多用了空间。\"",
     "input":"一个整数n。","output":"n的阶乘。",
     "sample_in":"4","sample_out":"24","constraint":"0 ≤ n ≤ 10",
     "sol":"递归三板斧：1.基条件if n==0 return 1；2.递归调用fact(n-1)；3.组合结果n*fact(n-1)。递归需要调用栈——每层递归占用栈空间。循环O(1)空间，递归O(n)栈空间——这是递归的代价。",
     "tip":"Python递归深度默认限制1000层（可改）。递归优雅但对深度大的问题可能栈溢出（Stack Overflow——是的，那个著名的程序员问答网站名字就这么来的）。小n用递归，大n用循环。"},
    {"nq":"NQ090","acw":820,"title":"递归求斐波那契数列",
     "story":"\"fib(n) = fib(n-1) + fib(n-2)——多优雅的递归定义！\"小鲁兴奋地写下了递归版的斐波那契。\"但是n=40时我的电脑卡住了！\"小华严肃地说：\"这就是经典的反面教材——朴素的递归斐波那契做了大量重复计算（fib(5)被算了8次！）。解决方法有两种：循环递推或带缓存的递归。Python的@lru_cache装饰器——一行注解，递归变成O(n)，魔法般的效果。\"",
     "input":"一个整数n。","output":"第n项斐波那契数。",
     "sample_in":"5","sample_out":"5","constraint":"0 ≤ n ≤ 60",
     "sol":"朴素递归O(2ⁿ)——指数爆炸。加缓存（Python的@lru_cache或手写字典记录已算过的值）→O(n)。递推循环O(n)+O(1)空间。递归+缓存和递推循环等价——前者自顶向下（Top-down DP），后者自底向上（Bottom-up DP）。",
     "tip":"Python: from functools import lru_cache; @lru_cache(None); def fib(n): return n if n<2 else fib(n-1)+fib(n-2)。@lru_cache是Python动态规划的核武器——加一行注解，任何纯函数的重复计算问题瞬间解决。"},
    {"nq":"NQ091","acw":821,"title":"跳台阶",
     "story":"小鲁在操场上练习跳台阶——每次可以跳1级或2级。\"10级台阶有多少种不同的跳法？\"小华问。小鲁想了想：\"到第n级的跳法=到第n-1级的跳法（跳1级上来）+到第n-2级的跳法（跳2级上来）。这不就是斐波那契数列吗？\"小华笑了：\"没错！这就是为什么递推思维如此重要——表面上不同的问题，底层可能是同一个数学模型。\"",
     "input":"一个整数n。","output":"跳法总数。",
     "sample_in":"4","sample_out":"5","constraint":"1 ≤ n ≤ 15",
     "sol":"f(n)=f(n-1)+f(n-2)，f(1)=1,f(2)=2。和斐波那契的递推公式一样但基条件不同（f(2)=2而非1）。注意n≤15时int足够。Python一行：a,b=1,2;for _ in range(n-1):a,b=b,a+b;print(a)。",
     "tip":"这是最简单的DP入门题。学会识别\"可以从前一步/前两步转移过来\"的模式。这种\"状态转移\"思维将贯穿整个算法学习——背包、最长子序列、编辑距离……本质都是这个框架。"},
    {"nq":"NQ092","acw":822,"title":"走方格",
     "story":"小栋画了一个n×m的网格：\"从(0,0)走到(n,m)，每次只能向右或向下走一步——有多少种不同的走法？\"小鲁兴奋地说：\"这不就是组合数C(n+m, n)吗？总共要走n+m步，选其中n步向右。\"小华补充道：\"对——但如果你想用代码算，递推公式f[i][j]=f[i-1][j]+f[i][j-1]更通用。Python一行math.comb(n+m, n)搞定——标准库的强大之处。\"",
     "input":"一行，两个整数n和m。","output":"走法总数。",
     "sample_in":"2 3","sample_out":"10","constraint":"1 ≤ n,m ≤ 10",
     "sol":"组合数C(n+m, n) = (n+m)! / (n!×m!)。Python: math.comb(n+m, n)一行。递推DP: f[i][j]=f[i-1][j]+f[i][j-1]; f[0][*]=f[*][0]=1。两种思维都正确——前者用数学知识，后者用DP框架。",
     "tip":"Python 3.8+的math.comb(n,k)计算组合数——比手写阶乘除法更安全（避免了整数溢出）。C++中n+m≤20时可用long long存组合数。"},
    {"nq":"NQ093","acw":823,"title":"排列",
     "story":"\"用递归生成1到n的所有排列——这是搜索算法的入门课。\"小华在白板上画出搜索树：\"第1层选第1个数（n种选择），第2层选第2个数（n-1种选择）……一直到选完n个数。每次递归深入一层，用used数组标记哪些数已经被用了。这个回溯框架将贯穿你的整个搜索算法学习——从排列到N皇后，从数独到旅行商问题。\"",
     "input":"一个整数n。","output":"1~n的所有排列，每行一个排列。",
     "sample_in":"3","sample_out":"1 2 3\n1 3 2\n2 1 3\n2 3 1\n3 1 2\n3 2 1","constraint":"1 ≤ n ≤ 9",
     "sol":"DFS回溯：dfs(path, used)，当len(path)==n时输出。每次从未被used标记的数中选一个加入path，递归完成后撤销选择（回溯）。Python的itertools.permutations(range(1,n+1))一行搞定——库函数也是用类似的算法实现的。",
     "tip":"Python: from itertools import permutations; for p in permutations(range(1,n+1)): print(*p)。手写回溯用递归+used数组，itertools用C实现更快。理解回溯框架>会调库——因为库不能解决所有搜索问题。"},
    {"nq":"NQ094","acw":818,"title":"数组排序",
     "story":"\"这一章的最后一道题——写一个函数把数组排序。\"小华说，\"当然Python有sort()，C++有std::sort()，但手写排序算法的意义在于——理解不同排序的思想：选择排序每次选最小的放前面，冒泡排序相邻比较交换，插入排序像整理扑克牌……这些思维训练让你的算法直觉不断提升。\"",
     "input":"第一行n和size，第二行n个数。","output":"排序后的前size个元素。",
     "sample_in":"5 3\n3 1 4 1 5","sample_out":"1 1 3","constraint":"1 ≤ size ≤ n ≤ 1000",
     "sol":"多种排序可选：选择排序（找最小放前面）、冒泡排序（相邻交换）、插入排序（扑克牌式）。复杂度O(n²)对n≤1000足矣。Python: arr.sort()或sorted(arr)一行。C++: sort(arr,arr+n)使用快速排序O(n log n)。",
     "tip":"Python的sort()是Timsort（归并+插入的混合算法），C++的std::sort()是Introsort（快速排序+堆排序的混合）。标准库的排序经过数十年优化——实际开发中绝不要手写排序。"},
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
body{font-family:"PingFang SC","Hiragino Sans GB","Noto Serif CJK SC","STSong",serif;font-size:9.5pt;line-height:1.7;color:#222;string-set:chapter"第7章 模块化的力量——函数、递归与库的威力"}
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
    parts.append('<div class="chapter-title">模块化的力量</div>')
    parts.append('<div class="chapter-subtitle">函数、递归与库的威力 · 12题 · C++ &amp; Python 双语对照</div>')
    parts.append('<div class="preface">')
    parts.append('<p>小鲁已经写了上百行代码了。但他发现一个问题：\"同样的逻辑我写了好几遍——求最大值、算阶乘、交换变量……能不能写一次，到处用？\"小华笑道：\"你终于感受到<strong>函数</strong>的需求了！函数是编程中最基本、最重要的抽象手段——把一段逻辑打包装箱，贴个标签，以后直接叫名字就能用。\"</p>')
    parts.append('<p>本章12道题分三个板块：<strong>函数定义与调用</strong>（NQ083-088）——学会参数传递、返回值、数组传参；<strong>递归思维</strong>（NQ089-093）——函数自己调用自己，基础案例→记忆化优化→回溯搜索；<strong>标准库的威力</strong>——Python的math/lib等内置库让你的代码量减少90%。记住：<strong>写函数的第一原则是</strong>——先看看标准库有没有现成的。</p>')
    parts.append('<h3>本章角色</h3>')
    parts.append('<p>🧑‍🎓 <strong>小鲁</strong>（初学者）· 从\"重复代码\"的痛苦中领悟函数的必要性</p>')
    parts.append('<p>🧠 <strong>小华</strong>（算法高手）· 深入讲解C++引用传递vs Python对象引用，递归vs递推</p>')
    parts.append('<p>🏗️ <strong>小栋</strong>（工程师）· 用网格走方格、跳台阶等实际问题引入DP思维</p>')
    parts.append('<p>🏛️ <strong>小嘉</strong>（校主精神）· 带来《九章算术》的gcd算法，强调数学与编程的千年共鸣</p>')
    parts.append('</div>')
    parts.append('<div class="knowledge-box"><div class="k-title">🧩 函数三大价值 + C++ vs Python 对比</div><ul>')
    parts.append('<li><strong>封装：</strong>把逻辑打包→隐藏细节→只暴露接口。调用者不需要知道内部实现</li>')
    parts.append('<li><strong>复用：</strong>写一次用百次。修改时只改一处</li>')
    parts.append('<li><strong>抽象：</strong>fact(n)比\"从1乘到n\"高一个思考层次——用函数名表达意图</li>')
    parts.append('<li><strong>参数传递：</strong>C++值传递vs引用传递(&)→&使函数能修改外部变量；Python\"传对象引用\"→可变对象（list）可被修改，不可变对象（int）不能</li>')
    parts.append('<li><strong>递归vs递推：</strong>递归自顶向下（优雅但耗栈），递推自底向上（高效但需手动管理状态）</li>')
    parts.append('<li><strong>标准库优先：</strong>math.gcd/factorial/comb, itertools.permutations, @lru_cache——先查库再动手</li></ul></div>')

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
    parts.append('<li><strong>函数三价值：</strong>封装（隐藏细节）、复用（一次编写多次调用）、抽象（更高层次的思考）</li>')
    parts.append('<li><strong>参数传递差异：</strong>C++值vs引用(&)，Python\"传对象引用\"——理解这个差异是写出正确函数的前提</li>')
    parts.append('<li><strong>递归三板斧：</strong>基条件→递归调用→组合结果。注意栈溢出风险和重复计算问题</li>')
    parts.append('<li><strong>@lru_cache：</strong>一行注解将指数级递归变成多项式级——Python动态规划的核武器</li>')
    parts.append('<li><strong>回溯框架：</strong>选→递归→撤销。排列问题是搜索算法的入门课，这个框架贯穿整个算法学习</li>')
    parts.append('<li><strong>标准库优先：</strong>math.gcd/factorial/comb, itertools.permutations, functools.lru_cache——先查库再动手</li>')
    parts.append('</ul></div>')
    parts.append('<div class="chapter-end">— 第7章完 · 共12题 · 自强不息 —</div>')

    html=f"""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"><title>第7章 模块化的力量</title><style>{CSS}</style></head><body>{chr(10).join(parts)}</body></html>"""
    out=BOOK_ROOT/"textbook"/"chapter07_print.html"
    out.write_text(html,encoding='utf-8')
    print(f"✅ Ch7 dialog version: {len(html)} chars")

if __name__=="__main__":
    build_html()
