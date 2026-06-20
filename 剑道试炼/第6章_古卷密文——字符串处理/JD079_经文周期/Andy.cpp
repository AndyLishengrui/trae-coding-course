#include <iostream>

using namespace std;

// 经文周期：找字符串最小重复周期
int main()
{
    string str;

    while (cin >> str, str != ".")
    {
      int len = str.size();

      for (int n = len; n; n -- )
          if (len % n == 0)
          {
            int m = len / n;
            string s = str.substr(0, m);
            string r;
            for (int i = 0; i < n; i ++ ) r += s;

            if (r == str)
            {
              cout << n << endl;
              break;
            }
          }
    }

    return 0;
}
