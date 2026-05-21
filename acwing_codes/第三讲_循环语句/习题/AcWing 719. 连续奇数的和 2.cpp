#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
  int n;
  cin >> n;

  while (n -- )
  {
    int x, y;
    cin >> x >> y;

    if (x > y) swap(x, y);

    int s = 0;
    for (int i = x + 1; i < y; i ++ )
        if (i % 2)
           s += i;
    cout << s << endl;       
  }

  return 0;
}