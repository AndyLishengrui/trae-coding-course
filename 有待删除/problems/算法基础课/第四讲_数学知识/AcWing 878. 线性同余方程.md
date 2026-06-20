# AcWing 878. 线性同余方程 — 线性同余方程

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/878/

## 题目描述

给定 n 组数据 ai, bi, mi，对于每组数据求出一个 xi，使其满足 ai×xi≡ bi(mod mi)。如果无解则输出 impossible。

### 输入格式

第一行包含整数 n (1 ≤ n ≤ 105)。接下来 n 行，每行包含三个整数 ai, bi, mi(1 ≤ ai, bi, mi≤ 2×109)。

### 输出格式

输出共 n 行，每组数据输出一个整数 xi，如果无解则输出`impossible`。

### 样例

**输入:**
```
2
2 3 6
4 3 5
```

**输出:**
```
impossible
-3
```

### 提示

设 g = gcd(a, m)。若 b % g ≠ 0 则无解；否则记 a' = a/g, b' = b/g, m' = m/g。求得 a' 在 m' 模下的逆元 inv 后，x = inv * b' 为一个解。

## AC代码

```cpp
//题解:https://www.acwing.com/solution/content/11231/
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
      int a,b,m;
      scanf("%d%d%d", &a, &b, &m);
      int x,y;
      int d = exgcd(a,m,x,y);
      if( b % d == 0) {
        int t = b/d;
        printf("%d\n", ((long long) x * t % (m/d)+(m/d))%(m/d));
      }
      else 
        puts("impossible");
    }

    return 0;
}
```
