# AcWing 3. 完全背包问题

> ⚠ 此题暂未收录到XMUOJ公共题库，题面待补充
> 原题链接: https://www.acwing.com/problem/content/3/

## 题目描述
> 待补充

### 输入格式
> 待补充

### 输出格式
> 待补充

### 样例
> 待补充

## AC代码

```cpp
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 1007;

int n,m;
int f[N][N];
int v[N],w[N];

int main()
{
    cin >>n >>m;
    for (int i = 1; i <= n; i++) cin>>v[i]>>w[i];

    //完全背包
    // 1.f[i][j] = f[i-1][j];(不选物品i)
    // 2.f[i][j]= max(f[i-1][j], f[i][j-v]+w)(选若干个物品i)
    for (int i = 1; i <= n; i++)
      for (int j=0; j <= m; j ++)
      {
        f[i][j]=f[i-1][j];
        if (j >= v[i])
          f[i][j] = max(f[i-1][j], f[i][j-v[i]]+w[i]);
      }


    cout<<f[n][m]<<endl;
    return 0;
}
```
