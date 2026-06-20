// w4p01 爬天梯(记忆化搜索)
#include <iostream>
#include <vector>
using namespace std;
const int N = 1000000, MOD = 1000000007;
int a[N];  //搜索备忘录
int stairs(int n) {
  if (a[n] != 0) return a[n];  //查表
  if (n <= 1) return 1;
  a[n] = stairs(n - 1) + stairs(n - 2);  //写表
  a[n] %= MOD;
  return a[n];
}
int main() {
  int n;
  cin >> n;
  cout << stairs(n) << endl;
  return 0;
}
