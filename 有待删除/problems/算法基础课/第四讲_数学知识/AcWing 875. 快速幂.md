# AcWing 875. 快速幂 — 快速幂

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/875/

## 题目描述

给定`n`组`ai, bi, pi`，对于每组数据，求出`a^b i mod p i`的值。

### 输入格式

第一行包含整数`n`。

接下来`n`行，每行包含三个整数`ai, bi, pi`。

**数据范围**

`1≤n≤100000`

`1≤ai, bi, pi≤2×10^9`

### 输出格式

对于每组数据，输出一个结果，表示`a^b i mod p i`的值。

每个结果占一行。

### 样例

**输入:**
```
5
1326 8312 7553
1550 7708 3792
500 6795 6235
6880 7895 7532
1904 9984 7790
```

**输出:**
```
2613
3520
1785
7244
5346
```

### 提示

原题链接

Y总讲解

## AC代码

```cpp
#include <iostream>
#include <algorithm>
using namespace std;
typedef long long LL;
int qmi(int a, int b, int p)
{
    int res = 1; //初始值为1
    while (b)
    {
        if (b & 1)                 //b的最末尾为1
            res = (LL)res * a % p; //必须用long long防止溢出
        b >>= 1;                   //去掉b最低位
        a = (LL)a * a % p;
    }
    return res;
}

int main()
{
    int n;
    scanf("%d", &n); //数据很大，需要用LL读入
    while (n--)
    {
        int a, b, p;
        scanf("%d%d%d", &a, &b, &p); //读入a b p

        printf("%d\n", qmi(a, b, p)); //计算快速幂
    }
    return 0;
}
```
