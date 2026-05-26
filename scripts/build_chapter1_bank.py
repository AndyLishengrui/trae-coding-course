#!/usr/bin/env python3
"""
第1章题库构建器 — 为14道题生成完整题库组件

输出结构：
  chapter1_bank/
    ACW001.A+B/
      problem.md          # 题面（与教材一致）
      problem.json        # 16字段XMUOJ格式
      Andy.cpp            # C++参考解答
      Andy.py             # Python参考解答
      gen.cpp             # 测试数据生成器（10组）
      ai.sh               # 自动化编译→生成→验证→打包
      样例.zip             # 样例包
      xmuoj-import.zip    # XMUOJ导入包
    ACW608.差/
    ... (14个目录)
"""
import os, sys, json, zipfile, shutil, subprocess, tempfile, time
from pathlib import Path

BOOK_ROOT = Path(__file__).parent.parent
OUTPUT = BOOK_ROOT / "chapter1_bank"

# ============================================================
# 题目定义 (14题)
# ============================================================
PROBLEMS = [
    {
        "pid": "ACW001", "acw": 1, "title": "A + B", "nq": "NQ001",
        "desc": "输入两个整数A和B，计算它们的和。这是学习编程的第一道题。",
        "input_fmt": "一行，两个整数A和B，用空格隔开。",
        "output_fmt": "一个整数，即A+B的结果。",
        "sample_in": "3 4", "sample_out": "7",
        "tags": ["基础语法", "输入输出"],
        "gen_type": "simple_math",  # generator type
        "cpp_code": '#include <iostream>\nusing namespace std;\nint main() { int a, b; cin >> a >> b; cout << a + b << endl; return 0; }',
        "py_code": 'a, b = map(int, input().split())\nprint(a + b)',
    },
    {
        "pid": "ACW608", "acw": 608, "title": "差", "nq": "NQ002",
        "desc": "读取四个整数A、B、C、D，计算A×B−C×D的结果。",
        "input_fmt": "一行，四个整数A、B、C、D，用空格隔开。",
        "output_fmt": "输出\"DIFERENCA = \"后跟计算结果。",
        "sample_in": "5 6 7 8", "sample_out": "DIFERENCA = -26",
        "tags": ["基础语法", "四则运算"],
        "gen_type": "simple_math",
        "cpp_code": '#include <cstdio>\nint main() { int a,b,c,d; scanf("%d%d%d%d",&a,&b,&c,&d); printf("DIFERENCA = %d\\n",a*b-c*d); return 0; }',
        "py_code": 'a, b, c, d = map(int, input().split())\nprint(f"DIFERENCA = {a * b - c * d}")',
    },
    {
        "pid": "ACW604", "acw": 604, "title": "圆的面积", "nq": "NQ003",
        "desc": "给定圆的半径r，计算圆的面积。π取3.14159。",
        "input_fmt": "一个浮点数r，表示圆的半径。",
        "output_fmt": "输出\"A=\"后跟圆的面积，结果保留4位小数。",
        "sample_in": "2.00", "sample_out": "A=12.5664",
        "tags": ["基础语法", "浮点数"],
        "gen_type": "circle_area",
        "cpp_code": '#include <cstdio>\nint main() { double r; scanf("%lf",&r); printf("A=%.4lf\\n",3.14159*r*r); return 0; }',
        "py_code": 'r = float(input())\nprint(f"A={3.14159 * r * r:.4f}")',
    },
    {
        "pid": "ACW606", "acw": 606, "title": "平均数1", "nq": "NQ004",
        "desc": "读取两个学生的成绩A和B，A的权重3.5，B的权重7.5，计算加权平均分。",
        "input_fmt": "两行，每行一个浮点数，分别表示A和B。",
        "output_fmt": "输出\"MEDIA = \"后跟加权平均分，保留5位小数。",
        "sample_in": "5.0\n7.1", "sample_out": "MEDIA = 6.43182",
        "tags": ["基础语法", "浮点数", "加权平均"],
        "gen_type": "weighted_avg",
        "cpp_code": '#include <cstdio>\nint main() { double a,b; scanf("%lf%lf",&a,&b); printf("MEDIA = %.5lf\\n",(a*3.5+b*7.5)/11); return 0; }',
        "py_code": 'a = float(input())\nb = float(input())\nprint(f"MEDIA = {(a * 3.5 + b * 7.5) / 11:.5f}")',
    },
    {
        "pid": "ACW609", "acw": 609, "title": "工资", "nq": "NQ005",
        "desc": "输入员工编号（整数）、月工作时数（整数）和时薪（浮点数），计算工资总额。",
        "input_fmt": "三行：编号、时数、时薪。",
        "output_fmt": "第一行\"NUMBER = X\"，第二行\"SALARY = U$ XX.XX\"。",
        "sample_in": "25\n100\n5.50", "sample_out": "NUMBER = 25\nSALARY = U$ 550.00",
        "tags": ["基础语法", "格式化输出"],
        "gen_type": "salary",
        "cpp_code": '#include <cstdio>\nint main() { int n,h; double m; scanf("%d%d%lf",&n,&h,&m); printf("NUMBER = %d\\nSALARY = U$ %.2lf\\n",n,h*m); return 0; }',
        "py_code": 'n = int(input())\nh = int(input())\nm = float(input())\nprint(f"NUMBER = {n}")\nprint(f"SALARY = U$ {h * m:.2f}")',
    },
    {
        "pid": "ACW615", "acw": 615, "title": "油耗", "nq": "NQ006",
        "desc": "输入行驶距离(km)和消耗汽油量(L)，计算每升汽油行驶的公里数。",
        "input_fmt": "两行：距离(float)和汽油量(float)。",
        "output_fmt": "保留3位小数，后跟\" km/l\"。",
        "sample_in": "500\n35.0", "sample_out": "14.286 km/l",
        "tags": ["基础语法", "浮点数"],
        "gen_type": "fuel",
        "cpp_code": '#include <cstdio>\nint main() { double x,y; scanf("%lf%lf",&x,&y); printf("%.3lf km/l\\n",x/y); return 0; }',
        "py_code": 'x = float(input())\ny = float(input())\nprint(f"{x / y:.3f} km/l")',
    },
    {
        "pid": "ACW616", "acw": 616, "title": "两点间的距离", "nq": "NQ007",
        "desc": "给定两点坐标P1(x1,y1)和P2(x2,y2)，计算欧几里得距离。",
        "input_fmt": "一行，四个浮点数x1 y1 x2 y2。",
        "output_fmt": "距离，保留4位小数。",
        "sample_in": "1.0 7.0 5.0 9.0", "sample_out": "4.4721",
        "tags": ["基础语法", "数学库"],
        "gen_type": "distance",
        "cpp_code": '#include <cstdio>\n#include <cmath>\nint main() { double x1,y1,x2,y2; scanf("%lf%lf%lf%lf",&x1,&y1,&x2,&y2); printf("%.4lf\\n",sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))); return 0; }',
        "py_code": 'import math\nx1, y1, x2, y2 = map(float, input().split())\nprint(f"{math.sqrt((x1-x2)**2 + (y1-y2)**2):.4f}")',
    },
    {
        "pid": "ACW653", "acw": 653, "title": "钞票", "nq": "NQ008",
        "desc": "给定金额N，用最少的钞票数量支付。面额：100,50,20,10,5,2,1。",
        "input_fmt": "一个整数N。",
        "output_fmt": "第一行输出N。然后7行，按面额从大到小输出\"X nota(s) de R$ Y,00\"。",
        "sample_in": "576", "sample_out": "576\n5 nota(s) de R$ 100,00\n1 nota(s) de R$ 50,00\n1 nota(s) de R$ 20,00\n0 nota(s) de R$ 10,00\n1 nota(s) de R$ 5,00\n0 nota(s) de R$ 2,00\n1 nota(s) de R$ 1,00",
        "tags": ["基础语法", "循环", "贪心"],
        "gen_type": "banknotes",
        "cpp_code": '#include <cstdio>\nint main() { int n,s[]={100,50,20,10,5,2,1}; scanf("%d",&n); printf("%d\\n",n); for(int i=0;i<7;i++){printf("%d nota(s) de R$ %d,00\\n",n/s[i],s[i]);n%=s[i];} return 0; }',
        "py_code": 'n = int(input())\nprint(n)\nfor v in [100,50,20,10,5,2,1]:\n    print(f"{n // v} nota(s) de R$ {v},00")\n    n %= v',
    },
    {
        "pid": "ACW654", "acw": 654, "title": "时间转换", "nq": "NQ009",
        "desc": "将总秒数N转换为HH:MM:SS格式。",
        "input_fmt": "一个整数N，表示总秒数。",
        "output_fmt": "HH:MM:SS格式的时间。",
        "sample_in": "556", "sample_out": "0:9:16",
        "tags": ["基础语法", "整除求余"],
        "gen_type": "time_convert",
        "cpp_code": '#include <cstdio>\nint main() { int n; scanf("%d",&n); printf("%d:%d:%d",n/3600,n%3600/60,n%60); return 0; }',
        "py_code": 'n = int(input())\nh, r = divmod(n, 3600)\nm, s = divmod(r, 60)\nprint(f"{h}:{m}:{s}")',
    },
    {
        "pid": "ACW605", "acw": 605, "title": "简单乘积", "nq": "NQ010",
        "desc": "读取两个整数，输出\"PROD = \"后跟它们的乘积。",
        "input_fmt": "两行，每行一个整数。",
        "output_fmt": "输出\"PROD = X\"。",
        "sample_in": "3\n9", "sample_out": "PROD = 27",
        "tags": ["基础语法", "乘法"],
        "gen_type": "simple_math",
        "cpp_code": '#include <iostream>\nusing namespace std;\nint main() { int a,b; cin>>a>>b; cout<<"PROD = "<<a*b<<endl; return 0; }',
        "py_code": 'a = int(input())\nb = int(input())\nprint(f"PROD = {a * b}")',
    },
    {
        "pid": "ACW611", "acw": 611, "title": "简单计算", "nq": "NQ011",
        "desc": "根据产品编号、数量和单价，计算总价。",
        "input_fmt": "第一行两个整数（编号和数量），第二行一个浮点数（单价）。",
        "output_fmt": "\"VALOR A PAGAR: R$ XX.XX\"。",
        "sample_in": "12 1\n5.30", "sample_out": "VALOR A PAGAR: R$ 5.30",
        "tags": ["基础语法", "浮点数"],
        "gen_type": "simple_math",
        "cpp_code": '#include <cstdio>\nint main() { int c,q; double p; scanf("%d%d%lf",&c,&q,&p); printf("VALOR A PAGAR: R$ %.2lf\\n",q*p); return 0; }',
        "py_code": 'c, q = map(int, input().split())\np = float(input())\nprint(f"VALOR A PAGAR: R$ {q * p:.2f}")',
    },
    {
        "pid": "ACW612", "acw": 612, "title": "球的体积", "nq": "NQ012",
        "desc": "V=(4/3)πr³，π=3.14159。",
        "input_fmt": "一个整数r，表示半径。",
        "output_fmt": "\"VOLUME = XXX.XXX\"，保留3位小数。",
        "sample_in": "3", "sample_out": "VOLUME = 113.097",
        "tags": ["基础语法", "数学公式"],
        "gen_type": "sphere_volume",
        "cpp_code": '#include <cstdio>\nint main() { int r; scanf("%d",&r); printf("VOLUME = %.3lf\\n",4.0/3.0*3.14159*r*r*r); return 0; }',
        "py_code": 'r = int(input())\nprint(f"VOLUME = {4.0/3.0 * 3.14159 * r**3:.3f}")',
    },
    {
        "pid": "ACW613", "acw": 613, "title": "面积", "nq": "NQ013",
        "desc": "计算三个图形面积：直角三角形A*C/2、圆π*C²、梯形(A+B)*C/2。π=3.14159。",
        "input_fmt": "一行，三个浮点数A、B、C。",
        "output_fmt": "三行：TRIANGULO: X / CIRCULO: X / TRAPEZIO: X，各保留3位小数。",
        "sample_in": "3.0 4.0 5.2", "sample_out": "TRIANGULO: 7.800\nCIRCULO: 84.949\nTRAPEZIO: 18.200",
        "tags": ["基础语法", "几何"],
        "gen_type": "areas",
        "cpp_code": '#include <cstdio>\nint main() { double a,b,c; scanf("%lf%lf%lf",&a,&b,&c); printf("TRIANGULO: %.3lf\\nCIRCULO: %.3lf\\nTRAPEZIO: %.3lf\\n",a*c/2,3.14159*c*c,(a+b)*c/2); return 0; }',
        "py_code": 'a, b, c = map(float, input().split())\nprint(f"TRIANGULO: {a*c/2:.3f}")\nprint(f"CIRCULO: {3.14159*c*c:.3f}")\nprint(f"TRAPEZIO: {(a+b)*c/2:.3f}")',
    },
    {
        "pid": "ACW614", "acw": 614, "title": "最大值", "nq": "NQ014",
        "desc": "输入三个整数a、b、c，输出其中的最大者。",
        "input_fmt": "一行，三个整数，用空格隔开。",
        "output_fmt": "一个整数，即三个数中的最大值。",
        "sample_in": "7 14 106", "sample_out": "106",
        "tags": ["基础语法", "最值"],
        "gen_type": "max3",
        "cpp_code": '#include <iostream>\n#include <algorithm>\nusing namespace std;\nint main() { int a,b,c; cin>>a>>b>>c; cout<<max({a,b,c})<<endl; return 0; }',
        "py_code": 'a, b, c = map(int, input().split())\nprint(max(a, b, c))',
    },
]


