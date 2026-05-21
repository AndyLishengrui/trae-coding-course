#include <cstdio>
#include <iostream>

using namespace std;

int main()
{
  int c[20], d[20];

  for (int i = 0; i < 20; i ++ ) cin >> c[i]; 
  for (int i = 19, j = 0; i >= 0; i --, j ++ ) d[j] = c[i];

  for (int i = 0; i < 20; i ++ ) printf("N[%d] = %d\n", i, d[i]);

  return 0;
}