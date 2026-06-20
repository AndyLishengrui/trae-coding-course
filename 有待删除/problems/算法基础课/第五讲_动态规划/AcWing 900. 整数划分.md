# AcWing 900. 整数划分 — 整数划分

**难度:** 困难 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/900/

## 题目描述

数据范围1≤n≤1000

### 输入格式

共一行，包含一个整数n。

### 输出格式

共一行，包含一个整数，表示总划分数量。

由于答案可能很大，输出结果请对10^9+7取模。

### 样例

**输入:**
```
5
```

**输出:**
```
7
```

## AC代码

```cpp
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 1007, mod = 1e9+7;

int n;
int f[N];//完全背包,体积是i的方案数

int main()
{
    cin>>n;
    f[0] = 1;

    for (int i = 1; i <= n; i++)
      for (int j = i; j <=n; j++)
        f[j] = (f[j] + f[j-i]) % mod;

    cout <<f[n]<<endl;
}
```