# ============================================================
# 测试数据生成器模板（根据 gen_type 生成 gen.cpp）
# ============================================================
def make_gen_cpp(prob):
    """生成 gen.cpp — 10组测试数据"""
    lines = [
        '#include <iostream>',
        '#include <cstdlib>',
        '#include <ctime>',
        '#include <cmath>',
        '#include <iomanip>',
        'using namespace std;',
        '',
        'int main(int argc, char* argv[]) {',
        '    int tc = argc > 1 ? atoi(argv[1]) : 1;',
        '    srand(time(0) + tc * 1000);',
        '    ',
        '    switch(tc) {',
    ]

    gen = prob["gen_type"]
    sample_in = prob["sample_in"]
    sample_out = prob["sample_out"]

    if gen == "simple_math":
        for i in range(1, 11):
            if i <= 2:  # sample
                lines.append(f'        case {i}: cout << "{sample_in}" << endl; break;')
            elif i <= 4:  # boundary
                lines.append(f'        case {i}: cout << rand()%100 << " " << rand()%100 << endl; break;')
            elif i <= 7:  # medium
                lines.append(f'        case {i}: cout << rand()%10000-5000 << " " << rand()%10000-5000 << endl; break;')
            elif i <= 9:  # large
                lines.append(f'        case {i}: cout << rand()%1000000 << " " << rand()%1000000 << endl; break;')
            else:
                lines.append(f'        case {i}: cout << 1000000000 << " " << 1000000000 << endl; break;')

    elif gen == "circle_area":
        for i in range(1, 11):
            if i <= 2: lines.append(f'        case {i}: cout << "2.00" << endl; break;')
            elif i <= 4: lines.append(f'        case {i}: cout << "0.01" << endl; break;')
            elif i <= 7: lines.append(f'        case {i}: printf("%.2f\\n", (rand()%10000)/100.0); break;')
            elif i <= 9: lines.append(f'        case {i}: printf("%.2f\\n", (rand()%100000)/100.0); break;')
            else: lines.append(f'        case {i}: cout << "9999.99" << endl; break;')

    elif gen == "weighted_avg":
        for i in range(1, 11):
            if i <= 2: lines.append(f'        case {i}: cout << "5.0\\n7.1" << endl; break;')
            elif i <= 4: lines.append(f'        case {i}: cout << "0.0\\n10.0" << endl; break;')
            else: lines.append(f'        case {i}: printf("%.1f\\n%.1f\\n", (rand()%100)/10.0, (rand()%100)/10.0); break;')

    elif gen == "salary":
        for i in range(1, 11):
            if i <= 2: lines.append(f'        case {i}: cout << "25\\n100\\n5.50" << endl; break;')
            elif i <= 4: lines.append(f'        case {i}: cout << "1\\n1\\n1.00" << endl; break;')
            elif i <= 7: lines.append(f'        case {i}: printf("%d\\n%d\\n%.2f\\n", rand()%50+1, rand()%200+1, (rand()%5000)/100.0+1); break;')
            elif i <= 9: lines.append(f'        case {i}: printf("%d\\n%d\\n%.2f\\n", rand()%100+1, rand()%200+1, (rand()%5000)/100.0+1); break;')
            else: lines.append(f'        case {i}: cout << "100\\n200\\n50.00" << endl; break;')

    elif gen == "fuel":
        for i in range(1, 11):
            if i <= 2: lines.append(f'        case {i}: cout << "500\\n35.0" << endl; break;')
            elif i <= 4: lines.append(f'        case {i}: cout << "1\\n0.1" << endl; break;')
            elif i <= 7: lines.append(f'        case {i}: printf("%.1f\\n%.1f\\n", (rand()%1000+1)*1.0, (rand()%100+1)*1.0); break;')
            elif i <= 9: lines.append(f'        case {i}: printf("%.1f\\n%.1f\\n", (rand()%10000+1)*1.0, (rand()%1000+1)*1.0); break;')
            else: lines.append(f'        case {i}: cout << "1000000\\n1.0" << endl; break;')

    elif gen == "distance":
        for i in range(1, 11):
            if i <= 2: lines.append(f'        case {i}: cout << "1.0 7.0 5.0 9.0" << endl; break;')
            elif i <= 4: lines.append(f'        case {i}: cout << "0 0 0 0" << endl; break;')
            elif i <= 7: lines.append(f'        case {i}: printf("%.1f %.1f %.1f %.1f\\n", (rand()%200-100)*1.0, (rand()%200-100)*1.0, (rand()%200-100)*1.0, (rand()%200-100)*1.0); break;')
            elif i <= 9: lines.append(f'        case {i}: printf("%.1f %.1f %.1f %.1f\\n", (rand()%20000-10000)*1.0, (rand()%20000-10000)*1.0, (rand()%20000-10000)*1.0, (rand()%20000-10000)*1.0); break;')
            else: lines.append(f'        case {i}: cout << "-10000 -10000 10000 10000" << endl; break;')

    elif gen == "banknotes":
        for i in range(1, 11):
            if i <= 2: lines.append(f'        case {i}: cout << "576" << endl; break;')
            elif i <= 4: lines.append(f'        case {i}: cout << "1" << endl; break;')
            elif i <= 7: lines.append(f'        case {i}: cout << rand()%500+1 << endl; break;')
            elif i <= 9: lines.append(f'        case {i}: cout << rand()%50000+500 << endl; break;')
            else: lines.append(f'        case {i}: cout << "999999" << endl; break;')

    elif gen == "time_convert":
        for i in range(1, 11):
            if i <= 2: lines.append(f'        case {i}: cout << "556" << endl; break;')
            elif i <= 4: lines.append(f'        case {i}: cout << "0" << endl; break;')
            elif i <= 7: lines.append(f'        case {i}: cout << rand()%3600+1 << endl; break;')
            elif i <= 9: lines.append(f'        case {i}: cout << rand()%86400+3600 << endl; break;')
            else: lines.append(f'        case {i}: cout << "1000000" << endl; break;')

    elif gen == "sphere_volume":
        for i in range(1, 11):
            if i <= 2: lines.append(f'        case {i}: cout << "3" << endl; break;')
            elif i <= 4: lines.append(f'        case {i}: cout << "1" << endl; break;')
            elif i <= 7: lines.append(f'        case {i}: cout << rand()%100+1 << endl; break;')
            elif i <= 9: lines.append(f'        case {i}: cout << rand()%500+100 << endl; break;')
            else: lines.append(f'        case {i}: cout << "1000" << endl; break;')

    elif gen == "areas":
        for i in range(1, 11):
            if i <= 2: lines.append(f'        case {i}: cout << "3.0 4.0 5.2" << endl; break;')
            elif i <= 4: lines.append(f'        case {i}: cout << "1.0 1.0 1.0" << endl; break;')
            elif i <= 7: lines.append(f'        case {i}: printf("%.1f %.1f %.1f\\n", (rand()%100)/10.0+0.1, (rand()%100)/10.0+0.1, (rand()%100)/10.0+0.1); break;')
            elif i <= 9: lines.append(f'        case {i}: printf("%.1f %.1f %.1f\\n", (rand()%1000)/10.0, (rand()%1000)/10.0, (rand()%1000)/10.0); break;')
            else: lines.append(f'        case {i}: cout << "100.0 100.0 100.0" << endl; break;')

    elif gen == "max3":
        for i in range(1, 11):
            if i <= 2: lines.append(f'        case {i}: cout << "7 14 106" << endl; break;')
            elif i <= 4: lines.append(f'        case {i}: cout << "-100 -200 -300" << endl; break;')
            elif i <= 7: lines.append(f'        case {i}: printf("%d %d %d\\n", rand()%1000-500, rand()%1000-500, rand()%1000-500); break;')
            elif i <= 9: lines.append(f'        case {i}: printf("%d %d %d\\n", rand()%2000000000-1000000000, rand()%2000000000-1000000000, rand()%2000000000-1000000000); break;')
            else: lines.append(f'        case {i}: cout << "1000000000 999999999 1000000000" << endl; break;')

    lines.extend([
        '    }',
        '    return 0;',
        '}',
    ])
    return '\n'.join(lines) + '\n'


