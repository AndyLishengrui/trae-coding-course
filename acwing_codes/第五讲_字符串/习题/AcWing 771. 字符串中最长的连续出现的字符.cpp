#include <iostream>

using namespace std;

int main()
{
    int n;
    cin >> n;

    while (n -- )
    {
      string str;
      cin >> str;

      int cnt = 0;
      char c;

      for (int i = 0; i < str.size(); i ++ )
      {
        int j = i;
        while (j < str.size() && str[j] == str[i]) j ++ ;
        if (j - i > cnt) cnt = j - i, c = str[i];
        i = j - 1;
      }

      cout << c << ' ' << cnt << endl;
    }

    return 0;
}