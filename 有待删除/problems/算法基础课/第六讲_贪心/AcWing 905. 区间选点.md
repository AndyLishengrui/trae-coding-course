# AcWing 905. 区间选点 — 区间选点

**难度:** 简单 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/905/

## 题目描述

给定N个闭区间[ai,bi]，请你在数轴上选择尽量少的点，使得每个区间内至少包含一个选出的点。

输出选择的点的最小数量。

位于区间端点上的点也算作区间内。

### 输入格式

第一行包含整数N，表示区间数。

接下来N行，每行包含两个整数ai,bi，表示一个区间的两个端点。

数据范围

1≤N≤10^5,

−10^9≤ai≤bi≤10^9

### 输出格式

输出一个整数，表示所需的点的最小数量。

### 样例

**输入:**
```
3
-1 1
2 4
3 5
```

**输出:**
```
2
```

### 提示

原题链接

Y总代码

参考题解

Y总讲解

## AC代码

```cpp
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 100007;

struct Range
{
  int l , r;
  bool operator< (const Range & R) const
  {
    return r < R.r;//重载比较符，根据r排序
  }
} range[N];

int main()
{
    int n;
    scanf("%d", &n);
    //读入区间
    for (int i = 0; i <n; i++)
    {
      int l,r;
      scanf("%d%d", &l, &r);
      range[i] = {l,r};
    }
    //按照右端点排序
    sort(range,range+n);
    //根据右端点计算覆盖的区间个数
    int res = 0, ed = -2e9;//已统计区间的右端点
    for (int i = 0; i < n; i ++ )
     if (range[i].l > ed)
     {
       res ++;
       ed = range[i].r;
     }
     printf("%d\n", res);

     return 0;
}
```
