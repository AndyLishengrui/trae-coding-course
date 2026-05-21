#include <cstdio>
#include <iostream>

using namespace std;

int main()
{
  string name;
  cin >> name;

  double x, y;
  cin >> x >> y;

  printf("TOTAL = R$ %.2lf\n", x + y * 0.15);

  return 0;
}