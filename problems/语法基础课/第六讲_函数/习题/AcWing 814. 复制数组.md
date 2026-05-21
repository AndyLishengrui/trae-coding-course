# AcWing 814. 复制数组 — 复制数组

**难度:** 简单 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/814/

## 题目描述

要编写函数 void copy(int a[], int b[], int size) 将 a 数组中的前 size 个数复制到 b 数组中并输出 b 数组。

### 输入格式

第一行 n, m, size 分别表示 a 数组长度、b 数组长度和要复制的个数；
第二行 n 个整数为数组 a；
第三行 m 个整数为数组 b。

数据范围：`1 ≤ n ≤ m ≤ 100`，`1 ≤ size ≤ n`

### 输出格式

一行 m 个整数表示复制后的数组 b。

### 样例

**输入:**
```
3 5 2
1 2 3
4 5 6 7 8
```

**输出:**
```
1 2 6 7 8
```

### 提示

注意输出格式。

来源：语法题

## AC代码

```cpp
#include <iostream>
#include <cstring>

using namespace std;

const int N = 110;

void copy(int a[], int b[], int size)
{
    memcpy(b, a, size * 4);
}

int main()
{
    int a[N], b[N];
    int n, m, size;
    cin >> n >> m >> size;
    for (int i = 0; i < n; i ++ ) cin >> a[i];
    for (int i = 0; i < m; i ++ ) cin >> b[i];

    copy(a, b, size);

    for (int i = 0; i < m; i ++ ) cout << b[i] << ' ';
    cout << endl;

    return 0;
}
```
