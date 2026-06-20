#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;
vector<vector<int>> fourSum(vector<int>& nums, int target) {
  vector<vector<int>> res;                                   //答案数组
  sort(nums.begin(), nums.end());                            //排序
  nums.erase(unique(nums.begin(), nums.end()), nums.end());  //去重

  //四重循环，后两重用双指针算法 i,j,k,l
  for (int i = 0; i < nums.size(); i++) {
    for (int j = i + 1; j < nums.size(); j++) {
      //双指针算法
      for (int k = j + 1, l = nums.size() - 1; k < l; k++) {
        while (k < l - 1 && nums[i] + nums[j] + nums[k] + nums[l - 1] >= target)
          l--;                                                //找到最小的l
        if (nums[i] + nums[j] + nums[k] + nums[l] == target)  //找到一组解
          res.push_back({nums[i], nums[j], nums[k], nums[l]});
      }
    }
  }
  return res;
}
//四元组的比较函数
bool comp(vector<int>& a, vector<int>& b) {
  if (a[0] < b[0])
    return true;
  else if (a[0] == b[0] && a[1] < b[1])
    return true;
  else if (a[0] == b[0] && a[1] == b[1] && a[2] < b[2])
    return true;
  else if (a[0] == b[0] && a[1] == b[1] && a[2] == b[2] && a[3] < b[3])
    return true;
  else
    return false;
}

int main() {
  //输入数据
  int target, n, x;
  cin >> target >> n;
  vector<int> nums(n);
  for (int i = 0; i < n; i++) cin >> nums[i];

  //寻找四元组
  vector<vector<int>> res;
  res = fourSum(nums, target);

  //输出四元组
  sort(res.begin(), res.end(), comp);
  for (auto line : res)
    cout << line[0] << " " << line[1] << " " << line[2] << " " << line[3]
         << endl;

  return 0;
}
