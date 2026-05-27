#!/usr/bin/env python3
"""第4章 数据的容器——数组与线性存储 (增强版)"""
import json, re, os, sys
from pathlib import Path
BOOK_ROOT = Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(BOOK_ROOT / 'scripts'))

# Problem data
PROBLEMS = [
    {"nq":"NQ043","acw":737,"title":"数组替换",
     "desc":"小鲁学习了数组。给定一个长度为10的数组，将其中所有小于等于0的元素替换为1，然后输出整个数组。",
     "input":"10行，每行一个整数。","output":"10行，每行\"X[i] = Y\"。",
     "sample_in":"0\n-5\n63\n-8\n0\n1\n2\n-100\n50\n200","sample_out":"X[0] = 1\nX[1] = 1\nX[2] = 63\n...","constraint":"−10⁹ ≤ 值 ≤ 10⁹",
     "sol":"遍历数组，如果元素≤0则替换为1。用下标循环或for-each+索引。这是数组最基础的操作模式：读入→判断→输出。注意C++中数组用int arr[10]或vector<int>，Python用list。",
     "tip":"Python的enumerate(arr)返回(index, value)元组，可以同时获取索引和值。C++的for(int i=0;i<10;i++)是经典模式。数组索引从0开始——这是初学者最易出错的地方。"},
    {"nq":"NQ044","acw":738,"title":"数组填充",
     "desc":"给定一个整数V，构造一个长度为10的数组，第0个元素是V，此后每个元素是前一个的两倍。",
     "input":"一个整数V。","output":"10行，每行\"N[i] = X\"。",
     "sample_in":"1","sample_out":"N[0] = 1\nN[1] = 2\nN[2] = 4\nN[3] = 8\n...","constraint":"−10⁴ ≤ V ≤ 10⁴",
     "sol":"递推生成数组：arr[0]=V, arr[i]=arr[i-1]*2。Python用列表推导[v*(2**i) for i in range(10)]。这是递推思想的入门——每个新值由前一个值计算得出。",
     "tip":"Python列表推导一行生成整个数组。C++中1<<i等价于2^i（位移运算）。注意V为负数时，乘2后的结果呈负增长。"},
    {"nq":"NQ045","acw":739,"title":"数组选择",
     "desc":"读取100个浮点数。对于每个小于等于10的数，按格式输出它在数组中的位置和值。",
     "input":"100行（或一行多个），每行一个浮点数。","output":"对每个≤10的数，输出\"A[i] = X\"（保留1位小数）。",
     "sample_in":"0\n-5\n63\n8.5\n100\n...","sample_out":"A[0] = 0.0\nA[1] = -5.0\nA[3] = 8.5\n...","constraint":"−10⁶ ≤ 值 ≤ 10⁶",
     "sol":"遍历100次读入，条件判断≤10则输出。流式处理：不需要把100个数都存下来，读一个判断一个输出一个。这种思维在处理大数据时非常重要——能省内存就省内存。",
     "tip":"Python格式化：f\"A[{i}] = {x:.1f}\"。C++用printf(\"A[%d] = %.1f\\n\", i, x)。条件判断用<=，注意浮点数比较的精度。"},
    {"nq":"NQ046","acw":743,"title":"数组中的行",
     "desc":"给定一个12×12的二维数组。读取行号L和操作类型T（'S'求和或'M'求平均），计算第L行所有元素的和或平均值。这是二维数组行操作的标准模板。",
     "input":"第一行L(0-11)。第二行T('S'或'M')。接下来144个浮点数（12×12矩阵）。",
     "output":"结果保留1位小数。","sample_in":"2\nS\n(144个浮点数...)","sample_out":"(第2行之和)","constraint":"矩阵元素−10⁶到10⁶",
     "sol":"双层循环遍历矩阵：外层for i in range(12)控制行，内层for j in range(12)控制列。当i==L时累加。如果T=='M'求平均则除以12.0。这种行列遍历模式贯穿所有多维数组题目。",
     "tip":"双层循环是二维数组的标准遍历方式。C++中矩阵用double M[12][12]或vector<vector<double>>。Python嵌套列表：[[0]*12 for _ in range(12)]。"},
    {"nq":"NQ047","acw":740,"title":"数组变换",
     "desc":"给定一个20个整数的数组。将数组前后对称位置互换（第0个和第19个交换，第1个和第18个交换...），输出变换后的数组。",
     "input":"20个整数。","output":"20行，每行\"N[i] = X\"。",
     "sample_in":"0\n1\n2\n...\n19","sample_out":"N[0] = 19\nN[1] = 18\n...","constraint":"−10⁹ ≤ 值 ≤ 10⁹",
     "sol":"对称交换：arr[i] ↔ arr[19-i]，只需循环10次（i从0到9）。Python用切片arr[::-1]一行翻转。理解算法和用库函数的区别——Python翻转一行，C++需要手写交换。",
     "tip":"Python的arr[::-1]是最简洁的数组翻转方式。C++用std::reverse()或手写swap循环。Python的切片非常强大但消耗额外内存（创建新列表）。"},
    {"nq":"NQ048","acw":741,"title":"斐波那契数列",
     "desc":"斐波那契数列前两项是0和1，之后每一项都是前两项之和。给定N（1≤N≤60），输出前N项。注意结果可能超过32位int范围！",
     "input":"一个整数N。","output":"一行，空格隔开的N个整数。",
     "sample_in":"5","sample_out":"0 1 1 2 3","constraint":"1 ≤ N ≤ 60",
     "sol":"递推标准模板：a=0, b=1; for i in range(N): output a; a,b = b, a+b。C++需用long long（64位整数），N=60时F(60)≈1.5×10¹²远超int范围。这是动态规划(DP)思想的萌芽——用前面算出的结果推导后面。",
     "tip":"Python自动大整数无需担心溢出。C++千万要用long long！int在N>46时就会溢出。Python的a,b=b,a+b是递推最优雅写法。"},
    {"nq":"NQ049","acw":742,"title":"最小数和它的位置",
     "desc":"给定N和一个包含N个整数的数组，找出数组中的最小值及其位置（如果有多个最小值，输出第一个的位置）。",
     "input":"第一行N。第二行N个整数。","output":"第一行\"Menor valor: X\"。第二行\"Posicao: Y\"（位置从0开始）。",
     "sample_in":"10\n1 2 3 4 -5 6 7 8 9 10","sample_out":"Menor valor: -5\nPosicao: 4","constraint":"1 ≤ N ≤ 1000",
     "sol":"遍历数组维护最小值和位置。Python用min(arr)和arr.index(min_val)一行搞定，但手写循环理解查找逻辑更重要。遍历时记录\"当前看到的最小值\"——这是线性扫描的标准模式。",
     "tip":"Python的min()和.index()组合简洁但需要两次遍历。手写版本一次遍历即可同时找到最小值和位置——效率更高的算法思维。"},
    {"nq":"NQ050","acw":744,"title":"数组中的列",
     "desc":"与NQ046类似，但这次操作的是列。给定列号C和操作类型T，计算12×12矩阵第C列的和或平均值。",
     "input":"第一行列号C。第二行操作类型T。接下来144个浮点数。","output":"结果保留1位小数。",
     "sample_in":"2\nS\n(144个浮点数...)","sample_out":"(第2列之和)","constraint":"同NQ046",
     "sol":"与行操作对称：当内层循环到目标列j==C时累加。行操作和列操作的双重循环结构完全相同，只在判断条件上差一个字母（i==L vs j==C）。这种对称性是理解多维数组遍历的关键。",
     "tip":"对比NQ046：改变的是累加条件。能灵活变换遍历条件是二维数组操作的进阶能力。建议两题对照阅读代码。"},
    {"nq":"NQ051","acw":717,"title":"简单斐波那契",
     "desc":"计算斐波那契数列的第N项。F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2)。本题只输出一项而非前N项，是递推算法的精简变体。",
     "input":"一个整数N。","output":"第N项的值。",
     "sample_in":"4","sample_out":"3","constraint":"0 ≤ N ≤ 60",
     "sol":"与NQ048类似但只输出最后一项。递推直到第N项，不需要存储所有中间结果——O(1)空间复杂度。注意N=0的情况：直接输出0。",
     "tip":"Python:a,b=0,1;for _ in range(n):a,b=b,a+b;print(a)。注意这个循环次数和输出的对应关系——循环n次后a就是第n项。"},
    {"nq":"NQ052","acw":722,"title":"数字序列和它的和",
     "desc":"对于每一对输入的正整数M和N（M<N），输出从M到N的所有整数及它们的和。以读入的M或N≤0为结束标志。",
     "input":"多行，每行两个整数M和N。以M≤0或N≤0结束。","output":"对每对M,N，输出一行所有整数（空格隔开）和\"Sum=X\"。",
     "sample_in":"5 10\n2 3\n0 0","sample_out":"5 6 7 8 9 10 Sum=45\n2 3 Sum=5","constraint":"M,N ≤ 100",
     "sol":"while循环读取，遇到非正数break。确保M≤N（必要时交换），然后for循环输出+累加。这是\"不定长输入\"的经典处理模式：while循环+break。",
     "tip":"Python:for i in range(m,n+1):print(i,end=' ')。注意输出格式——数字间空格隔开，最后跟\" Sum=X\"。C++中cout格式控制比printf更灵活。"},
    {"nq":"NQ053","acw":725,"title":"完全数",
     "desc":"一个数的所有真因子（不含自身）之和等于自身，称为完全数。给定N，输出不超过N的所有完全数。例如6=1+2+3，28=1+2+4+7+14。",
     "input":"一个整数N。","output":"每行一个完全数。",
     "sample_in":"30","sample_out":"6\n28","constraint":"1 ≤ N ≤ 10⁸",
     "sol":"10⁸以内只有四个完全数：6, 28, 496, 8128。直接判断它们是否≤N即可，不需要枚举计算！这是\"数学知识简化算法\"的经典案例——有时候知道答案比计算答案更高效。",
     "tip":"10⁸以内的完全数是被数学家证明的（欧几里得-欧拉定理）。编程中利用已知数学事实可以大幅简化算法。这是\"先思考，再编码\"的典范。"},
    {"nq":"NQ054","acw":726,"title":"质数",
     "desc":"给定N，输出2到N之间所有的质数（素数）。质数指大于1且只有1和自身两个因子的数。本题是算法优化的入门——同一个问题，不同实现效率差100倍。",
     "input":"一个整数N。","output":"每行一个质数。",
     "sample_in":"10","sample_out":"2\n3\n5\n7","constraint":"2 ≤ N ≤ 10⁶",
     "sol":"朴素方法：对2到N的每个数i，检查2到√i是否有因子。关键优化：j*j<=i作循环条件（只需检查到√i）。时间复杂度从O(n²)降到O(n√n)。如果N很大还可以用埃拉托色尼筛法——\"空间换时间\"思想。",
     "tip":"Python用math.isqrt(i)获得整数平方根。判断条件j*j<=i比j<=sqrt(i)更高效（避免浮点数运算）。这是算法优化的第一课。"},
]

