#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int N= 1007;
// 2维的解法
int n,m;
int f[N][N];
int v[N],w[N];

int main()
{
  cin>>n>>m;//读入N,V
  //读入v,w
  for (int i = 1; i <= n; i++) cin>>v[i]>>w[i];
  //朴素的二维dp
  for (int i = 1; i <= n; i++)
    for (int j = 0; j <=m; j++)
    {
      f[i][j]=f[i-1][j];
      if ( j >= v[i]) //剩余体积大于第i项的体积
      f[i][j] = max(f[i][j],f[i-1][j-v[i]]+w[i]);
    }
  //根据定义，从前n个物品中，选取总体积不超过m的选法集合f[n][m]就是答案
  cout<<f[n][m]<<endl;
}
