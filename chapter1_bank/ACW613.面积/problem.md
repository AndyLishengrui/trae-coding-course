# NQ013：面积

> 题目来源：AcWing 613 | 题目ID：ACW613 | 第1章 程序设计的第一个脚印

## 题目描述
计算三个图形面积：直角三角形A*C/2、圆π*C²、梯形(A+B)*C/2。π=3.14159。

### 输入格式
一行，三个浮点数A、B、C。

### 输出格式
三行：TRIANGULO: X / CIRCULO: X / TRAPEZIO: X，各保留3位小数。

### 样例
**输入：**
```
3.0 4.0 5.2
```
**输出：**
```
TRIANGULO: 7.800
CIRCULO: 84.949
TRAPEZIO: 18.200
```

## 解题思路
三道公式在一题。A、B、C在不同公式中扮演不同角色，需要仔细读题。

## 编程技巧
使用常量PI=3.14159。每个面积独立计算一行，分行输出。代码组织能力训练。

## 参考代码

### C++
```cpp
#include <cstdio>
int main() { double a,b,c; scanf("%lf%lf%lf",&a,&b,&c); printf("TRIANGULO: %.3lf\nCIRCULO: %.3lf\nTRAPEZIO: %.3lf\n",a*c/2,3.14159*c*c,(a+b)*c/2); return 0; }
```

### Python
```python
a, b, c = map(float, input().split())
print(f"TRIANGULO: {a*c/2:.3f}")
print(f"CIRCULO: {3.14159*c*c:.3f}")
print(f"TRAPEZIO: {(a+b)*c/2:.3f}")
```
