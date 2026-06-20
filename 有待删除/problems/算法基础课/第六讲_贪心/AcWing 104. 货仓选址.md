# AcWing 104. 货仓选址 — 货仓选址

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/104/

## 题目描述

在一条数轴上有N家商店，它们的坐标分别为A1~AN。

现在需要在数轴上建立一家货仓，每天清晨，从货仓到每家商店都要运送一车商品。

为了提高效率，求把货仓建在何处，可以使得货仓到每家商店的距离之和最小。

数据范围

1≤N≤100000

### 输入格式

第一行输入整数N。

第二行N个整数A1~AN。

### 输出格式

输出一个整数，表示距离之和的最小值。

### 样例

**输入:**
```
4
6 2 9 1
```

**输出:**
```
12
```

### 提示

原题链接

acwing讲解

## AC代码

```cpp
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 100007;

int n;
int a[N];

int main()
{
    cin >> n;
    for (int i = 0; i < n; i ++) cin >> a[i];
    sort(a, a+n);
    int res = 0;
    //中位数a[n/2],求距离之和的最小值
    for (int i = 0; i < n; i ++ ) res += abs(a[i]- a[n/2]);
    cout << res <<endl;
    return 0;
}
```
