#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 207,INF = 0x3f3f3f3f;

int n,m,k;//k组询问
int d[N][N];

void floyd()
{
  //用动态规划分析得出这个递推公式，使用三重循环
  for (int k = 1; k <=n; k++)
   for (int i = 1; i <=n; i++)
    for (int j = 1; j <= n; j ++ )
      d[i][j] = min(d[i][j], d[i][k]+d[k][j]);
}

int main()
{
    scanf("%d%d%d", &n, &m, &k);

    for (int i = 1; i <= n; i ++ )
     for (int j = 1; j <= n; j ++ )
       if (i==j) d[i][j] = 0;
       else d[i][j] = INF;

    //处理每条边，去掉重边和自环
    while (m -- )
    {
      int a,b,c;
      scanf("%d%d%d", &a, &b, &c);
      d[a][b] = min(d[a][b],c);
    }

    floyd();

    //k组查询
    while(k--)
    {
      int a,b;
      scanf("%d%d", &a, &b);
      int t = d[a][b];
      if (t > INF /2) puts("impossible");
      else printf("%d\n",t);
    }

    return 0;
}