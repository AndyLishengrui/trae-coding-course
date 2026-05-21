# AcWing 866. 试除法判定质数 — 试除法判定质数

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/866/

## 题目描述

给定 n 个正整数 ai，判定每个数是否为质数。

### 输入格式

第一行包含整数 n。接下来 n 行，每行包含一个正整数 ai。

### 输出格式

共 n 行，其中第 i 行输出第 i 个正整数 ai 是否为质数，是则输出 Yes，否则输出 No。

### 样例

**输入:**
```
2
2
6
```

**输出:**
```
Yes
No
```

### 提示

可利用试除法，在 √ai 范围内检查因子判断质数。

## AC代码

```cpp
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

bool is_prime(int x)  // 判定质数
{
    if (x < 2) return false;
    for (int i = 2; i <= x / i; i ++ )
        if (x % i == 0)
            return false;
    return true;
}

int main()
{
    int n;
    cin>>n;

    while (n -- )
    {
      int x; cin>>x;
      if (is_prime(x)) puts("Yes");
      else puts("No");
    }

    return 0;
}
```