from pygments import highlight
from pygments.lexers import CppLexer, PythonLexer
from pygments.formatters import HtmlFormatter
CPP_FMT = HtmlFormatter(style='vs', noclasses=True)
PY_FMT = HtmlFormatter(style='vs', noclasses=True)

def hl(code, lexer, fmt):
    if not code: return ''
    h = highlight(code, lexer, fmt)
    m = re.search(r'<pre[^>]*>(.*)</pre>', h, re.DOTALL)
    return re.sub(r'<span></span>\n?', '', m.group(1)) if m else code

# Load codes
CODE_CACHE = {}
for d in ['acwing_codes', 'algorithm_basic_codes']:
    for root, dirs, files in os.walk(str(BOOK_ROOT / d)):
        for f in files:
            if f.endswith('.cpp'):
                m = re.search(r'AcWing\s+(\d+)', f)
                if m:
                    with open(os.path.join(root, f)) as fh:
                        CODE_CACHE[int(m.group(1))] = fh.read().strip()

PY_CACHE = {}
for ch in range(1, 17):
    bank_dir = BOOK_ROOT / f'chapter{ch}_bank'
    if bank_dir.exists():
        for d in bank_dir.iterdir():
            if d.is_dir():
                py_file = d / 'Andy.py'
                if py_file.exists():
                    c = py_file.read_text().strip()
                    if len(c) > 20 and not c.startswith('# AcWing'):
                        m = re.search(r'ACW(\d+)', d.name)
                        if m: PY_CACHE[int(m.group(1))] = c

