# AcWing 847. 图中点的层次 — 图中点的层次

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/847/

## 题目描述

给定一个n个点m条边的有向图，图中可能存在重边和自环。

所有边的长度都是1，点的编号为1~n。

请你求出1号点到n号点的最短距离，如果从1号点无法走到n号点，输出-1。

数据范围：1≤n,m≤10^5

### 输入格式

第一行包含两个整数n和m。

接下来m行，每行包含两个整数a和b，表示存在一条从a走到b的长度为1的边。

### 输出格式

输出一个整数，表示1号点到n号点的最短距离。

### 样例

**输入:**
```
4 5
1 2
2 3
3 4
1 3
1 4
```

**输出:**
```
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
#include <queue>

using namespace std;

const int N = 100007;//有向图

int n,m;
int h[N], e[N], ne[N], idx;
int d[N];

void add(int a, int b)  // 添加一条边a->b
{
    e[idx] = b, ne[idx] = h[a], h[a] = idx ++ ;
}

int bfs()
{
  memset(d,-1,sizeof d);
  queue<int> q;
  d[1] = 0;//起始点
  q.push(1);

  while (q.size())
  {
    auto t = q.front();
    q.pop();

    for (int i = h[t]; i!=-1; i = ne[i])
    {
      int j = e[i];
      if (d[j]==-1)
      {
        d[j] = d[t]+1; //层次加1
        q.push(j);
      }
    }
  }
  return d[n];
}

int main()
{
    cin>>n>>m;
    memset(h, -1, sizeof h);

    for (int i = 0; i < m; i++)
    {
      int a, b;
      cin>>a>>b;
      add(a,b);
    }

    cout<<bfs()<<endl;
    return 0;
}
```
