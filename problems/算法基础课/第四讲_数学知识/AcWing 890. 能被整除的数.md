# AcWing 890. 能被整除的数 — 能被整除的数

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/890/

## 题目描述

给定一个整数 n 和 m 个不同的质数 p1, p2, …, pm。

请你求出 1∼n 中能被 p1, p2, …, pm 中至少一个质数整除的整数有多少个。

### 输入格式

第一行包含两个整数 n 和 m。

第二行包含 m 个质数。

### 输出格式

输出一个整数，表示满足条件的整数个数。

### 样例

**输入:**
```
10 2
2 3
```

**输出:**
```
7
```

### 提示

利用容斥原理：遍历所有非空质数组合，计算乘积 prod。若 prod ≤ n，则该组贡献值为 floor(n/prod)，按组合中质数个数的奇偶性相加或相减。

原题链接

## AC代码

```cpp
//容斥原理
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

typedef long long LL;

const int N = 20;

int n,m;
int p[N];

int main()
{
    cin>>n>>m;
    for (int i = 0; i < m; i++) cin >>p[i];

    int res = 0;
    //用i的二进制数来枚举集合的选取情况
    for (int i = 1; i < 1<<m; i++)
    {
      int t = 1, cnt =0;
      for (int j = 0; j < m; j++)
        if (i >>j & 1)
        {
          cnt ++;//计算二进制中1的个数
          if ((LL) t * p[j] > n)
          { 
            t = -1;
            break;
          }
          t *= p[j]; //分母
        }
        if (t != -1)
        {
          if (cnt % 2) res += n / t;
          else res -= n / t;
        }
    }
    cout <<res<<endl;

    return 0;
}
```
