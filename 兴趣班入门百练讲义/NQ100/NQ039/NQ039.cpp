// NQ039合法标识符
#include <cstring>
#include <iostream>
using namespace std;
int main() {
  int n;
  cin >> n;

  while (n--) {
    string s;
    cin >> s;
    //判定首字符是否为数字
    if (isdigit(s[0]))
      cout << "no" << endl;
    else {
      //循环判定每个字符是否合法
      bool valid = true;
      for (auto c : s)
        if (!(isdigit(c) || (isalpha(c)) || c == '_')) {
          valid = false;
          break;
        }

      if (valid)
        cout << "yes" << endl;
      else
        cout << "no" << endl;
    }
  }
  return 0;
}
