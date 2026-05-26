# 第1课：AI与你，Hello World

> **课时：** 2小时 | **题目：** 3例题 + 3练习 | **难度：** ⭐

---

## 一、本课目标

学完本课后，你将能够：

1. 使用 Trae AI 工具编写并运行你的第一个 C++ 和 Python 程序
2. 理解"输入 → 处理 → 输出"的基本程序结构
3. 掌握整数和浮点数的基本运算
4. 用 `cin/cout`（C++）和 `input/print`（Python）与程序交互
5. 初步体验 AI 辅助编程：用自然语言描述需求，让 AI 生成代码，然后逐行读懂

---

## 二、Python 工具箱预览

本课涉及的 Python 工具都很基础，但它们是后续一切的基石：

| 工具 | 作用 | 示例 |
|------|------|------|
| `input()` | 读取用户输入（返回字符串） | `name = input()` |
| `print()` | 输出到屏幕 | `print("Hello")` |
| `int()` | 转换为整数 | `int("42")` → `42` |
| `float()` | 转换为浮点数 | `float("3.14")` → `3.14` |
| `map(int, ...)` | 批量转换输入 | `a, b = map(int, input().split())` |
| `f-string` | 格式化字符串 | `f"A={value:.4f}"` |
| `math.pi` | 圆周率 π | `import math` 后使用 |

> **和 C++ 的主要差异：** Python 不需要声明变量类型，不需要分号结尾，也不需要 `main()` 函数。直接写逻辑即可。

---

## 三、例题精讲

### 例题1：A + B（NQ001）

**题目描述**

输入两个整数 A 和 B，输出它们的和。

**输入格式**
```
一行，两个整数 A 和 B，用空格分隔。
```

**输出格式**
```
一个整数，即 A + B 的结果。
```

**样例**
```
输入：3 4
输出：7
```

**C++ 解法**

```cpp
#include <iostream>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;
    cout << a + b << endl;
    return 0;
}
```

**Python 解法**

```python
a, b = map(int, input().split())
print(a + b)
```

**逐行对比 + AI 解读要点**

| 步骤 | C++ | Python | 理解 |
|------|-----|--------|------|
| 引入库 | `#include <iostream>` | （不需要） | Python 内置了输入输出 |
| 程序入口 | `int main() {` | （不需要） | Python 脚本从第一行开始执行 |
| 声明变量 | `int a, b;` | （不需要） | Python 的变量用的时候直接赋值 |
| 读取输入 | `cin >> a >> b;` | `input().split()` | C++ 用 `>>`，Python 用 `input()` 读取整行再分割 |
| 类型转换 | 声明时已定 | `map(int, ...)` | C++ 在声明时定类型，Python 在输入时指定 |
| 输出 | `cout << a + b << endl;` | `print(a + b)` | 两种语言都很直观 |

**AI 教学点：** 这是你的第一个程序。试着对 Trae 说：_"帮我写一个程序，读取两个用空格分开的整数，输出它们的和，用 C++ 和 Python 各写一份。"_ 观察 AI 生成的代码和你刚才看到的是否一致。**会问 AI 是第一层，能看懂 AI 的输出是第二层。**

---

### 例题2：圆的面积（NQ002）

**题目描述**

给定圆的半径 r，计算圆的面积。π 取 3.14159。

**输入格式**
```
一个浮点数 r，表示圆的半径。
```

**输出格式**
```
输出 "A=" 后跟圆的面积，结果保留4位小数。
```

**样例**
```
输入：2.00
输出：A=12.5664
```

**C++ 解法**

```cpp
#include <cstdio>
using namespace std;

int main() {
    double pi = 3.14159, r;
    scanf("%lf", &r);
    printf("A=%.4lf\n", pi * r * r);
    return 0;
}
```

**Python 解法**

```python
import math

r = float(input())
area = 3.14159 * r * r
print(f"A={area:.4f}")
```

**关键知识点：格式化输出**

C++ 的 `printf` 和 Python 的 `f-string` 都能精确控制小数位数：

| 需求 | C++ `printf` | Python `f-string` |
|------|-------------|-------------------|
| 保留2位小数 | `printf("%.2lf", x)` | `f"{x:.2f}"` |
| 保留4位小数 | `printf("%.4lf", x)` | `f"{x:.4f}"` |
| 整数输出 | `printf("%d", n)` | `f"{n}"` 或 `print(n)` |

**AI 教学点：** 你不需要记住这些格式。需要的时候对 Trae 说："帮我把变量 area 输出为保留4位小数的格式"。**但你要能读懂 AI 给出的代码里 `f"{area:.4f}"` 是什么意思。**

---

### 例题3：平均数1（NQ003）

**题目描述**

读取两个学生的成绩 A 和 B。A 的权重为 3.5，B 的权重为 7.5。计算加权平均分。

**输入格式**
```
两行，每行一个浮点数，分别表示 A 和 B。
```

**输出格式**
```
输出 "MEDIA = " 后跟加权平均分，保留5位小数。
```

**样例**
```
输入：
5.0
7.1
输出：MEDIA = 6.43182
```

**C++ 解法**

```cpp
#include <cstdio>

int main() {
    double a, b;
    scanf("%lf%lf", &a, &b);
    printf("MEDIA = %.5lf\n", (a * 3.5 + b * 7.5) / 11);
    return 0;
}
```

