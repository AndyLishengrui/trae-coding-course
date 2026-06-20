#include <bits/stdc++.h>
using namespace std;

int N;

int f[1005][1005];
char u[10005], v[10005];

int main() {
  scanf("%d%s%s", &N, u + 1, v + 1);

  for (int i = 1; i <= N; i++)
    for (int j = 1; j <= N; j++)
      if (u[i] == v[j])
        f[i][j] = f[i - 1][j - 1] + 1;
      else
        f[i][j] = max(f[i - 1][j], f[i][j - 1]);

  printf("%d\n", f[N][N]);

  return 0;
}