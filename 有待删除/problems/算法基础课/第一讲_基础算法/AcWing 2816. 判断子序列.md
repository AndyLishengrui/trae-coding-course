# AcWing 2816. 判断子序列 — 判断子序列

**难度:** 简单 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/2816/

## 题目描述

给定一个长度为`n`的整数序列`a1,a2,…,an`以及一个长度为`m`的整数序列`b1,b2,…,bm`。

请你判断`a`序列是否为`b`序列的子序列。

子序列指序列的一部分项按原有次序排列而得的序列，例如序列`{a1,a3,a5}`是序列`{a1,a2,a3,a4,a5}`的一个子序列。

### 输入格式

第一行包含两个整数`n,m`。

第二行包含`n`个整数，表示`a1,a2,…,an`。

第三行包含`m`个整数，表示`b1,b2,…,bm`。

**数据范围**

`1≤n≤m≤10^5`

`−10^9≤ai,bi≤10^9`

### 输出格式

如果a序列是b序列的子序列，输出一行`Yes`。

否则，输出`No`。

### 样例

**输入:**
```
3 5
1 3 5
1 2 3 4 5
```

**输出:**
```
Yes
```

## AC代码

```cpp
#include <iostream>
#include <cstdio>
using namespace std;
const int N = 1e5+7;//我的风格
int a[N],b[N];

int main()
{
  int n,m;
  scanf("%d%d",&n,&m);
  for (int i = 0; i<n; i++) scanf("%d",&a[i]);
  for (int i = 0; i<m; i++) scanf("%d",&b[i]);

  int p = 0;//指向a数组的指针
  for (int i = 0; i < m; i++)
  {
    if (p < n && a[p] == b[i]) p++;
  }
  //完全匹配
  if (p==n) puts("Yes");
  else puts("No");

  return 0;

}
```
