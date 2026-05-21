# AcWing 818. 数组排序 — 数组排序

**难度:** 简单 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/818/

## 题目描述

编写函数 void sort(int a[], int l, int r) 将 a[l] ~ a[r] 从小到大排序并输出排序后的数组 a。

### 输入格式

第一行 n, l, r 分别表示数组长度、排序起始和结束位置；
第二行 n 个整数为数组 a。

数据范围：`0 ≤ l ≤ r < n ≤ 1000`

### 输出格式

一行 n 个整数表示排序后的数组 a。

### 样例

**输入:**
```
5 2 4
4 5 1 3 2
```

**输出:**
```
4 5 1 2 3
```

### 提示

注意输出格式。

来源：语法题

## AC代码

```cpp
#include <iostream>

using namespace std;

void sort(int a[], int l, int r)
{
    for (int i = l; i <= r; i ++ )
        for (int j = i + 1; j <= r; j ++ )
            if (a[j] < a[i])
                swap(a[i], a[j]);
}

int main()
{
    int a[1000];
    int n, l, r;
    cin >> n >> l >> r;
    for (int i = 0; i < n; i ++ ) cin >> a[i];

    sort(a, l, r);

    for (int i = 0; i < n; i ++ ) cout << a[i] << ' ';

    return 0;
}
```
