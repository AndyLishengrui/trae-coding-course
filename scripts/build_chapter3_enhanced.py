#!/usr/bin/env python3
"""第2章 选择的艺术——条件判断与分支结构 (角色对话版)"""
import re,os,sys;from pathlib import Path
BOOK_ROOT=Path(__file__).parent.parent.resolve();sys.path.insert(0,str(BOOK_ROOT/'scripts'))

PROBLEMS=[
    {"nq":"NQ015","acw":665,"title":"倍数","story":"小鲁在数学课上学了倍数。\"如果A能被B整除，或者B能被A整除，它们就是倍数关系。\"小华说：\"编程里用%取模来判断——a%b==0说明a是b的倍数。用||(C++)或or(Python)把两个条件连起来。\"","input":"一行，两个整数A和B。","output":"互为倍数输出\"Sao Multiplos\"，否则\"Nao sao Multiplos\"。","sample_in":"6 24","sample_out":"Sao Multiplos","constraint":"−10⁴ ≤ A,B ≤ 10⁴（A,B≠0）","sol":"用取模判断倍数关系：A%B==0或B%A==0。两个条件用\"或\"连接。这是if-else最简单的形式——单一条件判断，两个分支。","tip":"Py的if语句不需要括号。C++的%运算符要求整数。a%b==0比!(a%b)更易读。"},
    {"nq":"NQ016","acw":660,"title":"零食","story":"小鲁去小卖部买零食：1号零食4元，2号4.5元，3号5元，4号2元，5号1.5元。\"这么多选项，怎么写？\"小华说：\"C++可以用if-else链或switch。Python可以用dict映射——一行搞定全部！\"","input":"一行，两个整数：零食编号X和数量Y。","output":"\"Total: R$ \"后跟总价（保留2位）。","sample_in":"3 2","sample_out":"Total: R$ 10.00","constraint":"1≤X≤5,1≤Y≤100。单价：1=4.00,2=4.50,3=5.00,4=2.00,5=1.50","sol":"多分支选择。C++用if-else链或switch，Python用if-elif或dict映射。本课重点：dict={1:4.0,2:4.5,3:5.0,4:2.0,5:1.5}，prices[x]*y一行出结果——O(1)查找，代码量减少50%。","tip":"Py的dict映射表：prices={1:4.0,2:4.5,3:5.0,4:2.0,5:1.5}。替代if-elif链。\"用数据驱动替代逻辑堆叠\"是进阶编程的核心理念。"},
    {"nq":"NQ017","acw":659,"title":"区间","story":"\"一个数落在哪个区间里？\"小鲁看着题目：\"0到25是闭区间，25到50是左开右闭……\"小华提醒他：\"注意开闭区间的区别——[0,25]包含25，(25,50]不包含25但包含50。Python的链式比较0<=x<=25比C++的0<=x&&x<=25更直观。\"","input":"一个浮点数x。","output":"区间名或\"Fora de intervalo\"。","sample_in":"25.01","sample_out":"Intervalo (25,50]","constraint":"−10⁹≤x≤10⁹","sol":"从最小区间开始判断，逐级向上。Python链式比较更直观，C++需分开写&&。注意开闭括号[包含](不包含)的数学含义——这是区间判断最容易出错的地方。","tip":"Python链式比较：0<=x<=25。C++需要0<=x&&x<=25。Python的链式比较是语法糖——编译器自动转换成两个比较的and。"},
    {"nq":"NQ018","acw":664,"title":"三角形","story":"\"给你三根木棍，长度分别是6.0、4.0和2.0——能拼成三角形吗？\"小栋问。小鲁想了想：\"三角形的条件是任意两边之和大于第三边。2+4=6，等于第三边……不能！\"小华说：\"必须同时满足A+B>C、A+C>B、B+C>A三个条件，用&&连接。\"","input":"一行，三个浮点数A、B、C。","output":"能构成则\"Perimetro = 周长\"，否则\"Area = 梯形面积\"。","sample_in":"6.0 4.0 2.0","sample_out":"Area = 10.0","constraint":"0<A,B,C≤100","sol":"三角形判定：A+B>C且A+C>B且B+C>A。三个条件必须同时满足，用&&(C++)或and(Python)连接。不能构成时输出梯形面积(A+B)*C/2。","tip":"三个条件同时满足：if a+b>c and a+c>b and b+c>a。Python可以写得非常干净。注意浮点数比较的精度问题——对于大数或极端接近的情况需谨慎。"},
    {"nq":"NQ019","acw":667,"title":"游戏时间","story":"小鲁玩游戏从下午4点玩到凌晨2点。\"这跨天了，怎么算？\"小华说：\"A=16,B=2。如果A<B直接相减10小时；如果A≥B——说明跨天了——需要24-A+B=24-16+2=10小时。\"","input":"两个整数A和B（0≤A,B≤23）。","output":"\"O JOGO DUROU X HORA(S)\"。","sample_in":"16 2","sample_out":"O JOGO DUROU 10 HORA(S)","constraint":"0≤A,B≤23","sol":"先判断是否跨天：A<B则B-A，否则(24-A)+B。这是时间循环判断的经典题，也是if-else的天然应用。","tip":"可以统一为(B-A+24)%24，但结果为0时需要特殊处理（表示24小时）。这种\"循环型\"问题在时间/角度/周期问题中反复出现。"},
    {"nq":"NQ020","acw":669,"title":"加薪","story":"小鲁收到年终调薪通知——涨多少取决于当前工资：0-400涨15%，400.01-800涨12%，800.01-1200涨10%，1200.01-2000涨7%，2000以上涨4%。\"这是分段函数！\"小华说：\"从低到高判断最自然——s<=400?15:s<=800?12:s<=1200?10:...\"","input":"一个浮点数表示当前工资。","output":"三行：新工资、涨薪金额、涨幅百分比。","sample_in":"400.00","sample_out":"Novo salario: 460.00\nReajuste ganho: 60.00\nEm percentual: 15 %","constraint":"0<工资≤10⁶","sol":"从低到高的if-elif链。区间互斥，顺序很重要——先判断小值再判断大值可以不加&&上限条件（因为前面的判断已经排除了）。注意输出格式：保留2位小数+空格+%。","tip":"C++中%%输出%字面量（printf需要转义）。Python直接写%。区间判断顺序从低到高可以利用else的\"否则\"语义简化条件。"},
    {"nq":"NQ021","acw":670,"title":"动物","story":"\"猜动物游戏！\"小鲁兴奋地说。\"输入三个特征——脊椎/非脊椎、哺乳/鸟/昆虫/环节动物、食性——判断是什么动物。\"小华说：\"这是嵌套if的完美案例——像一棵决策树，每个内部节点是判断，叶子节点是答案。\"","input":"三行字符串（vertebrado/invertebrado等）。","output":"动物名称（aguia/pomba/homem/vaca/pulga/lagarta/sanguessuga/minhoca）。","sample_in":"vertebrado\nmamifero\nonivoro","sample_out":"homem","constraint":"输入保证合法。","sol":"三层嵌套if。先判断脊椎/非脊椎→再判断纲→再判断食性。本质是一棵深度为3的决策树。Python的嵌套if-elif结构清晰易读。也可用dict嵌套：tree={'vertebrado':{'ave':{...}}}。","tip":"Python的嵌套dict可以替代嵌套if——tree[a][b][c]一行定位答案。但写if逻辑更透明，两者都是合理的方案。\"数据结构化思维\"是编程进阶的关键能力。"},
    {"nq":"NQ022","acw":657,"title":"选择练习1","story":"小鲁一口气写下五个条件：B>C、D>A、C+D>A+B、C>0、D>0、A是偶数。\"要同时满足才能输出accepted——用&&(and)把它们串起来。\"小华说：\"这是复杂布尔表达式的练习——五个条件，一个都不能少。\"","input":"一行四个整数A、B、C、D。","output":"全部满足输出\"Valores aceitos\"，否则\"Valores nao aceitos\"。","sample_in":"5 6 7 8","sample_out":"Valores nao aceitos","constraint":"−10⁹≤A,B,C,D≤10⁹","sol":"5个条件用&&(and)连接。同时满足才输出accepted。训练复杂布尔表达式的使用。条件的排列顺序影响短路求值——先放最容易判断的。","tip":"Python把5个条件写一行：if b>c and d>a and c+d>a+b and c>0 and d>0 and a%2==0。可读性极好。先放C>0、D>0这种简单条件可以触发短路优化。"},
    {"nq":"NQ023","acw":671,"title":"DDD","story":"小鲁想给其他城市的同学打电话。\"61是巴西利亚，71是萨尔瓦多，11是圣保罗……这么多城市怎么记？\"小华说：\"C++可以写8个if-else。但Python用dict——{'61':'Brasilia','71':'Salvador',...}，一行get()全搞定。这就是'用数据驱动替代代码堆叠'的力量。\"","input":"一个整数DDD区号。","output":"城市名或\"DDD nao cadastrado\"。","sample_in":"11","sample_out":"Sao Paulo","constraint":"DDD为正整数。","sol":"Python的dict映射表一行替代8个if-else。ddd.get(ddd, 'DDD nao cadastrado')——查找存在就返回，不存在就返回默认值。这是本课最重要的工程思维：看到重复的if-else模式时，用数据结构替代。" ,"tip":"ddd={61:'Brasilia',71:'Salvador',11:'Sao Paulo',21:'Rio de Janeiro',32:'Juiz de Fora',19:'Campinas',27:'Vitoria',31:'Belo Horizonte'}。print(ddd.get(x,'DDD nao cadastrado'))。"},
    {"nq":"NQ024","acw":662,"title":"点的坐标","story":"小鲁在坐标系上画了一个点：\"P(4.5,-2.2)——这是第几象限？\"\"第四象限！\"小华说，\"但要注意特殊情况：原点(0,0)、X轴(y=0)、Y轴(x=0)。判断顺序很重要——先判断原点，再判断轴，最后判断象限。如果顺序搞错——比如先判断x>0就归为Q1——可能把原点误判。\"","input":"两个浮点数x和y。","output":"Q1/Q2/Q3/Q4/Origem/Eixo X/Eixo Y。","sample_in":"4.5 -2.2","sample_out":"Q4","constraint":"−10⁹≤x,y≤10⁹","sol":"判断顺序：原点→轴→象限。这是分类讨论的标准流程——先特殊后一般。x>0且y>0→Q1，x<0且y>0→Q2，x<0且y<0→Q3，x>0且y<0→Q4。","tip":"判断顺序从特殊到一般：原点→轴→象限。Python中x==0和y==0用浮点比较在本题数据范围内安全。对于更精确的场景可使用abs(x)<1e-9。"},
    {"nq":"NQ025","acw":666,"title":"三角形类型","story":"\"不仅要判定能不能构成三角形，还要分直/钝/锐/等边/等腰——这一道题等于前一道的10倍工作量！\"小鲁被吓到了。小华笑道：\"别怕，先把三边降序排列（a≥b≥c），然后从一般到特殊逐个判断。排序降序是简化三角形分类的关键——排完序后一切都变简单了。\"","input":"三个浮点数A、B、C。","output":"按顺序判断：不构成→直角→钝角→锐角→等边→等腰。可能输出多行。","sample_in":"7.0 5.0 7.0","sample_out":"TRIANGULO ACUTANGULO\nTRIANGULO ISOSCELES","constraint":"0<A,B,C≤100","sol":"三步法：1.降序排列(swap直到a≥b≥c)；2.判三角形：a≥b+c?不能构成；3.角度类型：a²=b²+c²(直角)、a²>b²+c²(钝角)、a²<b²+c²(锐角)；4.边类型：a=b=c(等边)/a=b或b=c(等腰)。","tip":"Python一行排序：a,b,c=sorted([a,b,c],reverse=True)。排序降序后所有判断条件都变得简单。注意用多个if而非if-elif——因为可能同时满足多个条件（如既是锐角又是等腰）。"},
    {"nq":"NQ026","acw":668,"title":"游戏时间2","story":"\"上次只算了小时，这次要精确到分钟！\"小鲁升级了游戏计时器。\"起点7:08，终点9:10——持续多久？\"\"统一换算成分钟：7*60+8=428，9*60+10=550，差122分钟=2小时2分钟。如果终点≤起点，加24*60处理跨天。\"","input":"四个整数：A(开始时)、B(开始分)、C(结束时)、D(结束分)。","output":"\"O JOGO DUROU X HORA(S) E Y MINUTO(S)\"。","sample_in":"7 8 9 10","sample_out":"O JOGO DUROU 2 HORA(S) E 2 MINUTO(S)","constraint":"0≤A,C≤23,0≤B,D≤59","sol":"统一转换为分钟：start=A*60+B,end=C*60+D。若end≤start则加24*60。diff=end-start，再转回时=diff/60,分=diff%60。\"统一量纲\"是时间问题的通用技巧。","tip":"统一量纲(分钟)后比较和计算避免分别处理小时和分钟的复杂情况。Python的divmod(diff,60)可以直接分解时和分。"},
    {"nq":"NQ027","acw":672,"title":"税","story":"小鲁第一次交税。\"税率分段计算——0到2000免税，2000.01到3000收8%，3000.01到4500收18%，4500以上收28%。\"\"注意是分段计税，不是全额×最高税率！\"小华强调：\"每一段分别计算——超过2000的部分才需要交税。\"","input":"一个浮点数表示月收入。","output":"免税输出\"Isento\"，否则\"R$ XX.XX\"。","sample_in":"3002.00","sample_out":"R$ 80.36","constraint":"0<收入≤10⁶","sol":"分段计税：先判断是否≤2000(免税)。超出2000部分逐段按税率计算。Python用min()限制每段上限：tax=min(x,1000)*0.08+min(max(x-1000,0),1500)*0.18+...","tip":"Python的min/max组合：min(x,1000)*0.08处理第一段(0-1000按8%)。理解\"分段\"原理比写出代码更重要——这是个人所得税的核心逻辑。"},
    {"nq":"NQ028","acw":663,"title":"简单排序","story":"\"把三个数从小到大排列——这是排序算法的萌芽。\"小华说：\"三步比较交换：先比较a和b，必要时交换；再比较a和c；最后比较b和c。三步之后a≤b≤c——这就是冒泡排序思想的微型版。C++用swap()，Python用a,b=b,a——交换变量最优雅的方式。\"","input":"一行三个整数。","output":"升序排列的三个数。","sample_in":"7 21 -14","sample_out":"-14 7 21","constraint":"−10⁹≤a,b,c≤10⁹","sol":"三步交换排序：if a>b:swap(a,b); if a>c:swap(a,c); if b>c:swap(b,c)。这是排序算法的最小实现——理解交换操作的原理为后续学习排序算法打下基础。","tip":"Python的a,b=b,a是最优雅的交换写法——基于元组解包。C++用std::swap或临时变量。Python一行sorted()也行但手写交换理解原理更重要。"},
]

