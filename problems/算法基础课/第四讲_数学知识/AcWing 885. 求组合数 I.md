# AcWing 885. 求组合数 I — 求组合数(1)

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/885/

## 题目描述

给定`n`组询问，每组询问给定两个整数`a，b`，请你输出`C_a^b mod (10^9 + 7)`的值。

**数据范围**

`1≤n≤10000``1≤b≤a≤2000`

### 输入格式

第一行包含整数`n`。接下来`n`行，每行包含一组`a`和`b`。

### 输出格式

共`n`行，每行输出一个询问的解。

### 样例

**输入:**
```
3
3 1
5 3
2 2
```

**输出:**
```
3
10
1
```

### 提示

原题链接

## AC代码

```cpp
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 2007, mod = 1e9+7;

int c[N][N];

void init()
{
  for (int i = 0; i<N; i++)
    for (int j = 0; j <= i; j ++ )
      if (!j) c[i][j] = 1;
      else c[i][j] = (c[i-1][j-1]+c[i-1][j]) % mod;
}

int main()
{
    int n; 
    scanf("%d", &n);
    init();
    while (n -- )
    {
      int a,b;
      scanf("%d%d", &a, &b);
      printf("%d\n",c[a][b]);
    }
    return 0;
}
```
