# NQ002：差

> 题目来源：AcWing 608 | 题目ID：ACW608 | 第1章 程序设计的第一个脚印

## 题目描述
读取四个整数A、B、C、D，计算A×B−C×D的结果。

### 输入格式
一行，四个整数A、B、C、D，用空格隔开。

### 输出格式
输出"DIFERENCA = "后跟计算结果。

### 样例
**输入：**
```
5 6 7 8
```
**输出：**
```
DIFERENCA = -26
```

## 解题思路
直接按公式计算即可。注意运算顺序：先乘后减。输出时带前缀"DIFERENCA = "。

## 编程技巧
Python的f-string格式化输出：f"DIFERENCA = {a*b-c*d}"。f-string是Python 3.6+最推荐的格式化方式。

## 参考代码

### C++
```cpp
#include <cstdio>
int main() { int a,b,c,d; scanf("%d%d%d%d",&a,&b,&c,&d); printf("DIFERENCA = %d\n",a*b-c*d); return 0; }
```

### Python
```python
a, b, c, d = map(int, input().split())
print(f"DIFERENCA = {a * b - c * d}")
```
