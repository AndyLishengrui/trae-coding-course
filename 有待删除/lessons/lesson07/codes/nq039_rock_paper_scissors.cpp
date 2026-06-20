#include <cstdio>
#include <iostream>

using namespace std;

int main()
{
    int n;
    cin >> n;

    while (n -- )
    {
      string a, b;
      cin >> a >> b;

      int x, y;
      if (a == "Hunter") x = 0;
      else if (a == "Bear") x = 1;
      else x = 2;

      if (b == "Hunter") y = 0;
      else if (b == "Bear") y = 1;
      else y = 2;

      if (x == y) puts("Tie");
      else if (x == (y + 1) % 3) puts("Player1");
      else puts("Player2");
    }

  return 0;  
}