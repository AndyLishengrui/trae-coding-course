# AcWing 907. 区间覆盖 — 区间覆盖

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/907/

## 题目描述

给定 N 个区间 [ai, bi] 以及一个目标区间 [s, t]，请你选择尽量少的区间，使得所选区间的并集能够完全覆盖目标区间 [s, t]。如果无法完全覆盖，则输出 −1。

### 输入格式

第一行包含两个整数 s 和 t (−109 ≤ s ≤ t ≤ 109)，表示目标区间的两个端点。
第二行包含整数 N (1 ≤ N ≤ 105)，表示区间数。
接下来 N 行，每行包含两个整数 ai 和 bi (−109 ≤ ai ≤ bi ≤ 109)，表示一个区间的左右端点。

### 输出格式

输出一个整数，表示所需的最少区间数；若无法完全覆盖，则输出 −1。

### 样例

**输入:**
```
1 5
3
-1 3
2 4
3 5
```

**输出:**
```
2
```

### 提示

采用贪心策略：首先将所有区间按起点升序排序。从 s 开始，每次选择所有起点不大于当前覆盖点的区间中，具有最大终点的区间，然后更新当前覆盖点；若无法推进或覆盖不到 t，则无解，输出 -1。

## AC代码

```cpp
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 100007;

pair<int,int> range[N];
int n;

int main()
{
    int start,end;
    cin>>start>>end;
    cin>>n;
    for (int i = 0; i < n; i ++ )
    {
      int l,r;
      cin>>l>>r;
      range[i] = {l,r};
    }
    sort(range,range+n);//排序

    int res = 0;
    bool success = false;
    for (int i = 0; i < n; i ++ )
    {

      int j = i, r = -2e9;
      while(j<n && range[j].first <= start)
      {
        r =max(r,range[j].second); 
        j++;
      }

      if (r < start)
      {
        res = -1;
        break;
      }

      res++;
      if (r >= end)
      {
        success = true;
        break;
      }

      start = r;
      i = j-1;
    }

    if (!success) res = -1;
    cout<<res<<endl;

    return 0;
}
```
