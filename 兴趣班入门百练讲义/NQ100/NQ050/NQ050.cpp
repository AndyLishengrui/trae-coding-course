// NQ049 排序考试
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;
int main() {
  int T;
  cin >> T;
  while (T--) {
    int n, a, i;
    cin >> n;
    //读入每组数据
    vector<int> nums;
    for (i = 0; i < n; i++) {
      cin >> a;
      nums.push_back(a);
    }
    sort(nums.begin(), nums.end());  //排序
    //循环输出数组
    for (i = 0; i < n - 1; i++) cout << nums[i] << " ";
    //换行
    cout << nums[i] << endl;
  }
  return 0;
}
