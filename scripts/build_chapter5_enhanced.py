#!/usr/bin/env python3
"""第5章 矩阵的舞蹈(角色对话版) — 多维数组与矩阵模式"""
import json, re, os, sys
from pathlib import Path
BOOK_ROOT = Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(BOOK_ROOT / 'scripts'))

PROBLEMS = [
    {"nq":"NQ055","acw":745,"title":"数组的右上半部分",
     "story":"小鲁拿着一支荧光笔，在一张12×12的格子纸上涂色：右上三角。\"j>i——第0行从第1列到第11列，第1行从第2列到第11列……\"小鲁一边涂一边念叨。小华走过来：\"你在画什么？\"\"我在数右上三角有多少个元素！总共12×12减去对角线12，再除2——就是66个。\"小华笑道：\"你已经发现了三角区域的核心：找到行和列的关系表达式，剩下的循环就水到渠成。\"",
     "input":"第一行操作类型(S/M)。然后144个浮点数（逐行读入）。","output":"结果保留1位小数。S输出和，M输出平均值。",
     "sample_in":"S\n(144个浮点数...)","sample_out":"(sum,1 decimal)","constraint":"矩阵元素−10⁶到10⁶",
     "sol":"右上三角：j>i。双层循环遍历矩阵，当j>i时累加。不包括对角线。66个元素。S求总和，M求平均时除以66（注意不是144）。区域遍历是矩阵题的灵魂——关键在于找到正确的行列关系表达式。",
     "tip":"右上三角条件：j>i。共有元素数=(12×12−12)/2=66。C++用double型累加，注意不要用int。Python的float是双精度。"},
    {"nq":"NQ056","acw":747,"title":"数组的左上半部分",
     "story":"小鲁转向左上三角：\"这次应该用j<11-i吧？反对角线以上……\"小华在纸上画了一笔：\"看，反对角线满足i+j=11。左上三角就是j<11-i。但还有另外一种理解——它和右上三角本质上是同一个形状，只是参考线不一样。一个用主对角线(j>i)，一个用反对角线(j<11-i)。两题放一起对比，四种三角区域的条件就清晰了。\"",
     "input":"操作类型(S/M)+144浮点数。","output":"保留1位小数。","sample_in":"S\n(144...)","sample_out":"(sum,1 decimal)","constraint":"同NQ055",
     "sol":"左上三角：j<11-i（反对角线以上）。反对角线条件：i+j=11。元素数量也是66。将四个三角区域的遍历条件对比理解，是掌握矩阵区域操作的关键——j>i（右上）、j<i（左下）、i+j<11（左上）、i+j>11（右下）。",
     "tip":"反对角线条件：i+j==n-1（n=12时为11）。左上三角用<。四个区域条件对称且互补，理解这一规律后所有矩阵三角题迎刃而解。"},
    {"nq":"NQ057","acw":749,"title":"数组的上方区域",
     "story":"\"等等——'上方区域'又是什么？\"小鲁挠着头。小栋在屏幕上画了一个\"八\"字形：\"你看，把12×12矩阵的上半部分，去掉左边和右边的两个三角——剩下的就是上方区域。它其实是两个条件的交集：既在主对角线之上(i<j)，又在反对角线之上(i+j<11)。只有30个元素。\"\"双重条件！\"小鲁眼前一新，\"这就是用两个数学表达式精确切割一个小区域。\"",
     "input":"操作类型(S/M)+144浮点数。","output":"保留1位小数。","sample_in":"S\n(144...)","sample_out":"(sum,1 decimal)","constraint":"同NQ055",
     "sol":"上方区域是两个三角的交集：i<j（主对角线之上）且i+j<11（反对角线之上）。30个元素——矩阵的一半再减半。这种双重条件判断展示了用数学表达式精确描述区域的能力。",
     "tip":"交集条件：i<j and i+j<11。从\"单一条件描述三角\"到\"两个条件交集描述更小区域\"，是逻辑思维和代码能力的双重进阶。"},
    {"nq":"NQ058","acw":751,"title":"数组的左方区域",
     "story":"\"左边区域呢？\"小鲁问。小华说：\"对称的！把上方区域的j>i改成j<i就行——左方区域=j<i且j<11-i。\"小鲁恍然大悟：\"所以上下左右四个区域，其实是通过交换i和j的角色、变换关系符方向得到的——就像一个魔方，每一面都是对应的。掌握对称性，四道题瞬间变成一道。\"",
     "input":"操作类型(S/M)+144浮点数。","output":"保留1位小数。","sample_in":"S\n(144...)","sample_out":"(sum,1 decimal)","constraint":"同NQ055",
     "sol":"左方区域与上方区域对称：将条件改为j<i且i+j<11。观察NQ057和NQ058的条件——j和i的角色互换。这种对称模式是理解多维数组遍历的基础。",
     "tip":"左右对称：互换i和j的角色。上方=去掉左右三角的上部，左方=去掉上下三角的左部。对称思维是编程中的强大工具——写一遍代码，改一行条件就能得到四种区域的遍历。"},
    {"nq":"NQ059","acw":753,"title":"平方矩阵I",
     "story":"小嘉走进教室，手里拿着一张回字形的图纸：\"这在南洋叫'同心方'——外面一圈是1，往里一圈是2，再往里是3……最中心的值是min(N+1,N+1, N, N)+1。\"小鲁看得目瞪口呆：\"这么复杂的图案，用一个公式就能生成？！\"小华解释：\"每个位置的值=到四条边的最近距离+1。外层距离0→值1，往里一层距离1→值2。理解这个'距离模型'比写100行if更重要。\"",
     "input":"多个整数N，以0结束。","output":"每个矩阵占N行，每个数占3字符宽度右对齐。矩阵间空行。",
     "sample_in":"1\n2\n3\n0","sample_out":"  1\n\n  1  1\n  1  1\n\n  1  1  1\n  1  2  1\n  1  1  1","constraint":"1≤N≤100",
     "sol":"数学公式法：val=min(i,j,n-1-i,n-1-j)+1（0-indexed）。这个公式的物理意义：每个位置的值等于它到四条边的最短距离加1。最外层距离为0→值=1，往里一层距离为1→值=2，以此类推。理解公式比手写模拟更体现编程智慧。",
     "tip":"到四条边的距离：上i、左j、下n-1-i、右n-1-j。取最小值+1即为该位置的值。这个公式体现了\"数学建模\"的力量——用数学语言描述复杂的几何规律。"},
    {"nq":"NQ060","acw":748,"title":"数组的右下半部分",
     "story":"小鲁拿着一面镜子放在矩阵的左上角——\"如果从左上三角对称过去……\"小华笑道：\"没错！右上三角(j>i)的对称是左下三角(j<i)，左上三角(j<11-i)的对称是右下三角(i+j>10)。四题八遍的遍历模式，如果用'条件表达式'分类，一共就两种本质：主对角线分割和反对角线分割。\"",
     "input":"操作类型(S/M)+144浮点数。","output":"保留1位小数。","sample_in":"S\n(144...)","sample_out":"(sum,1 decimal)","constraint":"同NQ055",
     "sol":"右下三角：i+j>10。与NQ056的左上三角(i+j<11)对称。通过前6个矩阵三角题的系统训练，你应该已经掌握了区域遍历的核心技巧：找到正确的行列关系表达式。",
     "tip":"i+j>10与11-i-1通。矩阵遍历的4个三角区域至此全部覆盖。建议画一个5×5矩阵逐格验证——对着纸面比对着屏幕理解更快。"},
    {"nq":"NQ061","acw":746,"title":"数组的左下半部分",
     "story":"\"左下三角就是j<i——和右上三角j>i对称，只是方向反过来。\"小鲁总结说。小华欣慰地拍拍他：\"你已经从'逐题应付'升级到'找规律'了。记住这种感觉——以后学任何新算法，第一步都是找pattern：有没有对称性？能不能归约成已知问题？这是从学生到工程师的思维跃迁。\"",
     "input":"操作类型(S/M)+144浮点数。","output":"保留1位小数。","sample_in":"S\n(144...)","sample_out":"(sum,1 decimal)","constraint":"同NQ055",
     "sol":"左下三角：j<i。与右上三角(j>i)对称。遍历条件简单明了——i和j的大小关系决定位置归属。注意不包括主对角线。",
     "tip":"四个三角区域的条件总结：右上j>i、左下j<i、左上j<11-i、右下j>10-i。掌握这4个条件，所有标准矩阵三角题都不在话下。"},
    {"nq":"NQ062","acw":750,"title":"数组的下方区域",
     "story":"\"哎，下方区域的条件应该就是i>j且j>10-i吧？\"小鲁试着推导。\"等一下，j>10-i就是i+j>10。\"小栋纠正道。\"对对对，i>j且i+j>10——和上方区域的i<j且i+j<11完全对称！\"小鲁兴奋地在纸上比划：\"四个区域就像钟表上的12、3、6、9四个方向——每个区域都可以通过翻转和旋转得到其他三个。\"",
     "input":"操作类型(S/M)+144浮点数。","output":"保留1位小数。","sample_in":"S\n(144...)","sample_out":"(sum,1 decimal)","constraint":"同NQ055",
     "sol":"下方区域：i>j且i+j>10。与上方区域(i<j且i+j<11)对称。至此8道矩阵题全部完成——4个三角区域+2个交集区域+2个对角区域+蛇形矩阵。",
     "tip":"对称总结：上方(i<j,i+j<11)、下方(i>j,i+j>10)、左方(j<i,i+j<11)、右方(j>i,i+j>10)。四个区域构成一个完整的\"口\"字形框架。"},
    {"nq":"NQ063","acw":752,"title":"数组的右方区域",
     "story":"小鲁把四道区域题全部AC后，看着屏幕上的\"Accepted\"，长出了一口气。\"8道矩阵区域遍历题全部完成了！\"小华说：\"总结一下——你真正学到了什么？不是8个条件表达式，而是'精确描述几何区域的思维方式'。未来做图像处理、游戏碰撞检测、地图分析，用的还是这个思维——把视觉区域翻译成代码条件。\"",
     "input":"操作类型(S/M)+144浮点数。","output":"保留1位小数。","sample_in":"S\n(144...)","sample_out":"(sum,1 decimal)","constraint":"同NQ055",
     "sol":"右方区域：j>i且i+j>10。30个元素。至此矩阵区域遍历全部完成。8道题的变化本质是条件表达式的组合。掌握了规律，任何形状的区域都能精确描述。",
     "tip":"四个\"口\"字区域全部完成后，你的二维数组遍历能力已经达到面试水平。Key takeaway：精确的行列条件表达式=矩阵操作的全部。"},
    {"nq":"NQ064","acw":754,"title":"平方矩阵II",
     "story":"\"这道比上一道更简单！\"小鲁看着平方矩阵II的模式：对角线是1，往外一层是2，再往外是3……\"这不就是看每个位置到对角线的距离吗？\"小华回答：\"对！abs(i-j)就是到对角线的'曼哈顿距离'——对角线上abs(i-j)=0→值0+1=1，偏离一格abs=1→值1+1=2。两种平方矩阵展示了两种数学建模：一个是到四条边的距离，一个是到对角线的距离。\"",
     "input":"多个整数N（0结束）。","output":"N×N矩阵，每个数占3字符宽。矩阵间空行。",
     "sample_in":"3\n0","sample_out":"  1  2  3\n  2  1  2\n  3  2  1","constraint":"1≤N≤100",
     "sol":"|i-j|+1公式产生以主对角线为对称轴的矩阵。对角线上|i-j|=0→值=1，离对角线每远一步值增加1。这比平方矩阵I的\"四边距离\"公式更简单，展示了另一种数学建模方式。",
     "tip":"abs(i-j)+1。C++用stdlib的abs()，Python内置abs()。注意绝对值函数对负数的处理——自动取正。这种\"距离模型\"在矩阵题中非常常见。"},
    {"nq":"NQ065","acw":755,"title":"平方矩阵III",
     "story":"小鲁看着第三个平方矩阵：2^0, 2^1, 2^2... \"这是指数增长！\"\"对！\"小华说，\"两个技巧：第一，用位运算1<<(i+j)比pow(2,i+j)快很多；第二，N≤15的限制是精心设计的——N=15时最大值2^28≈2.68亿，刚好在int32范围内。如果N再大就要用long long甚至大整数了。题目设计者考虑得很周全。\"",
     "input":"多个整数N（0结束）。","output":"每个数右对齐到最大数的宽度+1。矩阵间空行。",
     "sample_in":"3\n0","sample_out":"  1  2  4\n  2  4  8\n  4  8 16","constraint":"1≤N≤15",
     "sol":"2^(i+j)模式。C++用1<<(i+j)位运算高效计算2的幂。Python可以2**(i+j)或1<<(i+j)。右对齐宽度=最长数字的位数+1。注意N≤15的限制：N=15时2^28≈2.68×10⁸(9位数)。",
     "tip":"C++的1<<k比pow(2,k)快得多。Python的2**k和1<<k性能相近。格式化右对齐：Python的f'{x:{w}d}'，C++的setw(w)。"},
    {"nq":"NQ066","acw":756,"title":"蛇形矩阵",
     "story":"\"最后一道是大boss——蛇形矩阵！\"小鲁聚精会神地盯着屏幕。小华拿出了他的'镇山法宝'：\"四向数组：dx=[0,1,0,-1], dy=[1,0,-1,0]——分别代表右、下、左、上。从(0,0)出发向右走，撞墙或遇到已填的格子就顺时针转90度。方向数组是网格类问题的屠龙刀。\"小栋补充道：\"其实你玩的贪吃蛇游戏引擎，底层就是这个算法。\"",
     "input":"一行两个整数n和m。","output":"n行m列的蛇形矩阵。",
     "sample_in":"3 3","sample_out":"1 2 3\n8 9 4\n7 6 5","constraint":"1≤n,m≤100",
     "sol":"方向数组+边界检测。dx=[0,1,0,-1], dy=[1,0,-1,0]依次控制→↓←↑。撞墙或已填则转向d=(d+1)%4。while循环填充所有格子。方向数组是解决螺旋/蛇形/遍历类问题的通用模板——只需改变方向顺序就能实现不同的遍历模式。",
     "tip":"方向数组是处理网格遍历的万能钥匙。记住4个方向的顺序和dx/dy的对应关系。Python中提前分配二维数组：[[0]*m for _ in range(n)]（注意不能用[[0]*m]*n——那是浅拷贝的经典陷阱！）。"},
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
body{font-family:"PingFang SC","Hiragino Sans GB","Noto Serif CJK SC","STSong",serif;font-size:9.5pt;line-height:1.7;color:#222;string-set:chapter"第5章 矩阵的舞蹈——多维数组与矩阵模式"}
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
    parts.append('<div class="chapter-title">矩阵的舞蹈</div>')
    parts.append('<div class="chapter-subtitle">多维数组与矩阵模式 · 12题 · C++ &amp; Python 双语对照</div>')
    parts.append('<div class="preface">')
    parts.append('<p>第四周结束，小鲁已经能熟练地操作一维数组了。但小华告诉他：\"一维数组只是第一步——真实世界的数据很少是一条线。想想电子表格、数码照片、游戏棋盘……这些都是<strong>二维</strong>的。\"小鲁若有所思：\"所以……我需要学会在行列之间跳舞？\"</p>')
    parts.append('<p>本章12道题分三个板块：<strong>区域遍历</strong>（NQ055-063）——学会用行列关系精确切割矩阵区域；<strong>模式填充</strong>（NQ059,064,065）——用数学公式一行替代几十行循环，体验\"数学建模\"的力量；<strong>蛇形遍历</strong>（NQ066）——方向数组的经典实战，贪吃蛇游戏引擎的底层算法。</p>')
    parts.append('<h3>本章角色</h3>')
    parts.append('<p>🧑‍🎓 <strong>小鲁</strong>（初学者）· 正在经历从\"逐题应付\"到\"寻找规律\"的思维跃迁</p>')
    parts.append('<p>🧠 <strong>小华</strong>（算法高手）· ACM竞赛队队长，用\"对称性\"一句话解决四道相似的题</p>')
    parts.append('<p>🏗️ <strong>小栋</strong>（工程师）· 把枯燥的矩阵遍历与游戏引擎、图像处理等实际应用联系起来</p>')
    parts.append('<p>🏛️ <strong>小嘉</strong>（校主精神）· 带着\"同心方\"从南洋归来，用数学和编程的交汇点启发学生</p>')
    parts.append('</div>')
    parts.append('<div class="knowledge-box"><div class="k-title">🧭 矩阵三角区域速查表（12×12矩阵）</div>')
    parts.append('<ul><li>↗ <strong>右上三角</strong>：j > i（不含对角线，66个元素）</li><li>↖ <strong>左上三角</strong>：j < 11-i（不含反对角线，66个元素）</li>')
    parts.append('<li>↙ <strong>左下三角</strong>：j < i（不含对角线，66个元素）</li><li>↘ <strong>右下三角</strong>：i+j > 10（66个元素）</li>')
    parts.append('<li>⬆ <strong>上方区域</strong>：i < j 且 i+j < 11（30个元素）</li><li>⬇ <strong>下方区域</strong>：i > j 且 i+j > 10（30个元素）</li>')
    parts.append('<li>⬅ <strong>左方区域</strong>：j < i 且 i+j < 11（30个元素）</li><li>➡ <strong>右方区域</strong>：j > i 且 i+j > 10（30个元素）</li></ul>')
    parts.append('<p><strong>核心心法：</strong>四个三角区域通过两种对角线分割（主对角线、反对角线），四个\"口\"字区域是两个三角的交集。掌握对称性=一道题的功夫解决四道题。</p></div>')

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
    parts.append('<li><strong>8种矩阵区域：</strong>4个三角（各66元素）+ 4个\"口\"字边（各30元素）= 精确遍历矩阵任意形状</li>')
    parts.append('<li><strong>3种填充模式：</strong>四边距离min公式、对角线距离abs公式、2的指数幂模式——用数学替代模拟</li>')
    parts.append('<li><strong>方向数组：</strong>dx=[0,1,0,-1], dy=[1,0,-1,0] → 控制四个方向旋转，蛇形/螺旋/遍历通用模板</li>')
    parts.append('<li><strong>对称思维：</strong>上下、左右区域只是i和j角色的互换。找规律>逐题应付——从学生到工程师的思维跃迁</li>')
    parts.append('<li><strong>关键技巧：</strong>Python二维列表[[0]*m for _ in range(n)]（不能用*操作符——那是浅拷贝陷阱！）</li>')
    parts.append('<li><strong>厦大精神：</strong>自强不息，止于至善。12道矩阵题过后，你的多维数组能力已经达到面试水平。</li>')
    parts.append('</ul></div>')
    parts.append('<div class="chapter-end">— 第5章完 · 共12题 · 自强不息 —</div>')

    html=f"""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"><title>第5章 矩阵的舞蹈</title><style>{CSS}</style></head><body>{chr(10).join(parts)}</body></html>"""
    out=BOOK_ROOT/"textbook"/"chapter05_print.html"
    out.write_text(html,encoding='utf-8')
    print(f"✅ Ch5 dialog version: {len(html)} chars")

if __name__=="__main__":
    build_html()