# ============================================================
# 构建 problem.json
# ============================================================
def make_problem_json(prob):
    # 完全对齐 problem-export.zip 的标准16字段格式
    return {
        "display_id": prob["pid"],
        "title": prob["title"],
        "description": {"format": "html", "value": f"<p>{prob['desc']}</p>"},
        "tags": prob["tags"],
        "input_description": {"format": "html", "value": f"<p>{prob['input_fmt']}</p>"},
        "output_description": {"format": "html", "value": f"<p>{prob['output_fmt']}</p>"},
        "test_case_score": [{"score": 10, "input_name": f"{i}.in", "output_name": f"{i}.out"} for i in range(1, 11)],
        "hint": {"format": "html", "value": f'<a href="https://www.acwing.com/problem/content/{prob["acw"]}/" target="_blank">原题链接</a>'},
        "time_limit": 1000,
        "memory_limit": 256,
        "samples": [{"input": prob["sample_in"], "output": prob["sample_out"]}],
        "template": {},
        "spj": None,
        "rule_type": "OI",
        "source": f"AcWing {prob['acw']} | {prob['nq']} | 第1章",
        "allow_public_test_case_download": False,
        "answers": [],
    }


# ============================================================
# 构建 problem.md
# ============================================================
def make_problem_md(prob):
    nq = prob["nq"]
    title = prob["title"]
    pid = prob["pid"]
    acw = prob["acw"]
    return f"""# {nq}：{title}

> 题目来源：AcWing {acw} | 题目ID：{pid} | 第1章 程序设计的第一个脚印

## 题目描述
{prob['desc']}

### 输入格式
{prob['input_fmt']}

### 输出格式
{prob['output_fmt']}

### 样例
**输入：**
```
{prob['sample_in']}
```
**输出：**
```
{prob['sample_out']}
```

## 解题思路
{get_solution_text(prob)}

## 编程技巧
{get_technique_text(prob)}

## 参考代码

### C++
```cpp
{prob['cpp_code']}
```

### Python
```python
{prob['py_code']}
```
"""


