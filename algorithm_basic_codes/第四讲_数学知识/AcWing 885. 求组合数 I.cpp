#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 2007, mod = 1e9+7;

int c[N][N];

void init()
{
  for (int i = 0; i<N; i++)
    for (int j = 0; j <= i; j ++ )
      if (!j) c[i][j] = 1;
      else c[i][j] = (c[i-1][j-1]+c[i-1][j]) % mod;
}

int main()
{
    int n; 
    scanf("%d", &n);
    init();
    while (n -- )
    {
      int a,b;
      scanf("%d%d", &a, &b);
      printf("%d\n",c[a][b]);
    }
    return 0;
}