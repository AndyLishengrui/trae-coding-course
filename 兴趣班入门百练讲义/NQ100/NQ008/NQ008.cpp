// NQ008 求数列中奇数之积
#include <iostream>
using namespace std;

int main() {
  int m;
  while (cin >> m) {
    long long x, res = 1;
    for (int i = 0; i < m; i++) {
      cin >> x;
      if (x % 2) res *= x;  //如果是奇数就累乘
    }
    cout << res << endl;  //输出结果
  }
  return 0;
}