CSS = """@page{size:A4;margin:2.2cm 2cm 2.2cm 2cm;@top-center{content:string(chapter);font-size:7.5pt;color:#999;font-family:"PingFang SC",sans-serif}@bottom-center{content:counter(page);font-size:7.5pt;color:#999}}
body{font-family:"PingFang SC","Hiragino Sans GB","Noto Serif CJK SC","STSong",serif;font-size:9.5pt;line-height:1.7;color:#222;string-set:chapter "第4章 数据的容器——数组与线性存储"}
.chapter-title{text-align:center;font-size:20pt;font-weight:bold;margin:1.5em 0 .1em 0;letter-spacing:3pt}
.chapter-subtitle{text-align:center;font-size:10pt;color:#777;margin-bottom:1.5em;padding-bottom:.8em;border-bottom:1px solid #bbb}
.preface{font-size:10pt;margin-bottom:1.5em;color:#444}.preface p{margin:.3em 0;text-indent:2em}
.preface h3{font-size:11pt;color:#2563eb;margin:1em 0 .3em 0}
.knowledge-box{background:#f0f6ff;border:1pt solid #bdd;border-radius:4px;padding:.7em 1em;margin:.8em 0;font-size:9pt}
.knowledge-box .k-title{font-weight:bold;color:#2563eb;margin-bottom:.3em;font-size:9.5pt}
.knowledge-box p{margin:.2em 0}
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
.chapter-summary h3{font-size:11pt;color:#2563eb;margin:0 0 .5em 0}
.chapter-summary ul{margin:.3em 0;padding-left:1.5em}
.chapter-end{text-align:center;margin-top:3em;font-size:8pt;color:#999}"""

