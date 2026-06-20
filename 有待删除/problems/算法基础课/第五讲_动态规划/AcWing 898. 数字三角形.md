# AcWing 898. 数字三角形 — 数字三角形

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/898/

## 题目描述

给定一个如下图所示的数字三角形，从顶部出发，在每一结点可以选择移动至其左下方的结点或移动至其右下方的结点，一直走到底层，要求找出一条路径，使路径上的数字的和最大。

        7
      3   8
    8   1   0
  2   7   4   4
4   5   2   6   5`

### 输入格式

第一行包含整数n，表示数字三角形的层数。

接下来n行，每行包含若干整数，其中第 i 行表示数字三角形第 i 层包含的整数。

### 输出格式

输出一个整数，表示最大的路径数字和。

### 样例

**输入:**
```
5
7
3 8
8 1 0 
2 7 4 4
4 5 2 6 5
```

**输出:**
```
30
```

### 提示

原题链接

## AC代码

```cpp
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 507;

int n;
int w[N][N], f[N][N];//三角矩阵依旧用2纬存储

int main()
{
    //读入n，w
    cin>>n;
    for (int i = 1; i <=n; i++)
      for (int j = 1; j <= i; j++)
        cin >> w[i][j];

   //初始化最底层的f[n][j]
   for (int i = 1; i <= n; i++) f[n][i] = w[n][i];

   //用dp从底层往上计算每个f[i][j]的值
   for (int i = n-1; i; i--)
     for (int j = 1; j < n; j++)
        f[i][j] = max(f[i+1][j]+w[i][j], f[i+1][j+1] + w[i][j]);

  cout<<f[1][1]<<endl;
  return 0;

}
```
