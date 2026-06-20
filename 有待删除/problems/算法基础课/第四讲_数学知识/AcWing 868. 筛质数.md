# AcWing 868. 筛质数 — 筛质数

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/868/

## 题目描述

给定一个正整数`n`，请你求出 1∼`n`中质数的个数。

### 输入格式

共一行，包含整数`n`。

**数据范围**

`1≤n≤10^6`

### 输出格式

共一行，包含一个整数，表示 1∼`n`中质数的个数。

### 样例

**输入:**
```
8
```

**输出:**
```
4
```

### 提示

原题链接

## AC代码

```cpp
// Andy 2021.06.04
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 100000007;

int primes[N],cnt;
bool st[N];
void get_primes(int n)  // 线性筛质数
{
    for (int i = 2; i <= n; i ++ )
    {
        if (!st[i]) primes[cnt ++ ] = i;
        for (int j = 0; primes[j] <= n / i; j ++ )
        {
            st[primes[j] * i] = true;
            if (i % primes[j] == 0) break;
        }
    }
}


int main()
{
    int n; cin>>n;
    get_primes(n);
    cout<<cnt<<endl;
    return 0;
}
```
