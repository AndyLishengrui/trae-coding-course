#!/usr/bin/env python3
"""第6章 字符的世界(角色对话版) — 字符串处理"""
import json, re, os, sys
from pathlib import Path
BOOK_ROOT = Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(BOOK_ROOT / 'scripts'))

PROBLEMS = [
    {"nq":"NQ067","acw":760,"title":"字符串长度",
     "story":"小鲁输入了一串文字，想知道它有多长。\"这还用编程？数一下不就行了……\"话没说完，小华就打断了他：\"如果有人给你一本1000页的书，你一个字一个字数吗？Python用len(s)一秒搞定。C++用s.length()或strlen()。字符串长度是所有文本处理的基础——搜索、替换、截取，第一步永远是知道字符串有多长。\"",
     "input":"一行，一个字符串（不超过100字符）。","output":"一个整数，表示字符串长度。",
     "sample_in":"hello world","sample_out":"11","constraint":"字符串长度≤100",
     "sol":"字符串长度是最基本的信息。Python: len(s)，C++: s.length()或s.size()（string类）或strlen(s)（C风格char数组）。注意空格也算长度——\"hello world\"是11个字符不是10个。",
     "tip":"Python的len()适用于所有序列类型（字符串/列表/元组），是一个全局函数而非方法。C++的length()和size()对于string完全等价。C风格字符串用strlen()但需要#include<cstring>。"},
    {"nq":"NQ068","acw":761,"title":"字符串中的数字个数",
     "story":"\"帮我统计这篇文章里有多少个数字字符……\"小栋拿着一份报纸对小鲁说。小鲁刚要用手指一个一个点，小华按住他：\"遍历字符串的每个字符，用isdigit()判断是不是数字。Python一行搞定——sum(c.isdigit() for c in s)。C++则是for循环判断c>='0' && c<='9'。\"小鲁这才意识到字符串里的每个字符都可以被'分类'——数字、字母、空格、标点……每种分类都有对应的判断方法。",
     "input":"一行，一个字符串（不超过100字符）。","output":"字符串中数字字符的个数。",
     "sample_in":"I am 20 years old.","sample_out":"2","constraint":"字符串长度≤100",
     "sol":"分类统计模式：遍历每个字符，判断是否为数字（'0'-'9'）。Python: sum(c.isdigit() for c in s)，C++: 循环+条件判断。isdigit()是Python字符串方法的强大之处。",
     "tip":"Python字符方法：s.isdigit()（数字）、s.isalpha()（字母）、s.isalnum()（字母数字）、s.isspace()（空白）。记住这些方法能让字符串处理效率翻倍。"},
    {"nq":"NQ069","acw":763,"title":"循环相克令",
     "story":"小鲁和小栋在玩\"锤子剪刀布\"的游戏——不过他们的版本叫\"Hunter/Bear/Gun\"。\"猎人怕熊，熊怕枪，枪怕猎人——形成一个循环克制关系。\"小华说，\"这种循环相克的问题可以用字符串比较解决。但更优雅的是数学方法：把每个角色映射成0/1/2，然后胜者=(a-b+3)%3。\"小鲁惊奇地发现——一个简单的取模竟然能判断所有博弈结果。",
     "input":"一个整数N。然后N行每行两个字符串（Hunter/Bear/Gun）。","output":"对每行输出Player1赢还是Player2赢。",
     "sample_in":"3\nHunter Bear\nBear Hunter\nGun Bear","sample_out":"Player2\nPlayer1\nPlayer1","constraint":"1 ≤ N ≤ 100",
     "sol":"字符串比较法：if-elif分支判断所有9种组合。数学法：将三个角色映射为0,1,2，则P1赢当且仅当(a-b+3)%3==2。数学法将9个if压缩成一行——用数学替代分支的艺术。",
     "tip":"Python用法：dic={'Hunter':0,'Bear':1,'Gun':2}，然后if (dic[a]-dic[b]+3)%3==2: P1赢。C++用map<string,int>或直接if-else。理解取模在循环问题中的通用性更关键。"},
    {"nq":"NQ070","acw":765,"title":"字符串加空格",
     "story":"小鲁在排版一个标题——需要给每个字符之间加上空格。\"这要手动打多少个空格……\"小华笑了：\"Python的join()方法就是为此而生的：' '.join(s)——用空格把字符串的每个字符连接起来。C++需要遍历输出每个字符后面加空格然后去掉末尾空格。两种语言对比，Python的join()堪称字符串处理的魔法。\"",
     "input":"一行，一个字符串（不含空格）。","output":"每个字符间加空格后的字符串。",
     "sample_in":"hello","sample_out":"h e l l o","constraint":"字符串长度≤100",
     "sol":"join()方法将一个可迭代对象用分隔符连接。' '.join(s)把s的每个字符用空格连接。C++版需要for循环逐个输出注意首尾空格。Python的join()是最常用的字符串操作之一。",
     "tip":"Python的join()和split()是互逆操作。'sep'.join(list)把列表用sep连起来，str.split(sep)把字符串按sep拆开。这两个方法是字符串处理的基础中的基础。"},
    {"nq":"NQ071","acw":769,"title":"替换字符",
     "story":"小鲁在编辑文本时发现有些字符需要换成别的：\"比如把所有的'a'换成'b'……\"小华说：\"Python直接s.replace(old, new)一行搞定。C++要手动遍历替换。不过注意——Python的字符串是不可变的，replace()返回的是新字符串，原字符串不变。理解'不可变性'是理解Python字符串操作的关键。\"",
     "input":"一行字符串（可能含空格）。然后一行，两个字符（要替换的和替换成的）。","output":"替换后的字符串。",
     "sample_in":"hello world\no e","sample_out":"helle werld","constraint":"字符串长度≤100",
     "sol":"字符替换：遍历每个字符，如果等于目标则输出新字符，否则原样输出。Python: s.replace(old, new)。C++: 用for+if或std::replace()。注意Python的字符串不可变性——replace()返回新的。",
     "tip":"Python字符串不可变意味着所有'修改'操作都返回新字符串。这保证了字符串的安全性（不会被意外修改），但创建大量新字符串时有性能开销。"},
    {"nq":"NQ072","acw":773,"title":"字符串插入",
     "story":"\"如果我想在字符串的第3个位置插入另一个字符串怎么办？\"小鲁问。小华说：\"拿到前面部分、后面部分，然后拼接：s[:p]+sub+s[p:]。注意位置p是从0开始还是从1开始——这是字符串操作中最容易出错的off-by-one问题。\"小鲁立刻想到：\"所以插入的本质就是'切片+拼接'——把字符串切成两段，中间塞进新内容。\"",
     "input":"三行：原字符串、要插入的字符串、插入位置。","output":"插入后的字符串。",
     "sample_in":"hello\nworld\n3","sample_out":"helworldlo","constraint":"字符串长度≤100，位置从0开始",
     "sol":"Python切片拼接：s[:p]+sub+s[p:]。C++: substr()取前后两部分再相加。切片是Python最优雅的特性之一——s[a:b]精确截取[a,b)区间，语义清晰。",
     "tip":"Python切片s[a:b]的区间是[a,b)（包含a不包含b）。插入位置p意味着新内容从p开始——s[:p]取p之前的字符，s[p:]取p及之后的字符。"},
    {"nq":"NQ073","acw":772,"title":"只出现一次的字符",
     "story":"\"我要在一段文字中找到第一个只出现一次的字符。\"小栋又在给小鲁出题。\"像'hello'里——'h','e','o'都只出现一次，但第一个是'h'。\"小华说：\"这需要两遍遍历：第一遍统计每个字符的出现次数，第二遍按顺序找出第一个次数为1的字符。Python用collections.Counter可以一行建好频次字典。\"",
     "input":"一个字符串。","output":"第一个只出现一次的字符的位置（1-indexed），如果没有则输出-1。",
     "sample_in":"hello","sample_out":"1","constraint":"字符串长度≤10⁵",
     "sol":"两遍遍历法：第一遍建立字符频次字典（Counter），第二遍按原字符串顺序查找第一个频次为1的字符。Python用Counter一键统计。注意频次统计不改变顺序——要按原串顺序输出。",
     "tip":"Python: from collections import Counter; cnt=Counter(s); for i,c in enumerate(s): if cnt[c]==1: print(i+1)。C++用int cnt[256]数组直接作哈希表——字符ASCII值作为索引，O(1)频次查找。"},
    {"nq":"NQ074","acw":762,"title":"字符串匹配",
     "story":"\"在一大段文字里，找一小段模式——这就是字符串匹配。\"小华在白板上写着，\"比如在'abababa'里找'aba'。最朴素的方法：从每个位置开始，逐个字符比较——这叫暴力匹配，O(n×m)。后续你会学到更高效的KMP算法，但暴力匹配首先让你理解匹配的本质：滑动窗口+逐位比较。\"",
     "input":"两行：文本串T和模式串P。","output":"P在T中第一次出现的位置（1-indexed），若不存在输出-1。",
     "sample_in":"abababa\naba","sample_out":"1","constraint":"1 ≤ |T|,|P| ≤ 100",
     "sol":"暴力匹配：对于i从0到n-m，检查T从i开始的m个字符是否等于P。Python直接用T.find(P)一行，但手写暴力匹配理解原理更重要。find()返回首次出现位置（-1表示不存在）。",
     "tip":"Python的T.find(P)底层是高效的混合算法（Boyer-Moore-Horspool），比手写暴力快得多。但手写暴力匹配是KMP和BM算法的基础——理解\"为什么慢\"才能理解\"如何变快\"。"},
    {"nq":"NQ075","acw":767,"title":"信息加密",
     "story":"小鲁对密码学产生了兴趣：\"如果能写个程序把每个字母往后移1位——a变b，b变c……z回到a——那就成了一个最简单的加密程序！\"小华说：\"这就是凯撒密码，两千年前的加密方法。编程关键是处理循环——'z'+1要变回'a'。可以用取模：(c-'a'+1)%26+'a'。大写和小写分别处理。\"",
     "input":"一个字符串（只含字母和空格）。","output":"字母后移1位，空格不变。",
     "sample_in":"abc XYZ","sample_out":"bcd YZA","constraint":"字符串长度≤100",
     "sol":"字符偏移+循环回绕。对字母：c='a'+(c-'a'+1)%26。大写字母同理用'A'和'Z'。非字母（空格等）原样保留。用isalpha()判断是否为字母，用isupper()/islower()判断大小写。",
     "tip":"Python: chr((ord(c)-base+1)%26+base)处理循环偏移。C++直接做字符运算。理解ASCII码编码规则——字母是连续排列的，这是字符运算的前提。"},
    {"nq":"NQ076","acw":764,"title":"输出字符串",
     "story":"\"这道题有点怪——输入两个字符串A和B，对于B的每个位置，如果它不是A对应位置的字符，就把这个位置到B末尾的子串输出来。\"小鲁读了三遍题目才明白。小华解释道：\"逐位比较A和B。一旦发现某个位置i的字符不同，就输出B从i开始的后缀子串。如果完全相同就输出A。关键是理解'后缀'概念——字符串从某位置到末尾的部分。\"",
     "input":"两行：字符串A和B。","output":"按规则输出。",
     "sample_in":"abcdef\nabcxyz","sample_out":"xyz","constraint":"1 ≤ |A|,|B| ≤ 100",
     "sol":"逐位比较：if A[i]!=B[i]: 输出B[i:]并结束。Python的B[i:]切片取后缀。这道题训练的是字符串逐位比较+后缀切片的概念。",
     "tip":"Python切片取后缀：s[i:]表示从i到末尾。s[:i]表示从开头到i-1。切片的三个参数[start:end:step]可以省略任意部分——省略start表示从0开始，省略end表示到末尾。"},
    {"nq":"NQ077","acw":770,"title":"单词替换",
     "story":"小鲁在写文本编辑器的一个功能：把所有出现的某个单词替换成另一个单词。\"比如把新闻里所有的'北京'改成'Beijing'……\"小华摇摇头：\"这个比你想象的复杂！如果用简单的replace，'北京大学'就会变成'Beijing大学'。在OJ环境下，输入是以空格分隔的单词——所以用split()分割后逐词判断替换，再用join()拼回去，更安全也更清晰。\"",
     "input":"三行：原文句子、要替换的单词、替换成的单词。","output":"替换后的句子。",
     "sample_in":"I like apple\napple\norange","sample_out":"I like orange","constraint":"字符串长度≤1000",
     "sol":"分词→逐词判断→重建句子。Python: words=s.split(); result=' '.join(w if w!=old else new for w in words)。注意区分单词和子串——用split和join保证按词替换而非子串替换。",
     "tip":"Python的split()默认按任意空白字符（空格、Tab、换行）分割。' '.join()则按单空格重新拼接。这两个方法组合是Python文本处理的黄金搭档。"},
    {"nq":"NQ078","acw":774,"title":"最长单词",
     "story":"\"在一句话里找最长的单词——小学生也能做。\"小鲁不屑地说。\"那如果有两个一样长的呢？输出先出现的那个。\"小栋又把条件加复杂了。小华说：\"用split()分词，然后遍历找最长的。Python一行就能搞定——max(words, key=len)。注意要去掉末尾的句号（这是一个小陷阱）。\"",
     "input":"一个英文句子，以'.'结尾。","output":"最长单词。若有多个，输出最先出现的。",
     "sample_in":"I love programming.","sample_out":"programming","constraint":"句子长度≤500",
     "sol":"去掉句号→split()分词→max()找最长。Python: s.rstrip('.').split()得到单词列表，max(words, key=len)选出最长。注意max()默认返回最先出现的（稳定性）。",
     "tip":"Python的max()在key相同时保持原始顺序（稳定排序）。rstrip('.')去掉末尾指定字符——这是去除标点的小技巧。split()不加参数会去掉所有空白字符。"},
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
body{font-family:"PingFang SC","Hiragino Sans GB","Noto Serif CJK SC","STSong",serif;font-size:9.5pt;line-height:1.7;color:#222;string-set:chapter"第6章 字符的世界——字符串处理"}
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
    parts.append('<div class="chapter-title">字符的世界</div>')
    parts.append('<div class="chapter-subtitle">字符串处理 · 12题 · C++ &amp; Python 双语对照</div>')
    parts.append('<div class="preface">')
    parts.append('<p>小鲁已经学会了数字的处理——整数、浮点数、数组。但真实世界的程序处理得最多的不是数字，而是<strong>文字</strong>。从搜索引擎到聊天软件，从代码编辑器到语音助手——字符串处理是每个程序员的基本功。而Python在字符串处理上的优势几乎是碾压级别的：切片、join、split、replace……C++需要好几行的操作，Python往往一行解决。</p>')
    parts.append('<p>本章12道题，涵盖了字符串六大核心操作：<strong>长度与遍历</strong>、<strong>字符分类</strong>、<strong>修改与替换</strong>、<strong>切片与拼接</strong>、<strong>频次统计</strong>、<strong>分词与重构</strong>。学完之后你会发现——用Python处理字符串是编程中最快乐的事之一。</p>')
    parts.append('<h3>本章角色</h3>')
    parts.append('<p>🧑‍🎓 <strong>小鲁</strong>（初学者）· 从\"数字世界\"迈入\"文字世界\"，发现Python字符串处理的魔法</p>')
    parts.append('<p>🧠 <strong>小华</strong>（算法高手）· 擅长对比C++和Python的字符串处理差异，强调\"理解原理\"</p>')
    parts.append('<p>🏗️ <strong>小栋</strong>（工程师）· 用\"文本编辑器\"\"搜索引擎\"等实际场景出题</p>')
    parts.append('<p>🏛️ <strong>小嘉</strong>（校主精神）· 偶尔提及密码学和南洋通信的故事，赋予字符串处理历史深度</p>')
    parts.append('</div>')
    parts.append('<div class="knowledge-box"><div class="k-title">📝 Python字符串处理四大法宝</div><ul>')
    parts.append('<li><strong>切片：</strong>s[a:b]截取[a,b)区间。s[:i]前缀、s[i:]后缀、s[::-1]反转</li>')
    parts.append('<li><strong>分割与拼接：</strong>s.split(sep)按分隔符拆分，sep.join(list)按分隔符拼接</li>')
    parts.append('<li><strong>查找与替换：</strong>s.find(sub)、s.replace(old,new)、sub in s 成员判断</li>')
    parts.append('<li><strong>字符分类：</strong>isdigit()/isalpha()/isupper()/islower()/isspace() 自动分类</li>')
    parts.append('<li><strong>频次统计：</strong>collections.Counter(s) 一行建字典。字符→频次的O(1)映射</li></ul>')
    parts.append('<p><strong>C++注意：</strong>字符串分为std::string（类）和char[]（C风格），后者需要strlen/strcpy/strcat。现代C++推荐用std::string。</p></div>')

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
    parts.append('<li><strong>字符串六大操作：</strong>长度遍历、字符分类、修改替换、切片拼接、频次统计、分词重构</li>')
    parts.append('<li><strong>Python四大法宝：</strong>切片s[a:b]、split+join、find+replace、isdigit+isalpha——一行代码等于C++五行的力量</li>')
    parts.append('<li><strong>字符串不可变：</strong>Python字符串修改操作全部返回新对象。理解这点才能正确使用replace/upper/lower等</li>')
    parts.append('<li><strong>暴力匹配：</strong>理解O(n×m)的朴素算法才能理解KMP的O(n+m)有多快。先学走再学跑</li>')
    parts.append('<li><strong>编码知识：</strong>ASCII码中字母连续排列，这是字符偏移加密的数学基础</li>')
    parts.append('<li><strong>厦大精神：</strong>自强不息，止于至善。从整数到字符串，你在成为更全面的程序员</li>')
    parts.append('</ul></div>')
    parts.append('<div class="chapter-end">— 第6章完 · 共12题 · 自强不息 —</div>')

    html=f"""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"><title>第6章 字符的世界</title><style>{CSS}</style></head><body>{chr(10).join(parts)}</body></html>"""
    out=BOOK_ROOT/"textbook"/"chapter06_print.html"
    out.write_text(html,encoding='utf-8')
    print(f"✅ Ch6 dialog version: {len(html)} chars")

if __name__=="__main__":
    build_html()
