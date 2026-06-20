#include <bits/stdc++.h>
using namespace std;

const int Mod = 1E9 + 7;
int N;
long long f[1005][1005];

long long dfs(int lef, int eeg) {
  if (lef == 0) return 1;
  if (f[lef][eeg]) return f[lef][eeg];
  f[lef][eeg] = 0;
  for (int a = min(eeg, lef); a; a--)
    f[lef][eeg] = (f[lef][eeg] + dfs(lef - a, a)) % Mod;
  return f[lef][eeg];
}

int main() {
  memset(f, 0, sizeof(f));
  cin >> N;
  printf("%lld\n", dfs(N, N));

  return 0;
}