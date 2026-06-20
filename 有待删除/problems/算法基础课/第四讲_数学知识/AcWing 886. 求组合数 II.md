# AcWing 886. 求组合数 II — 求组合数(2)

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/886/

## 题目描述

给定`n`组询问，每组询问给定两个整数`a，b`，请你输出`C_a^b mod (10^9 + 7)`的值。

**数据范围**

`1≤n≤10000`

`1≤b≤a≤10^5`

### 输入格式

第一行包含整数`n`。

接下来`n`行，每行包含一组`a`和`b`。

### 输出格式

共`n`行，每行输出一个询问的解。

### 样例

**输入:**
```
3
3 1
5 3
2 2
```

**输出:**
```
3
10
1
```

### 提示

原题链接

## AC代码

```cpp
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

typedef long long LL;
const int N = 100007, mod = 1e9+7;

int fact[N], infact[N];//逆元

int qmi(int a, int k, int p)  // 求a^k mod p
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

int main()
{
    fact[0]=infact[0]=1;
    for (int i = 1; i < N; i ++ )
    {
      fact[i] = (LL)fact[i-1] * i % mod;//求组合数分子
      infact[i] = (LL)infact[i-1] * qmi(i, mod-2, mod) % mod;//求逆元
    }

    int n;
    scanf("%d", &n);
    while (n -- )
    {
      int a,b;
      scanf("%d%d", &a, &b);
      printf("%d\n",(LL)fact[a] * infact[b] % mod * infact[a-b] % mod);//套用组合数公式
    }

    return 0;
}
```
