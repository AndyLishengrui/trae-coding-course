# NQ003：圆的面积

> 题目来源：AcWing 604 | 题目ID：ACW604 | 第1章 程序设计的第一个脚印

## 题目描述
给定圆的半径r，计算圆的面积。π取3.14159。

### 输入格式
一个浮点数r，表示圆的半径。

### 输出格式
输出"A="后跟圆的面积，结果保留4位小数。

### 样例
**输入：**
```
2.00
```
**输出：**
```
A=12.5664
```

## 解题思路
圆的面积 = π × r²。需要使用浮点数类型double/float。C++用printf("%.4lf")控制小数位数，Python用f"{area:.4f}"。

## 编程技巧
C++格式化输出两种风格：printf("%.4lf",x)简洁；cout<<fixed<<setprecision(4)<<x类型安全。Python的f"{x:.4f}"最直观。

## 参考代码

### C++
```cpp
#include <cstdio>
int main() { double r; scanf("%lf",&r); printf("A=%.4lf\n",3.14159*r*r); return 0; }
```

### Python
```python
r = float(input())
print(f"A={3.14159 * r * r:.4f}")
```
