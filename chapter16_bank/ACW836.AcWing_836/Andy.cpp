#include <cstdio>
const int N = 100007;
int p[N];
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
  for (int i = 1; i <= n; i++) p[i] = i;
  while (m--) {
    char op;
    int a, b;
    scanf(" %c%d%d", &op, &a, &b);
    if (op == 'M') p[find(a)] = find(b);
    else puts(find(a) == find(b) ? "Yes" : "No");
  }
  return 0;
}
