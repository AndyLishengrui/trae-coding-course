#include <cstdio>

int main()
{
  int a, b;
  scanf("%d%d", &a, &b);

  int res;
  if (a < b) res = b - a;
  else  res = b - a + 24;

  printf("O JOGO DUROU %d HORA(S)\n", res);

  return 0;
}