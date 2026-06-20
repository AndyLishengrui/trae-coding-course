# AcWing 895. 最长上升子序列 — 最长上升子序列

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/895/

## 题目描述

给定一个长度为N的数列，求数值严格单调递增的子序列的长度最长是多少。

### 输入格式

第一行包含整数N。

第二行包含N个整数，表示完整序列。

### 输出格式

输出一个整数，表示最大长度。

### 样例

**输入:**
```
7
3 1 2 1 8 5 6
```

**输出:**
```
4
```

### 提示

原题链接

## AC代码

```cpp
#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;
// f[i]定义为以s[i]结尾的最长的子序列
// 集合：所有以第i个数结尾的上升子序列集合
// 属性: Max 上升子序列长度的最大值
const int N = 10007;
int n;
int a[N], f[N];
//状态计算
int main()
{
    cin >> n;
    for (int i = 1; i <= n; i++)
        cin >> a[i]; //从1开始初始化

    for (int i = 1; i <= n; i++)
    {

        f[i] = 1;                   // a[i]只有一个元素，所以f[i]=1;
        for (int j = 1; j < i; j++) //求i之前的f[j]
            if (a[j] < a[i])
                f[i] = max(f[i], f[j] + 1);
    }

    int res = 1;
    for (int i = 1; i <= n; i++)
        res = max(res, f[i]);
    cout << res << endl;
    return 0;
}
```
