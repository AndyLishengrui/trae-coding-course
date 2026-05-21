# AcWing 860. 染色法判定二分图 — 染色法判定二分图

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/860/

## 题目描述

给定一个`n`个点`m`条边的无向图，图中可能存在重边和自环。

请你判断这个图是否是二分图。

### 输入格式

第一行包含两个整数`n`和`m`。

接下来`m`行，每行包含两个整数`u`和`v`，表示点`u`和点`v`之间存在一条边。

**数据范围**

`1≤n,m≤10^5`

### 输出格式

如果给定图是二分图，则输出`Yes`，否则输出`No`。

### 样例

**输入:**
```
4 4
1 3
1 4
2 3
2 4
```

**输出:**
```
Yes
```

### 提示

原题链接

视频讲解

参考题解

Y总代码

## AC代码

```cpp
#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;
//无向图
const int N=100007,M=200007;//两倍的边
int n,m;
int h[N],e[M],ne[M],idx;
int color[N];//0表示未访问，1表示颜色1，2表示颜色2.

void add(int a, int b){
  e[idx]=b, ne[idx]=h[a], h[a]=idx++; //数组模拟链表add操作
}

bool dfs(int u, int c){
  color[u]=c;

  for (int i=h[u]; i!=-1; i=ne[i])
  {
    int j=e[i]; //取i对应的另外一个顶点编号
    if (!color[j]) {
       if (!dfs(j,3-c)) return false;//颜色是1或者2切换，所以用3-color可以交换两种颜色
    }
    else if (color[j]==c) return false;//端点颜色相同
  }
  return true;  
}
int main(){

  scanf("%d%d",&n,&m);
  memset(h,-1,sizeof h);//初始化头结点
  //建图
  while (m--)
  {
     int a,b;
     scanf("%d%d",&a,&b);
     add(a,b); add(b,a);
  }
  bool flag = true;//表示染色有矛盾
  for (int i=1; i<=n; i++)
    if (!color[i]) {
      if (!dfs(i,1))
      {
        flag = false;
        break;
      }
    } 
  if (flag) puts("Yes"); else puts ("No");

  return 0;
}
```
