#include <algorithm>
#include <iostream>
using namespace std;
const int N = 1000010;
int p[N];
// int bsearch_1(int l, int r) {
//   while (l < r) {
//     int mid = l + r >> 1;
//     if (check(mid))
//       r = mid;
//     else
//       l = mid + 1;
//   }
//   return l;
// }

int bsearch_1(int l, int r, int target) {
  while (l < r) {
    int mid = l + r >> 1;
    if (p[mid] >= target)
      r = mid;  //去掉右边区间，在左区间查找
    else
      l = mid + 1;  //去掉左边区间，道右区间查找
  }
  //二分出口处判断：
  if (p[l] == target) return l;
  else
    return -1;
}

int main() {
  
  ios::sync_with_stdio(false);  //输入输出提速
  int n, t, x;
  cin >> n;
  for (int i = 0; i < n; i++) cin >> p[i];
  
  //读入t组询问
  cin >> t;
  while (t--) {
    cin >> x;
    cout << bsearch_1(0, n - 1, x) << endl;
  }
  return 0;
}
