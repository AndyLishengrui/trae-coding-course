// NQ034 求小数点后的数
#include <iostream>
using namespace std;

int main() {
  int n;
  cin >> n;
  while (n--) { // 循环n次
    double a;
    int t;
    cin >> a >> t;
    // 循环t次，每次将a乘以10
    while (t--) a *= 10.0;
    // 将a转化为整数后取模10，并输出
    cout << int(a) % 10 << endl;
  }
  return 0;
}