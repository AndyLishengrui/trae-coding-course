# AcWing 667. 游戏时间 — 游戏时间

**难度:** 简单 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/667/

## 题目描述

读取两个整数 A 和 B，表示游戏的开始时间和结束时间，以小时为单位。

然后请你计算游戏的持续时间，已知游戏可以在一天开始并在另一天结束，最长持续时间为 24 小时。

如果 A 与 B 相等，则视为持续了 24 小时。

### 输入格式

共一行，包含两个整数 A 和 B。

数据范围

0≤A,B≤23

### 输出格式

输出格式为`O JOGO DUROU X HORA(S)`，其中 X 为游戏持续时间。

### 样例1

**输入:**
```
16 2
```

**输出:**
```
O JOGO DUROU 10 HORA(S)
```

### 样例2

**输入:**
```
0 0
```

**输出:**
```
O JOGO DUROU 24 HORA(S)
```

### 样例3

**输入:**
```
2 16
```

**输出:**
```
O JOGO DUROU 14 HORA(S)
```

### 提示

注意时间的跨天情况。

## AC代码

```cpp
#include <cstdio>

int main()
{
  int a, b;
  scanf("%d%d", &a, &b);

  int res;
  if (a < b) res = b - a;
  else  res = b - a + 24;

  printf("O JOGO DUROU %d HORA(S)\n", res);

  return 0;
}
```
