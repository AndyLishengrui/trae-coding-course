#include <bits/stdc++.h>
using namespace std;

int N, M;

int f[1005];
int s[1010][2];

int main() {
  scanf("%d%d", &N, &M);
  for (int i = 1; i <= N; i++) scanf("%d%d", &s[i][0], &s[i][1]);

  for (int k = 1; k <= N; k++)
    for (int v = M; v >= s[k][0]; v--)
      f[v] = max(f[v], f[v - s[k][0]] + s[k][1]);

  int ans = 0;
  for (int v = M; v; v--) ans = max(ans, f[v]);

  printf("%d\n", ans);

  return 0;
}