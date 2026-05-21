# AcWing 811. 交换数值 — 交换数值

**难度:** 简单 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/811/

## 题目描述

输入两个整数 x 和 y，请编写一个函数，交换两个整数的数值并输出交换后的 x 和 y。

C++ 中的格式为：void swap(int &x, int &y) 。
Java 中的格式为：void swap(int[] a)，交换 a[0] 和 a[1] 。

### 输入格式

共一行，包含两个整数 x 和 y。

数据范围：`1 ≤ x, y ≤ 100`

### 输出格式

共一行，包含交换后的 x 和 y。

### 样例

**输入:**
```
3 5
```

**输出:**
```
5 3
```

### 提示

注意输出格式。

来源：语法题

## AC代码

```cpp
#include <iostream>

using namespace std;

void swap(int& x, int& y)
{
    if (x == y) return;

    int t = x;
    x = y;
    y = t;
}

int main()
{
    int x, y;
    cin >> x >> y;
    swap(x, y);

    cout << x << ' ' << y << endl;

    return 0;

}
```
