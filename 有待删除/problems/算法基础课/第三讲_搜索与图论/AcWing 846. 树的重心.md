# AcWing 846. 树的重心 — 树的重心

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/846/

## 题目描述

给定一颗树，树中包含n个结点（编号1~n）和n-1条无向边。

请你找到树的重心，并输出将重心删除后，剩余各个连通块中点数的最大值。

重心定义：重心是指树中的一个结点，如果将这个点删除后，剩余各个连通块中点数的最大值最小，那么这个节点被称为树的重心。

数据范围：1≤n≤10^5

### 输入格式

第一行包含整数n，表示树的结点数。

接下来n-1行，每行包含两个整数a和b，表示点a和点b之间存在一条边。

### 输出格式

输出一个整数m，表示重心的所有的子树中最大的子树的结点数目。

### 样例

**输入:**
```
9
1 2
1 7
1 4
2 8
2 5
4 3
3 9
4 6
```

**输出:**
```
4
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

const int N = 100007, M= N*2;//无向图

int n;
int h[N], e[M], ne[M], idx;
int ans = N;
bool st[N];//顶点n是否访问

void add(int a, int b)  // 添加一条边a->b
{
    e[idx] = b, ne[idx] = h[a], h[a] = idx ++ ;
}

int dfs(int u)
{
  st[u] = true;

  int size = 0;//去掉i节点后，i子树的最大子树节点数
  int sum = 0;//i子树的节点总数
  for (int i = h[u]; i!=-1; i=ne[i])
  {
    int j = e[i];
    if (st[j]) continue;

    int s = dfs(j);//返回j子树的大小
    size = max(size,s);
    sum += s;//计算所有子树和
  }

  size = max(size, n - sum - 1);//i子树和与 非i子树部分的和，取最大值
  ans = min(ans,size);

  return sum+1;//加上i节点本身
}

int main()
{
    cin>>n;
    memset(h, -1, sizeof h);
    for (int i = 0; i < n-1; i ++ )
    {
      int a,b;
      cin>>a>>b;
      add(a, b),add(b,a);//无向边
    }
    dfs(1);
    cout<<ans<<endl;
    return 0;
}
```