def get_solution_text(prob):
    solutions = {
        "A + B": "这是编程中最简单的题目，但它包含了所有程序的基本骨架：读入数据→计算→输出结果。C++用cin/cout，Python用input/print。两种语言体现了静态类型和动态类型的设计哲学差异。",
        "差": "直接按公式计算即可。注意运算顺序：先乘后减。输出时带前缀\"DIFERENCA = \"。",
        "圆的面积": "圆的面积 = π × r²。需要使用浮点数类型double/float。C++用printf(\"%.4lf\")控制小数位数，Python用f\"{area:.4f}\"。",
        "平均数1": "加权平均公式：(A×3.5 + B×7.5) / (3.5+7.5)。分母是权重之和=11，不是2。保留5位小数。",
        "工资": "工资 = 时数 × 时薪。输入包含整数和浮点数混合类型。注意输出两行，第二行保留2位小数。",
        "油耗": "燃油效率 = 距离 / 油耗。使用浮点数除法。输出保留3位小数。",
        "两点间的距离": "欧几里得距离 = √((x1-x2)² + (y1-y2)²)。需要使用数学库：C++的cmath/sqrt，Python的math.sqrt。",
        "钞票": "贪心算法雏形：从最大面额开始，每次尽可能多地使用当前面额。count = N // face_value; N %= face_value。Python用列表+循环消除重复代码。",
        "时间转换": "时 = N/3600，分 = N%3600/60，秒 = N%60。Python的divmod()可同时获得商和余数。",
        "简单乘积": "和第1题结构完全相同，只需把+改成*，添加\"PROD = \"前缀。",
        "简单计算": "总价 = 数量 × 单价。int × float自动转为double/float。",
        "球的体积": "V = (4/3)πr³。注意C++中4/3=1（整数除法），必须写4.0/3.0。",
        "面积": "三道公式在一题。A、B、C在不同公式中扮演不同角色，需要仔细读题。",
        "最大值": "Python的max(a,b,c)直接接收多参数。C++需max({a,b,c})（C++11）或嵌套调用。",
    }
    return solutions.get(prob["title"], "直接按题目公式计算即可。")


