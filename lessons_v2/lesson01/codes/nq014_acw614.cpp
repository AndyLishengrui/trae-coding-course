#include <iostream>

using namespace std;

int main()
{
  int a, b, c;
  cin >> a >> b >> c;

  int t = (a + b + abs(a - b)) / 2;
  int r = (t + c + abs(t - c)) / 2;

  cout << r << " eh o maior" << endl;

  return 0;

}