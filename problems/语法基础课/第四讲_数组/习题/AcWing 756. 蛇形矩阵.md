# AcWing 756. 蛇形矩阵 — 蛇形矩阵

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/756/

## 题目描述

输入两个整数 n 和 m，输出一个 n 行 m 列的矩阵，将数字 1 到 n×m 按照回字蛇形填充至矩阵中。

具体蛇形形式可参考样例。

### 输入格式

输入共一行，包含两个整数 n 和 m。

### 输出格式

输出满足要求的矩阵。矩阵占 n 行，每行包含 m 个用空格隔开的整数，输出完毕后需再输出一个空行。

### 样例

**输入:**
```
3 3
```

**输出:**
```
1 2 3
8 9 4
7 6 5
```

## AC代码

```cpp
#include <iostream>

using namespace std;

int res[100][100];

int main()
{
    int n, m;
    cin >> n >> m;

    int dx[] = {0, 1, 0, -1}, dy[] = {1, 0, -1, 0};

    for (int x = 0, y = 0, d = 0, k = 1; k <= n * m; k ++ )
    {
      res[x][y] = k;
      int a = x + dx[d], b = y + dy[d];
      if (a < 0 || a >= n || b < 0 || b >= m || res[a][b])
      {
        d = (d + 1) % 4;
        a = x + dx[d], b = y + dy[d];
      }
      x = a; y = b;
    }

    for (int i = 0; i < n; i ++ )
    {
      for (int j = 0; j < m; j ++ ) cout << res[i][j] << ' ';
      cout << endl;
    }

    return 0;
}
```
