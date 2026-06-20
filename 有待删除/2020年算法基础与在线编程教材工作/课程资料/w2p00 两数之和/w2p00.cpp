#include <iostream>
#include <vector>
using namespace std;
int main() {
 int target, n, x;
  cin >> target >> n;   //读入第一行
  vector<int> nums(n);  //一维数组大小为n
  for (int i = 0; i < n; i++) cin >> nums[i];

  //双指针算法 i < j
  for (int i = 0, j = n - 1; i <= j; i++) {
    while (j > i && nums[i] + nums[j] > target) j--;

    if (nums[i] + nums[j] == target) {
      cout << i << " " << j << endl;
      break;
    }
  }
  return 0;
}
