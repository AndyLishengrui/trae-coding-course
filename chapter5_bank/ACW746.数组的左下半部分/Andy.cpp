#include <cstdio>
#include <iostream>

using namespace std;

int main()
{
  char t;
  cin >> t;

  double m[12][12];
  for (int i = 0; i < 12; i ++ )
      for (int j = 0; j < 12; j ++ )
          cin >> m[i][j];

  double s = 0, c = 0;
  for (int i = 0; i < 12; i ++ )
      for (int j = 0; j <= i - 1; j ++ )
      {
        s += m[i][j];
        c += 1;
      }

  if (t == 'S') printf("%.1lf\n", s);
  else printf("%.1lf\n", s / c);

  return 0;
}
