# AcWing 877. 扩展欧几里得算法 — 扩展欧几里得算法

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/877/

## 题目描述

给定 n 对正整数 ai, bi，对于每对数，求出一组 xi, yi，使其满足 ai×xi + bi×yi = gcd(ai, bi)。

### 输入格式

第一行包含整数 n (1 ≤ n ≤ 105)。接下来 n 行，每行包含两个整数 ai 和 bi (1 ≤ ai, bi ≤ 2×109)。

### 输出格式

输出共 n 行，每行输出一组 xi 和 yi（以空格分隔），使得 ai×xi + bi×yi = gcd(ai, bi)。

### 样例

**输入:**
```
2
4 6
8 18
```

**输出:**
```
-1 1
-2 1
```

### 提示

可使用扩展欧几里得算法求解，返回 (gcd, x, y) 满足 a×x + b×y = gcd。

## AC代码

```cpp
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

int exgcd(int a, int b, int &x, int &y)  // 扩展欧几里得算法, 求x, y，使得ax + by = gcd(a, b)
{
    if (!b)
    {
        x = 1; y = 0;
        return a;
    }
    int d = exgcd(b, a % b, y, x);
    y -= (a / b) * x;
    return d;
}

int main()
{
    int n;
    scanf("%d", &n);
    while (n -- )
    {
      int a,b,x,y;
      scanf("%d%d", &a, &b);

      exgcd(a,b,x,y);

      printf("%d %d\n",x,y);
    }
    return 0;
}
```
