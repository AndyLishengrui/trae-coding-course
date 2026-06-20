#include <bits/stdc++.h>
using namespace std;

int T;
int N, M, P, Q;
int hv_y[1010];
int e_num, la[1010], to[200020], nx[200020], wi[200020];
void add(int u, int v, int t) {
  to[++e_num] = v;
  nx[e_num] = la[u];
  la[u] = e_num;
  wi[e_num] = t;
}
int dis[1010], ok[1010];

int Dij(int ben) {
  memset(dis, 0x3f, sizeof(dis));
  memset(ok, 0, sizeof(ok));
  dis[ben] = 0;
  for (int t = 1; t <= M; t++) {
    int mv = 0x3f3f3f3f, mp = 0;
    for (int a = 1; a <= M; a++)
      if (!ok[a] && mv > dis[a]) {
        mv = dis[a];
        mp = a;
      }
    if (!mp) break;
    ok[mp] = 1;
    for (int nxt, eg = la[mp]; eg; eg = nx[eg]) {
      nxt = to[eg];
      if (ok[nxt]) continue;
      dis[nxt] = min(dis[nxt], mv + wi[eg]);
    }
  }

  int ans = 0x3f3f3f3f;
  for (int a = 1; a <= M; a++)
    if (hv_y[a]) ans = min(ans, dis[a]);
  return ans;
}

int main() {
  scanf("%d", &T);
  while (T--) {
    scanf("%d%d%d%d", &N, &M, &P, &Q);

    memset(hv_y, 0, sizeof(hv_y));
    for (int a = 1; a <= N; a++) {
      int t;
      scanf("%d", &t);
      hv_y[t] = 1;
    }

    e_num = 0;
    memset(la, 0, sizeof(la));
    for (int a = 1; a <= P; a++) {
      int u, v, t;
      scanf("%d%d%d", &u, &v, &t);
      add(u, v, t);
      add(v, u, t);
    }

    printf("%d\n", Dij(Q));
  }

  return 0;
}