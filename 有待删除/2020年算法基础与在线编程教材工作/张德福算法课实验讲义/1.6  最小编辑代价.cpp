#include <bits/stdc++.h>
using namespace std;
template <typename AA>
inline void CMin(AA &u, AA v) {
  if (v < u) u = v;
}

int N, M;

int f[1505][1505];
char u[1505], v[1505];  // u to v
int i, e, r;

int main() {
  cin >> u + 1 >> v + 1 >> i >> e >> r;
  int lu = strlen(u + 1), lv = strlen(v + 1);

  memset(f, 0x3f, sizeof(f));
  f[0][0] = 0;
  for (int a = 1; a <= lu; a++) f[a][0] = e * a;
  for (int b = 1; b <= lv; b++) f[0][b] = i * b;

  for (int a = 1; a <= lu; a++)
    for (int b = 1; b <= lv; b++) {
      if (u[a] == v[b])
        CMin(f[a][b], f[a - 1][b - 1]);
      else
        CMin(f[a][b], f[a - 1][b - 1] + r);
      CMin(f[a][b], f[a][b - 1] + i);
      CMin(f[a][b], f[a - 1][b] + e);
    }
  cout << f[lu][lv] << endl;

  return 0;
}