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