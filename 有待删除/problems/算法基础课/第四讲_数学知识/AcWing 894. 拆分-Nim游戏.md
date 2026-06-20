# AcWing 894. 拆分-Nim游戏 — 拆分-Nim游戏

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/894/

## 题目描述

给定 n 堆石子，两位玩家轮流操作，每次操作可以取走其中一堆石子，

然后将该堆替换为两堆规模更小的石子（新堆规模可以为 0，且两个新堆中石子的总数不受限制）。

已经放到地面上的石子不能再被操作。

最后无法进行操作的玩家失败。

### 输入格式

第一行包含整数 n (1 ≤ n ≤ 100)。

第二行包含 n 个整数 a1, a2, …, an(1 ≤ ai≤ 100)，分别表示各堆石子的数量。

### 输出格式

如果先手必胜，则输出 "Yes"；否则输出 "No"。

### 样例

**输入:**
```
2
2 3
```

**输出:**
```
Yes
```

### 提示

将每堆石子视为一个子游戏。对于堆大小 A，允许的操作是将其拆分为两堆规模均小于 A 的石子，其 Grundy 值可定义为 g(0)=0，g(A)=mex({ g(i) xor g(j) : 0 ≤ i, j < A })。整局游戏的 Nim 和即为所有堆的 Grundy 值的异或值，先手必胜当且仅当 Nim 和不为 0。

原题链接

## AC代码

```cpp
//sg函数，mex操作，难理解，但很好用
#include <iostream>
#include <cstring>
#include <algorithm>
#include <unordered_set>

using namespace std;

const int N = 107;
int f[N];

int sg(int x)
{
  if (f[x] != -1) return f[x];

  unordered_set<int> S;
  for (int i = 0; i < x; i++)
     for (int j = 0; j <=i; j++)
       S.insert(sg(i)^sg(j));
  // mex操作
  for (int i = 0;; i++)
    if (!S.count(i))
      return f[x] = i;
}

int main()
{
    int n; cin>>n;

    memset(f, -1, sizeof f);

    int res = 0;
    for (int i = 0; i < n; i ++)
    {
      int x; cin>>x;
      res ^= sg(x);
    }

    if (res) puts("Yes");
    else puts("No");

    return 0;
}
```
