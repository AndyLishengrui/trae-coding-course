// code by melacau
#include <bits/stdc++.h>
using namespace std;

bool a[6][7], p[6][8];

bool check() {
  for (int i = 1; i < 5; ++i)
    for (int j = 1; j <= 6; ++j)
      p[i + 1][j] = p[i][j] ^ a[i][j] ^ p[i - 1][j] ^ p[i][j - 1] ^ p[i][j + 1];
  for (int i = 5, j = 1; j <= 6; ++j)
    if (p[i][j] ^ a[i][j] ^ p[i - 1][j] ^ p[i][j - 1] ^ p[i][j + 1]) return 0;
  for (int i = 1; i <= 5; ++i) {
    for (int j = 1; j <= 6; ++j) cout << p[i][j] << ' ';
    cout << endl;
  }
  return 1;
}

int main() {
  int T, t = 1;
  for (cin >> T; t <= T; ++t) {
    cout << "PUZZLE #" << t << endl;
    for (int i = 1; i <= 5; ++i)
      for (int j = 1; j <= 6; ++j) cin >> a[i][j];
    for (int s = 0; s < 64; ++s) {
      for (int j = 0; j < 6; ++j) p[1][j + 1] = s >> j & 1;
      if (check()) break;
    }
  }
}