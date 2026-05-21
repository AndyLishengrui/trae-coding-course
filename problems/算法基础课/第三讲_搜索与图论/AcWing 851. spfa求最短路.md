# AcWing 851. spfa求最短路 — spfa求最短路

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/851/

## 题目描述

给定一个 n 个点 m 条边的有向图，图中可能存在重边和自环，边权可能为负数。

请你求出 1 号点到 n 号点的最短距离，如果无法从 1 号点走到 n 号点，则输出 impossible。

数据保证不存在负权回路。

### 输入格式

第一行包含整数 n 和 m。

接下来 m 行每行包含三个整数 x, y, z，表示存在一条从点 x 到点 y 的有向边，边长为 z。

**数据范围**

1≤n, m≤10^5,

图中涉及边长绝对值均不超过 10000。

### 输出格式

输出一个整数，表示 1 号点到 n 号点的最短距离。

如果路径不存在，则输出 impossible。

### 样例

**输入:**
```
3 3
1 2 5
2 3 -3
1 3 4
```

**输出:**
```
2
```

### 提示

原题链接

Y总讲解

Y总代码

## AC代码

```cpp
#include <queue>
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 100007;

int n,m;
int h[N], e[N], w[N], ne[N], idx;
int q[N], dist[N];
bool st[N];

void add(int a, int b, int c)  // 添加一条边a->b，边权为c
{
    e[idx] = b, w[idx] = c, ne[idx] = h[a], h[a] = idx ++ ;
}

int spfa()  // 求1号点到n号点的最短路距离，如果从1号点无法走到n号点则返回-1
{
    int hh = 0, tt = 0;
    memset(dist, 0x3f, sizeof dist);
    dist[1] = 0;
    q[tt ++ ] = 1;
    st[1] = true;

    while (hh != tt)
    {
        int t = q[hh ++ ];
        if (hh == N) hh = 0;
        st[t] = false;

        for (int i = h[t]; i != -1; i = ne[i])
        {
            int j = e[i];
            if (dist[j] > dist[t] + w[i])
            {
                dist[j] = dist[t] + w[i];
                if (!st[j])     // 如果队列中已存在j，则不需要将j重复插入
                {
                    q[tt ++ ] = j;
                    if (tt == N) tt = 0;
                    st[j] = true;
                }
            }
        }
    }

    if (dist[n] == 0x3f3f3f3f) return -1;
    return dist[n];
}

int main()
{
    scanf("%d%d", &n, &m);
    memset(h, -1, sizeof h);
    while (m -- )
    {
      int a, b, c;
      scanf("%d%d%d", &a, &b, &c);
      add(a, b, c);
    }

    int t = spfa();

    if (t == -1) puts("impossible");
    else printf("%d\n",t);

    return 0;
}
```
