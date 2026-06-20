#include <cstdio>

int main()
{
  char t;
  scanf("%c", &t);
  double a[12][12];

  for (int i = 0; i < 12; i ++ )
      for (int j = 0; j < 12; j ++ )
          scanf("%lf", &a[i][j]);

  int c = 0;
  double s = 0;

  for (int i = 0; i < 12; i ++ )
      for (int j = i + 1; j < 12; j ++ )
      {
        c ++ ;
        s += a[i][j];
      }

  if (t == 'S') printf("%.1lf\n", s);
  else printf("%.1lf\n", s / c);

  return 0;
}