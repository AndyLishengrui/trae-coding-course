# AcWing 883. 高斯消元解线性方程组 — 高斯消元解线性方程组

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/883/

## 题目描述

输入一个包含 n 个方程 n 个未知数的线性方程组（系数为实数），求解该方程组。

下图为一个包含 m 个方程 n 个未知数的线性方程组示例：

### 输入格式

第一行包含整数 n (1 ≤ n ≤ 100)。接下来 n 行，每行包含 n+1 个实数，表示一个方程的 n 个系数及右侧的常数。

所有实数均保留两位小数，绝对值不超过 100。

### 输出格式

如果方程组存在唯一解，则输出 n 行，每行输出一个未知数的解，保留两位小数。
如果存在无数解，则输出 "Infinite group solutions"。
如果无解，则输出 "No solution"。

### 样例

**输入:**
```
3
1.00 2.00 -1.00 -6.00
2.00 1.00 -3.00 -9.00
-1.00 -1.00 2.00 7.00
```

**输出:**
```
1.00
-2.00
3.00
```

### 提示

使用高斯消元法求解。注意处理接近零（EPS）的情况，根据消元后的阶数判断系统是否有唯一解、无解或无穷多解。

注意：本题有 SPJ，当输出结果为`0.00`时，输出`-0.00`也会判对。在数学中，一般没有正零或负零的概念，所以严格来说应当输出`0.00`，但是考虑到本题作为一道模板题，考察点并不在于此，在此处卡住大多同学的代码没有太大意义，故增加 SPJ，对输出`-0.00`的代码也予以判对。

## AC代码

```cpp
//Andy代码，参考Y总
#include <iostream>
#include <cstring>
#include <algorithm>
#include <cmath>

using namespace std;
const int N = 110;
const double eps = 1e-6;

int n;
double a[N][N];

int gauss()  // 高斯消元，答案存于a[i][n]中，0 <= i < n
{
    int c, r;
    for (c = 0, r = 0; c < n; c ++ )
    {
        int t = r;
        for (int i = r; i < n; i ++ )  // 找绝对值最大的行
            if (fabs(a[i][c]) > fabs(a[t][c]))
                t = i;

        if (fabs(a[t][c]) < eps) continue;

        for (int i = c; i <= n; i ++ ) swap(a[t][i], a[r][i]);  // 将绝对值最大的行换到最顶端
        for (int i = n; i >= c; i -- ) a[r][i] /= a[r][c];  // 将当前行的首位变成1
        for (int i = r + 1; i < n; i ++ )  // 用当前行将下面所有的列消成0
            if (fabs(a[i][c]) > eps)
                for (int j = n; j >= c; j -- )
                    a[i][j] -= a[r][j] * a[i][c];

        r ++ ;
    }

    if (r < n)
    {
        for (int i = r; i < n; i ++ )
            if (fabs(a[i][n]) > eps)
                return 2; // 无解
        return 1; // 有无穷多组解
    }
    //将方程反推出答案
    for (int i = n - 1; i >= 0; i -- )
        for (int j = i + 1; j < n; j ++ )
            a[i][n] -= a[i][j] * a[j][n];

    return 0; // 有唯一解
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
      for (int i = 0; i<n;i++) printf("%.2lf\n",a[i][n]);
    }
    else if (t == 1) puts("Infinite group solutions");
    else puts("No solution");

    return 0;
}
```
