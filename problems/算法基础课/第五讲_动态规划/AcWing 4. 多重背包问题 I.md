# AcWing 4. 多重背包问题 I

> ⚠ 此题暂未收录到XMUOJ公共题库，题面待补充
> 原题链接: https://www.acwing.com/problem/content/4/

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
//二维枚举方法，没有降维优化
#include <iostream>
#include <algorithm>

using namespace std;

const int N=107;//100个物品

int n,m;
int v[N],w[N],s[N];//体积，重量，个数
int f[N][N];//f[i][j]=max(f[i-1][j-v[i]*k]+w[i]*k); k=0,1,2,...,s[i]

int main(){
    cin>>n>>m;

    for(int i=1; i<=n; i++) cin>>v[i]>>w[i]>>s[i];//输入

    for(int i=1; i<=n; i++)
       for(int j=0; j<=m; j++)//从小到大搜索
         for(int k=0; k<=s[i]&& k*v[i] <=j; k++)//物品个数从0开始枚举
           f[i][j] =max(f[i][j], f[i-1][j-v[i]*k]+w[i]*k);

   cout<<f[n][m]<<endl;
   return 0;
}
```
