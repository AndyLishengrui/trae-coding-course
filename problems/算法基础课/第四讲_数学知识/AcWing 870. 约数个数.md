# AcWing 870. 约数个数 — 约数个数

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/870/

## 题目描述

给定n个正整数ai，请你输出这些数的乘积的约数个数，答案对10^9+7取模。

### 输入格式

第一行包含整数n。

接下来n行，每行包含一个整数ai。

### 输出格式

输出一个整数，表示所给正整数的乘积的约数个数，答案需对10^9+7取模。

### 样例

**输入:**
```
3
2
6
8
```

**输出:**
```
12
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

const int N = 110, mod = 1e9+7;//大数取mod

int main()
{
    int n; cin>>n;

    unordered_map<int,int> primes;//存质因数与个数

    while (n -- )
    {
      //读入a，分解质因数
      int a; cin>>a;
      for (int i = 2; i <= a / i; i++)
        while(a % i == 0)
        {
          a /= i;//统计因子i的个数
          primes[i]++;
        }

      if (a > 1) primes[a]++;//剩下的最后一个因子
    }
    //根据公式直接计算答案
    LL res = 1;
    for (auto x:primes) res = res * (x.second + 1) % mod;

    cout<<res<<endl;

    return 0;
}
```
