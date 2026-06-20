# AcWing 91. 最短Hamilton路径

> ⚠ 此题暂未收录到XMUOJ公共题库，题面待补充
> 原题链接: https://www.acwing.com/problem/content/91/

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

const int N = 20,M = 1<<N;//M为状态数

int f[M][N];//f[i][j]不重不漏的走过集合i里面的所有点，并且结束点留在j号点的方案数的个数
int g[N][N];

int n;

int main()
{
    cin>>n;
    for (int i = 0; i < n; i++)
      for (int j = 0; j < n; j++) 
        cin>>g[i][j];

    memset(f,0x3f,sizeof f);//距离值初始化为无穷大

    //动态规划
    f[1][0] = 0;//从0点出发，抵达0点的方案数

    for (int i = 0; i < 1<<n; i++)//枚举所有的集合
     for (int j = 0; j < n; j++) //枚举所有顶点
     if (i>>j & 1)//从i从去掉第j位的剩下的集合中枚举以k位倒数第二个点的情况
        for (int k = 0; k < n; k++)
         if (i >> k & 1) 
           f[i][j] = min(f[i][j], f[i - (1 <<j)][k]+ g[k][j]);

    cout<<f[(1<<n)-1][n-1]<<endl;//包含所有点，结束在第n点的最下方案数

    return 0;
}
```
