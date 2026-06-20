# AcWing 849. Dijkstra求最短路 I — Dijkstra求最短路(1)

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/849/

## 题目描述

给定一个n个点m条边的有向图，图中可能存在重边和自环，所有边权均为正值。

请你求出1号点到n号点的最短距离，如果无法从1号点走到n号点，则输出-1。

### 输入格式

第一行包含整数n和m。

接下来m行每行包含三个整数x，y，z，表示存在一条从点x到点y的有向边，边长为z。

### 输出格式

输出一个整数，表示1号点到n号点的最短距离。

如果路径不存在，则输出-1。

### 样例

**输入:**
```
3 3
1 2 2
2 3 1
1 3 4
```

**输出:**
```
3
```

### 提示

原题链接

## AC代码

```cpp
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 510;//500*500
const int INF = 0x3f3f3f3f;

int g[N][N]; 
int dist[N];
bool st[N];

int n,m;

int Dijkstra()
{
  memset(dist,0x3f, sizeof dist);//初始化距离  0x3f代表无限大

  dist[1] = 0; //第一个点到自身的距离为0

  //有n个点，迭代n次
  for (int i = 0; i<n; i++)
  {
    int t = -1;//当前访问点的编号初始为-1

    for (int j = 1; j <= n; j++) //从点1到点n开始计算dist
      if (!st[j] && (t == -1 || dist[t] > dist[j]))
        t = j;// 更新点t，直到找到dist最小的点

    st[t]= true;//标记此点确定

    for (int j = 1; j <=n; j++)//每个点都要遍历所有点一遍
       dist[j] = min( dist[j], dist[t]+ g[t][j]);//遍历所有的点，求从点t到点j的最小值
   }


   if (dist[n] == INF) return -1;
   return dist[n];//返回第n个点的最短距离
}

int main()
{
  cin>>n>>m;

  memset(g, 0x3f, sizeof g);

  while (m--)
  {
    int x,y,z;
    cin>>x>>y>>z;
    g[x][y] = min( g[x][y],z);//取重边和自环的最小值，保留一条边
  }
  cout<<Dijkstra()<<endl;

  return 0;
}
```
