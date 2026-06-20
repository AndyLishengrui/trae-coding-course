#include <iostream>
#include <vector>
using namespace std;
int main() {
  int target, n, x;
  cin >> target >> n;   //读入第一行
  vector<int> nums(n);  //一维数组大小为n
  for (int i = 0; i < n; i++) cin >> nums[i];

  //暴力枚举
  for (int j = 0; j < nums.size(); j++)
    for (int i = 0; i < j; i++) {
      if (nums[i] + nums[j] == target) {
        cout << i << " " << j << endl;  //输出下标
        break;
      }
    }
  return 0;
}
