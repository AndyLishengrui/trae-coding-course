#include <algorithm>  //算法库
#include <iostream>   //输入输出库

using namespace std;
const int N = 100010;
int p[N];
int main() {
  ios::sync_with_stdio(false);  //输入输出提速
  int n;
  cin >> n;
  for (int i = 0; i < n; i++) cin >> p[i];
  sort(p, p + n);  //直接排序
  for (int i = 0; i < n; i++) cout << p[i] << " ";
  cout << endl;
}