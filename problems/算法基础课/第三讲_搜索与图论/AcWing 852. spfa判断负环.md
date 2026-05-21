# AcWing 852. spfa判断负环 — spfa判断负环

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/852/

## 题目描述

给定一个n个点m条边的有向图，图中可能存在重边和自环，**边权可能为负数。**

请你判断图中是否存在负权回路。

**数据范围**

1≤n≤2000,1≤m≤10000,

图中涉及边长绝对值均不超过 10000。

### 输入格式

第一行包含整数 n 和 m。

接下来 m 行每行包含三个整数 x, y, z，表示存在一条从点 x 到点 y 的有向边，边长为 z。

### 输出格式

如果图中存在负权回路，则输出 Yes，否则输出 No。

### 样例

**输入:**
```
3 3
1 2 -1
2 3 4
3 1 -4
```

**输出:**
```
Yes
```

### 提示

原题链接

Y总代码

Y总讲解

## AC代码

```cpp
#include <cstring>
#include <iostream>
#include <algorithm>
#include <queue>

using namespace std;

const int N = 2007, M=10007;

int n, m;
int h[N], w[M], e[M], ne[M], idx;
int dist[N],cnt[N];
bool st[N];

void add(int a, int b, int c)
{
    e[idx] = b, w[idx] = c, ne[idx] = h[a], h[a] = idx ++ ;
}

bool spfa()
{

    queue<int> q;

    //所有点都压入队列
    for (int i = 1; i <= n; i ++ )
    {
      st[i]= true;
      q.push(i);
    }

    while (q.size())
    {
        int t = q.front();
        q.pop();

        st[t] = false;

        for (int i = h[t]; i != -1; i = ne[i])
        {
            int j = e[i];
            if (dist[j] > dist[t] + w[i])
            {
                dist[j] = dist[t] + w[i];
                cnt[j] = cnt[t]+1;//更新cnt

                if (cnt[j]>=n) return true;//找到一个负环

                if (!st[j])
                {
                    q.push(j);
                    st[j] = true;
                }
            }
        }
    }

    return false;
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

    if (spfa()) puts("Yes");
    else puts("No");

    return 0;
}
```
