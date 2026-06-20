# AcWing 820. 递归求斐波那契数列 — 递归求斐波那契数列

**难度:** 简单 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/820/

## 题目描述

请使用递归的方式求斐波那契数列的第 n 项，下标从 1 开始。
斐波那契数列：1, 1, 2, 3, 5 ...，这个数列从第 3 项开始，每一项都等于前两项之和。

### 输入格式

共一行，包含整数 n。

数据范围：`1 ≤ n ≤ 30`

### 输出格式

共一行，包含一个整数，表示斐波那契数列的第 n 项。

### 样例

**输入:**
```
4
```

**输出:**
```
3
```

### 提示

注意输出格式。

来源：语法题

## AC代码

```cpp
#include <iostream>

using namespace std;

int f(int n)
{
    if (n <= 2) return 1;
    return f(n - 2) + f(n - 1);
}

int main()
{
    int n;
    cin >> n;
    cout << f(n) << endl;

    return 0;
}
```
