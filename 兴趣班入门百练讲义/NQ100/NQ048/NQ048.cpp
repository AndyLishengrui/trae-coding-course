// NQ048寻找多数元素
#include <iostream>

using namespace std;
int main() {
  int x, r, cnt = 0;
  while (cin >> x) {
    if (!cnt)
      r = x, cnt = 1;
    else if (r == x)
      cnt++;
    else
      cnt--;
  }
  //返回r就是多数数
  cout << r << endl;
  return 0;
}
