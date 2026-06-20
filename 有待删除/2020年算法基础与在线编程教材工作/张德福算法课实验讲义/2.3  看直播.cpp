#include <bits/stdc++.h>
using namespace std;

int N;
struct rg {
  int l, r;
  bool operator<(const rg &x) const { return r < x.r; }
} s[1000];

int main() {
  while (~scanf("%d", &N) && N) {
    for (int a = 1; a <= N; a++) scanf("%d%d", &s[a].l, &s[a].r);
    sort(s + 1, s + 1 + N);
    int bd = -2147483637, ans = 0;
    for (int a = 1; a <= N; a++) {
      if (s[a].l < bd) continue;
      ans++;
      bd = s[a].r;
    }
    printf("%d\n", ans);
  }

  return 0;
}