# AcWing 291. 蒙德里安的梦想 — 蒙德里安的梦想

**难度:** 困难 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/291/

## 题目描述

求把N*M的棋盘分割成若干个1*2的的长方形，有多少种方案。

例如当N=2，M=4时，共有5种方案。当N=2，M=3时，共有3种方案。

如下图所示：

数据范围1≤N,M≤11

### 输入格式

输入包含多组测试用例。

每组测试用例占一行，包含两个整数N和M。

当输入用例N=0，M=0时，表示输入终止，且该用例无需处理。

### 输出格式

每个测试用例输出一个结果，每个结果占一行。

### 样例

**输入:**
```
1 2
1 3
1 4
2 2
2 3
2 4
2 11
4 11
0 0
```

**输出:**
```
1
0
1
2
3
5
144
51205
```

### 提示

acwing讲解

原题链接

## AC代码

```cpp
//标准例题
#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;
typedef long long LL;

const int N = 12, M = 1 <<N;

int n,m;
LL f[N][M];
vector<int> state[M];
bool st[N];

int main()
{
    while ( cin >> n >> m, n||m)
    {
      for (int i = 0; i < 1 << n; i ++)
      {
        int cnt = 0;
        bool flag = true;
        for (int j = 0; j < n; j++)
          if (i >> j & 1)
          {
            if (cnt & 1)
            {
              flag = false;
              break;
            }
            cnt = 0;
          }
        else cnt ++;

        if (cnt & 1) flag = false;
        st[i] = flag;
      }

      for (int i = 0; i < 1<<n; i++)
      {
        state[i].clear();
        for (int j = 0; j < 1<<n; j++)
          if ((i&j) == 0 && st[i | j])//这个相当巧妙
            state[i].push_back(j);
      }

      memset(f,0,sizeof f);
      f[0][0] = 1;
      for (int i = 1; i <=m; i++)
       for (int j = 0; j < 1 << n; j++)
        for (auto k : state[j])
          f[i][j] += f[i-1][k];

      cout << f[m][0] <<endl;
    }
    return 0;
}
```
