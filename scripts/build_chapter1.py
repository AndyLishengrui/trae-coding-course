#!/usr/bin/env python3
"""Build Chapter 1 of the V2 textbook."""
import os

def read_cpp(nq_num, pid):
    path = f'lessons_v2/lesson01/codes/nq{nq_num:03d}_acw{pid}.cpp'
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return '// code not found'

def read_py(nq_num, pid):
    path = f'lessons_v2/lesson01/codes/nq{nq_num:03d}_acw{pid}.py'
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return '# Python solution'

problems = [
    {
        "nq": "001", "pid": 1, "title": "A + B",
        "desc": "小鲁第一次打开TRAE，AI助手提示他：\"想学编程，从最简单的计算开始。\"请输入两个整数A和B，计算它们的和。",
        "input_fmt": "一行，两个整数A和B，用空格隔开。",
        "output_fmt": "一个整数，即A+B的结果。",
        "sample_in": "3 4", "sample_out": "7",
        "constraints": "0 ≤ A, B ≤ 10⁸",
        "solution": "这是编程中最简单的题目，但它包含了所有程序的基本骨架：读入数据→计算→输出结果。C++中需要引入iostream库，声明main函数，用cin读入，cout输出。Python则更简洁，input()读入一行，split()分割，map(int,...)转为整数，print()输出。两种语言体现了静态类型和动态类型的设计哲学差异。",
        "technique": "Python的map(int, input().split())是处理空格分隔的整数输入的标准写法。C++的cin >> a >> b自动跳过空白字符，非常方便。",
    },
    {
        "nq": "002", "pid": 608, "title": "差",
        "desc": "小鲁在数学课上学到了\"差\"的概念。老师给出四个整数A、B、C、D，请计算A×B−C×D的结果。",
        "input_fmt": "一行，四个整数A、B、C、D，用空格隔开。",
        "output_fmt": "输出\"DIFERENCA = \"后跟计算结果。",
        "sample_in": "5 6 7 8", "sample_out": "DIFERENCA = -26",
        "constraints": "−10000 ≤ A,B,C,D ≤ 10000",
        "solution": "直接按公式计算即可。注意运算顺序：先乘后减。C++中用int可满足范围（−10⁸到10⁸）。Python的int无范围限制。输出时需要带前缀\"DIFERENCA = \"。",
        "technique": "Python的f-string格式化输出：f\"DIFERENCA = {a*b - c*d}\"。f-string是Python 3.6+最推荐的字符串格式化方式，比%和.format()更清晰。",
    },
    {
        "nq": "003", "pid": 604, "title": "圆的面积",
        "desc": "小鲁在几何课上学到了圆的面积公式S=πr²。他决定写一个程序来计算任意半径的圆的面积。π取3.14159。",
        "input_fmt": "一个浮点数r，表示圆的半径。",
        "output_fmt": "输出\"A=\"后跟圆的面积，结果保留4位小数。",
        "sample_in": "2.00", "sample_out": "A=12.5664",
        "constraints": "0 < r ≤ 10000",
        "solution": "圆的面积 = π × r²。需要使用浮点数类型：C++中为double，Python中为float。面积计算结果需要保留4位小数，C++用printf(\"%.4lf\")或cout<<fixed<<setprecision(4)，Python用f\"{area:.4f}\"。",
        "technique": "C++格式化输出的两种风格：C风格printf(\"%.4lf\", x)简洁精确；C++风格cout<<fixed<<setprecision(4)<<x类型安全。Python的f\"{x:.4f}\"最直观。",
    },
    {
        "nq": "004", "pid": 606, "title": "平均数1",
        "desc": "学期结束了，老师需要计算小鲁的加权平均成绩。A科目的权重是3.5，B科目的权重是7.5。请帮老师计算加权平均数。",
        "input_fmt": "两行，每行一个浮点数，分别表示成绩A和成绩B。",
        "output_fmt": "输出\"MEDIA = \"后跟加权平均分，保留5位小数。",
        "sample_in": "5.0\\n7.1", "sample_out": "MEDIA = 6.43182",
        "constraints": "0 ≤ A, B ≤ 10.0",
        "solution": "加权平均公式：(A×3.5 + B×7.5) / (3.5+7.5) = (A×3.5 + B×7.5) / 11。分母是权重之和(3.5+7.5=11)，不要误以为是2。保留5位小数的格式化输出。",
        "technique": "注意整数除法和浮点除法的区别。C++中3.5/11是浮点除法，结果正确。Python的/总是返回浮点数，无需担心。",
    },
    {
        "nq": "005", "pid": 609, "title": "工资",
        "desc": "小鲁暑假去打工，公司需要计算他的工资。已知员工编号（整数）、每月工作小时数（整数）和时薪（浮点数），请计算月工资总额。",
        "input_fmt": "三行：第一行员工编号（整数），第二行工作时数（整数），第三行时薪（浮点数）。",
        "output_fmt": "第一行输出\"NUMBER = \"后跟员工编号。第二行输出\"SALARY = U$ \"后跟工资总额（保留2位小数）。",
        "sample_in": "25\\n100\\n5.50", "sample_out": "NUMBER = 25\\nSALARY = U$ 550.00",
        "constraints": "1 ≤ 编号 ≤ 100，1 ≤ 时数 ≤ 200，1 ≤ 时薪 ≤ 50",
        "solution": "工资 = 工作小时数 × 时薪。注意输入类型：编号和时数是int，时薪是double/float。输出两行，第一行输出编号，第二行格式化输出工资。",
        "technique": "C++中用scanf可以精确控制多种类型混合输入：scanf(\"%d%d%lf\", &number, &hour, &money)。Python中注意int()和float()的转换。",
    },
    {
        "nq": "006", "pid": 615, "title": "油耗",
        "desc": "小鲁买了一辆二手车，想测试它的油耗。他记录了行驶的总距离（公里）和消耗的汽油总量（升）。请计算每升汽油可以行驶多少公里。",
        "input_fmt": "两行：第一行行驶距离（浮点数，km），第二行消耗汽油量（浮点数，L）。",
        "output_fmt": "输出每升行驶公里数，保留3位小数，后跟\" km/l\"。",
        "sample_in": "500\\n35.0", "sample_out": "14.286 km/l",
        "constraints": "1 ≤ 距离 ≤ 10⁶，0 < 汽油量 ≤ 10⁵",
        "solution": "燃油效率 = 行驶距离 / 消耗汽油量。注意除法的精度问题，用浮点数除法。输出格式：保留3位小数 + \" km/l\"。",
        "technique": "C++中如果距离是整数需先转为double再做除法。Python中/自动返回浮点数。",
    },
    {
        "nq": "007", "pid": 616, "title": "两点间的距离",
        "desc": "小鲁在坐标系上标记了两个点P1(x1,y1)和P2(x2,y2)。他想知道这两点之间的欧几里得距离。",
        "input_fmt": "一行，四个浮点数x1, y1, x2, y2，用空格隔开。",
        "output_fmt": "输出两点间的距离，保留4位小数。",
        "sample_in": "1.0 7.0 5.0 9.0", "sample_out": "4.4721",
        "constraints": "−10⁹ ≤ x1,y1,x2,y2 ≤ 10⁹",
        "solution": "距离公式：√((x1−x2)² + (y1−y2)²)。需要用math.sqrt()（Python）或sqrt()（C++的cmath）。这是第一次用到数学库函数。注意浮点数精度，使用double而非float。",
        "technique": "C++需要#include <cmath>并使用sqrt()。Python的math.sqrt()比**0.5更精确。f-string格式化：f\"{dist:.4f}\"。",
    },
    {
        "nq": "008", "pid": 653, "title": "钞票",
        "desc": "小鲁在银行取钱。ATM机需要给出最少数量的钞票。给定金额N（整数），请计算需要多少张100、50、20、10、5、2和1元钞票。",
        "input_fmt": "一个整数N，表示金额。",
        "output_fmt": "第一行输出N。然后7行，每行输出\"X nota(s) de R$ Y,00\"，X是张数，Y是面额。按面额从大到小输出。",
        "sample_in": "576",
        "sample_out": "576\\n5 nota(s) de R$ 100,00\\n1 nota(s) de R$ 50,00\\n1 nota(s) de R$ 20,00\\n0 nota(s) de R$ 10,00\\n1 nota(s) de R$ 5,00\\n0 nota(s) de R$ 2,00\\n1 nota(s) de R$ 1,00",
        "constraints": "0 < N < 10⁶",
        "solution": "这是贪心算法的雏形。从最大面额开始，每次尽可能多地使用当前面额，余数交给更小面额处理。用除法和取模：count = N // face_value; N %= face_value。C++代码中写了7段几乎相同的逻辑，而Python用列表+循环消除了重复——这是本课最重要的工程思维。",
        "technique": "Python用列表+循环消除重复代码：for note in [100,50,20,10,5,2,1]: count, n = divmod(n, note)。C++中重复7段相同逻辑。对比两版代码，理解\"用数据结构消除重复\"的工程思维。",
    },
    {
        "nq": "009", "pid": 654, "title": "时间转换",
        "desc": "小鲁的计时器只显示秒数，他想把它转换成\"时:分:秒\"的格式。给定总秒数N，请转换成HH:MM:SS格式。",
        "input_fmt": "一个整数N，表示总秒数。",
        "output_fmt": "输出\"HH:MM:SS\"格式的时间。",
        "sample_in": "556", "sample_out": "0:9:16",
        "constraints": "0 ≤ N ≤ 10⁶",
        "solution": "时 = N / 3600，余数 = N % 3600。分 = 余数 / 60。秒 = 余数 % 60。Python中divmod()函数可以一次同时获得商和余数：h, rem = divmod(n, 3600); m, s = divmod(rem, 60)。",
        "technique": "Python的divmod(a, b)返回(商, 余数)元组，可以优雅地用解包接收。C++中需要分开计算/和%。",
    },
    {
        "nq": "010", "pid": 605, "title": "简单乘积",
        "desc": "小鲁发现乘法比加法快得多。他想验证：给定两个整数，计算它们的乘积。",
        "input_fmt": "两行，每行一个整数。",
        "output_fmt": "输出\"PROD = \"后跟两数的乘积。",
        "sample_in": "3\\n9", "sample_out": "PROD = 27",
        "constraints": "−10⁴ ≤ A, B ≤ 10⁴",
        "solution": "和第1题A+B结构完全相同，只需把+改成*，并添加\"PROD = \"前缀。这个练习的目的是让学生自己独立完成一次\"修改→编译→运行→AC\"的完整流程。",
        "technique": "修改已有代码比从零开始更高效。用TRAE打开第1题的代码，让AI帮你把+改成*，添加PROD前缀，然后提交。",
    },
    {
        "nq": "011", "pid": 611, "title": "简单计算",
        "desc": "小鲁想写一个程序，根据给定的产品编号、数量和单价，计算总价。给定两行输入：第一行包含两个整数（产品编号和数量），第二行包含一个浮点数（单价）。",
        "input_fmt": "第一行：两个整数code和quantity。第二行：一个浮点数price。",
        "output_fmt": "输出\"VALOR A PAGAR: R$ \"后跟总价（保留2位小数）。",
        "sample_in": "12 1\\n5.30", "sample_out": "VALOR A PAGAR: R$ 5.30",
        "constraints": "1 ≤ code ≤ 100, 1 ≤ quantity ≤ 100, 0 < price ≤ 1000",
        "solution": "总价 = 数量 × 单价。混合使用整数和浮点数运算。输出需要保留2位小数。",
        "technique": "C++中int × double自动转换为double。Python中int × float自动转换为float。语言会自动处理类型提升。",
    },
    {
        "nq": "012", "pid": 612, "title": "球的体积",
        "desc": "小鲁在物理课上学习了球体的体积公式V = (4/3)πr³。请你写一个程序，根据给定的半径r计算球的体积。π取3.14159。",
        "input_fmt": "一个整数r，表示球的半径。",
        "output_fmt": "输出\"VOLUME = \"后跟球的体积，保留3位小数。",
        "sample_in": "3", "sample_out": "VOLUME = 113.097",
        "constraints": "1 ≤ r ≤ 1000",
        "solution": "公式：V = (4.0/3.0) × π × r³。注意4/3应写成4.0/3.0以确保浮点除法。π=3.14159。r³可以写成r*r*r或pow(r,3)。",
        "technique": "C++中4/3=1（整数除法陷阱），必须写成4.0/3.0。Python中4/3自动浮点。这是C++初学者最容易犯的错误之一。",
    },
    {
        "nq": "013", "pid": 613, "title": "面积",
        "desc": "小鲁需要计算三个常见几何图形的面积：(1)直角三角形（两条直角边A和C）；(2)圆（半径C，π=3.14159）；(3)梯形（上底A、下底B、高C）。",
        "input_fmt": "一行，三个浮点数A、B、C。",
        "output_fmt": "三行，分别输出三个面积，保留3位小数。格式：TRIANGULO: X / CIRCULO: X / TRAPEZIO: X。",
        "sample_in": "3.0 4.0 5.2",
        "sample_out": "TRIANGULO: 7.800\\nCIRCULO: 84.949\\nTRAPEZIO: 18.200",
        "constraints": "0 < A, B, C ≤ 100",
        "solution": "三道公式在一题：三角形面积 = A×C/2，圆面积 = π×C²，梯形面积 = (A+B)×C/2。需要仔细读题：不同公式中A、B、C扮演的角色不同。使用常量PI=3.14159。",
        "technique": "一道题包含三个独立计算，是测试代码组织能力的好题。每个面积用一行代码计算，分行输出。",
    },
    {
        "nq": "014", "pid": 614, "title": "最大值",
        "desc": "小鲁想写一个函数来找出三个整数中的最大值。输入三个整数a、b、c，输出其中的最大者。",
        "input_fmt": "一行，三个整数，用空格隔开。",
        "output_fmt": "一个整数，即三个数中的最大值。",
        "sample_in": "7 14 106", "sample_out": "106",
        "constraints": "−10⁹ ≤ a, b, c ≤ 10⁹",
        "solution": "方法1：用max()函数：C++中max({a,b,c})（需要C++11和<algorithm>），或max(a, max(b, c))。Python的max(a,b,c)直接接收多个参数。方法2：比较法，先比a和b取大的，再和c比。",
        "technique": "Python的max()和min()内置函数接受任意多个参数，比C++的嵌套调用更优雅。使用abs()求绝对值也是Python内置的。这体现了Python\"电池已包含\"的设计哲学。",
    },
]

