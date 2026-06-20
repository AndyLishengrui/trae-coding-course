#!/usr/bin/env python3
"""
格式化 chapter*_bank 中的 C++ 和 Python 代码：
- 合理的缩进与换行
- 关键注释（题目名、算法简介、时间复杂度）
- 同时写入 ACW 和 NQ 目录
"""
import os, sys
from pathlib import Path

BOOK_ROOT = Path(__file__).parent.parent

# ============================================================
# 第1章 — 14题完整代码定义
# ============================================================
CHAPTER1_PROBLEMS = [
    {
        "acw": 1, "nq": "NQ1-01",
        "cpp": """\
#include <iostream>
using namespace std;

/**
 * NQ1-01: A + B
 * 输入两个整数，输出它们的和。
 * 时间: O(1) | 空间: O(1)
 */
int main() {
    int a, b;
    cin >> a >> b;
    cout << a + b << endl;
    return 0;
}
""",
        "py": """\
# NQ1-01: A + B
# 输入两个整数，输出它们的和。

a, b = map(int, input().split())
print(a + b)
""",
    },
    {
        "acw": 608, "nq": "NQ1-02",
        "cpp": """\
#include <cstdio>

/**
 * NQ1-02: 差
 * 读取四个整数A,B,C,D，计算A*B-C*D。
 * 时间: O(1) | 空间: O(1)
 */
int main() {
    int a, b, c, d;
    scanf("%d%d%d%d", &a, &b, &c, &d);
    printf("DIFERENCA = %d\\n", a * b - c * d);
    return 0;
}
""",
        "py": """\
# NQ1-02: 差
# 读取四个整数，输出 A*B - C*D。

a, b, c, d = map(int, input().split())
print(f"DIFERENCA = {a * b - c * d}")
""",
    },
    {
        "acw": 604, "nq": "NQ1-03",
        "cpp": """\
#include <cstdio>

/**
 * NQ1-03: 圆的面积
 * 给定半径 r，计算面积。pi = 3.14159。
 * 时间: O(1) | 空间: O(1)
 */
int main() {
    double r;
    scanf("%lf", &r);
    printf("A=%.4lf\\n", 3.14159 * r * r);
    return 0;
}
""",
        "py": """\
# NQ1-03: 圆的面积
# 给定半径 r (浮点数)，计算圆的面积，保留4位小数。

PI = 3.14159
r = float(input())
print(f"A={PI * r * r:.4f}")
""",
    },
    {
        "acw": 606, "nq": "NQ1-04",
        "cpp": """\
#include <cstdio>

/**
 * NQ1-04: 平均数1
 * 加权平均分：A权重3.5，B权重7.5。
 * 时间: O(1) | 空间: O(1)
 */
int main() {
    double a, b;
    scanf("%lf%lf", &a, &b);
    printf("MEDIA = %.5lf\\n", (a * 3.5 + b * 7.5) / 11.0);
    return 0;
}
""",
        "py": """\
# NQ1-04: 平均数1
# 加权平均分: A(权重3.5) + B(权重7.5)，保留5位小数。

a = float(input())  # 学生A的成绩
b = float(input())  # 学生B的成绩
print(f"MEDIA = {(a * 3.5 + b * 7.5) / 11.0:.5f}")
""",
    },
    {
        "acw": 609, "nq": "NQ1-05",
        "cpp": """\
#include <cstdio>

/**
 * NQ1-05: 工资
 * 员工编号、月工作时数、时薪，计算工资总额。
 * 时间: O(1) | 空间: O(1)
 */
int main() {
    int number, hours;
    double rate;
    scanf("%d%d%lf", &number, &hours, &rate);
    printf("NUMBER = %d\\n", number);
    printf("SALARY = U$ %.2lf\\n", hours * rate);
    return 0;
}
""",
        "py": """\
# NQ1-05: 工资
# 输入员工编号、工作时数和时薪，计算工资总额。

number = int(input())   # 员工编号
hours = int(input())    # 月工作时数
rate = float(input())   # 时薪
print(f"NUMBER = {number}")
print(f"SALARY = U$ {hours * rate:.2f}")
""",
    },
    {
        "acw": 615, "nq": "NQ1-06",
        "cpp": """\
#include <cstdio>

/**
 * NQ1-06: 油耗
 * 行驶距离(km) / 消耗汽油量(L) = 每升公里数。
 * 时间: O(1) | 空间: O(1)
 */
int main() {
    double distance, fuel;
    scanf("%lf%lf", &distance, &fuel);
    printf("%.3lf km/l\\n", distance / fuel);
    return 0;
}
""",
        "py": """\
# NQ1-06: 油耗
# 输入行驶距离和消耗汽油量，计算每升公里数，保留3位小数。

distance = float(input())  # 行驶距离 (km)
fuel = float(input())      # 消耗汽油量 (L)
print(f"{distance / fuel:.3f} km/l")
""",
    },
    {
        "acw": 616, "nq": "NQ1-07",
        "cpp": """\
#include <cstdio>
#include <cmath>

/**
 * NQ1-07: 两点间的距离
 * 欧几里得距离: sqrt((x1-x2)^2 + (y1-y2)^2)。
 * 时间: O(1) | 空间: O(1)
 */
int main() {
    double x1, y1, x2, y2;
    scanf("%lf%lf%lf%lf", &x1, &y1, &x2, &y2);
    double dx = x1 - x2;
    double dy = y1 - y2;
    printf("%.4lf\\n", sqrt(dx * dx + dy * dy));
    return 0;
}
""",
        "py": """\
# NQ1-07: 两点间的距离
# 计算平面两点 P1(x1,y1) 和 P2(x2,y2) 的欧几里得距离，保留4位小数。

import math

x1, y1, x2, y2 = map(float, input().split())
distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
print(f"{distance:.4f}")
""",
    },
    {
        "acw": 653, "nq": "NQ1-08",
        "cpp": """\
#include <cstdio>

/**
 * NQ1-08: 钞票
 * 贪心: 用最少钞票数支付金额N。面额: 100,50,20,10,5,2,1。
 * 时间: O(1) | 空间: O(1)
 */
int main() {
    int n;
    int bills[] = {100, 50, 20, 10, 5, 2, 1};
    scanf("%d", &n);
    printf("%d\\n", n);
    for (int i = 0; i < 7; i++) {
        printf("%d nota(s) de R$ %d,00\\n", n / bills[i], bills[i]);
        n %= bills[i];
    }
    return 0;
}
""",
        "py": """\
# NQ1-08: 钞票
# 贪心算法: 用最少的钞票数量支付金额N。

n = int(input())
bills = [100, 50, 20, 10, 5, 2, 1]  # 面额从大到小

print(n)
for value in bills:
    print(f"{n // value} nota(s) de R$ {value},00")
    n %= value
""",
    },
    {
        "acw": 654, "nq": "NQ1-09",
        "cpp": """\
#include <cstdio>

/**
 * NQ1-09: 时间转换
 * 将总秒数N转换为时:分:秒格式。
 * 时间: O(1) | 空间: O(1)
 */
int main() {
    int n;
    scanf("%d", &n);
    int hours = n / 3600;
    int minutes = (n % 3600) / 60;
    int seconds = n % 60;
    printf("%d:%d:%d\\n", hours, minutes, seconds);
    return 0;
}
""",
        "py": """\
# NQ1-09: 时间转换
# 将总秒数N转换为 HH:MM:SS 格式。

n = int(input())

hours, remainder = divmod(n, 3600)
minutes, seconds = divmod(remainder, 60)

print(f"{hours}:{minutes}:{seconds}")
""",
    },
    {
        "acw": 605, "nq": "NQ1-10",
        "cpp": """\
#include <iostream>
using namespace std;

/**
 * NQ1-10: 简单乘积
 * 读取两个整数，输出 PROD = 乘积。
 * 时间: O(1) | 空间: O(1)
 */
int main() {
    int a, b;
    cin >> a >> b;
    cout << "PROD = " << a * b << endl;
    return 0;
}
""",
        "py": """\
# NQ1-10: 简单乘积
# 读取两个整数，输出它们的乘积。

a = int(input())
b = int(input())
print(f"PROD = {a * b}")
""",
    },
    {
        "acw": 611, "nq": "NQ1-11",
        "cpp": """\
#include <cstdio>

/**
 * NQ1-11: 简单计算
 * 根据产品编号、数量和单价，计算总价。
 * 时间: O(1) | 空间: O(1)
 */
int main() {
    int code, quantity;
    double price;
    scanf("%d%d%lf", &code, &quantity, &price);
    printf("VALOR A PAGAR: R$ %.2lf\\n", quantity * price);
    return 0;
}
""",
        "py": """\
# NQ1-11: 简单计算
# 输入产品编号、数量和单价，计算应付总额。

code, quantity = map(int, input().split())
price = float(input())
print(f"VALOR A PAGAR: R$ {quantity * price:.2f}")
""",
    },
    {
        "acw": 612, "nq": "NQ1-12",
        "cpp": """\
#include <cstdio>

/**
 * NQ1-12: 球的体积
 * V = (4/3) * pi * r^3, pi = 3.14159。
 * 时间: O(1) | 空间: O(1)
 */
int main() {
    int r;
    scanf("%d", &r);
    double volume = (4.0 / 3.0) * 3.14159 * r * r * r;
    printf("VOLUME = %.3lf\\n", volume);
    return 0;
}
""",
        "py": """\
# NQ1-12: 球的体积
# V = (4/3) * pi * r^3, pi = 3.14159, 保留3位小数。

PI = 3.14159
r = int(input())
volume = (4.0 / 3.0) * PI * (r ** 3)
print(f"VOLUME = {volume:.3f}")
""",
    },
    {
        "acw": 613, "nq": "NQ1-13",
        "cpp": """\
#include <cstdio>

/**
 * NQ1-13: 面积
 * 计算三个图形面积: 直角三角形、圆、梯形。
 * 时间: O(1) | 空间: O(1)
 */
int main() {
    double a, b, c;
    scanf("%lf%lf%lf", &a, &b, &c);
    const double PI = 3.14159;
    printf("TRIANGULO: %.3lf\\n", a * c / 2.0);          // 直角三角形
    printf("CIRCULO: %.3lf\\n", PI * c * c);              // 圆
    printf("TRAPEZIO: %.3lf\\n", (a + b) * c / 2.0);     // 梯形
    return 0;
}
""",
        "py": """\
# NQ1-13: 面积
# 计算三个图形面积: 直角三角形、圆、梯形，各保留3位小数。

PI = 3.14159
a, b, c = map(float, input().split())

print(f"TRIANGULO: {a * c / 2.0:.3f}")   # 直角三角形: A*C/2
print(f"CIRCULO: {PI * c * c:.3f}")       # 圆: pi*C^2
print(f"TRAPEZIO: {(a + b) * c / 2.0:.3f}")  # 梯形: (A+B)*C/2
""",
    },
    {
        "acw": 614, "nq": "NQ1-14",
        "cpp": """\
#include <iostream>
#include <algorithm>
using namespace std;

/**
 * NQ1-14: 最大值
 * 输入三个整数，输出其中的最大值。
 * 时间: O(1) | 空间: O(1)
 */
int main() {
    int a, b, c;
    cin >> a >> b >> c;
    // max({...}) 是 C++11 的初始化列表用法
    cout << max({a, b, c}) << endl;
    return 0;
}
""",
        "py": """\
# NQ1-14: 最大值
# 输入三个整数 a, b, c，输出其中的最大值。

a, b, c = map(int, input().split())
print(max(a, b, c))
""",
    },
]


