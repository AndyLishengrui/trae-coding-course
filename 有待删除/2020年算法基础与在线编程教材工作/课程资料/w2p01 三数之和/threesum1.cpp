#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;
vector<vector<int>> threeSum0(vector<int>& nums, int target) {
  vector<vector<int>> res;
  //暴力枚举
  for (int k = 2; k < nums.size(); k++)
    for (int j = 1; j < k; j++)
      for (int i = 0; i < j; i++)
        if (nums[i] + nums[j] + nums[k] == target) {
          res.push_back({nums[i], nums[j], nums[k]});
        }
  return res;
}

bool comp(vector<int>& a, vector<int>& b) {
  if (a[0] < b[0])
    return true;
  else if (a[0] == b[0] && a[1] < b[1])
    return true;
  else  ///这里的else return false非常重要！！！！！
    return false;
}
vector<vector<int>> threeSum(vector<int> &nums, int target) {
  vector<vector<int>> res;
  //双指针做法
  // 1.排序
  sort(nums.begin(), nums.end());
  // 2.双指针,3重循环i,j,k 要求 i<j<k
  for (int i = 0; i < nums.size(); i++) {
    //跳过重复项
    if (i && nums[i] == nums[i - 1]) continue;
    //双指针循环
    for (int j = i + 1, k = nums.size() - 1; j < k; j++) {
      //跳过重复项
      if (j > i + 1 && nums[j] == nums[j - 1]) continue;
      //预判下一个数，如果下一个数k与j没有重叠，并且下一个数满足nums[i]+num[j]+nums[k-1]>=0
      //移动k指针 k--
      while (j < k - 1 && nums[i] + nums[j] + nums[k - 1] >= target) k--;
      //判断是否找到和为0的三个数
      if (nums[i] + nums[j] + nums[k] == target)
        res.push_back({nums[i], nums[j], nums[k]});
    }
  }
  return res;
}
int main() {
  int target, n, x;
  cin >> target >> n;   //读入第一行
  vector<int> nums(n);  //一维数组大小为n
  for (int i = 0; i < n; i++) cin >> nums[i];

  //双指针
  vector<vector<int>> res; //三元组存储在res中
  res = threeSum(nums, target); //调用threeSum求出所有三元组

  sort(res.begin(), res.end(), comp); //排序找到的三元组

  for (auto line : res) //输出所有的三元组
    cout << line[0] << " " << line[1] << " " << line[2] << endl;
  return 0;
}
