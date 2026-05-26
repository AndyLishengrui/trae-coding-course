#!/usr/bin/env python3
"""第2章完整构建：教材PDF/DOCX + 题库 + 实验 + AC验证"""
import json, re, os, sys, time, tempfile, zipfile, shutil, subprocess
from pathlib import Path

BOOK_ROOT = Path(__file__).parent.parent

# ============================================================
PROBLEMS = [
    {"nq": "NQ015", "acw": 665, "title": "倍数",
     "desc": "小鲁在数学课上学了倍数和约数的概念。给定两个整数A和B，判断它们是否互为倍数关系（即A能被B整除，或B能被A整除）。",
     "input_fmt": "一行，两个整数A和B。",
     "output_fmt": "如果互为倍数，输出\"Sao Multiplos\"；否则输出\"Nao sao Multiplos\"。",
     "sample_in": "6 24", "sample_out": "Sao Multiplos",
     "constraint": "−10⁴ ≤ A, B ≤ 10⁴（A, B ≠ 0）",
     "solution": "用取模运算判断倍数关系：A % B == 0 或 B % A == 0。注意两个条件用\"或\"（|| / or）连接。这是最简单的条件判断结构。",
     "technique": "Python的if语句不需要括号，直接写条件表达式。C++中%运算符要求操作数为整数。",
     "cpp": '#include <iostream>\nusing namespace std;\nint main() {\n    int a, b;\n    cin >> a >> b;\n    if (a % b == 0 || b % a == 0)\n        cout << "Sao Multiplos" << endl;\n    else\n        cout << "Nao sao Multiplos" << endl;\n    return 0;\n}',
     "py": 'a, b = map(int, input().split())\nif a % b == 0 or b % a == 0:\n    print("Sao Multiplos")\nelse:\n    print("Nao sao Multiplos")',
     "gen_args": "2 ints: small"},
    {"nq": "NQ016", "acw": 660, "title": "零食",
     "desc": "小鲁去小卖部买零食。每种零食有编号（1到5）和单价。给定零食编号和数量，请计算总价。",
     "input_fmt": "一行，两个整数：零食编号X（1-5）和数量Y。",
     "output_fmt": "输出\"Total: R$ \"后跟总价（保留2位小数）。",
     "sample_in": "3 2", "sample_out": "Total: R$ 10.00",
     "constraint": "1 ≤ X ≤ 5, 1 ≤ Y ≤ 100，单价：1=4.00, 2=4.50, 3=5.00, 4=2.00, 5=1.50",
     "solution": "多分支选择：根据编号选择对应单价。C++可用if-else链或switch；Python用if-elif或dict映射表。本课重点：dict映射表比长if-else链更优雅。",
     "technique": "Python dict映射表替代if-else：prices={1:4.0,2:4.5,3:5.0,4:2.0,5:1.5}。O(1)查找，代码量减少50%。",
     "cpp": '#include <cstdio>\nint main() {\n    int x, y;\n    scanf("%d%d", &x, &y);\n    double p;\n    if (x == 1) p = 4.0;\n    else if (x == 2) p = 4.5;\n    else if (x == 3) p = 5.0;\n    else if (x == 4) p = 2.0;\n    else p = 1.5;\n    printf("Total: R$ %.2lf\\n", p * y);\n    return 0;\n}',
     "py": 'prices = {1: 4.0, 2: 4.5, 3: 5.0, 4: 2.0, 5: 1.5}\nx, y = map(int, input().split())\nprint(f"Total: R$ {prices[x] * y:.2f}")',
     "gen_args": "snack"},
    {"nq": "NQ017", "acw": 659, "title": "区间",
     "desc": "小鲁在做数据分析，需要判断一个浮点数属于哪个数值区间。给定一个浮点数x，判断它落在[0,25], (25,50], (50,75], (75,100]中的哪一个，或者都不在。",
     "input_fmt": "一个浮点数x。",
     "output_fmt": "输出区间名称，或\"Fora de intervalo\"。",
     "sample_in": "25.01", "sample_out": "Intervalo (25,50]",
     "constraint": "−10⁹ ≤ x ≤ 10⁹",
     "solution": "区间判断的典型模板。注意开闭区间的区别：[0,25]包含25，(25,50]不包含25但包含50。Python支持链式比较：0 <= x <= 25。C++需0 <= x && x <= 25。",
     "technique": "Python链式比较：0 <= x <= 25，比C++的0 <= x && x <= 25更直观。从最小区间开始判断，逐级向上。",
     "cpp": '#include <iostream>\nusing namespace std;\nint main() {\n    double x;\n    cin >> x;\n    if (x >= 0 && x <= 25) cout << "Intervalo [0,25]" << endl;\n    else if (x > 25 && x <= 50) cout << "Intervalo (25,50]" << endl;\n    else if (x > 50 && x <= 75) cout << "Intervalo (50,75]" << endl;\n    else if (x > 75 && x <= 100) cout << "Intervalo (75,100]" << endl;\n    else cout << "Fora de intervalo" << endl;\n    return 0;\n}',
     "py": 'x = float(input())\nif 0 <= x <= 25:\n    print("Intervalo [0,25]")\nelif 25 < x <= 50:\n    print("Intervalo (25,50]")\nelif 50 < x <= 75:\n    print("Intervalo (50,75]")\nelif 75 < x <= 100:\n    print("Intervalo (75,100]")\nelse:\n    print("Fora de intervalo")',
     "gen_args": "interval"},
    {"nq": "NQ018", "acw": 664, "title": "三角形",
     "desc": "小鲁在几何课上学了三角形的判定。给定三个浮点数A、B、C，判断它们能否构成三角形。如果能，计算周长；如果不能，计算以A、B为底的梯形面积。",
     "input_fmt": "一行，三个浮点数A、B、C。",
     "output_fmt": "能构成三角形：\"Perimetro = XX.X\"（周长，1位小数）。不能：\"Area = XX.X\"（梯形面积(A+B)*C/2）。",
     "sample_in": "6.0 4.0 2.0", "sample_out": "Area = 10.0",
     "constraint": "0 < A, B, C ≤ 100",
     "solution": "三角形判定条件：任意两边之和大于第三边。即 A+B>C && A+C>B && B+C>A。需要同时满足三个条件。这是一个多条件与（&&/and）判断的经典例题。",
     "technique": "三个条件必须同时满足，用&&/and连接。C++中注意浮点数比较的精度问题，但本题数据范围不会触发浮点精度bug。",
     "cpp": '#include <cstdio>\n#include <iostream>\nusing namespace std;\nint main() {\n    double a, b, c;\n    cin >> a >> b >> c;\n    if (a + b > c && a + c > b && b + c > a)\n        printf("Perimetro = %.1lf\\n", a + b + c);\n    else\n        printf("Area = %.1lf\\n", (a + b) * c / 2);\n    return 0;\n}',
     "py": 'a, b, c = map(float, input().split())\nif a + b > c and a + c > b and b + c > a:\n    print(f"Perimetro = {a + b + c:.1f}")\nelse:\n    print(f"Area = {(a + b) * c / 2:.1f}")',
     "gen_args": "triangle"},
    {"nq": "NQ019", "acw": 667, "title": "游戏时间",
     "desc": "小鲁和小伙伴玩游戏，从A时开始到B时结束。如果A<B，持续时间 = B-A；如果A≥B（跨天），持续时间 = B-A+24。计算游戏持续的小时数。",
     "input_fmt": "一行，两个整数A和B（0 ≤ A, B ≤ 23）。",
     "output_fmt": "\"O JOGO DUROU X HORA(S)\"。",
     "sample_in": "16 2", "sample_out": "O JOGO DUROU 10 HORA(S)",
     "constraint": "0 ≤ A, B ≤ 23",
     "solution": "时间循环判断的经典题。关键：如果A < B则直接相减；否则说明跨天了，需要B-A+24。也可以统一公式：duration = (B-A+24) % 24，但结果为0时需要输出24。",
     "technique": "Python中可以用(B-A) % 24处理循环型问题，但注意结果为0的特殊情况（表示24小时）。C++中取模运算对负数结果依赖实现。",
     "cpp": '#include <cstdio>\nint main() {\n    int a, b;\n    scanf("%d%d", &a, &b);\n    int res;\n    if (a < b) res = b - a;\n    else res = b - a + 24;\n    printf("O JOGO DUROU %d HORA(S)\\n", res);\n    return 0;\n}',
     "py": 'a, b = map(int, input().split())\nif a < b:\n    d = b - a\nelse:\n    d = b - a + 24\nprint(f"O JOGO DUROU {d} HORA(S)")',
     "gen_args": "game_time"},
    {"nq": "NQ020", "acw": 669, "title": "加薪",
     "desc": "公司年终调薪，小鲁想知道自己的新工资。根据当前工资所在的区间，涨幅不同：0-400涨15%，400.01-800涨12%，800.01-1200涨10%，1200.01-2000涨7%，2000以上涨4%。",
     "input_fmt": "一个浮点数，表示当前工资。",
     "output_fmt": "三行：新工资、涨薪金额、涨幅百分比（整数%）。",
     "sample_in": "400.00",
     "sample_out": "Novo salario: 460.00\nReajuste ganho: 60.00\nEm percentual: 15 %",
     "constraint": "0 < 工资 ≤ 10⁶",
     "solution": "多级区间判断。从上限往下判断可以减少条件（因为区间连续且互斥）。注意输出格式：保留2位小数+空格+%。",
     "technique": "多级条件判断的顺序很重要。从大到小判断可以减少else分支。C++中printf的%%可以输出%字面量。Python用f-string直接写%。",
     "cpp": '#include <cstdio>\nint main() {\n    double s;\n    scanf("%lf", &s);\n    int p;\n    if (s <= 400) p = 15;\n    else if (s <= 800) p = 12;\n    else if (s <= 1200) p = 10;\n    else if (s <= 2000) p = 7;\n    else p = 4;\n    double r = s * p / 100;\n    printf("Novo salario: %.2lf\\nReajuste ganho: %.2lf\\nEm percentual: %d %%\\n", s + r, r, p);\n    return 0;\n}',
     "py": 's = float(input())\nif s <= 400: p = 15\nelif s <= 800: p = 12\nelif s <= 1200: p = 10\nelif s <= 2000: p = 7\nelse: p = 4\nr = s * p / 100\nprint(f"Novo salario: {s + r:.2f}")\nprint(f"Reajuste ganho: {r:.2f}")\nprint(f"Em percentual: {p} %")',
     "gen_args": "salary_raise"},
    {"nq": "NQ021", "acw": 670, "title": "动物",
     "desc": "小鲁在生物课上学了动物分类。根据三个特征（脊椎/无脊椎、哺乳/鸟/爬虫/昆虫、食性），判断动物的种类名称。这是一个嵌套条件判断的经典题。",
     "input_fmt": "三行：第一行\"vertebrado\"或\"invertebrado\"；第二、三行根据第一行不同。",
     "output_fmt": "动物名称（如aguia, pomba, homem, vaca, pulga, lagarta, sanguessuga, minhoca）。",
     "sample_in": "vertebrado\nmamifero\nonivoro",
     "sample_out": "homem",
     "constraint": "输入保证合法。",
     "solution": "三层嵌套条件判断。先判断脊椎/无脊椎，再判断具体的纲，最后根据食性确定种类。可以看作决策树：每个内部节点是一个判断，叶子节点是答案。",
     "technique": "Python嵌套if-elif结构。也可以用dict嵌套：tree={'vertebrado':{'ave':{...}}}。数据结构化思维是进阶编程的关键能力。",
     "cpp": '#include <iostream>\nusing namespace std;\nint main() {\n    string a, b, c;\n    cin >> a >> b >> c;\n    if (a == "vertebrado") {\n        if (b == "ave") {\n            if (c == "carnivoro") cout << "aguia" << endl;\n            else cout << "pomba" << endl;\n        } else {\n            if (c == "onivoro") cout << "homem" << endl;\n            else cout << "vaca" << endl;\n        }\n    } else {\n        if (b == "inseto") {\n            if (c == "hematofago") cout << "pulga" << endl;\n            else cout << "lagarta" << endl;\n        } else {\n            if (c == "hematofago") cout << "sanguessuga" << endl;\n            else cout << "minhoca" << endl;\n        }\n    }\n    return 0;\n}',
     "py": 'a, b, c = input(), input(), input()\nif a == "vertebrado":\n    if b == "ave":\n        print("aguia" if c == "carnivoro" else "pomba")\n    else:\n        print("homem" if c == "onivoro" else "vaca")\nelse:\n    if b == "inseto":\n        print("pulga" if c == "hematofago" else "lagarta")\n    else:\n        print("sanguessuga" if c == "hematofago" else "minhoca")',
     "gen_args": "animal"},
    {"nq": "NQ022", "acw": 657, "title": "选择练习1",
     "desc": "给定四个整数A、B、C、D，请判断是否同时满足：B>C、D>A、C+D>A+B、C和D都是正数、A是偶数。所有条件都满足才输出\"Valores aceitos\"。",
     "input_fmt": "一行，四个整数A、B、C、D。",
     "output_fmt": "满足所有条件输出\"Valores aceitos\"，否则\"Valores nao aceitos\"。",
     "sample_in": "5 6 7 8", "sample_out": "Valores nao aceitos",
     "constraint": "−10⁹ ≤ A,B,C,D ≤ 10⁹",
     "solution": "五个条件需要用&&（and）连接。同时满足才输出accepted。这道题训练了复杂布尔表达式的组合使用。",
     "technique": "Python把多个条件写在一行可读性很好：if b>c and d>a and c+d>a+b and c>0 and d>0 and a%2==0。注意条件的排列顺序：先放最容易判断的可以短路求值。",
     "cpp": '#include <iostream>\nusing namespace std;\nint main() {\n    int a, b, c, d;\n    cin >> a >> b >> c >> d;\n    if (b > c && d > a && c + d > a + b && c > 0 && d > 0 && a % 2 == 0)\n        cout << "Valores aceitos" << endl;\n    else\n        cout << "Valores nao aceitos" << endl;\n    return 0;\n}',
     "py": 'a, b, c, d = map(int, input().split())\nif b > c and d > a and c + d > a + b and c > 0 and d > 0 and a % 2 == 0:\n    print("Valores aceitos")\nelse:\n    print("Valores nao aceitos")',
     "gen_args": "2 ints"},
    {"nq": "NQ023", "acw": 671, "title": "DDD",
     "desc": "小鲁想打电话给其他城市的同学。给定一个DDD区号，输出对应的城市名。DDD与城市的对应关系：61-Brasilia, 71-Salvador, 11-Sao Paulo, 21-Rio de Janeiro, 32-Juiz de Fora, 19-Campinas, 27-Vitoria, 31-Belo Horizonte。",
     "input_fmt": "一个整数DDD。",
     "output_fmt": "输出城市名，或\"DDD nao cadastrado\"。",
     "sample_in": "11", "sample_out": "Sao Paulo",
     "constraint": "DDD为正整数。",
     "solution": "多分支映射的经典题。C++用8个if-else分支，Python用dict映射表一行搞定。本课最重要的工程思维：当看到重复的if-else模式时，用数据结构替代逻辑堆叠。",
     "technique": "Python dict.get(ddd, 'DDD nao cadastrado')一行替代8个if-else。这是\"用数据驱动代替逻辑驱动\"的典范。",
     "cpp": '#include <iostream>\nusing namespace std;\nint main() {\n    int x;\n    cin >> x;\n    if (x == 61) cout << "Brasilia" << endl;\n    else if (x == 71) cout << "Salvador" << endl;\n    else if (x == 11) cout << "Sao Paulo" << endl;\n    else if (x == 21) cout << "Rio de Janeiro" << endl;\n    else if (x == 32) cout << "Juiz de Fora" << endl;\n    else if (x == 19) cout << "Campinas" << endl;\n    else if (x == 27) cout << "Vitoria" << endl;\n    else if (x == 31) cout << "Belo Horizonte" << endl;\n    else cout << "DDD nao cadastrado" << endl;\n    return 0;\n}',
     "py": 'ddd = {61:"Brasilia",71:"Salvador",11:"Sao Paulo",21:"Rio de Janeiro",32:"Juiz de Fora",19:"Campinas",27:"Vitoria",31:"Belo Horizonte"}\nx = int(input())\nprint(ddd.get(x, "DDD nao cadastrado"))',
     "gen_args": "ddd"},
    {"nq": "NQ024", "acw": 662, "title": "点的坐标",
     "desc": "小鲁在坐标系上画了一个点P(x,y)。请判断这个点在第几象限，或者在坐标轴上（Eixo X / Eixo Y），或者在原点（Origem）。",
     "input_fmt": "一行，两个浮点数x和y。",
     "output_fmt": "输出\"Q1\"、\"Q2\"、\"Q3\"、\"Q4\"、\"Origem\"、\"Eixo X\"或\"Eixo Y\"。",
     "sample_in": "4.5 -2.2", "sample_out": "Q4",
     "constraint": "−10⁹ ≤ x, y ≤ 10⁹",
     "solution": "象限判断的顺序很重要：先判断原点（x=0且y=0），再判断轴（x=0或y=0），最后判断象限（x和y的符号组合）。如果顺序颠倒会得到错误结果。",
     "technique": "判断顺序：原点→轴→象限。浮点数比较用==在本题数据范围内安全。C++中注意小数点的精确表示。",
     "cpp": '#include <iostream>\nusing namespace std;\nint main() {\n    double x, y;\n    cin >> x >> y;\n    if (x > 0 && y > 0) cout << "Q1" << endl;\n    else if (x < 0 && y > 0) cout << "Q2" << endl;\n    else if (x < 0 && y < 0) cout << "Q3" << endl;\n    else if (x > 0 && y < 0) cout << "Q4" << endl;\n    else if (x == 0 && y == 0) cout << "Origem" << endl;\n    else if (x == 0) cout << "Eixo Y" << endl;\n    else cout << "Eixo X" << endl;\n    return 0;\n}',
     "py": 'x, y = map(float, input().split())\nif x > 0 and y > 0: print("Q1")\nelif x < 0 and y > 0: print("Q2")\nelif x < 0 and y < 0: print("Q3")\nelif x > 0 and y < 0: print("Q4")\nelif x == 0 and y == 0: print("Origem")\nelif x == 0: print("Eixo Y")\nelse: print("Eixo X")',
     "gen_args": "quadrant"},
    {"nq": "NQ025", "acw": 666, "title": "三角形类型",
     "desc": "给定三个浮点数，先判断能否构成三角形，如果能，再进一步判断是直角三角形、钝角三角形、锐角三角形、等边三角形还是等腰三角形。",
     "input_fmt": "一行，三个浮点数A、B、C。",
     "output_fmt": "按顺序输出满足的类型，可能多行。先输出\"NAO FORMA TRIANGULO\"（不能构成），否则依次检查直/钝/锐/等边/等腰。",
     "sample_in": "7.0 5.0 7.0", "sample_out": "TRIANGULO ACUTANGULO\nTRIANGULO ISOSCELES",
     "constraint": "0 < A, B, C ≤ 100",
     "solution": "先把三个数降序排列（a≥b≥c），简化后续判断。不能构成：a≥b+c。直角：a²=b²+c²。钝角：a²>b²+c²。锐角：a²<b²+c²。等边：a=b=c。等腰：a=b或b=c。",
     "technique": "排序降序是简化条件判断的核心技巧。Python的sorted()配合reverse=True。判断顺序从一般到特殊：先判不能构成，再判角度类型，最后判边长相等等。",
     "cpp": '#include <iostream>\n#include <algorithm>\nusing namespace std;\nint main() {\n    double a, b, c;\n    cin >> a >> b >> c;\n    if (b > a) swap(a, b);\n    if (c > a) swap(a, c);\n    if (c > b) swap(b, c);\n    if (a >= b + c) cout << "NAO FORMA TRIANGULO" << endl;\n    else {\n        if (a*a == b*b + c*c) cout << "TRIANGULO RETANGULO" << endl;\n        if (a*a > b*b + c*c) cout << "TRIANGULO OBTUSANGULO" << endl;\n        if (a*a < b*b + c*c) cout << "TRIANGULO ACUTANGULO" << endl;\n        if (a == b && b == c) cout << "TRIANGULO EQUILATERO" << endl;\n        else if (a == b || a == c || b == c) cout << "TRIANGULO ISOSCELES" << endl;\n    }\n    return 0;\n}',
     "py": 'a, b, c = sorted(map(float, input().split()), reverse=True)\nif a >= b + c:\n    print("NAO FORMA TRIANGULO")\nelse:\n    if a*a == b*b + c*c: print("TRIANGULO RETANGULO")\n    if a*a > b*b + c*c: print("TRIANGULO OBTUSANGULO")\n    if a*a < b*b + c*c: print("TRIANGULO ACUTANGULO")\n    if a == b == c: print("TRIANGULO EQUILATERO")\n    elif a == b or b == c or a == c: print("TRIANGULO ISOSCELES")',
     "gen_args": "triangle_types"},
    {"nq": "NQ026", "acw": 668, "title": "游戏时间2",
     "desc": "和NQ019类似，但这次游戏时间精确到分钟。输入开始和结束的小时和分钟，计算游戏的持续时间（时和分）。",
     "input_fmt": "一行，四个整数：开始的小时A、分钟B，结束的小时C、分钟D。",
     "output_fmt": "\"O JOGO DUROU X HORA(S) E Y MINUTO(S)\"。",
     "sample_in": "7 8 9 10", "sample_out": "O JOGO DUROU 2 HORA(S) E 2 MINUTO(S)",
     "constraint": "0 ≤ A, C ≤ 23, 0 ≤ B, D ≤ 59",
     "solution": "统一转换为分钟数便于计算：start = A*60+B, end = C*60+D。如果end≤start，end += 24*60（跨天）。duration = end - start，再转回时和分。",
     "technique": "统一量纲（转为分钟）后比较和计算是处理时间问题的通用技巧。避免分别处理小时和分钟的复杂情况。",
     "cpp": '#include <cstdio>\nint main() {\n    int a, b, c, d;\n    scanf("%d%d%d%d", &a, &b, &c, &d);\n    int start = a * 60 + b, end = c * 60 + d;\n    if (end <= start) end += 24 * 60;\n    int diff = end - start;\n    printf("O JOGO DUROU %d HORA(S) E %d MINUTO(S)\\n", diff / 60, diff % 60);\n    return 0;\n}',
     "py": 'a, b, c, d = map(int, input().split())\ns = a * 60 + b\ne = c * 60 + d\nif e <= s: e += 24 * 60\nd = e - s\nprint(f"O JOGO DUROU {d // 60} HORA(S) E {d % 60} MINUTO(S)")',
     "gen_args": "game_time"},
    {"nq": "NQ027", "acw": 672, "title": "税",
     "desc": "小鲁工作了，需要计算个人所得税。税率分档：0-2000免税，2000.01-3000税率8%，3000.01-4500税率18%，4500以上税率28%。注意是分段计税。",
     "input_fmt": "一个浮点数，表示月收入。",
     "output_fmt": "如免税输出\"Isento\"，否则输出\"R$ XX.XX\"（保留2位小数）。",
     "sample_in": "3002.00", "sample_out": "R$ 80.36",
     "constraint": "0 < 收入 ≤ 10⁶",
     "solution": "分段计税是逐段计算的典型例子。先判断是否在免税范围，然后对超出2000的部分逐段按税率计算。关键是理解\"分段\"的含义：不是全额乘以最高税率，而是每段分别计算。",
     "technique": "分段计算用min()限制每段的上限。Python写法比C++更简洁：tax = min(x, 1000)*0.08 + min(max(x-1000,0), 1500)*0.18 + ...",
     "cpp": '#include <cstdio>\nint main() {\n    double x;\n    scanf("%lf", &x);\n    if (x <= 2000) { printf("Isento\\n"); return 0; }\n    x -= 2000;\n    double t = 0;\n    if (x > 0) { double v = x < 1000 ? x : 1000; t += v * 0.08; x -= v; }\n    if (x > 0) { double v = x < 1500 ? x : 1500; t += v * 0.18; x -= v; }\n    if (x > 0) t += x * 0.28;\n    printf("R$ %.2lf\\n", t);\n    return 0;\n}',
     "py": 'x = float(input())\nif x <= 2000:\n    print("Isento")\nelse:\n    x -= 2000\n    t = 0\n    if x > 0:\n        v = min(x, 1000)\n        t += v * 0.08\n        x -= v\n    if x > 0:\n        v = min(x, 1500)\n        t += v * 0.18\n        x -= v\n    if x > 0:\n        t += x * 0.28\n    print(f"R$ {t:.2f}")',
     "gen_args": "tax"},
    {"nq": "NQ028", "acw": 663, "title": "简单排序",
     "desc": "小鲁想把三个数从小到大排列。给定三个整数，输出它们按升序排列的结果。",
     "input_fmt": "一行，三个整数。",
     "output_fmt": "升序排列的三个数，空格隔开。",
     "sample_in": "7 21 -14", "sample_out": "-14 7 21",
     "constraint": "−10⁹ ≤ a,b,c ≤ 10⁹",
     "solution": "三个数的排序：比较a和b，必要时交换；再比较a和c；最后比较b和c。经过这三步，a≤b≤c。这是冒泡排序思想的萌芽，也是交换操作（swap）的练习。",
     "technique": "Python可以用sorted()一行搞定，但手写交换理解排序原理更重要。C++用swap()函数或临时变量。Python的a,b=b,a是最优雅的交换写法。",
     "cpp": '#include <iostream>\nusing namespace std;\nint main() {\n    int a, b, c;\n    cin >> a >> b >> c;\n    if (a > b) swap(a, b);\n    if (a > c) swap(a, c);\n    if (b > c) swap(b, c);\n    cout << a << " " << b << " " << c << endl;\n    return 0;\n}',
     "py": 'a, b, c = map(int, input().split())\nif a > b: a, b = b, a\nif a > c: a, c = c, a\nif b > c: b, c = c, b\nprint(a, b, c)',
     "gen_args": "2 ints"},
]

