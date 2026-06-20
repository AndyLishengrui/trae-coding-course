#include <cstdio>

int main()
{
  double a[12][12];

  int l;
  char t;
  scanf("%d\n%c", &l, &t);

  for (int i = 0; i < 12; i ++ )
      for (int j = 0; j < 12; j ++ )
          scanf("%lf", &a[i][j]);

  double s = 0;
  for (int i = 0; i < 12; i ++ ) s += a[l][i];

  if (t == 'S') printf("%.1lf\n", s);
  else printf("%.1lf\n", s / 12);

  return 0;        
}