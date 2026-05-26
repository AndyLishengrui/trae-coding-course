# NQ011：简单计算

> 题目来源：AcWing 611 | 题目ID：ACW611 | 第1章 程序设计的第一个脚印

## 题目描述
根据产品编号、数量和单价，计算总价。

### 输入格式
第一行两个整数（编号和数量），第二行一个浮点数（单价）。

### 输出格式
"VALOR A PAGAR: R$ XX.XX"。

### 样例
**输入：**
```
12 1
5.30
```
**输出：**
```
VALOR A PAGAR: R$ 5.30
```

## 解题思路
总价 = 数量 × 单价。int × float自动转为double/float。

## 编程技巧
类型提升规则：int×float自动得到更精确的类型。C++提升到double，Python提升到float。

## 参考代码

### C++
```cpp
#include <cstdio>
int main() { int c,q; double p; scanf("%d%d%lf",&c,&q,&p); printf("VALOR A PAGAR: R$ %.2lf\n",q*p); return 0; }
```

### Python
```python
c, q = map(int, input().split())
p = float(input())
print(f"VALOR A PAGAR: R$ {q * p:.2f}")
```
