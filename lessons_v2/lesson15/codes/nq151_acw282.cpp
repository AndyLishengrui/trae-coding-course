#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 307;

int n;
int s[N]; //前缀和
int f[N][N]; //所有将[i,j]合并成一堆的方案数

int main()
{
    cin>>n;
    for (int i = 1; i <=n; i ++) cin>>s[i], s[i] += s[i-1];//计算前缀和

    //区间DP，先枚举长度，后枚举端点
    for (int len = 2; len <= n; len ++)
     for (int i = 1; i+len-1 <= n; i++)//区间左端点
     {
       //区间右端点
       int j = i + len -1;
       f[i][j] = 1e9;//初始化为无穷大
       for (int k = i ; k < j; k++)//区间dp，枚举分隔点
         f[i][j] = min(f[i][j], f[i][k]+f[k+1][j]+s[j]-s[i-1]);
     }

     cout<<f[1][n]<<endl;
     return 0;
}
