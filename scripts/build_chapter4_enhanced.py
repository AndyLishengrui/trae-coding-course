#!/usr/bin/env python3
"""第4章 数据的容器(角色对话版) — 小鲁学数组，小华当助教"""
import json, re, os, sys
from pathlib import Path
BOOK_ROOT = Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(BOOK_ROOT / 'scripts'))

PROBLEMS = [
    {"nq":"NQ043","acw":737,"title":"数组替换",
     "story":"小鲁正在写一个数据处理程序，但发现数据里混入了一些负数和零——这些\"脏数据\"会影响后面的计算。\"得想个办法，把不合格的数据统一替换成1……\"小鲁嘀咕着。小华凑过来看了一眼屏幕：\"这不就是数组遍历+条件判断吗？遍历每个元素，如果≤0就改成1，一行代码的事。\"",
     "input":"10行，每行一个整数。","output":"10行，每行\"X[i] = Y\"。",
     "sample_in":"0\n-5\n63\n-8\n0\n1\n2\n-100\n50\n200","sample_out":"X[0] = 1\nX[1] = 1\nX[2] = 63\n...","constraint":"−10⁹ ≤ 值 ≤ 10⁹",
     "sol":"这是数组最基础的操作模式：读入→判断→输出。遍历每个元素时检查其值，如果≤0就替换为1。C++中用for(int i=0;i<10;i++)访问，Python用enumerate()同时获取索引和值。",
     "tip":"Python的enumerate(arr)返回(index, value)元组。C++中数组索引从0开始——这是初学者最常犯的off-by-one错误来源。记住：第0个位置是第一个元素。"},
    {"nq":"NQ044","acw":738,"title":"数组填充",
     "story":"小华在教小鲁数组的递推生成：\"你看，这不就像我们小时候学过的'翻倍'游戏吗？第0个是V，第1个是V×2，第2个是(V×2)×2...\"小鲁恍然大悟：\"原来数组可以这样自动生成！不用我一个一个敲数字了。\"",
     "input":"一个整数V。","output":"10行，每行\"N[i] = X\"。",
     "sample_in":"1","sample_out":"N[0] = 1\nN[1] = 2\nN[2] = 4\nN[3] = 8\n...","constraint":"−10⁴ ≤ V ≤ 10⁴",
     "sol":"递推生成：每个新值由前一个值×2得出。这是\"递推思想\"的入门——每个新结果基于之前的结果计算，不需要从头算起。Python列表推导：[v*(2**i) for i in range(10)]一行搞定。",
     "tip":"Python的一行列表推导：arr = [v * (2**i) for i in range(10)]。C++中i从0开始，v每次乘2。注意V为负数时序列呈负增长。"},
    {"nq":"NQ045","acw":739,"title":"数组选择",
     "story":"小鲁看着屏幕上的100个数据犯了愁：\"这么多数据，我怎么能快速找出哪些小于等于10的？\"小华笑道：\"这不就是'筛选'吗？Python一行代码就能搞定——列表推导或者边读边判断。记住，你不需要把所有数据都存下来，读一个判断一个就行。\"",
     "input":"100行（或一行多个），每行一个浮点数。","output":"对每个≤10的数，输出\"A[i] = X\"（保留1位小数）。",
     "sample_in":"0\n-5\n63\n8.5\n100\n...","sample_out":"A[0] = 0.0\nA[1] = -5.0\nA[3] = 8.5\n...","constraint":"−10⁶ ≤ 值 ≤ 10⁶",
     "sol":"流式处理：不需要把100个数都存下来，读一个判断一个输出一个。这种\"边读边处理\"的思维在处理海量数据时至关重要——内存是有限的，流式处理可以处理任意大小的数据。",
     "tip":"Python格式化f\"A[{i}] = {x:.1f}\"。C++用printf(\"A[%d] = %.1f\\n\", i, x)。条件用<=，注意浮点精度。"},
    {"nq":"NQ046","acw":743,"title":"数组中的行",
     "story":"小鲁在整理12个月的销售数据，每个月的销售额存在不同的行里。\"我想单独看某个月的总销售额……\"小华点点头：\"这就是二维数组的行操作。外层循环控制行，内层循环控制列，当行号匹配时累加。\"",
     "input":"第一行L(0-11)。第二行T('S'或'M')。接下来144个浮点数（12×12矩阵）。","output":"结果保留1位小数。","sample_in":"2\nS\n(144个浮点数...)","sample_out":"(第2行之和)","constraint":"矩阵元素−10⁶到10⁶",
     "sol":"双层循环是二维数组的标准遍历方式。外层for i in range(12)控制行，内层for j in range(12)控制列。当i==L时累加。这种行列遍历模式贯穿所有多维数组题目。",
     "tip":"Python嵌套列表：[[0]*12 for _ in range(12)]。注意不能用[[0]*12]*12——那是浅拷贝，所有行指向同一个列表！"},
    {"nq":"NQ047","acw":740,"title":"数组变换",
     "story":"小鲁想把20个数据\"倒过来看\"——第一个放最后，最后一个放最前。\"这不就是翻转吗？\"小华说，\"Python用arr[::-1]一行搞定，C++要手写交换循环。但理解算法比会用库更重要——你知道翻转的原理是什么吗？\"",
     "input":"20个整数。","output":"20行，每行\"N[i] = X\"。","sample_in":"0\n1\n2\n...\n19","sample_out":"N[0] = 19\nN[1] = 18\n...","constraint":"−10⁹ ≤ 值 ≤ 10⁹",
     "sol":"对称交换算法：arr[i]与arr[19-i]交换，只需循环10次（i从0到9）。每步交换两个对称位置的元素。这是理解\"手写翻转\"和\"调用库函数\"差异的好例子。",
     "tip":"Python翻转用arr[::-1]（切片反转）或arr.reverse()（原地反转）。C++用std::reverse()或手写swap。切片创建新列表消耗额外内存。"},
    {"nq":"NQ048","acw":741,"title":"斐波那契数列",
     "story":"小鲁在图书上看到了斐波那契数列：0,1,1,2,3,5,8,13... \"这个数列有什么神奇的吗？\"小华兴奋地说：\"太多了！兔子的繁殖、花瓣的排列、黄金分割……在编程里，它是最经典的递推题——每个数都是前两个数的和，这就是动态规划(DP)的萌芽！\"\"不过要注意，第60项已经超过20亿了，C++要用long long。\"",
     "input":"一个整数N。","output":"一行，空格隔开的N个整数。","sample_in":"5","sample_out":"0 1 1 2 3","constraint":"1 ≤ N ≤ 60",
     "sol":"递推标准模板：a=0,b=1;不断输出a，然后a,b=b,a+b。Python的a,b=b,a+b是最优雅的递推写法。C++必须用long long（64位），N=60时F(60)≈1.5×10¹²远超出int范围。",
     "tip":"C++千万用long long！int在N>46时就会溢出。Python自动大整数。a,b=b,a+b是Python递推的\"指纹\"——看到这行代码就知道在做递推。"},
    {"nq":"NQ049","acw":742,"title":"最小数和它的位置",
     "story":"小栋找小鲁帮忙：\"我在做数据分析，找一组测量数据中的最小值以及它出现的位置。\"小鲁打开TRAE，写下了min()和index()。小华看了说：\"不错，但你知道吗——你这实际上遍历了两遍数据。更好的方法是只遍历一次，同时记录最小值和位置。\"",
     "input":"第一行N。第二行N个整数。","output":"第一行\"Menor valor: X\"。第二行\"Posicao: Y\"（从0开始）。","sample_in":"10\n1 2 3 4 -5 6 7 8 9 10","sample_out":"Menor valor: -5\nPosicao: 4","constraint":"1 ≤ N ≤ 1000",
     "sol":"一次遍历同时找最小值和位置：初始设第一个值为最小值，后续每遇到更小的就更新。Python用min()+index()简洁但需要两次遍历。手写版本只需一次O(n)——理解算法效率的差异。",
     "tip":"Python的min(arr)和arr.index(mn)组合虽简洁但效率不是最优。手写版本通过单次遍历实现O(n)时间+O(1)空间，是算法优化的入门案例。"},
    {"nq":"NQ050","acw":744,"title":"数组中的列",
     "story":"\"刚才你帮我算了某行的总和，现在我想算某列的总和——比如第3列，代表3月份各产品的销售额。\"小栋说。小鲁看了一下代码：\"咦，这不就是把i==L改成j==C吗？其他都一样。\"小华赞许地点点头：\"这就是编程的对称思维——理解了关系表达式，行和列的操作本质上是对称的。\"",
     "input":"第一行列号C。第二行操作类型T。接下来144个浮点数。","output":"结果保留1位小数。","sample_in":"2\nS\n(144个浮点数...)","sample_out":"(第2列之和)","constraint":"同NQ046",
     "sol":"与行操作对称：判断条件从i==L改为j==C。这种对称性是理解多维数组遍历的关键——能灵活变换遍历条件才是真正的掌握。","tip":"对比NQ046：代码几乎一样，只改变了一个字母。行列对称是编程美学的体现。"},
    {"nq":"NQ051","acw":717,"title":"简单斐波那契",
     "story":"\"我突然想——能不能只算第N项，不输出前面的？\"小鲁问。\"当然可以！\"小华说，\"只需要把输出改为只输出最后一个值，中间结果不用存储。这就是O(1)空间复杂度——不管N多大，你只需要两个变量a和b。\"",
     "input":"一个整数N。","output":"第N项的值。","sample_in":"4","sample_out":"3","constraint":"0 ≤ N ≤ 60",
     "sol":"Py:a,b=0,1;for _ in range(n):a,b=b,a+b;print(a)。循环n次后a就是第n项。注意循环次数和输出的对应关系——这是递推的\"根\"模式。",
     "tip":"O(1)空间的意思是：无论N=10还是N=60，内存用量恒定（只需2个变量）。这展示了递推相比递归的最大优势——不需要存储所有历史结果。"},
    {"nq":"NQ052","acw":722,"title":"数字序列和它的和",
     "story":"小鲁在练习while循环的用法。\"如果我想一直读数据直到遇到0为止怎么办？\"小华说：\"while True:读入→判断→break。这是处理'不定长输入'的标准模式。结合for循环生成序列和累加，你就能处理各种输入场景了。\"",
     "input":"多行，每行两个整数M和N。以M≤0或N≤0结束。","output":"对每对M,N，输出所有整数和\"Sum=X\"。","sample_in":"5 10\n2 3\n0 0","sample_out":"5 6 7 8 9 10 Sum=45\n2 3 Sum=5","constraint":"M,N ≤ 100",
     "sol":"while+break是不定长输入的标准处理模式。对每对M,N，先交换确保M≤N，然后用for循环从M输出到N并累加。Python的range()+sum()组合最优雅。",
     "tip":"Python: print(' '.join(map(str, range(m, n+1))), f'Sum={sum(range(m, n+1))}')。一行搞定！"},
    {"nq":"NQ053","acw":725,"title":"完全数",
     "story":"小华在图书馆看到一本书上写着\"完全数\"。\"6=1+2+3，28=1+2+4+7+14……这些数太美了！\"他兴奋地对小鲁说：\"你知道吗？在10⁸以内只有四个完全数：6,28,496,8128。这是数学家欧几里得和欧拉证明的。所以说——有时候数学知识可以让你少写很多代码！\"",
     "input":"一个整数N。","output":"每行一个完全数。","sample_in":"30","sample_out":"6\n28","constraint":"1 ≤ N ≤ 10⁸",
     "sol":"10⁸以内只有4个完全数。直接判断它们是否≤N即可。如果用朴素算法（枚举因子求和），对于N=10⁸需要几十秒——而用数学知识，O(1)时间解决。数学+算法=效率的天花板。",
     "tip":"这是\"先思考，再编码\"的典范。编程不是蛮力计算——有时候知道答案比计算答案更高效。厦门大学数学系有深厚的数论传统——学编程时别忘了你的数学课！"},
    {"nq":"NQ054","acw":726,"title":"质数",
     "story":"小嘉路过实验室，看到小鲁和伙伴们正在讨论质数判定。\"质数呀！\"小嘉饶有兴趣地说，\"我在南洋做生意的时候，数学帮我解决了不少问题。你们知道吗——判断一个数是不是质数，不需要检查到N-1，只需要检查到√N。因为如果N有大于√N的因子，一定有一个小于√N的对应因子。\"",
     "input":"一个整数N。","output":"每行一个质数。","sample_in":"10","sample_out":"2\n3\n5\n7","constraint":"2 ≤ N ≤ 10⁶",
     "sol":"√N优化：对2到N的每个数i，只需检查2到√i的因子。j*j<=i作循环条件比j<=sqrt(i)更高效（避免浮点运算）。时间复杂度从O(n²)降到O(n√n)。算法优化的第一课——数学知识直接转化为效率提升。",
     "tip":"Py用math.isqrt(i)获得整数平方根。j*j<=i替代j<=sqrt(i)避免浮点。小嘉说得对：√N的数学原理是优化算法的关键。厦大校训\"自强不息\"——算法优化永无止境。"},
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
body{font-family:"PingFang SC","Hiragino Sans GB","Noto Serif CJK SC","STSong",serif;font-size:9.5pt;line-height:1.7;color:#222;string-set:chapter"第4章 数据的容器——数组与线性存储"}
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
    parts.append('<div class="chapter-title">数据的容器</div>')
    parts.append('<div class="chapter-subtitle">数组与线性存储 · 12题 · C++ &amp; Python 双语对照</div>')
    parts.append('<div class="preface">')
    parts.append('<p>小鲁最近发现一个难题：他想统计全班50个同学的成绩，难不成要写50个变量？\"这也太麻烦了吧！\"他抱怨道。小华走了过来：\"你需要的是<strong>数组</strong>——编程中最基本的数据容器。\"</p>')
    parts.append('<p>本章12道题，小鲁将在小华（数学天才）和小栋（工程师）的帮助下，从基础的一维数组操作，逐步掌握二维矩阵、递推算法和算法优化。每一题都是一个故事——编程不应该是枯燥的，它应该像厦大芙蓉湖畔的凤凰花一样美丽。</p>')
    parts.append('<h3>本章角色</h3>')
    parts.append('<p>🧑‍🎓 <strong>小鲁</strong>（初学者）· 代表正在学习编程的你，会犯错、会提问、会进步</p>')
    parts.append('<p>🧠 <strong>小华</strong>（算法高手）· 数学天才，ACM竞赛队成员，总能用简单的话解释复杂算法</p>')
    parts.append('<p>🏗️ <strong>小栋</strong>（工程师）· 喜欢用编程解决实际问题，数据分析爱好者</p>')
    parts.append('<p>🏛️ <strong>小嘉</strong>（校主精神）· 厦大创始人，偶尔现身，带来数学智慧与校训力量</p>')
    parts.append('</div>')

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
        cpp=CODE_CACHE.get(p['acw'],'// code')
        py=PY_CACHE.get(p['acw'],'# Python solution')
        pb.append('<div class="code-dual">')
        pb.append(f'<div class="code-col"><div class="lang-badge">C++</div><pre>{hl(cpp,CppLexer(),CPP_FMT)}</pre></div>')
        pb.append(f'<div class="code-col"><div class="lang-badge">Python</div><pre>{hl(py,PythonLexer(),PY_FMT)}</pre></div>')
        pb.append('</div></div><hr class="section-divider">')
        parts.append('\n'.join(pb))

    parts.append('<div class="chapter-summary"><h3>📋 本章知识点总结</h3><ul>')
    parts.append('<li><strong>数组五大操作：</strong>遍历(iterate)、筛选(filter)、变换(transform)、翻转(reverse)、查找(search)</li>')
    parts.append('<li><strong>C++ vs Python：</strong>定长栈数组 vs 动态堆列表。C++更快，Python更灵活</li>')
    parts.append('<li><strong>递推思想：</strong>斐波那契——每个新值由前两个已知值计算，是DP的萌芽</li>')
    parts.append('<li><strong>算法优化第一课：</strong>质数判定的√N优化——用数学将复杂度从O(n²)降到O(n√n)</li>')
    parts.append('<li><strong>厦大校训：</strong>自强不息，止于至善。编程之路漫长，但每一步都在进步</li>')
    parts.append('</ul></div>')
    parts.append('<div class="chapter-end">— 第4章完 · 共12题 · 自强不息 —</div>')

    html=f"""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"><title>第4章 数据的容器</title><style>{CSS}</style></head><body>{chr(10).join(parts)}</body></html>"""
    out=BOOK_ROOT/"textbook"/"chapter04_print.html"
    out.write_text(html,encoding='utf-8')
    print(f"✅ Ch4 dialog version: {len(html)} chars")

if __name__=="__main__":
    build_html()
