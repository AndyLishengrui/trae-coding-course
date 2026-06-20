#include <iostream>
using namespace std;
#define ll long long
ll qsm(ll a, ll b, ll p) {
  // b = 0 则 qsm(a,0,p) = 1;
  if (b == 0) return 1;
  // b = 1 的情况
  if (b == 1) return a % p;
  //先求偶数时候b/2的快速幂值
  ll res = qsm(a, b >> 1, p);
  // 偶数情况
  if (b % 2 == 0)
    return res * res % p;
  else  //奇数情况为偶数情况乘a再取模
    return (((res * res) % p) * a) % p;
}
int main() {
  int n;
  cin >> n;
  while (n--) {
    int a, b, p;
    cin >> a >> b >> p;
    cout << qsm(a, b, p) << endl;
  }
  return 0;
}
