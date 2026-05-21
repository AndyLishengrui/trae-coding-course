// NQ029 回文数
#include <iostream>
using namespace std;

bool isPalindrome(int x) {
  if (x < 0) return false;      //负数不是回文数
  long long res = 0;
  long long oldx = x;  //把旧的x存下来
  while (x) {
    res = res * 10 + x % 10;
    x /= 10;
  }
  return res == oldx;  //判断逆转后的两个数是否相同
}

int main() {
  int n;
  while (cin >> n)

    if (isPalindrome(n))
      cout << "true" << endl;
    else
      cout << "false" << endl;
  return 0;
}
