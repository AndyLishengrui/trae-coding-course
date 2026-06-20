#include <bits/stdc++.h>
using namespace std;

int N;
char s[10][10];
int pc[10][10] = {};
int ans = 0;

int check(int u, int v) {
  int r, c;
  r = u;
  c = v;
  while (--r && s[r][c] == '.')
    if (pc[r][c]) return 0;
  r = u;
  c = v;
  while (++r <= N && s[r][c] == '.')
    if (pc[r][c]) return 0;
  r = u;
  c = v;
  while (--c && s[r][c] == '.')
    if (pc[r][c]) return 0;
  r = u;
  c = v;
  while (++c <= N && s[r][c] == '.')
    if (pc[r][c]) return 0;
  return 1;
}

void dfs(int u, int v, int dep) {
  if (v > N) {
    u++;
    v = 1;
  }
  if (u == N + 1) {
    ans = max(ans, dep);
    return;
  }

  if (s[u][v] == 'X')
    dfs(u, v + 1, dep);
  else {
    if (check(u, v)) {
      pc[u][v] = 1;
      dfs(u, v + 1, dep + 1);
    }
    pc[u][v] = 0;
    dfs(u, v + 1, dep);
  }
}

int main() {
  cin >> N;
  for (int a = 1; a <= N; a++) cin >> s[a] + 1;

  dfs(1, 1, 0);

  cout << ans << endl;

  return 0;
}