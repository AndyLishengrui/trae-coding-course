#include <iostream>

using namespace std;

int main()
{
    int a, b, c;
    cin >> a >> b >> c;

    int x = a, y = b, z = c;

    if (b < a)
    {
      int t = a;
      a = b;
      b = t;
    }
    if (c < a)
    {
      int t = a;
      a = c;
      c = t;
    }
    if (c < b)
    {
      int t = b;
      b = c;
      c = t;
    }

    cout << a << endl << b << endl << c << endl << endl;
    cout << x << endl << y << endl << z << endl;

    return 0;
}