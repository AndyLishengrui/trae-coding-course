#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> threeSum(vector<int>& nums, int target) {
  vector<vector<int>> res;
  //双指针做法
  // 1.排序
  sort(nums.begin(), nums.end());
  nums.erase(unique(nums.begin(),nums.end()),nums.end());//去重
  
  // 2.双指针,3重循环i,j,k 要求 i<j<k
  for (int i = 0; i < nums.size(); i++) {    
    //双指针循环
    for (int j = i + 1, k = nums.size() - 1; j < k; j++) {      
      //预判下一个数，如果下一个数k与j没有重叠，并且下一个数满足
      // nums[i]+num[j]+nums[k-1]>=target 则移动k指针 k--
      while (j < k - 1 && nums[i] + nums[j] + nums[k - 1] >= target) k--;
      //判断是否找到和为target的三个数
      if (nums[i] + nums[j] + nums[k] == target)
        res.push_back({nums[i], nums[j], nums[k]});
    }
  }
  return res;
}

bool comp(vector<int>& a, vector<int>& b) {
  if (a[0] < b[0])
    return true;
  else if (a[0] == b[0] && a[1] < b[1])
    return true;
  else if (a[0] == b[0] && a[1] == b[1] && a[2] < b[2])
    return true;
  else  ///这里的else return false非常重要！！！！！
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
  //寻找三元组
  res = threeSum(a, target);
  //输出三元组
  sort(res.begin(), res.end(), comp);
  for (auto line : res)
    cout << line[0] << " " << line[1] << " " << line[2] << endl;

  return 0;
}
