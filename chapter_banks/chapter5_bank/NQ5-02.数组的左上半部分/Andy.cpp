#include <cstdio>

int main()
{
  double a[12][12];
  char t;

  scanf("%c", &t);
  for (int i = 0; i < 12; i ++ )
      for (int j = 0; j < 12; j ++ )
       scanf("%lf", &a[i][j]);

  int c = 0;
  double s = 0;
  for (int i = 0; i < 12; i ++ )
      for (int j = 0; j <= 10 - i; j ++ )
      {
        c ++ ;
        s += a[i][j];
      }

  if (t == 'S') printf("%.1lf\n", s);
  else printf("%.1lf\n", s / c);

  return 0;
}
