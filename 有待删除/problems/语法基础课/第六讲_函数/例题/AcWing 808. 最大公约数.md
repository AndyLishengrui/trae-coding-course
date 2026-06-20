# AcWing 808. 最大公约数 — 最大公约数

**难度:** 简单 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/808/

## 题目描述

输入两个整数 a 和 b，请编写一个函数 int gcd(int a, int b)，计算并输出 a 和 b 的最大公约数。

### 输入格式

共一行，包含两个整数 a 和 b。

数据范围：`1 ≤ a, b ≤ 1000`

### 输出格式

共一行，包含一个整数，表示 a 和 b 的最大公约数。

### 样例

**输入:**
```
12 16
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

using namespace std;

int gcd(int a, int b) 
{
    for (int i = 1000; i; i -- )
        if (a % i == 0 && b % i == 0)
           return i;
    return -1;       
}

int main()
{
    int a, b;
    cin >> a >> b;
    cout << gcd(a, b) << endl;

    return 0;
}
```