lines = []
lines.append("# 第1章 程序设计的第一个脚印\n")
lines.append("> **变量、输入输出与顺序结构**  |  14题  |  NQ001-NQ014\n")
lines.append("> 看完每一题的解题思路，读懂C++和Python的双语代码，然后上机AC。\n")
lines.append("---\n")

for p in problems:
    nq = p["nq"]
    pid = p["pid"]

    lines.append(f"## NQ{nq}：{p['title']}")
    lines.append(f"> 题目来源：AcWing {pid}")
    lines.append("")
    lines.append("### 描述")
    lines.append(p["desc"])
    lines.append("")
    lines.append("### 输入格式")
    lines.append(p["input_fmt"])
    lines.append("")
    lines.append("### 输出格式")
    lines.append(p["output_fmt"])
    lines.append("")
    lines.append("### 样例")
    lines.append("**输入：**")
    lines.append("```")
    lines.append(p["sample_in"].replace("\\n", "\n"))
    lines.append("```")
    lines.append("**输出：**")
    lines.append("```")
    lines.append(p["sample_out"].replace("\\n", "\n"))
    lines.append("```")
    lines.append("")
    lines.append(f"**数据范围：** {p['constraints']}")
    lines.append("")
    lines.append("### 解题思路")
    lines.append(p["solution"])
    lines.append("")
    lines.append("### 编程技巧")
    lines.append(p["technique"])
    lines.append("")
    lines.append("### 参考代码")
    lines.append("")

    nq_int = int(nq)
    cpp_code = read_cpp(nq_int, pid)
    py_code = read_py(nq_int, pid)

    lines.append("**C++ Code:**")
    lines.append("```cpp")
    lines.append(cpp_code)
    lines.append("```")
    lines.append("")
    lines.append("**Python Code:**")
    lines.append("```python")
    lines.append(py_code)
    lines.append("```")
    lines.append("")
    lines.append("---")
    lines.append("")

textbook_path = 'textbook/chapter01_basics.md'
with open(textbook_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

content = '\n'.join(lines)
print(f"Chapter 1 written: {len(problems)} problems, {len(content)} chars")
print(f"Saved to: {textbook_path}")
