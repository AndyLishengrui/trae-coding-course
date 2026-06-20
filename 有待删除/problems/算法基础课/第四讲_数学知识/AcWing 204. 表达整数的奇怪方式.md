# AcWing 204. 表达整数的奇怪方式 — 表达整数的奇怪方式

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/204/

## 题目描述

给定 n 对整数，其中第 i 行提供两个整数 ai 和 mi，求最小的非负整数 x，使得对于所有 i∈[1,n]，x ≡ mi (mod ai)。如果无解，则输出 -1。

### 输入格式

第 1 行包含整数 n (1 ≤ n ≤ 25)。第 2 至 n+1 行，每行包含两个整数 ai 和 mi，满足 1 ≤ ai ≤ 2^31−1 且 0 ≤ mi < ai。

### 输出格式

输出一个整数 x，表示满足所有同余条件的最小非负解；若不存在，则输出 -1。

### 样例

**输入:**
```
2
8 7
11 9
```

**输出:**
```
31
```

### 提示

可使用中国剩余定理（CRT）求解。结合扩展欧几里得算法，依次合并同余方程。如果合并过程中 (r2 - x) % g ≠ 0 则无解。

## AC代码

```cpp
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

//LL版exgcd
typedef long long LL;
LL exgcd(LL a, LL b, LL &x, LL &y)  // 扩展欧几里得算法, 求x, y，使得ax + by = gcd(a, b)
{
    if (!b)
    {
        x = 1; y = 0;
        return a;
    }
    LL d = exgcd(b, a % b, y, x);
    y -= (a / b) * x;
    return d;
}

int main()
{
    int n; cin>>n;
    bool flag = true;
    //读入第一个方程
    LL a1,m1;
    cin>>a1>>m1;

    for (int i = 0; i < n -1; i ++ )//合并方程
    {
      LL a2,m2;
      cin >> a2 >> m2;//读入第二个方程

      LL k1, k2;//求系数
      LL d = exgcd(a1, a2, k1, k2);

      if ((m2-m1) % d)
      {
        flag = false;
        break;
      }

      //求新的k1参数和m1参数
      k1 *= (m2-m1)/d;
      LL t = a2/d;
      k1 = (k1 %t + t) % t;//求最小余数

      m1 = a1 * k1 + m1;
      a1 = abs(a1 /d * a2);
    }

    if (flag)
    {
      cout << (m1 % a1 + a1) % a1 <<endl;//求最小余数
    }
    else puts("-1");

    return 0;
}
```
