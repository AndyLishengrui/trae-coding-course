# AcWing 657. 选择练习1 — 选择练习1

**难度:** 简单 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/657/

## 题目描述

读取 4 个整数 A，B，C 和 D。如果四个整数同时满足以下条件：

B 大于 A。D 大于 A。C 和 D 的总和大于 A 和 B 的总和。C 是正数。A 是偶数。则输出`Valores aceitos`，否则，输出`Valores nao aceitos`。

### 输入格式

输入占一行，包含四个整数 A, B, C, D。

数据范围

−100≤A,B,C,D≤100

### 输出格式

如果输入数值满足题目条件则输出`Valores aceitos`，否则输出`Valores nao aceitos`。

### 样例

**输入:**
```
5 6 7 8
```

**输出:**
```
Valores nao aceitos
```

### 提示

注意条件的顺序和逻辑关系。

## AC代码

```cpp
if(b > c && d > a && c + d > a + b && c > 0 && d > 0 && a % 2 == 0) 
   cout << "Valores aceitos" << endl;
else
   cout << "Valores nao aceitos" << endl;

return 0;
```
