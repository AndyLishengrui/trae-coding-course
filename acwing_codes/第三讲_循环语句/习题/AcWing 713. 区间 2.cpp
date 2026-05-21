#include <iostream>

using namespace std;

int main()
{
  int n;
  cin >> n;

  int x = 0, y = 0;
  while (n -- )
  {
    int t;
    cin >> t;
    if (t >= 10 && t <= 20) x ++ ;
    else y ++ ;
  }

  cout << x << " in" << endl;
  cout << y << " out" << endl;

  return 0;
}