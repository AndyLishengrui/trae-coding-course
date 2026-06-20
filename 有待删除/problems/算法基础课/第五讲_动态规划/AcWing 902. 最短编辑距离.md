# AcWing 902. 最短编辑距离 — 最短编辑距离

**难度:** 困难 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/902/

## 题目描述

给定两个字符串A和B，现在要将A经过若干操作变为B，可进行的操作有：

删除–将字符串A中的某个字符删除。插入–在字符串A的某个位置插入某个字符。替换–将字符串A中的某个字符替换为另一个字符。现在请你求出，将A变为B至少需要进行多少次操作。

数据范围1≤n,m≤1000

### 输入格式

第一行包含整数n，表示字符串A的长度。

第二行包含一个长度为n的字符串A。

第三行包含整数m，表示字符串B的长度。

第四行包含一个长度为m的字符串B。

字符串中均只包含大写字母。

### 输出格式

输出一个整数，表示最少操作次数。

### 样例

**输入:**
```
10 
AGTCTGACGC
11 
AGTAAGTAGGC
```

**输出:**
```
4
```

### 提示

原题链接

## AC代码

```cpp
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;
const int N = 1007;

int n,m;
char a[N],b[N];
int f[N][N];//所有將a[i]變爲b[i]的操作步驟

int main()
{
    cin>>n>>a+1;//下標從1開始
    cin>>m>>b+1;

    //初始化
    for (int i = 0; i < N; i ++ ) f[i][0] = i;//把a[i]變爲空串
    for (int i = 0; i < N; i ++ ) f[0][i] = i;//把空串變爲b[i]

    // DP
    for (int i = 1; i <=n; i++)
      for (int j = 1; j <= m; j++)
      {
        f[i][j] = min(f[i-1][j] +1, f[i][j-1]+1);
        if (a[i]==b[j]) f[i][j] = min(f[i][j], f[i-1][j-1]);
        else f[i][j] = min(f[i][j], f[i-1][j-1]+ 1);
      }

    cout<<f[n][m]<<endl;

    return 0;

}
```
