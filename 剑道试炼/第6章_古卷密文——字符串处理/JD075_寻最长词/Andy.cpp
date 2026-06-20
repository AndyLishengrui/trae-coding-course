#include <iostream>

using namespace std;

// 寻最长词：找出最长的单词
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
