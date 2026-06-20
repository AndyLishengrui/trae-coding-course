# AcWing 822. 走方格 — 走方格

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/822/

## 题目描述

给定 n x m 的方格阵，从左上角 (0, 0) 开始，每次只能往右或往下走一个单位距离，求走到右下角 (n, m) 的走法数量。

### 输入格式

一行两个整数 n 和 m。

数据范围：`1 ≤ n, m ≤ 10`

### 输出格式

一个整数表示走法数量。

### 样例

**输入:**
```
2 3
```

**输出:**
```
10
```

### 提示

注意输出格式。

来源：语法题

## AC代码

```cpp
#include <iostream>

using namespace std;

int n, m;
int ans;

void dfs(int x, int y)
{
    if (x == n && y == m) ans ++ ;
    else
    {
      if (y < m) dfs(x, y + 1);
      if (x < n) dfs(x + 1, y);
    }
}

int main()
{
    cin >> n >> m;
    dfs(0, 0);
    cout << ans << endl;

    return 0;
}
```
