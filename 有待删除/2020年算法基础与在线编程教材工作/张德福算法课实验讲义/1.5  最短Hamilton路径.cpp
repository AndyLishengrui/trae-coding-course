#include <bits/stdc++.h>
using namespace std;
template <typename AA>
inline void CMin(AA &u, AA v) {
  if (v < u) u = v;
}

int N, M;

int f[20][1 << 20], top, m[20][20];

int main() {
  scanf("%d", &N);
  for (int a = 0; a < N; a++)
    for (int b = 0; b < N; b++) scanf("%d", &m[a][b]);

  memset(f, 0x3f, sizeof(f));
  f[0][1] = 0;
  top = 1 << N;

  for (int k = 3; k < top; k += 2)
    for (int p = 1; p < N; p++)
      if (k & (1 << p)) {
        for (int i = 0; i < N; i++)
          if ((i != p) && (k & (1 << i))) {
            CMin(f[p][k], f[i][k ^ (1 << p)] + m[i][p]);
            // printf("%d %d %d\n",p,k,f[p][k]);
          }
      }

  printf("%d\n", f[N - 1][top - 1]);

  return 0;
}