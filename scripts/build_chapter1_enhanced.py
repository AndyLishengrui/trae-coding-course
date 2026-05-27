#!/usr/bin/env python3
"""第1章 程序设计的第一个脚印(角色对话版) — 小鲁第一次打开TRAE"""
import json, re, os, sys
from pathlib import Path
BOOK_ROOT = Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(BOOK_ROOT / 'scripts'))

PROBLEMS = [
    {"nq":"NQ001","acw":1,"title":"A + B",
     "story":"小鲁第一次打开TRAE。AI助手弹出提示：\"你好，我是你的编程伙伴！想学编程，就从最简单的计算开始吧——输入两个整数，我来帮你算它们的和。\"小鲁半信半疑地输入了\"3 4\"……屏幕上出现了\"7\"。\"就这么简单？！\"小鲁惊讶地喊道。小华从旁边探过头来：\"没错！程序本质上就是三个步骤——输入数据、计算处理、输出结果。你刚刚写的，就是世界上最著名的'Hello World'在算法竞赛中的版本。\"",
     "input":"一行，两个整数A和B，用空格隔开。","output":"一个整数，即A+B的结果。",
     "sample_in":"3 4","sample_out":"7","constraint":"0 ≤ A, B ≤ 10⁸",
     "sol":"这是所有程序的基本骨架：读入→计算→输出。C++用cin/cout，Python用input/print。两种语言体现了不同的设计哲学——C++需要声明main函数和变量类型，Python则更直白，直接写逻辑即可。","tip":"Python的a,b=map(int,input().split())是处理空格分隔整数输入的标准写法。C++的cin>>a>>b自动跳过空白字符。记住这个模式，它将伴随你整个编程生涯。"},
    {"nq":"NQ002","acw":608,"title":"差",
     "story":"\"既然能做加法，那减法呢？乘法呢？\"小鲁迫不及待地问。小华笑着在纸上写下：\"A×B−C×D，四个数，先各自相乘，再相减。\"小鲁试着输入四个数……\"DIFERENCA = -26\"出现了！\"原来编程就是换个方式做数学题啊。\"小华点点头：\"从某种意义上说，是的——编程就是把数学思维转化为机器能理解的指令。\"",
     "input":"一行，四个整数A、B、C、D，用空格隔开。","output":"输出\"DIFERENCA = \"后跟计算结果。","sample_in":"5 6 7 8","sample_out":"DIFERENCA = -26","constraint":"−10⁴ ≤ A,B,C,D ≤ 10⁴",
     "sol":"按公式计算，注意运算顺序（先乘后减）。C++用int可满足范围。Python的int无范围限制。输出需要带前缀\"DIFERENCA = \"——这种\"前缀+结果\"的格式是OJ题目常见要求。","tip":"Python的f-string格式化：f\"DIFERENCA = {a*b-c*d}\"。f-string是Python 3.6+最推荐的格式化方式，比%和.format()更直观清晰。"},
    {"nq":"NQ003","acw":604,"title":"圆的面积",
     "story":"小嘉路过时看到了小鲁在练习编程。\"年轻人，你知道π吗？\"小嘉问。\"就是3.14159……\"小鲁回答。\"对，我在南洋经商时常常用到它——计算圆形的土地面积。来，写个程序，输入半径，算出圆的面积。\"小鲁照做了，屏幕上出现了\"A=12.5664\"。\"看，编程不只是做题——它能解决真实世界的问题。\"",
     "input":"一个浮点数r，表示圆的半径。","output":"输出\"A=\"后跟面积，保留4位小数。","sample_in":"2.00","sample_out":"A=12.5664","constraint":"0 < r ≤ 10000",
     "sol":"圆面积=π×r²。需要浮点数类型：C++的double，Python的float。C++用printf(\"%.4lf\")控制小数位；Python用f\"{area:.4f}\"。这是第一次用到实数精度控制。","tip":"C++两种格式化输出：C风格printf(\"%.4lf\",x)简洁精确；C++风格cout<<fixed<<setprecision(4)<<x类型安全。Python的f\"{x:.4f}\"最直观。"},
    {"nq":"NQ004","acw":606,"title":"平均数1",
     "story":"小鲁拿到了两个科目的成绩：一门权重3.5，一门7.5。\"哎，这加权平均怎么算来着？\"小华提醒他：\"(A×3.5+B×7.5)/(3.5+7.5)。注意分母是权重之和=11，不是科目数2——很多人都会搞错。\"\"原来如此！\"小鲁恍然大悟，\"就像奖学金评定，不同课程的重要程度不一样。\"",
     "input":"两行，每行一个浮点数（成绩A和B）。","output":"\"MEDIA = \"后跟加权平均分，保留5位小数。","sample_in":"5.0\n7.1","sample_out":"MEDIA = 6.43182","constraint":"0 ≤ A, B ≤ 10.0",
     "sol":"加权平均公式：(A×3.5+B×7.5)/(3.5+7.5)= (A×3.5+B×7.5)/11。分母是权重之和，不是题目数——这是加权平均最常见的陷阱。保留5位小数需要精确的浮点格式化。","tip":"C++所有浮点字面量默认double。Python的/总是返回浮点数。注意：3.5+7.5=11.0不是2——这与普通平均完全不同。"},
    {"nq":"NQ005","acw":609,"title":"工资",
     "story":"小鲁暑假打工了！他需要计算自己的工资——员工编号25，工作了100小时，时薪5.50元。\"帮我写个程序算总工资！\"小栋接过键盘：\"工资=时数×时薪。输入包含整数和浮点数混合类型。注意输出两行——第一行编号，第二行工资（保留两位小数）。\"",
     "input":"三行：编号（整数）、时数（整数）、时薪（浮点数）。","output":"\"NUMBER = X\"换行\"SALARY = U$ XX.XX\"。","sample_in":"25\n100\n5.50","sample_out":"NUMBER = 25\nSALARY = U$ 550.00","constraint":"1 ≤ 编号 ≤ 100, 1 ≤ 时数 ≤ 200, 1 ≤ 时薪 ≤ 50",
     "sol":"工资=时数×时薪。混合使用int和double/float：C++的scanf可精确控制格式，Python逐行读取更清晰。输出两行各自需要格式化。","tip":"C++: scanf(\"%d%d%lf\",&n,&h,&m)精确控制混合输入。Python: 逐行int(input())和float(input())更安全清晰。"},
    {"nq":"NQ006","acw":615,"title":"油耗",
     "story":"小鲁买了一辆二手车，想测试它的油耗。他记录了行驶500公里用了35升油。\"每升能跑多少公里？\"500÷35≈14.286。小华说：\"这是除法运算——但注意，要用浮点数除法，否则C++会做整数除法截断。Python的/自动浮点，安全得多。\"",
     "input":"两行：距离（浮点数, km）、汽油量（浮点数, L）。","output":"每升公里数，保留3位小数，后跟\" km/l\"。","sample_in":"500\n35.0","sample_out":"14.286 km/l","constraint":"1 ≤ 距离 ≤ 10⁶, 0 < 汽油量 ≤ 10⁵",
     "sol":"燃油效率=距离÷汽油量。浮点除法，保留3位小数。C++中距离如果是整数需先转double。Python的/自动浮点——这是两种语言在处理除法上的核心差异。","tip":"C++整数除法陷阱：5/2=2不是2.5！必须写成5.0/2或(double)5/2。Python的5/2=2.5自动浮点——这也是C++初学者最易犯的错误之一。"},
    {"nq":"NQ007","acw":616,"title":"两点间的距离",
     "story":"小鲁用坐标纸画了两个点：P1(1,7)和P2(5,9)。\"这两点之间距离是多少？\"小栋说：\"欧几里得距离=√((x1-x2)²+(y1-y2)²)。这需要用到数学库的sqrt函数——编程第一次用到外部库。\"",
     "input":"一行，四个浮点数x1 y1 x2 y2。","output":"两点间距离，保留4位小数。","sample_in":"1.0 7.0 5.0 9.0","sample_out":"4.4721","constraint":"−10⁹ ≤ 坐标 ≤ 10⁹",
     "sol":"距离=√((x1−x2)²+(y1−y2)²)。C++需要#include<cmath>，Python需import math。注意使用double而非float（精度更高）。保留4位小数。","tip":"C++链接时需要-lm（某些编译器）。Python的import math后调用math.sqrt()。f\"{dist:.4f}\"格式化输出。这是数学库使用的第一课。"},
    {"nq":"NQ008","acw":653,"title":"钞票",
     "story":"小鲁去银行取576元，ATM机吐出了：5张100、1张50、1张20、0张10、1张5、0张2、1张1。\"为什么是这些面额？\"小华解释道：\"这是贪心策略——从最大面额开始，能用多少用多少，余下的交给更小面额。你看，100元用5张还剩76，50元用1张还剩26……\"小鲁瞪大了眼睛：\"这算法好聪明！\"",
     "input":"一个整数N。","output":"第一行N，然后7行按面额100到1输出张数。","sample_in":"576","sample_out":"576\n5 nota(s) de R$ 100,00\n1 nota(s) de R$ 50,00\n1 nota(s) de R$ 20,00\n0 nota(s) de R$ 10,00\n1 nota(s) de R$ 5,00\n0 nota(s) de R$ 2,00\n1 nota(s) de R$ 1,00","constraint":"0 < N < 10⁶",
     "sol":"贪心策略：count=N/face_value; N%=face_value。C++写了7段重复代码，Python用列表+循环消除了重复——这是本课最重要的工程思维：用数据结构消除重复逻辑。","tip":"Python: for v in [100,50,20,10,5,2,1]: print(f\"{n//v} nota(s) de R$ {v},00\"); n%=v。7行→3行，这就是\"用数据结构替代重复代码\"的力量。"},
    {"nq":"NQ009","acw":654,"title":"时间转换",
     "story":"\"556秒等于多少小时多少分钟多少秒？\"小鲁拿着计时器犯了难。\"这简单——\"小华说，\"556÷3600=0小时，余556。556÷60=9分钟，余16。所以是0:9:16。Python有个divmod()函数可以一次得到商和余数，特别方便。\"",
     "input":"一个整数N。","output":"HH:MM:SS格式。","sample_in":"556","sample_out":"0:9:16","constraint":"0 ≤ N ≤ 10⁶",
     "sol":"时=N/3600, 分=N%3600/60, 秒=N%60。Python的divmod(a,b)返回(商,余数)元组：h,r=divmod(n,3600); m,s=divmod(r,60)。","tip":"Python的divmod()优雅解包接收。C++需分别计算/和%。divmod是Python\"电池已包含\"哲学的体现——常见操作都内置了。"},
    {"nq":"NQ010","acw":605,"title":"简单乘积",
     "story":"\"A+B已经会了，A×B呢？\"小鲁跃跃欲试。小华把键盘推过去：\"你自己来。把第一题的代码复制过来，把+改成*，再加个'PROD = '前缀。\"小鲁三下五除二就搞定了——\"原来修改已有代码比从零开始快这么多！\"","input":"两行，每行一个整数。","output":"\"PROD = \"后跟乘积。","sample_in":"3\n9","sample_out":"PROD = 27","constraint":"−10⁴ ≤ A, B ≤ 10⁴","sol":"与NQ001结构完全相同，+改成*，加\"PROD = \"前缀即可。这是让学生独立完成\"修改→编译→AC\"完整流程的训练题。","tip":"修改已有代码是最实用的编程技能之一。用TRAE打开NQ001的代码，告诉AI\"把加法改成乘法，加PROD前缀\"——这就是AI协同编程的日常。"},
    {"nq":"NQ011","acw":611,"title":"简单计算",
     "story":"小鲁去买东西：产品编号12，买1个，单价5.30元。\"总共多少钱？\"小栋说：\"数量×单价。注意输入混合了整数（编号和数量）和浮点数（单价）。int×float自动转换为float——数据类型会自动'提升'到更精确的类型。\"",
     "input":"第一行：code和quantity（整数）。第二行：price（浮点数）。","output":"\"VALOR A PAGAR: R$ XX.XX\"。","sample_in":"12 1\n5.30","sample_out":"VALOR A PAGAR: R$ 5.30","constraint":"1 ≤ code ≤ 100, 1 ≤ quantity ≤ 100","sol":"总价=数量×单价。int×float自动提升为float/double。C++中int×double→double。Python中int×float→float。类型提升规则确保精度不丢失。","tip":"类型自动提升：宽类型\"吸收\"窄类型。记住这个原则：运算中最宽的类型决定结果类型。"},
    {"nq":"NQ012","acw":612,"title":"球的体积",
     "story":"小鲁在物理实验课上测量了一个半径3cm的球。\"这个球的体积是多少？\"小华写下公式：V=(4/3)πr³。\"注意——C++中4/3等于1不是1.333！整数除法会截断。必须写成4.0/3.0。这是C++初学者最经典的陷阱。\"","input":"一个整数r。","output":"\"VOLUME = \"后跟体积，保留3位小数。","sample_in":"3","sample_out":"VOLUME = 113.097","constraint":"1 ≤ r ≤ 1000","sol":"V=(4.0/3.0)×π×r³。C++中4/3=1(整数除法)！必须写成4.0/3.0。Python自动浮点无此问题。这是C++整数除法的经典陷阱。","tip":"C++的4/3=1是初学者最容易犯的错误。任何涉及除法的表达式，至少保证一个操作数是浮点数。Python没有这个烦恼。"},
    {"nq":"NQ013","acw":613,"title":"面积",
     "story":"\"一题算三种图形的面积——三角形A*C/2、圆π*C²、梯形(A+B)*C/2。注意A、B、C在不同公式中担任不同的角色！\"小华提醒道。\"这题考察的是细心——公式本身都很简单，但把三个公式的正确参数搞对才是关键。\"","input":"一行，三个浮点数A、B、C。","output":"三行：TRIANGULO/CIRCULO/TRAPEZIO，各保留3位小数。","sample_in":"3.0 4.0 5.2","sample_out":"TRIANGULO: 7.800\nCIRCULO: 84.949\nTRAPEZIO: 18.200","constraint":"0 < A, B, C ≤ 100","sol":"三个独立公式，每个一行计算一行输出。三角形=A*C/2，圆=3.14159*C²，梯形=(A+B)*C/2。PI=3.14159。代码组织能力训练。","tip":"一道题含三个计算是测试代码组织能力的好题。每个面积独立计算、独立输出，清晰直观。多使用const/常量避免魔法数字。"},
    {"nq":"NQ014","acw":614,"title":"最大值",
     "story":"小鲁拿到三份考试成绩：7分、14分、106分。\"最高分是多少？\"\"max(7,14,106)=106。\"小鲁用Python的max(a,b,c)一行搞定。\"Python太方便了！\"小华说：\"C++需要max({a,b,c})（C++11初始化列表）或嵌套max。Python的'电池已包含'设计哲学——常用的都给你准备好了。\"",
     "input":"一行，三个整数。","output":"一个整数，即最大值。","sample_in":"7 14 106","sample_out":"106","constraint":"−10⁹ ≤ a, b, c ≤ 10⁹",
     "sol":"Python的max(a,b,c)接收多参数。C++的max({a,b,c})需C++11和<algorithm>，或嵌套max(a,max(b,c))。体现了Python\"电池已包含\"vs C++\"按需引入\"的设计差异。","tip":"Python内置max/min/sum/abs等函数无需import。C++需要#include<algorithm>。两种语言的哲学差异在这一题得到完美体现。"},
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
body{font-family:"PingFang SC","Hiragino Sans GB","Noto Serif CJK SC","STSong",serif;font-size:9.5pt;line-height:1.7;color:#222;string-set:chapter"第1章 程序设计的第一个脚印——变量、输入输出与顺序结构"}
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
    parts.append('<div class="chapter-title">程序设计的第一个脚印</div>')
    parts.append('<div class="chapter-subtitle">变量、输入输出与顺序结构 · 14题 · C++ &amp; Python 双语对照</div>')
    parts.append('<div class="preface">')
    parts.append('<p>九月，厦门大学芙蓉湖畔，凤凰花开得正红。小鲁背着新买的笔记本电脑走进海韵园实验室——今天是他的第一节编程课。</p>')
    parts.append('<p>\"编程？那不是数学天才华罗庚才玩的东西吗？\"小鲁心里打鼓。但当他看到屏幕上第一个程序的输出结果时，他愣住了：\"这么简单？我也会！\"</p>')
    parts.append('<p>本章14道题，从最简单的A+B开始，到多类型混合运算。你会认识小鲁、小华（数学天才）、小嘉（校主精神）和小栋（工程师），跟着他们的对话，一步步踏入编程的世界。<strong>记住：编程不难，难的是开始。现在，打开TRAE，写下你的第一行代码吧。</strong></p>')
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
        cpp=CODE_CACHE.get(p['acw'],f'// AcWing {p["acw"]}')
        py=PY_CACHE.get(p['acw'],'# Python solution')
        pb.append('<div class="code-dual">')
        pb.append(f'<div class="code-col"><div class="lang-badge">C++</div><pre>{hl(cpp,CppLexer(),CPP_FMT)}</pre></div>')
        pb.append(f'<div class="code-col"><div class="lang-badge">Python</div><pre>{hl(py,PythonLexer(),PY_FMT)}</pre></div>')
        pb.append('</div></div><hr class="section-divider">')
        parts.append('\n'.join(pb))

    parts.append('<div class="chapter-summary"><h3>本章知识点总结</h3><ul>')
    parts.append('<li><strong>程序三要素：</strong>输入(Input)→处理(Process)→输出(Output)</li>')
    parts.append('<li><strong>变量与类型：</strong>C++声明类型(int/double)，Python动态类型</li>')
    parts.append('<li><strong>格式化输出：</strong>C++用printf，Python用f-string</li>')
    parts.append('<li><strong>常见陷阱：</strong>C++整数除法截断(4/3=1)，Python无此问题</li>')
    parts.append('<li><strong>厦大校训：</strong>自强不息——编程之路始于足下，每一步都是进步</li>')
    parts.append('</ul></div>')
    parts.append('<div class="chapter-end">— 第1章完 · 共14题 · 凤凰花开 · 自强不息 —</div>')

    html=f"""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"><title>第1章 程序设计的第一个脚印</title><style>{CSS}</style></head><body>{chr(10).join(parts)}</body></html>"""
    out=BOOK_ROOT/"textbook"/"chapter01_print.html"
    out.write_text(html,encoding='utf-8')
    print(f"✅ Ch1 dialog version: {len(html)} chars")

if __name__=="__main__":
    build_html()
