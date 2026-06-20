// 方法一 nlog(n)
#include <algorithm>
#include <iostream>
using namespace std;
const int N = 1000010;  // 10^5
int q[N];
int main() {
  ios::sync_with_stdio(false);  //输入输出提速
  //输入数据
  int n, k;
  cin >> n;
  for (int i = 0; i < n; i++) cin >> q[i];
  cin >> k; //读入k

  sort(q, q + n);  //排序
  //输出后k个数
  for (int j = 0; j < k; j++) cout << q[n - j - 1] << endl;
  return 0;
}