# ============================================================
# 题库构建（14题，每道10组测试数据）
# ============================================================
def build_bank():
    BANK = BOOK_ROOT / "chapter2_bank"
    if BANK.exists(): shutil.rmtree(BANK)
    BANK.mkdir()

    for i, p in enumerate(PROBLEMS):
        pid = f"ACW{p['acw']:03d}" if p['acw'] >= 100 else f"ACW{p['acw']:03d}"
        dirname = f"{pid}.{p['title'].replace(' ', '_')}"
        d = BANK / dirname
        d.mkdir()
        (d / "Andy.cpp").write_text(p['cpp'] + '\n')
        (d / "Andy.py").write_text(p['py'] + '\n')
        (d / "problem.json").write_text(json.dumps({
            "display_id": f"ACW{p['acw']}", "title": p["title"],
            "description": {"format":"html","value":f"<p>{p['desc']}</p>"},
            "tags": ["基础语法"],
            "input_description": {"format":"html","value":f"<p>{p['input_fmt']}</p>"},
            "output_description": {"format":"html","value":f"<p>{p['output_fmt']}</p>"},
            "test_case_score": [{"score":10,"input_name":f"{j}.in","output_name":f"{j}.out"} for j in range(1,11)],
            "hint": {"format":"html","value":f'<a href="https://www.acwing.com/problem/content/{p["acw"]}/" target="_blank">原题链接</a>'},
            "time_limit":1000,"memory_limit":256,
            "samples":[{"input":p["sample_in"],"output":p["sample_out"]}],
            "template":{},"spj":None,"rule_type":"OI",
            "source":f"AcWing {p['acw']} | {p['nq']} | 第2章",
            "allow_public_test_case_download":False,"answers":[],
        }, indent=2, ensure_ascii=False))

        # Generate gen.cpp with proper test data for each problem type
        gen_cpp = make_gen_cpp(p)
        (d / "gen.cpp").write_text(gen_cpp)

        # Compile, generate test cases, build ZIP
        subprocess.run(['g++','-std=c++11','-O2',str(d/'gen.cpp'),'-o',str(d/'gen.out')], capture_output=True)
        subprocess.run(['g++','-std=c++11','-O2',str(d/'Andy.cpp'),'-o',str(d/'Andy.out')], capture_output=True)
        tc_dir = d / 'testcase'
        tc_dir.mkdir()
        for tc in range(1, 11):
            gen = subprocess.run([str(d/'gen.out'), str(tc)], capture_output=True, text=True)
            (tc_dir / f'{tc}.in').write_text(gen.stdout)
            andy = subprocess.run([str(d/'Andy.out')], input=gen.stdout, capture_output=True, text=True)
            (tc_dir / f'{tc}.out').write_text(andy.stdout)

        # ZIP
        tmp = d / '1'; (tmp/'testcase').mkdir(parents=True)
        shutil.copy(d/'problem.json', tmp/'problem.json')
        for tc in range(1, 11):
            shutil.copy(tc_dir/f'{tc}.in', tmp/'testcase'/f'{tc}.in')
            shutil.copy(tc_dir/f'{tc}.out', tmp/'testcase'/f'{tc}.out')
        with zipfile.ZipFile(d/'xmuoj-import.zip', 'w', zipfile.ZIP_DEFLATED) as zf:
            for root, dirs, files in os.walk(str(tmp)):
                for fn in files:
                    fp = os.path.join(root, fn)
                    zf.write(fp, os.path.relpath(fp, str(d)))
        shutil.rmtree(tmp)
        for f in ['gen.out', 'Andy.out']:
            pf = d / f
            if pf.exists(): pf.unlink()
        print(f'  [{i+1:2d}/14] {pid} {p["title"]} ✅')

    print(f'\n✅ Chapter 2 bank: {BANK}')
    return BANK


