# AcWing 884. 高斯消元解异或线性方程组 — 高斯消元解异或线性方程组

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/884/

## 题目描述

输入一个包含 n 个方程 n 个未知数的异或线性方程组。方程组中的所有系数和常数均为 0 或 1，每个未知数的取值也为 0 或 1。

求解该方程组。

异或线性方程组示例如下：

M[1][1]x[1] ^ M[1][2]x[2] ^ … ^ M[1][n]x[n] = B[1]
M[2][1]x[1] ^ M[2][2]x[2] ^ … ^ M[2][n]x[n] = B[2]
…
M[n][1]x[1] ^ M[n][2]x[2] ^ … ^ M[n][n]x[n] = B[n]`其中“^”表示异或(XOR)，M[i][j]表示第i个式子中x[j]的系数，B[i]是第i个方程右端的常数，取值均为0或1。

### 输入格式

第一行包含整数 n (1 ≤ n ≤ 100)。

接下来 n 行，每行包含 n+1 个整数（每个数字均为 0 或 1），表示一个方程的 n 个系数以及常数。

### 输出格式

如果方程组存在唯一解，则输出 n 行，每行输出一个未知数的解。
如果存在多组解，则输出 "Multiple sets of solutions"。
如果无解，则输出 "No solution"。

### 样例

**输入:**
```
3
1 1 0 1
0 1 1 0
1 0 0 1
```

**输出:**
```
1
0
0
```

### 提示

利用模2下的高斯消元进行求解。对每一列找到主元，对其他行使用异或消元。

最后检查是否存在矛盾（系数全部为 0 而常数为 1），或是否有自由变量。如果自由变量存在则说明有多组解。

## AC代码

```cpp
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 110;

int n;
int a[N][N];

int gauss()  // 高斯消元，答案存于a[i][n]中，0 <= i < n
{
    int c, r;
    for (c = 0, r = 0; c < n; c ++ )
    {
        int t = r;
        for (int i = r; i < n; i ++ )  // 找非零行
            if (a[i][c])
                t = i;

        if (!a[t][c]) continue;

        for (int i = c; i <= n; i ++ ) swap(a[r][i], a[t][i]);  // 将非零行换到最顶端
        for (int i = r + 1; i < n; i ++ )  // 用当前行将下面所有的列消成0
            if (a[i][c])
                for (int j = n; j >= c; j -- )
                    a[i][j] ^= a[r][j];

        r ++ ;
    }

    if (r < n)
    {
        for (int i = r; i < n; i ++ )
            if (a[i][n])
                return 2;  // 无解
        return 1;  // 有多组解
    }

    for (int i = n - 1; i >= 0; i -- )
        for (int j = i + 1; j < n; j ++ )
            a[i][n] ^= a[i][j] * a[j][n];

    return 0;  // 有唯一解
}


int main()
{
    cin >> n;
    for (int i = 0; i < n; i++)
      for (int j = 0; j < n+1; j++)
        cin >> a[i][j];

    int t = gauss();
    if (t == 0)
    {
      for (int i = 0; i<n;i++) cout<< a[i][n] <<endl;
    }
    else if (t == 1) puts("Multiple sets of solutions");
    else puts("No solution");

    return 0;
}
```
