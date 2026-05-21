# AcWing 861. 二分图的最大匹配 — 二分图的最大匹配

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/861/

## 题目描述

给定一个二分图，其中左半部包含`n1`个点（编号 1∼`n1`），右半部包含`n2`个点（编号 1∼`n2`），二分图共包含`m`条边。

数据保证任意一条边的两个端点都不可能在同一部分中。

请你求出二分图的最大匹配数。

二分图的匹配：给定一个二分图`G`，在`G`的一个子图`M`中，`M`的边集`{E}`中的任意两条边都不依附于同一个顶点，则称`M`是一个匹配。

二分图的最大匹配：所有匹配中包含边数最多的一组匹配被称为二分图的最大匹配，其边数即为最大匹配数。

### 输入格式

第一行包含三个整数`n1`、`n2`和`m`。

接下来`m`行，每行包含两个整数`u`和`v`，表示左半部点集中的点`u`和右半部点集中的点`v`之间存在一条边。

**数据范围**

`1≤n1,n2≤500`

`1≤u≤n1`

`1≤v≤n2`

`1≤m≤10^5`

### 输出格式

输出一个整数，表示二分图的最大匹配数。

### 样例

**输入:**
```
2 2 4
1 1
1 2
2 1
2 2
```

**输出:**
```
2
```

### 提示

原题链接

Y总讲解

参考题解

Y总代码

## AC代码

```cpp
#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;
const int N=510, M=100010;
int n1,n2,m;
int h[N],e[N],ne[N],idx;//数组存储图,使用链表
int match[N];
bool visited[N];//判重
void add(int a, int b){
  e[idx]=b, ne[idx]=h[a], h[a]=idx++; //数组模拟链表add操作
}
bool find(int x)//深搜
{
  for (int i=h[x]; i!=-1; i=ne[i])//枚举所有边相连的顶点
  {
    int j=e[i];//取顶点下标
    if (!visited[j]) {
      visited[j]=true;
      if (match[j]==0 || find(match[j]))//未匹配，或者可以找到下家
      {
        match[j]=x; return true;
      }
    }
  }
 return false; 
}

int main()
{
  scanf("%d%d%d",&n1,&n2,&m);
  memset(h,-1,sizeof h);
  while(m--) {
   int a,b;//读入点
    scanf("%d%d",&a,&b);
    add(a,b);    
  }
  int res=0;//最大匹配数，也就是统计完全匹配的数量
  for(int i=1; i<=n1;i++) {
    memset(visited,false,sizeof visited);
    if (find(i)) res++;
  }
  printf("%d\n",res);

}
```
