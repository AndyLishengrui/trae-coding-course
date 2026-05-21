// NQ037 最长回文子串
#include <cstring>
#include <iostream>
using namespace std;

string longestPalindrome(string s) {
  string res;  // 结果字符串

  for (int i = 0; i < s.size(); i++) {
    // 奇数长度回文子串扩展
    int l = i - 1, r = i + 1;
    while (l >= 0 && r < s.size() && s[l] == s[r]) l--, r++;
    if (res.size() < r - l - 1) res = s.substr(l + 1, r - l - 1);

    // 偶数长度回文子串扩展
    l = i; r = i + 1;
    while (l >= 0 && r < s.size() && s[l] == s[r]) l--, r++;
    if (res.size() < r - l - 1) res = s.substr(l + 1, r - l - 1);
  }
  return res;
}

int main() {
  string s;
  cin >> s;
  cout << longestPalindrome(s) << endl;
  return 0;
}