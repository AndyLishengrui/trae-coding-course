#include <bits/stdc++.h>
using namespace std;

int N, m[1000][1000], ans = 0;
int ok[1000], w[1000];

int main() {
  cin >> N;
  memset(w, 0x3f, sizeof(w));
  for (int a = 1; a <= N; a++)
    for (int b = 1; b <= N; b++) cin >> m[a][b];

  w[1] = 0;
  for (int t = 1; t <= N; t++) {
    int mv = 0x3f3f3f3f, mp = 0;
    for (int a = 1; a <= N; a++)
      if (!ok[a] && w[a] < mv) {
        mv = w[a];
        mp = a;
      }
    ok[mp] = 1;
    ans += mv;
    for (int b = 1; b <= N; b++)
      if (!ok[b] && w[b] > m[mp][b]) {
        w[b] = m[mp][b];
      }
  }
  cout << ans << endl;

  return 0;
}