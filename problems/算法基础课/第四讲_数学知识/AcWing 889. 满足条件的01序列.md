# AcWing 889. 满足条件的01序列 — 满足条件的01序列

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/889/

## 题目描述

给定 n 个 0 和 n 个 1，它们将按照某种顺序排成长度为 2n 的序列。

求这些序列中满足任意前缀中 0 的个数均不少于 1 的个数的序列总数，并对 10^9+7 取模。

### 输入格式

共一行，包含一个整数 n (1 ≤ n ≤ 10^5)。

### 输出格式

共一行，输出一个整数，表示满足条件的序列数对 10^9+7 取模后的结果。

### 样例

**输入:**
```
3
```

**输出:**
```
5
```

### 提示

答案是 Catalan 数：Catalan(n) = (1/(n+1)) × C(2n, n)。记得对 109+7 取模，并预处理阶乘和逆元。

原题链接

## AC代码

```cpp
//这道题就是求卡特兰数
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

typedef long long LL;

const int N = 100007, mod = 1e9+7;

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

//用快速幂求逆元，求组合数
int main()
{
    int n; cin>>n;

    // C(n,2n) - C(n-1, 2n) = C(n,2n)/(n+1)

    int a = n * 2, b = n;//套用卡特兰数公式

    int res = 1;
    // 求C(b,a) 即 C(n,2n),公式的计算需要仔细消化理解
    for (int i = a; i > a-b; i--) res = (LL) res *i % mod;

    for (int i = 1; i<=b; i++) res = (LL) res * qmi(i, mod-2,mod) % mod;

    res = (LL) res  * qmi(n+1,mod-2,mod) % mod;

    cout <<res<<endl;

    return 0;

}
```
