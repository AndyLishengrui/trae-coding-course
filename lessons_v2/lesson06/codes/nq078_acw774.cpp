#include <iostream>

using namespace std;

int main()
{
    string res, str;

    while (cin >> str)
    {
      if (str.back() == '.') str.pop_back();
      if (str.size() > res.size()) res = str;
    }

    cout << res << endl;

    return 0;
}
