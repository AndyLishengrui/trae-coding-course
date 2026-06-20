# AcWing 285. 没有上司的舞会 — 没有上司的舞会

**难度:** 困难 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/285/

## 题目描述

Ural大学有N名职员，编号为1~N。

他们的关系就像一棵以校长为根的树，父节点就是子节点的直接上司。

每个职员有一个快乐指数，用整数Hi给出，其中1≤i≤N。

现在要召开一场周年庆宴会，不过，没有职员愿意和直接上司一起参会。

在满足这个条件的前提下，主办方希望邀请一部分职员参会，使得所有参会职员的快乐指数总和最大，求这个最大值。

数据范围

1≤N≤6000,
−128≤Hi≤127

### 输入格式

第一行一个整数N。

接下来N行，第 i 行表示 i 号职员的快乐指数Hi。

接下来N-1行，每行输入一对整数L, K,表示K是L的直接上司。

### 输出格式

输出最大的快乐指数。

### 样例

**输入:**
```
7
1
1
1
1
1
1
1
1 3
2 3
6 4
7 4
4 5
3 5
```

**输出:**
```
5
```

### 提示

acwing讲解

原题链接

题解参考

## AC代码

```cpp
#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

const int N = 6007;

int n;
int happy[N];
//邻接表
int h[N],e[N], ne[N],idx;
int f[N][2];
bool has_father[N];//判断是否是根节点
void add(int a, int b)
{
    e[idx] = b, ne[idx] = h[a], h[a] = idx ++;
}


void dfs(int u)
{
    f[u][1] = happy[u];
    for (int i = h[u]; i!= -1; i = ne[i])
    {
        int j = e[i];
        dfs(j);
        f[u][0] += max(f[j][0], f[j][1]);
        f[u][1] += f[j][0];
    }
}


int main()
{
    scanf("%d",&n);
    for (int i = 1; i <=n; i++) scanf("%d",&happy[i]);

    memset(h,-1,sizeof h);
    for (int i = 0; i < n-1; i++)
    {
        int a,b;
        scanf("%d%d", &a, &b);
        has_father[a] = true;
        add(b,a);
    }
    //判断有多少根节点
    int root = 1;
    while (has_father[root]) root++;
    dfs(root);
    //只有两种情况，是否选择根节点
    printf("%d\n",max(f[root][0], f[root][1]));
    return 0;
}
```
