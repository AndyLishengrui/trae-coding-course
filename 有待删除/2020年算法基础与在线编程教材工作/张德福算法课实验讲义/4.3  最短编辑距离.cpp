#include <bits/stdc++.h>
using namespace std;

int N, M;
char s[1010], t[1010];
int f[1010][1010];

int main() {
  cin >> N >> s + 1 >> M >> t + 1;
  memset(f, 0x3f, sizeof(f));
  f[0][0] = 0;

  for (int a = 1; a <= N; a++)
    for (int b = 1; b <= M; b++) {
      f[a][b] = min(min(f[a - 1][b] + 1, f[a][b - 1] + 1),
                    f[a - 1][b - 1] + (s[a] != t[b]));
    }
  cout << f[N][M] << endl;

  return 0;
}