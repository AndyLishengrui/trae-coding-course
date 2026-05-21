# AcWing 913. 排队打水 — 排队打水

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/913/

## 题目描述

有 n 个人排队到 1 个水龙头处打水，第 i 个人装满水桶所需的时间为 ti。

请你安排打水顺序，使得所有人的等待时间之和最小，并输出该最小总等待时间。

一个人的等待时间为他前面所有人打水所花费的时间之和。

### 输入格式

第一行包含整数 n (1 ≤ n ≤ 105)。
第二行包含 n 个整数 ti(1 ≤ ti≤ 104)，表示每个人打水所需时间。

### 输出格式

输出一个整数，表示所有人的等待时间之和的最小值。

### 样例

**输入:**
```
7
3 6 1 4 2 5 7
```

**输出:**
```
56
```

### 提示

贪心策略：将所有人的打水时间排序，然后依次计算前缀和，累加即为总等待时间。

原题链接

## AC代码

```cpp
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;
typedef long long LL;

const int N = 100007;
int t[N];

int main()
{
    ios::sync_with_stdio(false);
    int n;
    cin>>n;
    for (int i = 0; i < n; i ++ ) cin>>t[i];

    sort(t,t+n);

    LL res=0;
    for (int i = 0; i < n; i ++ ) res += t[i] * (n-i-1);

    cout<<res<<endl;

    return 0;

}
```
