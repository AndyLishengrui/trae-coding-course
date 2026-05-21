# AcWing 809. 最小公倍数 — 最小公倍数

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/809/

## 题目描述

给定两个正整数，求它们的最小公倍数。

### 输入格式

输入一行，包含两个正整数 a 和 b，数字之间用空格隔开。
数据范围：`1 ≤ a, b ≤ 10^5`

### 输出格式

输出一个整数，表示 a 和 b 的最小公倍数。

### 样例

**输入:**
```
4 6
```

**输出:**
```
12
```

### 提示

可以先求出两个数的最大公约数，再利用公式 `lcm = a * b / gcd(a, b)` 求解。

## AC代码

```cpp
#include <iostream>

using namespace std;

int lcm(int a, int b)
{
  for (int i = 1; i <= a * b; i ++ )
      if (i % a == 0 && i % b == 0)
          return i;
  return -1;        
}

int main()
{
    int a, b;
    cin >> a >> b;
    cout << lcm(a, b) << endl;

    return 0;
}
```