from pygments import highlight;from pygments.lexers import CppLexer,PythonLexer;from pygments.formatters import HtmlFormatter
CPP_FMT=HtmlFormatter(style='vs',noclasses=True);PY_FMT=HtmlFormatter(style='vs',noclasses=True)
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
body{font-family:"PingFang SC","Hiragino Sans GB","Noto Serif CJK SC","STSong",serif;font-size:9.5pt;line-height:1.7;color:#222;string-set:chapter"第2章 选择的艺术——条件判断与分支结构"}
.chapter-title{text-align:center;font-size:20pt;font-weight:bold;margin:1.5em 0 .1em 0;letter-spacing:3pt}
.chapter-subtitle{text-align:center;font-size:10pt;color:#777;margin-bottom:1.5em;padding-bottom:.8em;border-bottom:1px solid #bbb}
.preface{font-size:10pt;margin-bottom:1.5em;color:#444}.preface p{margin:.3em 0;text-indent:2em}
.preface h3{font-size:11pt;color:#2563eb;margin:1em 0 .3em 0}
.knowledge-box{background:#f0f6ff;border:1pt solid #bdd;border-radius:4px;padding:.7em 1em;margin:.8em 0;font-size:9pt}
.knowledge-box .k-title{font-weight:bold;color:#2563eb;margin-bottom:.3em;font-size:9.5pt}.knowledge-box p{margin:.2em 0}.knowledge-box ul{margin:.2em 0;padding-left:1.5em}
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
    parts.append('<div class="chapter-title">选择的艺术</div>')
    parts.append('<div class="chapter-subtitle">条件判断与分支结构 · 14题 · C++ &amp; Python 双语对照</div>')
    parts.append('<div class="preface">')
    parts.append('<p>第二周，小鲁已经能熟练地写A+B了。但小华说：\"真正的程序不会只是直线执行——你需要根据不同的情况做出不同的决定。如果成绩及格就通过，否则补考；如果是周一就升旗，否则早读……这就是<strong>条件判断</strong>。\"</p>')
    parts.append('<p>本章14道题，小鲁将从简单的if-else开始，逐步掌握多分支、嵌套条件、决策树和dict映射表。最重要的是学会\"<strong>用数据结构替代逻辑堆叠</strong>\"——当你看到一大串if-elif-else的时候，第一反应应该问自己：\"能不能用一张表来替代？\"</p>')
    parts.append('</div>')
    parts.append('<div class="knowledge-box"><div class="k-title">🔀 C++ vs Python 条件判断速查</div><ul>')
    parts.append('<li><strong>单分支：</strong>if(cond){...} → if cond:...</li><li><strong>多分支：</strong>if/else if/else → if/elif/else</li>')
    parts.append('<li><strong>链式比较：</strong>0<=x&&x<=25 → 0<=x<=25 (Python独有!)</li>')
    parts.append('<li><strong>映射表：</strong>8个if-else → dict.get(key,default) (Python独有!)</li>')
    parts.append('<li><strong>三元表达式：</strong>cond?a:b → a if cond else b</li></ul></div>')

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
    parts.append('<li><strong>if-else/if-elif-else：</strong>条件分支的基本语法，两语言核心差异在于Python的elif和缩进</li>')
    parts.append('<li><strong>Python链式比较：</strong>a<=x<=b等价于a<=x and x<=b，语法糖但可读性极好</li>')
    parts.append('<li><strong>dict映射表：</strong>替代长if-else链的利器。O(1)查找，代码减少50%+</li>')
    parts.append('<li><strong>决策树思维：</strong>嵌套条件判断本质是决策树——从根到叶的路径</li>')
    parts.append('<li><strong>排序简化：</strong>三角形类型题——先排序使a≥b≥c，后续所有判断条件简化</li>')
    parts.append('<li><strong>分段计算：</strong>税务题——min/max组合处理分段，理解\"分段\"而非\"全额\"</li>')
    parts.append('</ul></div>')
    parts.append('<div class="chapter-end">— 第2章完 · 共14题 · 自强不息 —</div>')

    html=f"""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"><title>第2章 选择的艺术</title><style>{CSS}</style></head><body>{chr(10).join(parts)}</body></html>"""
    out=BOOK_ROOT/"textbook"/"chapter02_print.html"
    out.write_text(html,encoding='utf-8')
    print(f"✅ Ch2: {len(html)} chars")

if __name__=="__main__":
    build_html()
