#include <bits/stdc++.h>
using namespace std;
typedef long long lon;
const lon Lnf = 0x3f3f3f3f3f3f;
struct Dinic {
#define MXN 2100
#define MXM 10010  // 2M
  int S, M, N, T;
  struct Edge {
    bool operator<(Edge t1) { return f < t1.f; }
    int nx, to, fr;
    lon f;
  } e[MXM];
  struct edge {
    bool operator<(edge t1) { return f < t1.f; }
    int nx, to, fr;
    lon f;
  } E[MXM];

  int e_num, la[MXN], cr[MXN];
  void init(int s, int t) {
    S = s;
    T = t;
    e_num = 1;
    memset(la, 0, sizeof(int) * (N + 1));
    for (int j = 1; j <= M; j++) add(E[j].fr, E[j].to, E[j].f);
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
      while (f = dfs(S, Lnf)) {
        ans += f;
      }
    return ans;
  }

  void csh() {
    cin >> M >> N;
    for (int i = 1; i <= M; i++) scanf("%d%d%d", &E[i].fr, &E[i].to, &E[i].f);
    init(1, N);
    cout << deal();
  }
} dinic;
int main() {
  dinic.csh();
  return 0;
}