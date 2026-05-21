# AcWing 837. 连通块中点的数量 — 并查集试炼之连通块中点的数量

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/837/

## 题目描述

给定一个包含n个点（编号为1~n）的无向图，初始时图中没有边。

现在要进行m个操作，操作共有三种：

“C a b”，在点a和点b之间连一条边，a和b可能相等；“Q1 a b”，询问点a和点b是否在同一个连通块中，a和b可能相等；“Q2 a”，询问点a所在连通块中点的数量；数据范围:1≤n,m≤10^5

### 输入格式

第一行输入整数n和m。

接下来m行，每行包含一个操作指令，指令为“C a b”，“Q1 a b”或“Q2 a”中的一种。

### 输出格式

对于每个询问指令”Q1 a b”，如果a和b在同一个连通块中，则输出“Yes”，否则输出“No”。

对于每个询问指令“Q2 a”，输出一个整数表示点a所在连通块中点的数量

每个结果占一行。

### 样例

**输入:**
```
5 5
C 1 2
Q1 1 2
Q2 1
C 2 5
Q2 5
```

**输出:**
```
Yes
2
3
```

### 提示

原题

Y总代码

Y总讲解

## AC代码

```cpp
#include <iostream>
#include <cstring>

using namespace std;
const int N = 100007;
int p[N],Size[N];
int n;

//返回x的father节点+路径压缩
int find(int x)
{
  if (p[x] != x) p[x] = find(p[x]);
  return p[x];
}
void merge(int a, int b)
{
  Size[find(b)] += Size[find(a)];
  p[find(a)] = find(b);
}
void query(int a, int b)
{
   if (find(a) == find(b)) puts("Yes");
    else puts("No");
}
int count(int x)
{
  return Size[find(x)];
}
int main()
{ 
   int  m;
   cin>>n>>m;//输入n
  //创造并查集数
  for (int i = 1; i <=n; i++) p[i] = i , Size[i] = 1;
  while (m--)
  {
    string op;
    int a,b;
    cin>>op;
    if (op == "C") 
    { 
      cin>>a>>b;
      if (find(a) == find(b)) continue;//已经在同一个集合里，跳过merge操作
      merge(a,b);
    }
    else if (op == "Q1") cin>>a>>b, query(a,b);
    else cin>>a, cout<<count(a)<<endl;;
  }
  return 0;
}
```