def make_gen_cpp(p):
    """生成10组测试数据的 gen.cpp"""
    lines = ['#include <iostream>','#include <cstdlib>','#include <ctime>','using namespace std;',
             'int main(int argc, char* argv[]) {',
             '    int tc = argc > 1 ? atoi(argv[1]) : 1;',
             '    srand(time(0) + tc * 1000);',
             '    switch(tc) {']
    gen = p.get('gen_args', '')
    si = p['sample_in']

    if '2 ints' in gen or 'simple' in gen:
        for i in range(1, 11):
            if i <= 2: lines.append(f'        case {i}: cout << "{si}" << endl; break;')
            elif i <= 4: lines.append(f'        case {i}: cout << rand()%10+1 << " " << rand()%10+1 << endl; break;')
            elif i <= 7: lines.append(f'        case {i}: cout << rand()%100-50 << " " << rand()%100-50 << endl; break;')
            elif i <= 9: lines.append(f'        case {i}: cout << rand()%10000-5000 << " " << rand()%10000-5000 << endl; break;')
            else: lines.append(f'        case {i}: cout << "10000 10000" << endl; break;')
    elif 'snack' in gen:
        for i in range(1, 11):
            if i <= 2: lines.append(f'        case {i}: cout << "{si}" << endl; break;')
            elif i <= 5: lines.append(f'        case {i}: cout << rand()%5+1 << " " << rand()%10+1 << endl; break;')
            else: lines.append(f'        case {i}: cout << rand()%5+1 << " " << rand()%100+1 << endl; break;')
    elif 'interval' in gen:
        vals = ['25.01', '-10.0', '0', '25', '50', '50.01', '75', '100', '100.01', '200']
        for i in range(1, 11):
            lines.append(f'        case {i}: cout << "{vals[i-1]}" << endl; break;')
    elif 'triangle' in gen:
        vals = ['6.0 4.0 2.0', '3.0 4.0 5.0', '5.0 5.0 5.0', '1.0 2.0 3.0', '10.0 10.0 1.0']
        for i in range(1, 6):
            lines.append(f'        case {i}: cout << "{vals[i-1]}" << endl; break;')
        for i in range(6, 11):
            lines.append(f'        case {i}: printf("%.1f %.1f %.1f\\n", (rand()%100+1)*1.0, (rand()%100+1)*1.0, (rand()%100+1)*1.0); break;')
    elif 'game_time' in gen:
        vals = ['16 2', '0 0', '7 8 9 10', '0 0 0 0', '23 59 0 0']
        for i in range(1, 6):
            lines.append(f'        case {i}: cout << "{vals[i-1]}" << endl; break;')
        for i in range(6, 11):
            lines.append(f'        case {i}: printf("%d %d\\n", rand()%24, rand()%24); break;')
    elif 'salary_raise' in gen:
        vals = ['400.00', '800.01', '1200.00', '2000.00', '3000.00']
        for i in range(1, 6):
            v = vals[i-1]
            v_escaped = v.replace('\n', '\\n')
            lines.append(f'        case {i}: cout << "{v_escaped}" << endl; break;')
        for i in range(6, 11):
            lines.append(f'        case {i}: printf("%.2f\\n", (rand()%50000)/100.0+0.01); break;')
    elif 'animal' in gen:
        escaped_vals = [v.replace('\n', '\\n') for v in ['vertebrado\nmamifero\nonivoro', 'vertebrado\nave\ncarnivoro', 'invertebrado\ninseto\nhematofago', 'invertebrado\nanelideo\nonivoro']]
        for i in range(1, 5):
            lines.append(f'        case {i}: cout << "{escaped_vals[i-1]}" << endl; break;')
        for i in range(5, 11):
            lines.append(f'        case {i}: cout << "{escaped_vals[(i-1)%4]}" << endl; break;')
    elif 'ddd' in gen:
        ddd_vals = ['11', '61', '71', '21', '32', '19', '27', '31', '99', '100']
        for i in range(1, 11):
            lines.append(f'        case {i}: cout << "{ddd_vals[i-1]}" << endl; break;')
    elif 'quadrant' in gen:
        vals = ['4.5 -2.2', '0 0', '0 5', '-3 0', '10 20', '-5 -5', '-1 8', '7 -3', '0.1 0', '0 -0.1']
        for i in range(1, 11):
            lines.append(f'        case {i}: cout << "{vals[i-1]}" << endl; break;')
    elif 'triangle_types' in gen:
        vals = ['7.0 5.0 7.0', '3.0 4.0 5.0', '6.0 6.0 6.0', '1.0 2.0 3.0', '10.0 6.0 8.0']
        for i in range(1, 6):
            lines.append(f'        case {i}: cout << "{vals[i-1]}" << endl; break;')
        for i in range(6, 11):
            lines.append(f'        case {i}: printf("%.1f %.1f %.1f\\n", (rand()%100+1)*1.0, (rand()%100+1)*1.0, (rand()%100+1)*1.0); break;')
    elif 'tax' in gen:
        vals = ['3002.00', '1701.12', '4500.00', '6000.00', '2000.00']
        for i in range(1, 6):
            lines.append(f'        case {i}: cout << "{vals[i-1]}" << endl; break;')
        for i in range(6, 11):
            lines.append(f'        case {i}: printf("%.2f\\n", (rand()%100000)/100.0+0.01); break;')
    else:
        for i in range(1, 11):
            lines.append(f'        case {i}: cout << "{si}" << endl; break;')

    lines.extend(['    }', '    return 0;', '}'])
    return '\n'.join(lines) + '\n'