def get_technique_text(prob):
    techniques = {
        "A + B": "Python的map(int, input().split())是处理空格分隔整数输入的标准写法。C++的cin >> a >> b自动跳过空白字符。",
        "差": "Python的f-string格式化输出：f\"DIFERENCA = {a*b-c*d}\"。f-string是Python 3.6+最推荐的格式化方式。",
        "圆的面积": "C++格式化输出两种风格：printf(\"%.4lf\",x)简洁；cout<<fixed<<setprecision(4)<<x类型安全。Python的f\"{x:.4f}\"最直观。",
        "平均数1": "C++中所有浮点字面量默认double。Python的/总是返回浮点数，无需担心整数除法。",
        "工资": "C++中scanf可精确控制混合输入：scanf(\"%d%d%lf\",&n,&h,&m)。Python逐行读取更清晰。",
        "油耗": "C++中整数除法会截断。如果距离是int需要先转double。Python中/自动浮点。",
        "两点间的距离": "C++需要#include<cmath>并链接-lm。Python的import math后math.sqrt()简洁明了。注意用double不用float（精度更高）。",
        "钞票": "Python用列表+循环消除重复代码：for v in [100,50,20,10,5,2,1]。C++中消除重复是重要的工程思维。",
        "时间转换": "Python的divmod(a,b)返回(商,余数)元组。链式调用：h,r=divmod(n,3600); m,s=divmod(r,60)。",
        "简单乘积": "修改已有代码比从零开始更高效。用AI把L1的代码改成乘法版本。",
        "简单计算": "类型提升规则：int×float自动得到更精确的类型。C++提升到double，Python提升到float。",
        "球的体积": "C++中整数除法的陷阱：4/3=1而不是1.333。必须写成4.0/3.0。Python无此问题。",
        "面积": "使用常量PI=3.14159。每个面积独立计算一行，分行输出。代码组织能力训练。",
        "最大值": "Python内置max/min/sum等。C++的<algorithm>提供类似功能。Python的设计哲学是\"电池已包含\"。",
    }
    return techniques.get(prob["title"], "直接实现即可。")


