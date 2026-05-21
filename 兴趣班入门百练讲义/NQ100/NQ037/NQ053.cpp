//NQ053数列的绝对值排序
#include <algorithm>
#include <cmath>
#include <iostream>
using namespace std;
//定义比较函数
bool less_abs(int a, int b) { return abs(a) > abs(b); }
int main() {
  int n;
  cin >> n;
  while (n--) {
    int m;
    cin >> m;
    vector<int> nums;
    for (int i = 0; i < m; i++) {
      int x;
      cin >> x;
      nums.push_back(x);
    }
    //排序
    sort(nums.begin(), nums.end(), less_abs);
    //输出
    for (int i = 0; i < m - 1; i++) cout << nums[i] << " ";
    cout << nums[m - 1] << endl;
  }
  return 0;
}
