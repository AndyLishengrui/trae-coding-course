#include <cstdio>
#include <iostream>

using namespace std;

int main()
{
  int n;
  cin >> n;

  while (n -- )
  {
    int x;
    cin >> x;

    int s = 0;
    for (int i = 1; i * i <= x; i ++ )
        if (x % i == 0)
        {
          if (i < x) s += i;
          if (i != x / i && x / i < x) s += x / i;
        }

    if (s == x) printf("%d is perfect\n", x);
    else printf("%d is not perfect\n", x);
  }

  return 0;
}