# AcWing 906. 区间分组 — 区间分组

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/906/

## 题目描述

给定N个闭区间[ai,bi]，请你将这些区间分成若干组，使得每组内部的区间两两之间（包括端点）没有交集，并使得组数尽可能小。

输出最小组数。

### 输入格式

第一行包含整数N，表示区间数。

接下来N行，每行包含两个整数ai,bi，表示一个区间的两个端点。

数据范围

1≤N≤10^5,

−10^9≤ai≤bi≤10^9

### 输出格式

输出一个整数，表示最小组数。

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

## AC代码

```cpp
#include <iostream>
#include <cstring>
#include <algorithm>
#include <queue>
#include <utility>

using namespace std;

const int N = 100007;

pair<int,int> range[N];
int n;
int main()
{
    cin>>n;
    for (int i = 0; i < n; i ++ )
    {
      int a , b;
      cin>>a>>b;

      range[i]={a,b};
    }
    //排序
    sort(range,range+n);
    //用小根堆维护max_r
    priority_queue<int, vector<int>, greater<int>> heap;

    for (int i = 0; i < n; i ++ )
    {
      if (heap.empty() || heap.top() >= range[i].first)
      {
        heap.push(range[i].second);//创建新分组
      }
      else
      {
        heap.pop(); //更新mar_r
        heap.push(range[i].second);//右端点入堆
      }
    }
    cout<<heap.size()<<endl;

    return 0;
}
```
