# AcWing 844. 走迷宫 — BFS试炼之走迷宫

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/844/

## 题目描述

给定一个n*m的二维整数数组，用来表示一个迷宫，数组中只包含0或1，其中0表示可以走的路，1表示不可通过的墙壁。

最初，有一个人位于左上角(1, 1)处，已知该人每次可以向上、下、左、右任意一个方向移动一个位置。

请问，该人从左上角移动至右下角(n, m)处，至少需要移动多少次。

数据保证(1, 1)处和(n, m)处的数字为0，且一定至少存在一条通路。

数据范围：1<=n<=10

### 输入格式

第一行包含两个整数n和m。

接下来n行，每行包含m个整数（0或1），表示完整的二维数组迷宫。

### 输出格式

输出一个整数，表示从左上角移动至右下角的最少移动次数。

### 样例

**输入:**
```
5 5
0 1 0 0 0
0 1 0 1 0
0 0 0 0 0
0 1 1 1 0
0 0 0 1 0
```

**输出:**
```
8
```

### 提示

原题链接

Y总讲解

参考代码

## AC代码

```cpp
#include <algorithm>
#include <iostream>
#include <queue>
#include <cstring>
using namespace std;

typedef pair<int, int> PII;  // Y总风格pair<int,int>声明

const int N = 107;

int n, m;
int g[N][N],d[N][N];  

//广搜
int bfs() {

  queue<PII> q;      //队列

  memset(d,-1,sizeof d);
  d[0][0]=0;
  q.push({0,0});

  // 四个方向向量
  int dx[] = {-1, 0, 1, 0}, dy[] = {0, 1, 0, -1};

  while (q.size()) 
  { //队列为空的时候退出广搜
    auto t = q.front();  //取队头
    q.pop();             //弹出队头

    //搜索四个方向
    for (int i = 0; i < 4; i++)
    {
      int x = t.first + dx[i], y = t.second + dy[i];  //待搜索的新坐标点

      if (x < 0 || x >= n || y < 0 || y >= m || g[x][y] != 0 || d[x][y]!=-1) continue;

      d[x][y] = d[t.first][t.second]+1;

      q.push({x, y});//入队


    }
  }

  return d[n-1][m-1];
}

int main() {

    cin >> n >> m;

    for (int i = 0; i < n; i++) 
      for (int j = 0; j <m; j++)
        cin >> g[i][j];

    cout << bfs() << endl;

  return 0;
}
```
