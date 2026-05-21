# AcWing 817. 数组去重 — 数组去重

**难度:** 简单 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/817/

## 题目描述

编写函数 int get_unique_count(int a[], int n) 返回数组前 n 个数中的不同数的个数。

### 输入格式

第一行 n 表示数组长度；
第二行 n 个整数为数组 a。

数据范围：`1 ≤ n ≤ 1000`，`1 ≤ a[i] ≤ 1000`

### 输出格式

一个整数表示不同数的个数。

### 样例

**输入:**
```
5
1 1 2 4 5
```

**输出:**
```
4
```

### 提示

注意输出格式。

来源：语法题

## AC代码

```cpp
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 1010;

int n;
int q[N];

int main()
{
    cin >> n;
    for (int i = 0; i < n; i ++ ) cin >> q[i];

    sort(q, q + n);

    int k = 1;
    for (int i = 1; i < n; i ++ )
        if (q[i] != q[k - 1])
            q[k ++ ] = q[i];
    cout << k << endl;
    return 0;
}
```