**Python 解法**

```python
a = float(input())
b = float(input())
avg = (a * 3.5 + b * 7.5) / 11.0
print(f"MEDIA = {avg:.5f}")
```

**知识点深入：类型转换与精度**

- C++ 中 `3.5` 默认是 `double` 类型，`11` 是 `int`，`11.0` 是 `double`。除以 `int` 和除以 `double` 的结果不同。
- Python 的 `/` 总是返回浮点数，不需要担心整数除法的问题。

**AI 教学点：** 让 Trae 解释"加权平均"的公式 `(a * 3.5 + b * 7.5) / 11` 中分母为什么是 11 而不是 2。这也是 AI 辅助学习的重要技能——**不仅要让 AI 写代码，还要让它解释"为什么"。**

---

## 四、课堂练习

### 练习1：简单乘积（NQ004）

读取两个整数，输出 `"PROD = "` 后跟它们的乘积。

```
输入：
3
9
输出：PROD = 27
```

| 文件 | 路径 |
|------|------|
| C++ | `codes/nq004_simple_product.cpp` |
| Python | `codes/nq004_simple_product.py` |

**提示：** 将例题1的 `a + b` 改为 `a * b`，并添加输出前缀 `"PROD = "`。

---

### 练习2：工资（NQ005）

输入员工编号（整数）、工作时数（整数）、时薪（浮点数）。输出员工编号和工资 `"SALARY = U$ "` 后跟总工资（时数×时薪，保留2位小数）。

```
输入：
25
100
5.50
输出：
NUMBER = 25
SALARY = U$ 550.00
```

| 文件 | 路径 |
|------|------|
| C++ | `codes/nq005_salary.cpp` |
| Python | `codes/nq005_salary.py` |

**提示：** 注意 `double`（C++）和 `float`（Python）的使用。格式化时薪保留2位小数。

---

### 练习3：油耗（NQ006）

输入行驶距离（km，浮点数）和消耗燃料量（L，浮点数），输出每升燃料能行驶的公里数（保留3位小数）。

```
输入：
500
35.0
输出：14.286 km/l
```

| 文件 | 路径 |
|------|------|
| C++ | `codes/nq006_fuel_consumption.cpp` |
| Python | `codes/nq006_fuel_consumption.py` |

**提示：** 本题只需一次除法。重点是格式化输出的精度控制。

---

## 五、AI 协作要点

本课是学生第一次用 AI 写代码。以下是教练需要强调的三个关键理念：

### 1. AI 是"副驾驶"，不是"自动驾驶"

```
❌ 错误用法：把题目直接丢给AI → 复制结果 → 提交
✅ 正确用法：把题目丢给AI → 逐行阅读代码 → 修改不理解的地方 → 运行测试 → 理解后提交
```

### 2. 读代码能力是第一课的核心

本课6道题都很简单。简单的目的不是"让学生自己写出来"，而是**"让学生完全理解AI写的每一行"**。

如果学生无法解释 `a, b = map(int, input().split())` 中每个部分的作用，那么就算他提交了100道题，也没学会编程。

### 3. "问为什么"比"得到答案"更重要

当学生对AI生成的代码有疑问时，他应该：
1. 先把疑问用自然语言写出来
2. 把这个问题发给AI
3. 阅读AI的解释
4. 用一个小例子验证自己理解了

---

## 六、课后总结

```
本课核心 takeaway：

1. 程序 = 输入 + 处理 + 输出
2. C++ 需要声明类型和 main 函数，Python 更直白
3. 格式化输出：C++用 printf，Python用 f-string
4. AI 是工具，读懂 AI 写的代码才是你要学的
5. 不懂就问 AI "为什么"，别只看答案
```

**下一课预告：** 第2课《变量与选择》—— 更多数据类型、条件判断（if/else）、以及 Python 中链式比较的魔法。

---

## 题目对照表

| 题号 | 题目 | 类型 | AcWing | C++ | Python |
|------|------|------|--------|-----|--------|
| NQ001 | A + B | 例题 | AcWing 1 | [nq001_A_plus_B.cpp](codes/nq001_A_plus_B.cpp) | [nq001_A_plus_B.py](codes/nq001_A_plus_B.py) |
| NQ002 | 圆的面积 | 例题 | AcWing 604 | [nq002_circle_area.cpp](codes/nq002_circle_area.cpp) | [nq002_circle_area.py](codes/nq002_circle_area.py) |
| NQ003 | 平均数1 | 例题 | AcWing 606 | [nq003_average1.cpp](codes/nq003_average1.cpp) | [nq003_average1.py](codes/nq003_average1.py) |
| NQ004 | 简单乘积 | 练习 | AcWing 605 | [nq004_simple_product.cpp](codes/nq004_simple_product.cpp) | [nq004_simple_product.py](codes/nq004_simple_product.py) |
| NQ005 | 工资 | 练习 | AcWing 609 | [nq005_salary.cpp](codes/nq005_salary.cpp) | [nq005_salary.py](codes/nq005_salary.py) |
| NQ006 | 油耗 | 练习 | AcWing 615 | [nq006_fuel_consumption.cpp](codes/nq006_fuel_consumption.cpp) | [nq006_fuel_consumption.py](codes/nq006_fuel_consumption.py) |
