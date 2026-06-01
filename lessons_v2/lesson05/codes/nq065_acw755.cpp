#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    int n;
    while (cin >> n, n)
    {
      for (int i = 0; i < n; i ++ )
      {
        for (int j = 0; j < n; j ++ )
        {
          int v = 1;
          for (int k = 0; k < i + j; k ++ ) v *= 2;
          cout << v << ' ';
        }
        cout << endl;
      }

      cout << endl;
    }

    return 0;
}
