# AcWing 816. 数组翻转 — 数组翻转

**难度:** 简单 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/816/

## 题目描述

编写函数 void reverse(int a[], int size) 实现将数组 a 中的前 size 个数翻转并输出翻转后的数组 a。

### 输入格式

第一行 n 和 size 分别表示数组长度和要翻转的个数；
第二行 n 个整数为数组 a。

数据范围：`1 ≤ size ≤ n ≤ 1000`，`1 ≤ a[i] ≤ 1000`

### 输出格式

一行 n 个整数表示翻转后的数组 a。

### 样例

**输入:**
```
5 3
1 2 3 4 5
```

**输出:**
```
3 2 1 4 5
```

### 提示

注意输出格式。

来源：语法题

## AC代码

```cpp
#include <iostream>

using namespace std;

void reverse(int a[], int size)
{
    for (int i = 0, j = size - 1; i < j; i ++, j -- )
        swap(a[i], a[j]);
}

int main()
{
    int a[1000];
    int n, size;

    cin >> n >> size;
    for (int i = 0; i < n; i ++ ) cin >> a[i];
    reverse(a, size);

    for (int i = 0; i < n; i ++ ) cout << a[i] << ' ';

    return 0;
}
```
