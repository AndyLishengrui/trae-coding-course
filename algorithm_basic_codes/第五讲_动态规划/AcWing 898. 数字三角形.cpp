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