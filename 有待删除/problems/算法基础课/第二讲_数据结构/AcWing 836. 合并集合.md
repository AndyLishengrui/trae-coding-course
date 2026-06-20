# AcWing 836. 合并集合 — 并查集试炼之合并集合

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/836/

## 题目描述

一共有n个数，编号是1~n，最开始每个数各自在一个集合中。

现在要进行m个操作，操作共有两种：

“M a b”，将编号为a和b的两个数所在的集合合并，如果两个数已经在同一个集合中，则忽略这个操作；“Q a b”，询问编号为a和b的两个数是否在同一个集合中；数据范围：1≤n,m≤10^5

### 输入格式

第一行输入整数n和m。

接下来m行，每行包含一个操作指令，指令为“M a b”或“Q a b”中的一种。

### 输出格式

对于每个询问指令”Q a b”，都要输出一个结果，如果a和b在同一集合内，则输出“Yes”，否则输出“No”。

每个结果占一行。

### 样例

**输入:**
```
4 5
M 1 2
M 3 4
Q 1 2
Q 1 3
Q 3 4
```

**输出:**
```
Yes
No
Yes
```

### 提示

原题链接

Y总代码

Y总讲解

## AC代码

```cpp
#include <iostream>
using namespace std;
const int N = 100007;
int p[N];
int n;

//返回x的father节点+路径压缩
int find(int x)
{
  if (p[x] != x) p[x] = find(p[x]);
  return p[x];
}
void merge(int a, int b)
{
  p[find(a)] = find(b);
}
void query(int a, int b)
{
   if (find(a) == find(b)) puts("Yes");
    else puts("No");
}
int main()
{ 
   int  m;
   cin>>n>>m;//输入n
  //创造并查集数
  for (int i = 1; i <=n; i++) p[i] = i;
  while (m--)
  {
    char op;
    int a,b;
    cin>>op;
    cin>>a>>b;
    if (op == 'M') merge(a,b);
    else if (op == 'Q') query(a,b);
  }
  return 0;
}
```