# ============================================================
# 教材 PDF/DOCX 构建（复用第1章框架）
# ============================================================
from pygments import highlight
from pygments.lexers import CppLexer, PythonLexer
from pygments.formatters import HtmlFormatter
from pygments.token import Token

CPP_FMT = HtmlFormatter(style='vs', noclasses=True)
PY_FMT = HtmlFormatter(style='vs', noclasses=True)

def highlight_code(code, lexer, fmt):
    html = highlight(code, lexer, fmt)
    m = re.search(r'<pre[^>]*>(.*)</pre>', html, re.DOTALL)
    if m:
        inner = m.group(1)
        inner = re.sub(r'<span></span>\n?', '', inner)
        return inner
    return code

def h_cpp(c): return highlight_code(c, CppLexer(), CPP_FMT)
def h_py(c): return highlight_code(c, PythonLexer(), PY_FMT)

CSS = r"""
@page { size: A4; margin: 2.2cm 2cm 2.2cm 2cm;
    @top-center { content: string(chapter); font-size: 7.5pt; color: #999; font-family: "PingFang SC", sans-serif; }
    @bottom-center { content: counter(page); font-size: 7.5pt; color: #999; } }
body { font-family: "PingFang SC","Hiragino Sans GB","Noto Serif CJK SC","STSong",serif; font-size:9.5pt; line-height:1.7; color:#222;
    string-set: chapter "第2章 选择的艺术 —— 条件判断与分支结构"; }
.chapter-title { text-align:center; font-size:20pt; font-weight:bold; margin:1.5em 0 0.1em 0; letter-spacing:3pt; }
.chapter-subtitle { text-align:center; font-size:10pt; color:#777; margin-bottom:1.5em; padding-bottom:0.8em; border-bottom:1px solid #bbb; }
.preface { font-size:10pt; margin-bottom:2em; color:#444; } .preface p { margin:0.4em 0; text-indent:2em; }
.problem-title { font-size:12pt; font-weight:bold; margin:1.5em 0 0.4em 0; padding-bottom:0.15em; border-bottom:1pt solid #444; }
.problem-title .nq { color:#2563eb; margin-right:0.6em; font-size:11pt; }
.problem-title .acw { font-size:7.5pt; color:#aaa; font-weight:normal; margin-left:1em; }
.problem-desc { margin:0.6em 0 1em 0; text-indent:2em; line-height:1.85; }
.spec-table { width:100%; border-collapse:collapse; margin:0.3em 0 0.5em 0; font-size:9pt; }
.spec-table td { padding:0.3em 0.8em; vertical-align:top; border:none; }
.spec-table .spec-label { width:4em; font-size:8pt; font-weight:bold; text-align:right; padding-right:1em; white-space:nowrap; }
.spec-table .spec-label .tag { display:inline-block; padding:0.15em 0.5em; border-radius:2px; color:#fff; font-size:7.5pt; letter-spacing:0.5pt; }
.spec-table .spec-label .tag.in { background:#2563eb; } .spec-table .spec-label .tag.out { background:#059669; } .spec-table .spec-label .tag.lim { background:#d97706; }
.spec-table .spec-value { color:#333; font-size:9pt; }
.sample-box { background:#f7f8fa; border:0.5pt solid #dde; border-radius:4px; padding:0.7em 1em; margin:1em 0 1.2em 0; }
.sample-grid { display:flex; gap:2em; } .sample-col { flex:1; }
.sample-col .col-label { font-size:7.5pt; color:#888; margin-bottom:0.2em; font-weight:bold; }
.sample-col pre { background:none; border:none; padding:0.3em 0; margin:0; font-family:"SF Mono","Menlo","Consolas",monospace; font-size:9pt; line-height:1.4; white-space:pre-wrap; color:#333; }
.insight-block { margin:0.8em 0; padding:0.5em 0.8em; border-left:3px solid #2563eb; background:#f8faff; }
.insight-block .insight-label { font-size:8pt; font-weight:bold; color:#2563eb; margin-right:0.5em; }
.code-dual { display:flex; gap:1.5em; margin:1.2em 0; page-break-inside:avoid; } .code-col { flex:1; min-width:0; }
.code-col .lang-badge { display:inline-block; font-size:7.5pt; font-weight:bold; color:#fff; background:#2563eb; padding:0.2em 0.7em; border-radius:3px; margin-bottom:0.4em; }
.code-col pre { background:#f8f8f0; border:0.5pt solid #e0e0e0; border-radius:4px; padding:0.7em 0.9em; font-family:"SF Mono","Menlo","Consolas","Courier New",monospace; font-size:7.5pt; line-height:1.45; overflow-x:auto; margin:0; white-space:pre-wrap; word-break:break-all; }
.section-divider { border:none; border-top:0.3pt solid #e0e0e0; margin:1em 0 0 0; } .chapter-end { text-align:center; margin-top:3em; font-size:8pt; color:#999; }
"""

