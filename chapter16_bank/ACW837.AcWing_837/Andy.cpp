#include <cstdio>
const int N = 100007;
int p[N], sz[N];
int n;

int find(int x)
{
  while (p[x] != x) {
    p[x] = p[p[x]];
    x = p[x];
  }
  return x;
}

int main()
{
  int m;
  scanf("%d%d", &n, &m);
  for (int i = 1; i <= n; i++) { p[i] = i; sz[i] = 1; }
  while (m--) {
    char op[4];
    scanf("%s", op);
    if (op[0] == 'C') {
      int a, b;
      scanf("%d%d", &a, &b);
      int ra = find(a), rb = find(b);
      if (ra != rb) { p[ra] = rb; sz[rb] += sz[ra]; }
    } else if (op[1] == '1') {
      int a, b;
      scanf("%d%d", &a, &b);
      puts(find(a) == find(b) ? "Yes" : "No");
    } else {
      int a;
      scanf("%d", &a);
      printf("%d\n", sz[find(a)]);
    }
  }
  return 0;
}
