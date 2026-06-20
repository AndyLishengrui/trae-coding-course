# AcWing 741. 斐波那契数列 — 斐波那契数列

**难度:** 简单 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/741/

## 题目描述

输入整数 T 表示共有 T 个测试数据。接下来 T 行，每行输入一个整数 N（0 ≤ N ≤ 60）。

斐波那契数列定义为：Fib(0)=0, Fib(1)=1，从 Fib(2) 开始，Fib(N)=Fib(N-1)+Fib(N-2)。

对于每个 N，输出格式为`Fib(N) = x`，其中 x 为第 N 项的值。

### 输入格式

第一行输入 T；接下来 T 行，每行包含一个整数 N，数据范围：0 ≤ N ≤ 60

### 输出格式

对于每组测试数据，输出一行结果，格式为`Fib(N) = x`

### 样例

**输入:**
```
3
0
4
2
```

**输出:**
```
Fib(0) = 0
Fib(4) = 3
Fib(2) = 1
```

### 提示

可以利用迭代或动态规划的方法求解斐波那契数列。

## AC代码

```cpp
#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    long long f[61];
    f[0] = 0; f[1] = 1;

    for (int i = 2; i <= 60; i ++ ) f[i] = f[i - 1] + f[i - 2];

    int n;
    cin >> n;
    while (n -- )
    {
      int x;
      cin >> x;
      printf("Fib(%d) = %lld\n", x, f[x]);
    }

    return 0;
}
```
