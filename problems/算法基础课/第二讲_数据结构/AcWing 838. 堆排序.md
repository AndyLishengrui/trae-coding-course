# AcWing 838. 堆排序 — 堆排序

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/838/

## 题目描述

输入一个长度为n的整数数列，从小到大输出前m小的数。

数据范围:

1≤m≤n≤10^5，

1≤数列中元素≤10^9

### 输入格式

第一行包含整数n和m。

第二行包含n个整数，表示整数数列。

### 输出格式

共一行，包含m个整数，表示整数数列中前m小的数。

### 样例

**输入:**
```
5 3
4 5 1 3 2
```

**输出:**
```
1 2 3
```

### 提示

原题链接

原理讲解

Y总讲解

## AC代码

```cpp
#include <iostream>
#include <algorithm>

using namespace std;

const int N = 100007;//Andy风格

int h[N],heapSize;

int n,m;

void down(int u)
{
  int t = u;
  if (2 * u <= heapSize && h[t] > h[2*u]) t = 2*u;

  if (2 * u + 1 <= heapSize && h[t] > h[2*u+1]) t = 2*u+1;

  if (u!=t)
  {
    swap(h[u], h[t]);
    down(t);
  }
}

int main() {
  cin>>n>>m;
  heapSize = n;
  //i从1开始
  for (int i = 1; i<=n; i++)
  scanf("%d",&h[i]);
  for (int i = n/2; i; i--) down(i);//初始化堆

  while (m--)
  {
    cout<<h[1]<<" ";
    h[1] = h[heapSize--];
    down(1);
  }
  return 0;
}
```
