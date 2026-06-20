#include <bits/stdc++.h>
using namespace std;
const int Lnf = 1e9;
struct Dinic {
#define MXN 1300
#define MXM 10001  // 2M
#define lon int
  int S, T, N;
  struct Edge {
    int nx, to;
    lon f;
  } e[MXM];
  int e_num, la[MXN], cr[MXN];
  void init(int n, int s, int t) {
    N = n;
    S = s;
    T = t;
    e_num = 1;
    memset(la, 0, sizeof(int) * (N + 1));
  }
  void add(int fr, int to, lon f) {
    e[++e_num].to = to;
    e[e_num].nx = la[fr];
    la[fr] = e_num;
    e[e_num].f = f;
    e[++e_num].to = fr;
    e[e_num].nx = la[to];
    la[to] = e_num;
    e[e_num].f = 0;
  }
  int q[MXN], hd, tl, dep[MXN];
  int bfs() {
    memset(dep, 0, sizeof(int) * (N + 1));
    memset(cr, 0, sizeof(int) * (N + 1));
    hd = 0;
    dep[q[tl = 1] = S] = 1;
    while (++hd <= tl) {
      int now = q[hd];
      for (int nxt, eg = la[now]; eg; eg = e[eg].nx) {
        nxt = e[eg].to;
        if (dep[nxt] || !e[eg].f) continue;
        if (!cr[now]) cr[now] = eg;
        dep[nxt] = dep[now] + 1;
        q[++tl] = nxt;
        if (nxt == T) return 1;
      }
    }
    return 0;
  }
  lon dfs(int now, lon lef) {
    if (now == T || !lef) return lef;
    lon res = lef, i;
    for (int &eg = cr[now]; eg; eg = e[eg].nx) {
      if (dep[now] + 1 != dep[e[eg].to] || !e[eg].f) continue;
      i = dfs(e[eg].to, min(res, e[eg].f));
      if (i) e[eg].f -= i, e[eg ^ 1].f += i, res -= i;
    }
    return lef - res;
  }
  lon deal() {
    lon ans = 0, f;
    while (bfs())
      while (f = dfs(S, Lnf)) ans += f;
    return ans;
  }
} d;

int K, N, M;

int main() {
  cin >> M >> N;
  d.init(200, 1, N);
  for (int a = 1; a <= M; a++) {
    int f, t, c;
    cin >> f >> t >> c;
    d.add(f, t, c);
  }

  printf("%d\n", d.deal());

  return 0;
}