def build_html():
    parts = []
    for p in PROBLEMS:
        pb = ['<div class="problem-block">']
        pb.append(f'<div class="problem-title"><span class="nq">{p["nq"]}</span>{p["title"]}<span class="acw">AcWing {p["acw"]}</span></div>')
        pb.append(f'<div class="problem-desc">{p["desc"]}</div>')
        pb.append('<table class="spec-table">')
        pb.append(f'<tr><td class="spec-label"><span class="tag in">输入</span></td><td class="spec-value">{p["input_fmt"]}</td></tr>')
        pb.append(f'<tr><td class="spec-label"><span class="tag out">输出</span></td><td class="spec-value">{p["output_fmt"]}</td></tr>')
        pb.append(f'<tr><td class="spec-label"><span class="tag lim">范围</span></td><td class="spec-value">{p["constraint"]}</td></tr>')
        pb.append('</table>')
        pb.append('<div class="sample-box"><div class="sample-grid">')
        pb.append(f'<div class="sample-col"><div class="col-label">输入</div><pre>{p["sample_in"]}</pre></div>')
        pb.append(f'<div class="sample-col"><div class="col-label">输出</div><pre>{p["sample_out"]}</pre></div>')
        pb.append('</div></div>')
        pb.append(f'<div class="insight-block"><span class="insight-label">思路</span><span>{p["solution"]}</span></div>')
        pb.append(f'<div class="insight-block"><span class="insight-label">技巧</span><span>{p["technique"]}</span></div>')
        pb.append('<div class="code-dual">')
        pb.append(f'<div class="code-col"><div class="lang-badge">C++</div><pre>{h_cpp(p["cpp"])}</pre></div>')
        pb.append(f'<div class="code-col"><div class="lang-badge">Python</div><pre>{h_py(p["py"])}</pre></div>')
        pb.append('</div></div><hr class="section-divider">')
        parts.append('\n'.join(pb))

    html = f"""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8">
<title>第2章 选择的艺术</title><style>{CSS}</style></head><body>
<div class="chapter-title">选择的艺术</div>
<div class="chapter-subtitle">条件判断与分支结构 · 14题 · C++ &amp; Python 双语对照</div>
<div class="preface">
<p>本章聚焦于编程中最核心的控制结构之一——条件判断。14道题目从简单的取模判倍数开始，逐步深入区间判断、三角形判定、时间跨越、分段计税和嵌套分类。你将学会用数据驱动替代逻辑堆叠（dict映射 > 长if-else链），并掌握Python的链式比较、元组解包交换等特性。</p>
<p>学完本章，面对任何需要"分情况讨论"的问题，你都能条理清晰地将判断条件转化为代码。</p>
</div>
{chr(10).join(parts)}
<div class="chapter-end">— 第2章完 · 共14题 —</div>
</body></html>"""
    (BOOK_ROOT / "textbook" / "chapter02_print.html").write_text(html, encoding="utf-8")
    return html


