# NQ005：工资

> 题目来源：AcWing 609 | 题目ID：ACW609 | 第1章 程序设计的第一个脚印

## 题目描述
输入员工编号（整数）、月工作时数（整数）和时薪（浮点数），计算工资总额。

### 输入格式
三行：编号、时数、时薪。

### 输出格式
第一行"NUMBER = X"，第二行"SALARY = U$ XX.XX"。

### 样例
**输入：**
```
25
100
5.50
```
**输出：**
```
NUMBER = 25
SALARY = U$ 550.00
```

## 解题思路
工资 = 时数 × 时薪。输入包含整数和浮点数混合类型。注意输出两行，第二行保留2位小数。

## 编程技巧
C++中scanf可精确控制混合输入：scanf("%d%d%lf",&n,&h,&m)。Python逐行读取更清晰。

## 参考代码

### C++
```cpp
#include <cstdio>
int main() { int n,h; double m; scanf("%d%d%lf",&n,&h,&m); printf("NUMBER = %d\nSALARY = U$ %.2lf\n",n,h*m); return 0; }
```

### Python
```python
n = int(input())
h = int(input())
m = float(input())
print(f"NUMBER = {n}")
print(f"SALARY = U$ {h * m:.2f}")
```
