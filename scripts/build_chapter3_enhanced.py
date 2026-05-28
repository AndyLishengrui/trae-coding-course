#!/usr/bin/env python3
"""第3章 循环的魔力(角色对话版) — for/while与嵌套循环"""
import json, re, os, sys
from pathlib import Path
BOOK_ROOT = Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(BOOK_ROOT / 'scripts'))

PROBLEMS = [
    {"nq":"NQ029","acw":708,"title":"偶数",
     "story":"\"我想打印出2到100之间的所有偶数，难道要写49行cout？！\"小鲁被这重复劳动吓到了。小华指了指屏幕：\"看到这个模式了吗？2,4,6,8...100——每个数比前一个大2。这种重复操作正是循环的用武之地。一行for循环，49行的活一秒搞定——这就是为什么程序员永远不会被机器取代：因为我们知道什么时候让机器替我们干活。\"",
     "input":"无。","output":"每行一个偶数，从2到100。",
     "sample_in":"(无输入)","sample_out":"2\n4\n6\n...\n100","constraint":"无",
     "sol":"for循环的基础形态：设定起始值、终止条件、步长。C++: for(int i=2;i<=100;i+=2)，Python: for i in range(2,101,2)。注意range的end是不包含的，所以写101而非100。",
     "tip":"Python的range(start, end, step)中end是exclusive。这是Python初学者最常见的off-by-one错误来源。i+=2比i=i+2更简洁——在所有类C语言中都通用。"},
    {"nq":"NQ030","acw":709,"title":"奇数",
     "story":"\"偶数搞定了，那奇数呢？\"小鲁问。小华写下了：for i in range(1, X+1, 2)。\"你看，只需改两个数——起始值从2改成1，步长保持2。奇偶的区别只差一个起始位置。\"小鲁恍然大悟：\"所以循环的威力就在于——一个模式能生成无穷多个结果。从1到X的所有奇数，只需要一行range！\"",
     "input":"一个正整数X。","output":"从1到X的所有奇数，每行一个。",
     "sample_in":"8","sample_out":"1\n3\n5\n7","constraint":"1 ≤ X ≤ 1000",
     "sol":"奇数序列：步长固定为2，起始值决定是奇数(1)还是偶数(2)。range(1, X+1, 2)自动跳过偶数。注意上限是X（包含），所以写X+1。",
     "tip":"Python的range不会包含end值——这是与很多其他语言不同的地方。记住这个特征：range(a,b)实际遍历[a, b-1]。"},
    {"nq":"NQ031","acw":712,"title":"正数",
     "story":"小鲁在做班级的成绩统计：\"6个同学的成绩里，有几个是正数？\"\"这需要循环+条件计数。\"小华在屏幕上写了起来，\"遍历每个数，如果大于0就让计数器加1。关键是理解'计数器'的概念：int cnt=0; 每满足条件就cnt++。Python更简洁——sum(1 for x in arr if x>0)。\"",
     "input":"6行，每行一个浮点数。","output":"\"X positive numbers\"，其中X为正数个数。",
     "sample_in":"7\n-5\n6\n-3.4\n4.6\n12","sample_out":"4 positive numbers","constraint":"−10⁹ ≤ 值 ≤ 10⁹",
     "sol":"条件计数模式：遍历→判断→累加计数器。计数器初始化为0，每次满足条件+1。Python的sum()配合生成器表达式一行搞定。C++中浮点数与0比较注意精度。",
     "tip":"Python生成器表达式sum(1 for x in arr if x>0)以O(n)时间和O(1)空间优雅地完成计数。C++的条件判断中整数和浮点数都适用>0。"},
    {"nq":"NQ032","acw":714,"title":"连续奇数的和1",
     "story":"\"设计一个有趣的数学游戏：\"小华说，\"随便选两个整数X和Y，然后求X和Y之间所有奇数的和。比如2和15之间的奇数是3+5+7+9+11+13+15=63。\"小鲁眼睛一亮：\"关键是要先确定X和Y谁大谁小，再从小的遍历到大的。\"\"没错——编程第一步总是在处理边界。\"",
     "input":"一行两个整数X和Y。","output":"一个整数，X和Y之间所有奇数的和。",
     "sample_in":"2 15","sample_out":"63","constraint":"−10⁶ ≤ X,Y ≤ 10⁶",
     "sol":"三步：1.确保起点≤终点（交换）；2.从起点到终点遍历每个数；3.如果是奇数则累加。Python的sum(i for i in range(lo,hi+1) if i%2==1)一行完成。C++需要手写for+if+累加。",
     "tip":"Python的range(lo,hi+1)[lo%2::2]可以只生成奇数——利用切片+步长直接跳过偶数。但生成器表达式更可读。先确定边界再遍历是处理区间问题的通用习惯。"},
    {"nq":"NQ033","acw":716,"title":"最大数和它的位置",
     "story":"小栋拿着一叠数据找到小鲁：\"帮我找这100个数里的最大值，还有第几个是它。\"小鲁试了max()和index()：\"搞定了！\"小华看了代码后说：\"不错，但你知道吗——你用了两遍遍历。更好的方法是遍历一次，同时记住最大值和位置。虽然对于100个数没区别，但如果是一亿个数，差一倍的时间就是差一个午饭。\"",
     "input":"100行，每行一个整数。","output":"第一行最大值，第二行位置（1-indexed）。",
     "sample_in":"2\n113\n45\n34565\n6\n...","sample_out":"34565\n4","constraint":"−10⁹ ≤ 值 ≤ 10⁹",
     "sol":"一次遍历找最值：初设第一个为最大值位置1，然后从第二个开始，遇到更大的就更新值和位置。O(n)一次遍历完成。这比Python的max()+index()两次遍历更高效——算法优化的意识从小题培养。",
     "tip":"Python的max()底层也是C实现的O(n)。但max()+index()会导致两次O(n)遍历。手写的O(n)单次遍历在数据量大时更优。这种\"一次遍历完成多件事\"的思维是算法设计的核心。"},
    {"nq":"NQ034","acw":721,"title":"递增序列",
     "story":"\"有一个特殊的数据集——每个数都比前一个数大，形成一个递增序列。\"小华在纸上画着：\"5,10,15,20,25...我们需要一种新的循环——不知道要循环多少次，因为不知道序列有多长。\"\"那就是while循环！\"小鲁抢答，\"while True读入，遇到0就break——这就是'不定长输入'的处理模式。\"",
     "input":"多组，每组一个整数X。0结束。","output":"对每个非0的X，输出从1到X的所有整数。",
     "sample_in":"5\n10\n3\n0","sample_out":"1 2 3 4 5\n1 2 3 4 5 6 7 8 9 10\n1 2 3","constraint":"0 ≤ X ≤ 10⁶",
     "sol":"while+break是不定长输入的标准处理模式：while(1){读入; if(==0) break; 处理}。Python的while True和C++的while(cin>>x,x)都支持。while和for的区别在于：while适合\"不知道次数\"的循环。",
     "tip":"Python: while True: x=int(input()); if x==0: break; 输出序列。C++可以用逗号表达式while(cin>>x,x)——利用逗号运算符取最后一个值。但可读性不如先读入再break。"},
    {"nq":"NQ035","acw":720,"title":"连续整数相加",
     "story":"小鲁遇到了变种题：\"读入A和N，求从A开始的连续N个整数的和。\"比如A=3,N=2 => 3+4=7。\"这跟NQ032有点像——但这次N告诉你要加几个数。\"小华提示道：\"在循环中用一个累加器sum，循环N次，每次加上当前值然后当前值加1。Python的range(a, a+n)直接生成这一串数。\"",
     "input":"多对整数A和N，一直读到N≤0。","output":"每对输出\"Sum = X\"。",
     "sample_in":"3 2\n4 -1","sample_out":"Sum = 7","constraint":"A,N ≤ 10⁶",
     "sol":"连续N个整数从A+A+1+...+A+N-1 = N×A+N(N-1)/2。但循环版本更易懂：sum=0; for i in range(a, a+n): sum+=i。也可以数学公式直接算——但理解循环累加的思维更重要。",
     "tip":"Python: sum(range(a, a+n))一行完成。但手写循环累加才能理解\"累加器模式\"——这是所有求和、求积、统计类问题的基础。数学公式法体现了\"先思考再编码\"——但不要忘了循环是理解问题的第一步。"},
    {"nq":"NQ036","acw":724,"title":"约数",
     "story":"小鲁在数学课上学到了约数：\"6能被1,2,3,6整除——所以6有4个约数。\"小华说：\"编程找约数很简单：从1到N遍历每个数，如果N%i==0就输出。不过有个优化技巧——约数是成对出现的，你只需要遍历到√N。比如6的约数：i=1找到1和6，i=2找到2和3——√6≈2.45所以搜索到2就够了。\"",
     "input":"一个整数N。","output":"按升序输出N的所有约数，每行一个。",
     "sample_in":"6","sample_out":"1\n2\n3\n6","constraint":"1 ≤ N ≤ 10⁹",
     "sol":"基础方法：从1到N遍历，N%i==0则输出。优化方法：只遍历到√N，每个i找到两个约数i和N/i。注意完全平方数（如16）时i=N/i只算一次。√N优化将复杂度从O(N)降到O(√N)——对于N=10⁹，从10亿降到3万。",
     "tip":"C++的遍历条件i*i<=N比i<=sqrt(N)更高效（避免浮点数）。Python用while i*i<=n。注意输出顺序——如果要求升序，需要收集约数再排序输出。本课主要理解基本的枚举模式。"},
    {"nq":"NQ037","acw":723,"title":"PUM",
     "story":"小鲁看到了一道来自巴西OJ的题目：\"输出N行，每行M个数——但每行最后一个数要替换成'PUM'。比如N=7,M=4……\"小华笑道：\"这其实是考你对换行的精确控制——第M列不是数字而是'PUM'。关键是判断位置：如果(j+1)%M==0就输出PUM并换行，否则输出数字后跟空格。\"",
     "input":"一行两个整数N和M。","output":"N×M格式的序列，每行第M列输出\"PUM\"。",
     "sample_in":"7 4","sample_out":"1 2 3 PUM\n5 6 7 PUM\n9 10 11 PUM\n...","constraint":"1 ≤ N,M ≤ 20",
     "sol":"计数器从1开始，每输出一个数+1。判断是否第M列：用cnt%M==0（cnt从1开始）。是则输出PUM换行，否则输出数字+空格。这是格式化循环输出题——训练对循环索引和输出格式的精确控制。",
     "tip":"Python: for i in range(n): 输出一行m-1个数字(空格分隔)+' PUM'。C++注意末尾空格的处理。理解%取模判断\"是否该换行\"是这类题的通用技巧。"},
    {"nq":"NQ038","acw":710,"title":"六个奇数",
     "story":"\"给定一个整数X，输出从X开始的6个连续的奇数。\"小栋出了一道题考小鲁。\"但是我怎么知道X是奇数还是偶数？\"小鲁问。小华提醒道：\"如果X是偶数，就从X+1开始——因为偶数+1就是奇数。然后用循环输出6个，每次步长2。关键是先处理奇偶性。\"",
     "input":"一个整数X。","output":"从X开始（如果X是偶数则从X+1开始）的6个连续奇数。",
     "sample_in":"8","sample_out":"9\n11\n13\n15\n17\n19","constraint":"−10⁹ ≤ X ≤ 10⁹",
     "sol":"先归一化起点：if x%2==0: start=x+1 else start=x。然后用for循环6次，每次输出start+2*i。这是\"预处理起点\"的标准模式——先统一格式，再统一处理。",
     "tip":"Python一行：start = x+1 if x%2==0 else x，然后for i in range(6): print(start + 2*i)。C++可以用x%2==0?x+1:x做起点。这种\"先定点再循环\"的模式在循环题中反复出现。"},
    {"nq":"NQ039","acw":711,"title":"乘法表",
     "story":"\"九九乘法表——这是我奶奶都会背的东西！\"小鲁笑道。\"但用代码生成它，需要你在一个循环里再套一个循环——这就是嵌套循环。\"小华打开TRAE演示，\"外层控制行，内层控制列。第i行第j列输出i*j。两层for循环，一共N×N次操作。注意格式对齐——每个数占4个字符宽度。\"",
     "input":"一个整数N（表示表格大小）。","output":"N×N的乘法表，每个数占4宽对齐。",
     "sample_in":"3","sample_out":"  1   2   3\n  2   4   6\n  3   6   9","constraint":"1 ≤ N ≤ 15",
     "sol":"嵌套循环的标准结构：for i in range(1,N+1): for j in range(1,N+1): print(i*j)。内层循环完整执行N次后外层才进入下一次。注意格式化宽度——Python的f'{i*j:4d}'。嵌套循环是程序设计的第一个心智跃迁。",
     "tip":"Python的f'{val:4d}'表示4宽度右对齐。C++用setw(4)或printf(\"%4d\")。嵌套循环复杂度O(N²)——当N翻倍时运算量翻4倍。这是理解\"时间复杂度\"的入门。"},
    {"nq":"NQ040","acw":718,"title":"实验",
     "story":"小鲁的生物课在做动物实验：统计N组数据中青蛙、老鼠和兔子的总数及占比。\"每组数据有两个数：数量和动物类型——C代表rabbit、R代表rat、S代表frog。\"\"这不就是分类统计吗？\"小华说，\"用三个计数器分别统计，最后算百分比。Python可以用collections.Counter自动分类，但手写三个if分支更直观。\"",
     "input":"第一行N。接下来N行，每行\"数量 类型(C/R/S)\"。","output":"实验动物总数+各类数量+百分比。",
     "sample_in":"3\n5 C\n7 R\n8 S","sample_out":"Total: 20 animais\nTotal de coelhos: 5\nTotal de ratos: 7\nTotal de sapos: 8\nPercentual de coelhos: 25.00 %\nPercentual de ratos: 35.00 %\nPercentual de sapos: 40.00 %","constraint":"1 ≤ N ≤ 100",
     "sol":"分类统计：three counters。每次根据类型字符判断加到哪个计数器。最后算百分比=各类/总数×100。注意保留两位小数。Python的if-elif或dict映射都比C++的if-else更简洁。",
     "tip":"Python用dict映射：cnt={'C':0,'R':0,'S':0}，然后cnt[t]+=qty。比三个if更灵活。百分比输出用f\"{cnt['C']/total*100:.2f} %\"。注意%号的转义——f-string中用%%。"},
    {"nq":"NQ041","acw":715,"title":"余数",
     "story":"小鲁在整理数据时发现了一个规律：\"这组数里，除了2以外，其他被2整除的都不对……\"小华纠正道：\"你想说的是'除了2以外的所有整数，除以2的余数都是0或1'对吧？这道题就是数一数从1到10000有多少个数除以N余2。'小小的循环条件就能精准筛选。\"",
     "input":"一个整数N。","output":"从1到10000中除以N余2的所有数，每行一个。",
     "sample_in":"13","sample_out":"2\n15\n28\n...","constraint":"1 ≤ N ≤ 10000",
     "sol":"条件循环：for i in range(1,10001): if i%N==2: print(i)。取模运算%是循环中最高频的条件运算符——余数判断可用于奇偶(i%2)、整除(i%N==0)、特定余数(i%N==k)等。",
     "tip":"if i%N==2表示i除以N的余数等于2。比如N=13时，2÷13=0余2，15÷13=1余2，28÷13=2余2……余数是最基础的数论概念之一——理解它，后续的哈希、质数等问题才不会被拦在门外。"},
    {"nq":"NQ042","acw":713,"title":"区间2",
     "story":"\"上次我们数了正数有多少个——现在升级一下，统计位于[10,20]区间内的个数，以及区间外的个数。\"小栋把题目升级了。小鲁自信满满：\"这简单！读入N个数，如果x在10到20之间（包含两端），in_counter++；否则out_counter++。一道题，两个计数器，一次遍历。\"",
     "input":"第一行N。接下来N个整数。","output":"\"X in\"换行\"Y out\"。",
     "sample_in":"4\n14\n123\n10\n-25","sample_out":"2 in\n2 out","constraint":"1 ≤ N ≤ 10000",
     "sol":"双计数器+区间判断：in_cnt统计10≤x≤20，out_cnt统计x其他。一次遍历完成两个统计任务。Python用链式比较10<=x<=20最直观。注意包含端点——10和20都算in。",
     "tip":"Python链式比较：if 10 <= x <= 20。比C++的x>=10 && x<=20更自然。两个计数器互斥且完备——in+out = N，可以只统一个数推另一个，但分别统计更安全（验证用的N个都处理了）。"},
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
body{font-family:"PingFang SC","Hiragino Sans GB","Noto Serif CJK SC","STSong",serif;font-size:9.5pt;line-height:1.7;color:#222;string-set:chapter"第3章 循环的魔力——for/while与嵌套循环"}
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
    parts.append('<div class="chapter-title">循环的魔力</div>')
    parts.append('<div class="chapter-subtitle">for/while与嵌套循环 · 14题 · C++ &amp; Python 双语对照</div>')
    parts.append('<div class="preface">')
    parts.append('<p>第三周，小鲁发现了一个令他震惊的事实：\"一个for循环能替我做100行重复代码？！\"小华笑了：\"这就是<strong>循环</strong>的威力——编程从手动执行进化到自动重复的时刻，就像从步行变成了骑车。能识别出重复模式并用循环解决，才是真正学会了编程思维。\"</p>')
    parts.append('<p>本章14道题，小鲁将在小华的指导下，从最简单的for循环开始，逐步掌握while循环、嵌套循环和条件循环。更重要的是，学会\"<strong>什么时候用循环，什么时候用公式</strong>\"——循环是工具，不是信仰。当数学公式能一行搞定1000次循环时，数学和编程的结合才真正开始。</p>')
    parts.append('<h3>本章角色</h3>')
    parts.append('<p>🧑‍🎓 <strong>小鲁</strong>（初学者）· 从\"手动写100行\"的困惑中觉醒，学习循环的力量</p>')
    parts.append('<p>🧠 <strong>小华</strong>（算法高手）· ACM集训队队长，能用最生动的比喻解释while vs for</p>')
    parts.append('<p>🏗️ <strong>小栋</strong>（工程师）· 喜欢用实际问题挑战小鲁，代表真实编程场景</p>')
    parts.append('<p>🏛️ <strong>小嘉</strong>（校主精神）· 偶尔现身，用\"自强不息\"激励大家在算法之路上坚持</p>')
    parts.append('</div>')
    parts.append('<div class="knowledge-box"><div class="k-title">🔄 C++ vs Python 循环速查</div><ul>')
    parts.append('<li><strong>for循环：</strong>for(int i=0;i<N;i++) → for i in range(N)</li>')
    parts.append('<li><strong>步长：</strong>i+=2 → range(0,N,2)（注意range的end不包含！）</li>')
    parts.append('<li><strong>while循环：</strong>while(cond){...} → while cond:...（几乎一样）</li>')
    parts.append('<li><strong>不定长输入：</strong>while(cin>>x) → while True: x=input(); if not x: break</li>')
    parts.append('<li><strong>嵌套循环：</strong>两层for在两种语言中语法不同、逻辑相同</li>')
    parts.append('<li><strong>Python独有：</strong>列表推导式一行替代循环+条件+赋值。生成器表达式处理大数据无内存压力</li></ul></div>')

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
    parts.append('<li><strong>for循环：</strong>确定次数的循环首选。Python的range(start,end,step)注意end不包含</li>')
    parts.append('<li><strong>while循环：</strong>不确定次数的循环首选。while+break处理不定长输入</li>')
    parts.append('<li><strong>嵌套循环：</strong>外层行内层列，复杂度O(N²)。理解两次for的执行顺序</li>')
    parts.append('<li><strong>条件循环：</strong>循环中嵌入if判断——计数、筛选、分类，90%的算法代码都是这个模式</li>')
    parts.append('<li><strong>累加器模式：</strong>sum/cnt初始化为0，循环中逐次更新。这是所有统计/求和的基础</li>')
    parts.append('<li><strong>先思考再编码：</strong>约数的√N优化、等差数列求和公式——数学知识直接减少循环次数</li>')
    parts.append('</ul></div>')
    parts.append('<div class="chapter-end">— 第3章完 · 共14题 · 自强不息 —</div>')

    html=f"""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"><title>第3章 循环的魔力</title><style>{CSS}</style></head><body>{chr(10).join(parts)}</body></html>"""
    out=BOOK_ROOT/"textbook"/"chapter03_print.html"
    out.write_text(html,encoding='utf-8')
    print(f"✅ Ch3 dialog version: {len(html)} chars")

if __name__=="__main__":
    build_html()
