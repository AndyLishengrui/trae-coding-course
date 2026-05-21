# AcWing 874. 筛法求欧拉函数 — 筛法求欧拉函数

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/874/

## 题目描述

给定一个正整数 n，求 1∼n 中每个数的欧拉函数之和。

### 输入格式

共一行，包含一个整数 n。

数据范围

1≤n≤10^6

### 输出格式

共一行，输出 1∼n 中每个数的欧拉函数之和。

### 样例

**输入:**
```
6
```

**输出:**
```
12
```

### 提示

利用筛法预处理 1∼n 的欧拉函数，初始 φ[i]=i，然后对每个素数 p 更新所有 p 的倍数：φ[j] -= φ[j]/p。

参考题解

Y总讲解

Y总代码

## AC代码

```cpp
//Andy代码，参考Y总
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

typedef long long LL;

const int N = 1000007;

int primes[N],cnt;
int euler[N];
int st[N];

void get_eulers(int n)  // 线性筛法求1~n的欧拉函数
{
    euler[1] = 1;
    for (int i = 2; i <= n; i ++ )
    {
        if (!st[i])
        {
            primes[cnt ++ ] = i;//找到一个质数
            euler[i] = i - 1; //质数i的欧拉函数个数为i-1
        }
        //线性筛法，每次都/掉一个i
        for (int j = 0; primes[j] <= n / i; j ++ )
        {
            int t = primes[j] * i;
            st[t] = true;
            if (i % primes[j] == 0)
            {
                euler[t] = euler[i] * primes[j];
                break;
            }
            euler[t] = euler[i] * (primes[j] - 1);
        }
    }
}

int main()
{
    int n; cin>>n;

    get_eulers(n);

    LL res = 0;
    for (int i = 1; i <=n; i++) res += euler[i];
    cout<<res<<endl;

    return 0;
}
```
