# AcWing 848. 有向图的拓扑序列 — 拓扑排序试炼之有向图的拓扑序列

**难度:** 中等 | **时间限制:** 2000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/848/

## 题目描述

给定一个n个点m条边的有向图，点的编号是1到n，图中可能存在重边和自环。

请输出任意一个该有向图的拓扑序列，如果拓扑序列不存在，则输出-1。

若一个由图中所有点构成的序列A满足：对于图中的每条边(x, y)，x在A中都出现在y之前，则称A是该图的一个拓扑序列。

数据范围：1≤n,m≤10^5

### 输入格式

第一行包含两个整数n和m

接下来m行，每行包含两个整数x和y，表示存在一条从点x到点y的有向边(x, y)。

### 输出格式

共一行，如果存在拓扑序列，则输出拓扑序列。

否则输出-1。

### 样例

**输入:**
```
3 3
1 2
2 3
1 3
```

**输出:**
```
1 2 3
```

## AC代码

```cpp
#include <iostream>
#include <algorithm>
#include <queue>
#include <cstring>

using namespace std;
#define For(a, begin, end) for (int a = (begin); a < (end); a++)
const int N = 1000007;

int n, m;
int head[N], edge[N], nextVertex[N], idx; //邻接表
int q[N], d[N]; //队列，入度

void add(int a, int b)
{    
    edge[idx] = b;
    nextVertex[idx] = head[a];
    head[a] = idx++;
}

bool topsort()
{
    int qHeadIdx = 0, qTailIdx = -1; //队头，队尾
    //从前往后遍历入度为0的点，插入队列
    for (int i = 1; i <= n; i++)
        if (!d[i])
            q[++qTailIdx] = i; //数组模拟队列，入队是尾指针+1
    while (qHeadIdx <= qTailIdx) //如果头指针小于尾指针
    {
        int t = q[qHeadIdx++]; //取队列头元素，，出队只是把头指针往后移动一位
        //遍历t的临边，空指针初始化为-1
        for (int i = head[t]; i != -1; i = nextVertex[i])
        {
            int j = edge[i]; //取到出边
            d[j]--;   //入度减一
            if (d[j] == 0)
                q[++qTailIdx] = j; //如若入度为0，压入队列
        }
    }
    //判断是否所有顶点都入队
    //也就是头指针qTailIdx是否等于n-1,即所有点都进入队列了
    return qTailIdx==n-1;
}
int main()
{

    cin >> n >> m;            //读入n,m
    memset(head, -1, sizeof(head)); //初始化Head数组指向-1顶点

    For(i, 0, m)
    {
        int a, b;
        cin >> a >> b;
        add(a, b); //插入边
        d[b]++;    //更新入度
    }

    if (topsort())
    {//数组队列里面的元素就是拓扑序
      for (int i =0; i<n; i++) printf("%d ",q[i]);
    }
    else
        puts("-1");
    return 0;
}
```
