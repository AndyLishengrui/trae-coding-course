// NQ019 最大公约数
#include <iostream>
using namespace std;

// 利用欧几里得算法：gcd(a , b) == gcd(b,a mod b)
int gcd(int a, int b) { return b ? gcd(b, a % b) : a; }

int main() {
  int n;
  cin >> n;
  while (n--) {
    int a, b;
    cin >> a >> b;
    cout << gcd(a, b) << endl;
  }
  return 0;
}