def build_docx():
    """生成DOCX — 复用第1章排版"""
    from docx import Document
    from docx.shared import Pt, Cm, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.enum.table import WD_TABLE_ALIGNMENT
    from docx.oxml.ns import qn, nsdecls
    from docx.oxml import parse_xml

    doc = Document()
    section = doc.sections[0]
    section.page_width = Cm(21); section.page_height = Cm(29.7)
    section.top_margin = Cm(2.2); section.bottom_margin = Cm(2.2)
    section.left_margin = Cm(2); section.right_margin = Cm(2)

    style = doc.styles['Normal']
    style.font.name = '等线'; style.font.size = Pt(9.5)
    style.paragraph_format.line_spacing = 1.35
    style.paragraph_format.space_after = Pt(3)
    style.element.rPr.rFonts.set(qn('w:eastAsia'), '等线')

    BLUE = RGBColor(0x25,0x63,0xEB); GREEN = RGBColor(0x05,0x96,0x69)
    ORANGE = RGBColor(0xD9,0x77,0x06); GRAY = RGBColor(0x66,0x66,0x66)
    LGRAY = RGBColor(0x99,0x99,0x99)

    def add_code_run(para, text, color=None, bold=False, italic=False, fs=Pt(7.5)):
        r = para.add_run(text); r.font.name = 'Courier New'; r.font.size = fs
        if color: r.font.color.rgb = color
        if bold: r.font.bold = True
        if italic: r.font.italic = True
        return r

    # 标题
    tp = doc.add_paragraph(); tp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    tr = tp.add_run('选择的艺术'); tr.font.size = Pt(20); tr.font.bold = True
    sp = doc.add_paragraph(); sp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    sr = sp.add_run('条件判断与分支结构 · 14题 · C++ & Python 双语对照')
    sr.font.size = Pt(10); sr.font.color.rgb = GRAY

    bp = doc.add_paragraph()
    pPr = bp._p.get_or_add_pPr()
    pBdr = parse_xml(f'<w:pBdr {nsdecls("w")}><w:bottom w:val="single" w:sz="4" w:space="1" w:color="BBBBBB"/></w:pBdr>')
    pPr.append(pBdr); bp.paragraph_format.space_after = Pt(12)

    preface = doc.add_paragraph('本章聚焦于编程中最核心的控制结构之一——条件判断。14道题目从简单的取模判倍数开始，逐步深入区间判断、三角形判定、时间跨越、分段计税和嵌套分类。')
    preface.paragraph_format.first_line_indent = Cm(0.7)

    for p in PROBLEMS:
        # Title
        tp = doc.add_paragraph(); tp.paragraph_format.space_before = Pt(14)
        nq = tp.add_run(f'{p["nq"]} '); nq.font.size = Pt(12); nq.font.bold = True; nq.font.color.rgb = BLUE
        tt = tp.add_run(p['title']); tt.font.size = Pt(12); tt.font.bold = True
        aw = tp.add_run(f'  AcWing {p["acw"]}'); aw.font.size = Pt(7.5); aw.font.color.rgb = LGRAY
        pPr = tp._p.get_or_add_pPr()
        pBdr = parse_xml(f'<w:pBdr {nsdecls("w")}><w:bottom w:val="single" w:sz="6" w:space="1" w:color="444444"/></w:pBdr>')
        pPr.append(pBdr)

        dp = doc.add_paragraph(p['desc']); dp.paragraph_format.first_line_indent = Cm(0.7)

        # Spec table
        st = doc.add_table(rows=3, cols=2); st.autofit = True
        for i, (label, value, color) in enumerate([('输入',p['input_fmt'],BLUE),('输出',p['output_fmt'],GREEN),('范围',p['constraint'],ORANGE)]):
            cl = st.cell(i,0); cl.width = Cm(1.5); cl.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.LEFT
            trun = cl.paragraphs[0].add_run(f' {label} '); trun.font.size = Pt(7.5); trun.font.bold = True
            trun.font.color.rgb = RGBColor(0xFF,0xFF,0xFF)
            shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color}" w:val="clear"/>')
            trun._r.get_or_add_rPr().append(shd)
            cv = st.cell(i,1); cv.width = Cm(14)
            vr = cv.paragraphs[0].add_run(value); vr.font.size = Pt(9)

        # Sample table
        st2 = doc.add_table(rows=1, cols=2); st2.autofit = True
        for col, (label, text) in enumerate([('输入',p['sample_in']),('输出',p['sample_out'])]):
            c = st2.cell(0,col); c.width = Cm(7.5)
            tcPr = c._tc.get_or_add_tcPr()
            shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="F7F8FA" w:val="clear"/>')
            tcPr.append(shd)
            lr = c.paragraphs[0].add_run(label); lr.font.size = Pt(7.5); lr.font.bold = True; lr.font.color.rgb = LGRAY
            vp = c.add_paragraph()
            vr = vp.add_run(text); vr.font.name = 'Courier New'; vr.font.size = Pt(9)

        # Insights — with spacing between blocks
        for lbl, txt in [('思路',p['solution']),('技巧',p['technique'])]:
            ip = doc.add_paragraph(); ip.paragraph_format.space_after = Pt(4); ip.paragraph_format.space_before = Pt(4)
            pPr = ip._p.get_or_add_pPr()
            shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="F8FAFF" w:val="clear"/>')
            pPr.append(shd)
            lr = ip.add_run(f'{lbl} '); lr.font.size = Pt(8); lr.font.bold = True; lr.font.color.rgb = BLUE
            ip.add_run(txt).font.size = Pt(9)

        # Code table — reduced left padding
        ct = doc.add_table(rows=1, cols=2); ct.autofit = False; ct.alignment = WD_TABLE_ALIGNMENT.CENTER
        for col, (lang, code, lexer) in enumerate([('C++',p['cpp'],CppLexer()),('Python',p['py'],PythonLexer())]):
            c = ct.cell(0,col); c.width = Cm(7.5); c.paragraphs[0].clear()
            # 语言标签
            bp2 = c.paragraphs[0]
            bp2.paragraph_format.left_indent = Cm(0.1)
            br = bp2.add_run(f' {lang} '); br.font.size = Pt(7); br.font.bold = True
            br.font.color.rgb = RGBColor(0xFF,0xFF,0xFF)
            shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="2563EB" w:val="clear"/>')
            br._r.get_or_add_rPr().append(shd)
            for line in code.split('\n'):
                cp2 = c.add_paragraph()
                cp2.paragraph_format.left_indent = Cm(0.1)
                cp2.paragraph_format.space_before = Pt(0); cp2.paragraph_format.space_after = Pt(0)
                cp2.paragraph_format.line_spacing = 1.1
                pPr = cp2._p.get_or_add_pPr()
                shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="F0F0F0" w:val="clear"/>')
                pPr.append(shd)
                if not line.strip():
                    add_code_run(cp2, ' ', fs=Pt(6)); continue
                for ttype, ttext in lexer.get_tokens(line):
                    if not ttext: continue
                    cmap = {Token.Keyword:RGBColor(0,0,255), Token.Keyword.Type:RGBColor(0x2B,0x91,0xAF),
                            Token.Name.Builtin:RGBColor(0,0,255), Token.String:RGBColor(0xA3,0x15,0x15),
                            Token.Comment:RGBColor(0,0x80,0), Token.Comment.Preproc:RGBColor(0,0,255),
                            Token.Number:RGBColor(0x09,0x80,0x85)}
                    c_found = None
                    for tk, clr in cmap.items():
                        if ttype in tk or tk in ttype: c_found = clr; break
                    is_kw = ttype in Token.Keyword or ttype in Token.Keyword.Type
                    is_cm = ttype in Token.Comment or ttype in Token.Comment.Preproc
                    add_code_run(cp2, ttext, c_found, is_kw, is_cm)

        # Divider
        sep = doc.add_paragraph(); sep.paragraph_format.space_before = Pt(8)
        pPr = sep._p.get_or_add_pPr()
        pBdr = parse_xml(f'<w:pBdr {nsdecls("w")}><w:bottom w:val="single" w:sz="4" w:space="1" w:color="E0E0E0"/></w:pBdr>')
        pPr.append(pBdr)

    ep = doc.add_paragraph(); ep.alignment = WD_ALIGN_PARAGRAPH.CENTER; ep.paragraph_format.space_before = Pt(24)
    er = ep.add_run('— 第2章完 · 共14题 —'); er.font.size = Pt(8); er.font.color.rgb = LGRAY

    out = BOOK_ROOT / "textbook" / "chapter02.docx"
    doc.save(str(out))
    return out


# ============================================================
# Main
# ============================================================
if __name__ == "__main__":
    print("=== Step 1: Build Problem Bank ===")
    bank = build_bank()

    print("\n=== Step 2: Build HTML ===")
    build_html()
    print("✅ chapter02_print.html")

    print("\n=== Step 3: Build DOCX ===")
    build_docx()
    print("✅ chapter02.docx")
