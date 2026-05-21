#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> fourSum(vector<int>& nums, int target) {
  vector<vector<int>> res;
  sort(nums.begin(), nums.end());

  // 遍历数组nums
  for (int i = 0; i < nums.size(); i++) {
    // 如果当前元素与前一个元素相同，则跳过
    if (i && nums[i] == nums[i - 1]) continue;

    // 从当前元素的后一个位置开始遍历
    for (int j = i + 1; j < nums.size(); j++) {
      // 如果当前元素与前一个元素相同，则跳过
      if (j > i + 1 && nums[j] == nums[j - 1]) continue;

      // 定义左右指针k和l
      for (int k = j + 1, l = nums.size() - 1; k < l; k++) {
        // 如果当前元素与前一个元素相同，则跳过
        if (k > j + 1 && nums[k] == nums[k - 1]) continue;

        // 当四个数的和大于目标值时，左指针右移
        while (l > k && nums[i] + nums[j] + nums[k] + nums[l] > target) {
          l--;
        }

        // 如果左指针等于右指针，则跳出内层循环
        if (l == k) break; // 避免重复

        // 如果四个数的和等于目标值，则将结果加入res中
        if (nums[i] + nums[j] + nums[k] + nums[l] == target) {
          res.push_back({nums[i], nums[j], nums[k], nums[l]});
        }
      }
    }
  }

  return res;
}



bool comp(vector<int>& a, vector<int>& b) {
  if (a[0] < b[0]) return true;
  if (a[0] == b[0] && a[1] < b[1]) return true;
  if (a[0] == b[0] && a[1] == b[1] && a[2] < b[2]) return true;
  return false;
}

int main() {
  int target, n, x;
  vector<int> a;
  vector<vector<int>> res;
  cin >> target >> n;
  for (int i = 0; i < n; i++) {
    cin >> x;
    a.push_back(x);
  }
  res = fourSum(a, target);
  sort(res.begin(), res.end(), comp);
  for (auto& line : res) {
    cout << line[0] << " " << line[1] << " " << line[2] << " " << line[3] << endl;
  }
  return 0;
}