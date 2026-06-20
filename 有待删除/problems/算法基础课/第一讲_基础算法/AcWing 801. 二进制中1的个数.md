# AcWing 801. 二进制中1的个数 — 二进制中1的个数

**难度:** 简单 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/801/

## 题目描述

给定一个长度为n的数列，请你求出数列中每个数的二进制表示中1的个数。

数据范围：1≤n≤100000,0≤数列中元素的值≤10^9

### 输入格式

第一行包含整数n。

第二行包含n个整数，表示整个数列。

### 输出格式

共一行，包含n个整数，其中的第 i 个数表示数列中的第 i 个数的二进制表示中1的个数。

### 样例

**输入:**
```
5
1 2 3 4 5
```

**输出:**
```
1 1 2 1 2
```

## AC代码

```cpp
#include <iostream>
using namespace std;
inline int lowbit(int &x)
{
    return x & -x;//x的二进制的最后一个1所构成的整数
}
int main()
{
    int n, x;
    cin >> n;
    while (n--)
    {
        //读入一个数，并且计算1的个数，并且输出
        cin >> x;
        int res = 0;//计数变量
        while (x)
            x -= lowbit(x), res++; //使用,表达式，简化代码去括号
        cout << res << " ";        //输出运算结果
    }
    return 0;
}
```
