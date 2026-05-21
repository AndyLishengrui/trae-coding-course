// NQ038 数字字符统计
#include <cstring>
#include <iostream>
using namespace std;
int main() {
  int n;
  cin >> n;

  while (n--) {
    string s;
    cin >> s;
    //循环统计数字个数
    int cnt = 0;
    for (auto c : s)
      if (isdigit(c)) cnt++;
    //输出字符个数
    cout << cnt << endl;
  }
  return 0;
}