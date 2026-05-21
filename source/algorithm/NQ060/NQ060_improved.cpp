#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

/**
 * 找到所有满足四数之和等于目标值的四元组
 * 时间复杂度：O(n³)，其中n是数组长度
 */
vector<vector<int>> fourSum(vector<int>& nums, int target) {
    vector<vector<int>> res;         // 答案数组
    sort(nums.begin(), nums.end());  // 排序
    
    int n = nums.size();
    
    // 四重循环，后两重用双指针算法 i,j,k,l
    for (int i = 0; i < n; i++) {
        // 去重
        if (i > 0 && nums[i] == nums[i - 1]) continue;
        
        for (int j = i + 1; j < n; j++) {
            // 去重
            if (j > i + 1 && nums[j] == nums[j - 1]) continue;
            
            // 双指针算法
            for (int k = j + 1, l = n - 1; k < l; k++) {
                // 去重
                if (k > j + 1 && nums[k] == nums[k - 1]) continue;
                
                // 找到最小的l使得四数之和大于等于目标值
                while (k < l - 1 && nums[i] + nums[j] + nums[k] + nums[l - 1] >= target) {
                    l--;
                }
                
                // 检查是否等于目标值
                if (nums[i] + nums[j] + nums[k] + nums[l] == target) {
                    res.push_back({nums[i], nums[j], nums[k], nums[l]});
                }
            }
        }
    }
    return res;
}

// 四元组的比较函数
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
    
    // 寻找四元组
    res = fourSum(a, target);
    
    // 对结果排序
    sort(res.begin(), res.end(), comp);
    
    // 输出四元组
    for (auto& line : res) {
        cout << line[0] << " " << line[1] << " " << line[2] << " " << line[3] << endl;
    }
    
    return 0;
}