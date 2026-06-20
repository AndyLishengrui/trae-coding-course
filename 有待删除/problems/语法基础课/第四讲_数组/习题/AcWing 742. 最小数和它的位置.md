# AcWing 742. 最小数和它的位置 — 最小数和它的位置

**难度:** 简单 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/742/

## 题目描述

输入一个整数 N 和一个长度为 N 的整数数组 X。请你找到数组中最小的元素，并输出它的值和下标。

注意，如果有多个最小值，则返回下标最小的那个。

### 输入格式

第一行包含整数 N。

第二行包含 N 个用空格隔开的整数 X[i]。

数据范围：`1 < N ≤ 1000`，`-1000 < X[i] ≤ 1000`

### 输出格式

第一行输出`Minimum value: x`，其中 x 为数组元素最小值。第二行输出`Position: y`，其中 y 为最小值元素的下标（下标从 0 开始计数）。

### 样例

**输入:**
```
10
1 2 3 4 -5 6 7 8 9 10
```

**输出:**
```
Minimum value: -5
Position: 4
```

### 提示

遍历数组找到最小值及其下标。

来源：语法题

## AC代码

```cpp
#include <cstdio>
#include <iostream>

using namespace std;

int main()
{
    int a[1001];
    int n;

    cin >> n;
    for (int i = 0; i < n; i ++ ) cin >> a[i];

    int p = 0;
    for (int i = 1; i < n; i ++ )
        if (a[i] < a[p])
            p = i;

    printf("Minimum value: %d\n", a[p]);        
    printf("Position: %d\n", p);

    return 0;
}
```
