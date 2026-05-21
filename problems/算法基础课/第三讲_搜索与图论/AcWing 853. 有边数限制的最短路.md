# AcWing 853. 有边数限制的最短路 — 有边数限制的最短路

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/853/

## 题目描述

给定一个n个点m条边的有向图，图中可能存在重边和自环，边权可能为负数。

请你求出从1号点到n号点的最多经过k条边的最短距离，如果无法从1号点走到n号点，输出impossible。

注意：图中可能存在负权回路。

### 输入格式

第一行包含三个整数n，m，k。

接下来m行，每行包含三个整数x，y，z，表示存在一条从点x到点y的有向边，边长为z。

### 输出格式

输出一个整数，表示从1号点到n号点的最多经过k条边的最短距离。

如果不存在满足条件的路径，则输出“impossible”。

### 样例

**输入:**
```
3 3 1
1 2 1
2 3 1
1 3 3
```

**输出:**
```
3
```

### 提示

原题链接

Y总代码

Y总讲解

## AC代码

```cpp
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;
const int N = 507, M = 100007;

struct edge {
  int a, b,w;
} edges[M];

int dist[N],backup[N];//备份数组，防止迭代的时候串联
int n,m,k;//k代表最短路径最多包含k条边

int bellman_ford(){
  memset(dist,0x3f,sizeof dist);//初始化为无穷大0x3f3f3f3f;
  dist[1] = 0;//顶点1为起点，搜索到顶点n的最短路径
  for (int i = 0; i<k; i++)
  {
    memcpy(backup,dist,sizeof dist);//备份dist数组

    for (int j = 0; j<m; j++) {//遍历所有边
    int a = edges[j].a, b=edges[j].b, w=edges[j].w;
    dist[b] = min(dist[b],backup[a]+w);//松弛操作

    }
  }

  if (dist[n] > 0x3f3f3f3f /2) return -1;
  else return dist[n];

}

int main()
{
    scanf("%d%d%d", &n,&m,&k);
    for (int i = 0; i < m; i ++ ) {
      int a, b, w;
      scanf("%d%d%d", &a,&b,&w);
      edges[i]={a,b,w};//直接用数组存储边和边权
    }

    int res = bellman_ford(); //调用bf算法
    if (res == -1) puts("impossible");
    else cout<<res;

    return 0;
}
```
