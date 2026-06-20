# AcWing 887. 求组合数 III — 求组合数(3)

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/887/

## 题目描述

给定`n`组询问，每组询问给定三个整数`a,b,p`，其中`p`是质数，请你输出`C_a^b mod p`的值。

**数据范围**

`1≤n≤20`

`1≤b≤a≤10^18`

`1≤p≤10^5`

### 输入格式

第一行包含整数`n`。

接下来`n`行，每行包含一组`a,b,p`。

### 输出格式

共`n`行，每行输出一个询问的解。

### 样例

**输入:**
```
3
5 3 7
3 1 5
6 4 13
```

**输出:**
```
3
3
2
```

### 提示

原题链接

## AC代码

```cpp
//使用Lucas定理
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

typedef long long LL;


int qmi(int a, int k, int p)  // 快速幂模板
{
    int res = 1 % p;
    while (k)
    {
        if (k & 1) res = (LL)res * a % p;
        a = (LL)a * a % p;
        k >>= 1;
    }
    return res;
}

int C(int a, int b, int p)  // 通过定理求组合数C(a, b)
{
    if (a < b) return 0;

    LL x = 1, y = 1;  // x是分子，y是分母
    for (int i = a, j = 1; j <= b; i --, j ++ )
    {
        x = (LL)x * i % p;
        y = (LL) y * j % p;
    }

    return x * (LL)qmi(y, p - 2, p) % p;
}

int lucas(LL a, LL b, int p)
{
    if (a < p && b < p) return C(a, b, p);
    return (LL)C(a % p, b % p, p) * lucas(a / p, b / p, p) % p;
}

int main()
{
    int n;
    cin >> n;
    while (n--)
    {
      LL a,b;
      int p;
      cin >> a >> b >>p;
      cout<< lucas(a,b,p) <<endl;
    }

    return 0;
}
```