# ============================================================
# ai.sh 自动化脚本
# ============================================================
def make_ai_sh():
    return """#!/bin/bash
set -e
echo "=== 编译 ==="
g++ -std=c++11 -O2 Andy.cpp -o Andy.out
g++ -std=c++11 -O2 gen.cpp -o gen.out
echo "=== 生成测试数据 ==="
mkdir -p testcase
for i in {1..10}; do
    ./gen.out $i > testcase/${i}.in
    ./Andy.out < testcase/${i}.in > testcase/${i}.out
    echo "  测试用例 ${i}: $(wc -c < testcase/${i}.in) bytes"
done
echo "=== 验证样例 ==="
head -1 testcase/1.in | while read line; do echo "  样例输入: $line"; done
head -1 testcase/1.out | while read line; do echo "  样例输出: $line"; done
echo "=== 打包 ==="
mkdir -p 1/testcase
cp problem.json 1/
cp testcase/*.in testcase/*.out 1/testcase/
rm -f xmuoj-import.zip
cd 1 && zip -r ../xmuoj-import.zip . && cd ..
rm -rf 1
echo "✅ 完成！xmuoj-import.zip 已生成"
"""


# ============================================================
# 主构建流程
# ============================================================
def build_all():
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    OUTPUT.mkdir(parents=True)

    total = len(PROBLEMS)
    for i, prob in enumerate(PROBLEMS, 1):
        pid = prob["pid"]
        acw = prob["acw"]
        dirname = f"{pid}.{prob['title'].replace(' ', '_')}"
        prob_dir = OUTPUT / dirname
        prob_dir.mkdir(parents=True)

        print(f"[{i:2d}/{total}] {pid} {prob['title']}...", end=" ")

        # 1. Write problem.md
        (prob_dir / "problem.md").write_text(make_problem_md(prob), encoding="utf-8")

        # 2. Write problem.json
        pj = make_problem_json(prob)
        (prob_dir / "problem.json").write_text(json.dumps(pj, indent=2, ensure_ascii=False), encoding="utf-8")

        # 3. Write Andy.cpp
        (prob_dir / "Andy.cpp").write_text(prob["cpp_code"] + "\n", encoding="utf-8")

        # 4. Write Andy.py
        (prob_dir / "Andy.py").write_text(prob["py_code"] + "\n", encoding="utf-8")

        # 5. Write gen.cpp
        (prob_dir / "gen.cpp").write_text(make_gen_cpp(prob), encoding="utf-8")

        # 6. Write ai.sh
        ai_sh = make_ai_sh()
        (prob_dir / "ai.sh").write_text(ai_sh, encoding="utf-8")
        os.chmod(prob_dir / "ai.sh", 0o755)

        # 7. Compile and generate test cases
        try:
            subprocess.run(
                ["g++", "-std=c++11", "-O2", str(prob_dir / "gen.cpp"), "-o", str(prob_dir / "gen.out")],
                capture_output=True, timeout=10
            )
            subprocess.run(
                ["g++", "-std=c++11", "-O2", str(prob_dir / "Andy.cpp"), "-o", str(prob_dir / "Andy.out")],
                capture_output=True, timeout=10
            )

            testcase_dir = prob_dir / "testcase"
            testcase_dir.mkdir(exist_ok=True)
            for tc in range(1, 11):
                gen_result = subprocess.run(
                    [str(prob_dir / "gen.out"), str(tc)],
                    capture_output=True, text=True, timeout=5
                )
                test_input = gen_result.stdout
                (testcase_dir / f"{tc}.in").write_text(test_input, encoding="utf-8")

                andy_result = subprocess.run(
                    [str(prob_dir / "Andy.out")],
                    input=test_input, capture_output=True, text=True, timeout=5
                )
                (testcase_dir / f"{tc}.out").write_text(andy_result.stdout, encoding="utf-8")

            # 8. Create xmuoj-import.zip
            tmp_import = prob_dir / "1"
            tmp_import.mkdir(exist_ok=True)
            (tmp_import / "testcase").mkdir(exist_ok=True)
            shutil.copy(prob_dir / "problem.json", tmp_import / "problem.json")
            for tc in range(1, 11):
                shutil.copy(testcase_dir / f"{tc}.in", tmp_import / "testcase" / f"{tc}.in")
                shutil.copy(testcase_dir / f"{tc}.out", tmp_import / "testcase" / f"{tc}.out")

            zip_path = prob_dir / "xmuoj-import.zip"
            with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
                for root, dirs, files in os.walk(str(tmp_import)):
                    for fname in files:
                        file_path = os.path.join(root, fname)
                        arcname = os.path.relpath(file_path, str(prob_dir))
                        zf.write(file_path, arcname)
            shutil.rmtree(tmp_import)

            # 9. Clean compiled binaries
            for f in ["gen.out", "Andy.out"]:
                p = prob_dir / f
                if p.exists(): p.unlink()

            zip_size = zip_path.stat().st_size
            tc_count = len(list(testcase_dir.glob("*.in")))
            print(f"✅ (ZIP:{zip_size}B, TC:{tc_count})")

        except Exception as e:
            print(f"❌ {e}")
            continue

    print(f"\n{'='*60}")
    print(f"✅ 第1章题库构建完成！")
    print(f"   路径: {OUTPUT}")
    print(f"   题目数: {total}")
    print(f"   总文件: {sum(1 for _ in OUTPUT.rglob('*') if _.is_file())}")
    print(f"{'='*60}")


if __name__ == "__main__":
    build_all()
