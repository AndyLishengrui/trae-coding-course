#include <iostream>

using namespace std;

const int N = 200;

int n;
string str[N];

int main()
{
    while (cin >> n, n)
    {
      int len = 1000;
      for (int i = 0; i < n; i ++ )
      {
        cin >> str[i];
        if (len > str[i].size()) len = str[i].size();
      }

      while (len)
      {
        bool success = true;
        for (int i = 1; i < n; i ++ )
        {
          bool is_same = true;
          for (int j = 1; j <= len; j ++ )
              if (str[0][str[0].size() - j] != str[i][str[i].size() - j])
              {
                is_same = false;
                break;
              }
          if (!is_same)
          {
            success = false;
            break;
          }
        }

        if (success) break;
        len -- ;
      }

      cout << str[0].substr(str[0].size() - len) << endl;
    }

    return 0;
}