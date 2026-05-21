# AcWing 668. 游戏时间2 — 游戏时间2

**难度:** 简单 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/668/

## 题目描述

读取四个整数 A, B, C, D，用来表示游戏的开始时间和结束时间。

其中 A 和 B 为开始时刻的小时和分钟数，C 和 D 为结束时刻的小时和分钟数。

请你计算游戏的持续时间。游戏最短持续 1 分钟，最长持续 24 小时。

### 输入格式

共一行，包含四个整数 A, B, C, D。

数据范围

0≤A,C≤23,0≤B,D≤59

### 输出格式

输出格式为`O JOGO DUROU X HORA(S) E Y MINUTO(S)`，表示游戏共持续了 X 小时 Y 分钟。

### 样例1

**输入:**
```
7 8 9 10
```

**输出:**
```
O JOGO DUROU 2 HORA(S) E 2 MINUTO(S)
```

### 样例2

**输入:**
```
7 7 7 7
```

**输出:**
```
O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)
```

### 样例3

**输入:**
```
7 8 8 9
```

**输出:**
```
O JOGO DUROU 1 HORA(S) E 1 MINUTO(S)
```

### 提示

注意时间的跨天情况。

## AC代码

```cpp
#include <cstdio>

int main()
{
    int a, b, c, d;
    scanf("%d%d%d%d", &a, &b, &c, &d);

    int start = a * 60 + b;
    int end = c * 60 + d;

    int spent_time = end - start;
    if (spent_time <= 0) spent_time += 1440;

    printf("O JOGO DUROU %d HORA(S) E %d MINUTO(S)", spent_time / 60, spent_time % 60);

    return 0;

}
```
