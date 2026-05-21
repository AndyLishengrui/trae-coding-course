#include <iostream>

using namespace std;
int a[100];

int main()
{
  int maxa = -1;
  int index = -1;
  for (int i = 0; i < 100; i ++) 
  {
    cin >> a[i];

    if (a[i] > maxa) 
    {
      maxa = a[i];
      index = i;
    }
  }

  cout << maxa << endl;
  cout << index+1 << endl;

  return 0;
}