# AcWing 823. 排列 — 排列

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/823/

## 题目描述

给定整数 n，将数字 1 ~ n 按字典序输出所有排列方法。

### 输入格式

一行一个整数 n。

数据范围：`1 ≤ n ≤ 9`

### 输出格式

按字典序输出所有排列方案，每个方案占一行。

### 样例

**输入:**
```
3
```

**输出:**
```
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
```

### 提示

注意输出格式。

来源：语法题

## AC代码

```cpp
#include <iostream>

using namespace std;

const int N = 10;

int n;

void dfs(int u, int nums[], bool st[])
{
  if (u > n)
  {
    for (int i = 1; i <= n; i ++ ) cout << nums[i] << ' ';
    cout << endl;
  }
  else
  {
    for (int i = 1; i <= n; i ++ )
        if (!st[i])
        {
          st[i] = true;
          nums[u] = i;
          dfs(u + 1, nums, st);
          st[i] = false;
        }
  }
}

int main()
{
    cin >> n;

    int nums[N];
    bool st[N] = {0};

    dfs(1, nums, st);

    return 0;
}
```