def build_html():
    parts = []

    # Chapter title
    parts.append('<div class="chapter-title">数据的容器</div>')
    parts.append('<div class="chapter-subtitle">数组与线性存储 · 14题 · C++ &amp; Python 双语对照</div>')

    # Chapter introduction
    parts.append('<div class="preface">')
    parts.append('<p>在编程的世界里，单个变量只能存储一个值。当我们需要处理成百上千个数据时——比如全班同学的成绩、一个月的温度记录、一首诗的所有字符——逐一命名变量变得不切实际。<strong>数组（Array）</strong>正是为解决这一问题而诞生的数据结构。</p>')
    parts.append('<p>数组的核心思想非常简单：<strong>连续存储，编号访问</strong>。想象一排编号从0开始的储物柜，每个柜子存放一个数据。通过柜子编号（索引），你可以在O(1)时间内直接访问任意一个柜子里的内容——这是计算机科学中最快的访问方式之一。</p>')
    parts.append('<h3>本章学习目标</h3>')
    parts.append('<p>① 理解数组的连续存储原理和索引访问机制</p>')
    parts.append('<p>② 掌握一维数组的遍历、筛选、变换、翻转、查找五大基础操作</p>')
    parts.append('<p>③ 入门二维数组的行列遍历模式</p>')
    parts.append('<p>④ 通过斐波那契数列体会<strong>递推</strong>思想——动态规划(DP)的萌芽</p>')
    parts.append('<p>⑤ 通过质数判定学习<strong>算法优化</strong>——从O(n²)到O(n√n)</p>')
    parts.append('</div>')

    # Knowledge box: C++ array vs Python list
    parts.append('<div class="knowledge-box">')
    parts.append('<div class="k-title">📦 C++数组 vs Python列表：两种设计哲学</div>')
    parts.append('<p><strong>C++原生数组：</strong>定长、类型严格、栈上分配、极高性能。声明int arr[10]时编译器在栈上预留40字节（10×4），访问arr[i]只做一次指针加法。但缺点也很明显：长度编译时确定、不提供越界检查（运行时不安全）。C++的vector弥补了定长缺陷，在堆上动态分配。</p>')
    parts.append('<p><strong>Python列表：</strong>动态扩容、类型灵活、堆上分配、自带越界检查。Python的list本质是一个指针数组，每个元素指向堆上实际对象。这带来了灵活性——可以在运行时任意增删元素，但也牺牲了性能——访问一个int需要两次指针跳转。</p>')
    parts.append('<p><strong>关键差异：</strong>C++中int arr[10]的10个int是连续存放的，CPU缓存友好。Python中[1,2,3]的3个元素是3个独立的对象，不保证连续。理解这种差异有助于你写出高性能代码。</p>')
    parts.append('</div>')

    # Build each problem
    for i, p in enumerate(PROBLEMS):
        pb = ['<div class="problem-block">']
        pb.append(f'<div class="problem-title"><span class="nq">{p["nq"]}</span>{p["title"]}<span class="acw">AcWing {p["acw"]}</span></div>')
        pb.append(f'<div class="problem-desc">{p["desc"]}</div>')
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

        cpp = CODE_CACHE.get(p['acw'], f'// AcWing {p["acw"]}')
        py = PY_CACHE.get(p['acw'], '# Python solution')
        pb.append('<div class="code-dual">')
        pb.append(f'<div class="code-col"><div class="lang-badge">C++</div><pre>{hl(cpp, CppLexer(), CPP_FMT)}</pre></div>')
        pb.append(f'<div class="code-col"><div class="lang-badge">Python</div><pre>{hl(py, PythonLexer(), PY_FMT)}</pre></div>')
        pb.append('</div></div><hr class="section-divider">')
        parts.append('\n'.join(pb))

    # Chapter summary
    parts.append('<div class="chapter-summary">')
    parts.append('<h3>📋 本章知识点总结</h3>')
    parts.append('<ul>')
    parts.append('<li><strong>数组的五大操作：</strong>遍历(iterate)、筛选(filter)、变换(transform)、翻转(reverse)、查找(search)</li>')
    parts.append('<li><strong>C++数组：</strong>int arr[n]（栈）、vector&lt;int&gt;（堆）、array&lt;int,n&gt;（栈+STL包装）</li>')
    parts.append('<li><strong>Python列表：</strong>动态扩容、负数索引、切片arr[::-1]、列表推导[x for x in arr if cond]</li>')
    parts.append('<li><strong>二维数组遍历：</strong>双层for循环——外层行(i)、内层列(j)。行列操作对称，只需改变判断条件</li>')
    parts.append('<li><strong>递推思想（DP萌芽）：</strong>斐波那契数列——每个新值由前两个已知值计算，不需要回溯所有历史</li>')
    parts.append('<li><strong>算法优化第一课：</strong>质数判定——从O(n²)穷举到O(n√n)开方优化。同样的结果，不同效率</li>')
    parts.append('<li><strong>数学知识助力：</strong>完全数——10⁸以内只有4个。数学事实可以大幅简化编程工作量</li>')
    parts.append('</ul>')
    parts.append('</div>')

    parts.append('<div class="chapter-end">— 第4章完 · 共14题 —</div>')

    html = f"""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"><title>第4章 数据的容器</title><style>{CSS}</style></head><body>{chr(10).join(parts)}</body></html>"""
    out = BOOK_ROOT / "textbook" / "chapter04_print.html"
    out.write_text(html, encoding='utf-8')
    print(f"✅ Chapter 4 enhanced: {out} ({len(html)} chars)")
    return out

if __name__ == "__main__":
    build_html()
