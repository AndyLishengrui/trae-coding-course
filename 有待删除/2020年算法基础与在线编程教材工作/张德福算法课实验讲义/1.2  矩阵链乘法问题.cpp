#include <algorithm>
#include <iostream>
using namespace std;
const int N = 1110, M = 3000;
int a[N], b[N], f[M][M];
int main() {
  int n;
  cin >> n;
  a[0] = 1;
  for (int j = 0; j < n; ++j) cin >> a[j] >> b[j];
  a[n] = b[n - 1];
  for (int r = 2; r <= n; ++r) {
    for (int i = 1; i <= n - r + 1; ++i) {
      int j = r + i - 1;
      f[i][j] = f[i][i] + f[i + 1][j] + a[i - 1] * a[i] * a[j];
      for (int k = i + 1; k < j; ++k)
        f[i][j] = min(f[i][j], f[i][k] + f[k + 1][j] + a[i - 1] * a[k] * a[j]);
    }
  }
  cout << f[1][n] << endl;
  return 0;
}