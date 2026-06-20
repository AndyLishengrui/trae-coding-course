#include <bits/stdc++.h>
using namespace std;

int T;
int N;
vector<pair<int, int> > e[55];
int cnt;
int vis[55];

int best;
int ph[55], np[55];

void dfs(int now, int dep, int sum) {
  cnt++;
  if (cnt >= 1e7) return;

  np[dep] = now;

  if (dep == N) {
    if (sum < best) {
      best = sum;
      memcpy(ph, np, sizeof(ph));
    }
    return;
  }
  vis[now] = 1;
  for (int a = 0; a < N - 1; a++) {
    int to = e[now][a].second, wi = e[now][a].first;
    if (!vis[to]) {
      dfs(to, dep + 1, sum + wi);
    }
  }
  vis[now] = 0;
}

int main() {
  while (scanf("%d", &T) != EOF) {
    printf("%d\n", T);

    cnt = 0;
    best = 1E9;
    memset(vis, 0, sizeof(vis));

    scanf("%d", &N);
    for (int a = 1; a <= N; a++) {
      e[a].clear();
      for (int b = 1; b <= N; b++) {
        int t;
        scanf("%d", &t);
        if (a != b) e[a].emplace_back(t, b);
      }
    }

    for (int a = 1; a <= N; a++) sort(e[a].begin(), e[a].end());

    for (int a = 1; a <= N; a++) dfs(a, 1, 0);

    for (int a = 1; a < N; a++) printf("%d ", ph[a]);
    printf("%d\n", ph[N]);
  }

  return 0;
}