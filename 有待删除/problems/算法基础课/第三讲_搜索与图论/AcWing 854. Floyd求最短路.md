# AcWing 854. Floyd求最短路 — Floyd求最短路

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/854/

## 题目描述

给定一个 n 个点 m 条边的有向图，图中可能存在重边和自环，边权可能为负数。

再给定 k 个询问，每个询问包含两个整数 x 和 y，表示查询从点 x 到点 y 的最短距离，如果路径不存在，则输出 impossible。

数据保证图中不存在负权回路。

**数据范围**

1≤n≤200,

1≤k≤n^2,

1≤m≤20000,

图中涉及边长绝对值均不超过 10000。

### 输入格式

第一行包含三个整数 n, m, k。

接下来 m 行，每行包含三个整数 x, y, z，表示存在一条从点 x 到点 y 的有向边，边长为 z。

接下来 k 行，每行包含两个整数 x, y，表示询问点 x 到点 y 的最短距离。

### 输出格式

共 k 行，每行输出一个整数，表示询问的结果，若询问两点间不存在路径，则输出 impossible。

### 样例

**输入:**
```
3 3 2
1 2 1
2 3 2
1 3 1
2 1
1 3
```

**输出:**
```
impossible
1
```

### 提示

原题链接

Y总讲解

Y总代码

## AC代码

```cpp
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 207,INF = 0x3f3f3f3f;

int n,m,k;//k组询问
int d[N][N];

void floyd()
{
  //用动态规划分析得出这个递推公式，使用三重循环
  for (int k = 1; k <=n; k++)
   for (int i = 1; i <=n; i++)
    for (int j = 1; j <= n; j ++ )
      d[i][j] = min(d[i][j], d[i][k]+d[k][j]);
}

int main()
{
    scanf("%d%d%d", &n, &m, &k);

    for (int i = 1; i <= n; i ++ )
     for (int j = 1; j <= n; j ++ )
       if (i==j) d[i][j] = 0;
       else d[i][j] = INF;

    //处理每条边，去掉重边和自环
    while (m -- )
    {
      int a,b,c;
      scanf("%d%d%d", &a, &b, &c);
      d[a][b] = min(d[a][b],c);
    }

    floyd();

    //k组查询
    while(k--)
    {
      int a,b;
      scanf("%d%d", &a, &b);
      int t = d[a][b];
      if (t > INF /2) puts("impossible");
      else printf("%d\n",t);
    }

    return 0;
}
```
