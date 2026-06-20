#include <algorithm>
#include <cmath>
#include <iostream>
using namespace std;

const int N = 15;
long long v[N], w[N];
long long res = 0;
long long bagv;
int n;

void dfs(int st, long long used, long long value) {
  if (used > bagv || st > n) return;
  res = max(res, value);
  dfs(st + 1, used + v[st], value + w[st]);
  dfs(st + 1, used, value);
}
int main() {
  cin >> n >> bagv;
  for (int i = 0; i < n; i++) cin >> v[i] >> w[i];
  dfs(0, 0, 0);
  cout << res;
}