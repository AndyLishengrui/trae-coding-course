# AcWing 876. 快速幂求逆元 — 快速幂求逆元

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/876/

## 题目描述

给定`n`组`ai, pi`，其中`pi`是质数，求`ai`模`pi`的乘法逆元，若逆元不存在则输出`impossible`。

注意：请返回在`0 ∼ p - 1`之间的逆元。

乘法逆元的定义：若整数`b，m`互质，并且对于任意的整数`a`，如果满足`b | a`，则存在一个整数`x`，使得`ab ≡ a×x (mod m)`，则称`x`为`b`的模`m`乘法逆元，记为`b^(-1) (mod m)`。

`b`存在乘法逆元的充要条件是`b`与模数`m`互质。当模数`m`为质数时，`b^(m - 2)`即为`b`的乘法逆元。

**数据范围**

`1≤n≤10^5`

`1≤ai, pi≤2*10^9`

### 输入格式

第一行包含整数`n`。

接下来`n`行，每行包含一个数组`ai, pi`，数据保证`pi`是质数。

### 输出格式

输出共`n`行，每组数据输出一个结果，每个结果占一行。

若`ai`模`pi`的乘法逆元存在，则输出一个整数，表示逆元，否则输出`impossible`。

### 样例

**输入:**
```
3
4 3
8 5
6 3
```

**输出:**
```
1
2
impossible
```

### 提示

原题链接

## AC代码

```cpp
#include <iostream>
#include <algorithm>
using namespace std;
typedef long long LL;
int qmi(int a, int k, int p)
{
    int res = 1; //初始值为1
    while (k)
    {
        if (k & 1)                 //b的最末尾为1
            res = (LL)res * a % p; //必须用long long防止溢出
        k >>= 1;                   //去掉b最低位
        a = (LL)a * a % p;
    }
    return res;
}

int main()
{
    int q;
    scanf("%d", &q); //数据很大，需要用LL读入
    while (q--)
    {
        int a, p;
        scanf("%d%d", &a, &p); //读入a b p
        if (a % p) printf("%d\n",qmi(a, p-2, p)); //计算快速幂
        else puts("impossible");
    }
    return 0;
}
```