def get_acw_dirname(bank_dir, acw_id):
    """找到匹配 AcWing ID 的目录名"""
    for subdir in bank_dir.iterdir():
        if subdir.is_dir():
            name = subdir.name.lower()
            if f"acw{acw_id}" in name or f"acw_{acw_id}" in name:
                return subdir
    return None


def get_nq_dirname(bank_dir, nq_id):
    """找到匹配 NQ ID 的目录名"""
    for subdir in bank_dir.iterdir():
        if subdir.is_dir() and subdir.name.startswith(nq_id):
            return subdir
    return None


def write_code(filepath, content):
    """写入代码文件，确保末尾换行"""
    filepath.write_text(content.strip() + "\n", encoding="utf-8")


def format_chapter(chapter, problems):
    """格式化一个章节的所有代码文件"""
    bank_dir = BOOK_ROOT / f"chapter{chapter}_bank"
    if not bank_dir.exists():
        print(f"⚠️  {bank_dir} 不存在，跳过")
        return

    formatted_cpp = 0
    formatted_py = 0
    created_cpp = 0
    created_py = 0

    for prob in problems:
        acw = prob["acw"]
        nq = prob["nq"]

        # 先找匹配的目录（优先 NQ，再 ACW）
        nq_dir = get_nq_dirname(bank_dir, nq)
        acw_dir = get_acw_dirname(bank_dir, acw)

        dirs_to_update = []
        if nq_dir:
            dirs_to_update.append(nq_dir)
        if acw_dir:
            dirs_to_update.append(acw_dir)
        if not dirs_to_update:
            # 都没有就创建 NQ 目录
            safe_title = "".join(c for c in prob["cpp"].split("\n")[3].replace("*","").replace(":","").strip().split(" ")[0] if c.isalnum() or '一' <= c <= '鿿')
            dirs_to_update.append(bank_dir / nq)

        for d in dirs_to_update:
            os.makedirs(d, exist_ok=True)

            cpp_path = d / "Andy.cpp"
            py_path = d / "Andy.py"

            if cpp_path.exists():
                formatted_cpp += 1
            else:
                created_cpp += 1
            write_code(cpp_path, prob["cpp"])

            if py_path.exists():
                formatted_py += 1
            else:
                created_py += 1
            write_code(py_path, prob["py"])

    print(f"\n📊 第{chapter}章代码格式化完成:")
    print(f"   C++: 格式化 {formatted_cpp}, 新建 {created_cpp}")
    print(f"   Python: 格式化 {formatted_py}, 新建 {created_py}")


def main():
    import argparse
    parser = argparse.ArgumentParser(description="格式化章节代码")
    parser.add_argument("--chapter", "-c", type=int, default=1, help="章节编号")
    args = parser.parse_args()

    if args.chapter == 1:
        format_chapter(1, CHAPTER1_PROBLEMS)
    else:
        print(f"第{args.chapter}章暂未定义代码模板。")
        print("请先在 format_chapter_codes.py 中添加 CHAPTER{args.chapter}_PROBLEMS。")
        sys.exit(1)

    print("\n✅ 完成！")


if __name__ == "__main__":
    main()
