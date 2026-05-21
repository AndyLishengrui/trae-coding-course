#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

using Triplet = vector<int>;
using Result = vector<Triplet>;

Result threeSum(vector<int>& nums, int target) {
    Result res;
    int n = nums.size();
    sort(nums.begin(), nums.end());
    
    for (int i = 0; i < n; ++i) {
        // 跳过重复元素
        if (i > 0 && nums[i] == nums[i-1]) continue;
        
        // 双指针初始化
        int j = i + 1, k = n - 1;
        while (j < k) {
            int sum = nums[i] + nums[j] + nums[k];
            
            if (sum == target) {
                // 满足x<y<z
                if (nums[i] < nums[j] && nums[j] < nums[k]) {
                    res.push_back({nums[i], nums[j], nums[k]});
                }
                // 跳重复
                while (j < k && nums[j] == nums[j+1]) ++j;
                while (j < k && nums[k] == nums[k-1]) --k;
                // 移动指针
                ++j;
                --k;
            } else if (sum > target) {
                --k; // 和过大，右指针左移
            } else {
                ++j; // 和过小，左指针右移
            }
        }
    }
    return res;
}

int main() {
    int target, n;
    cin >> target >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; ++i) {
        cin >> nums[i];
    }
    
    Result result = threeSum(nums, target);
    for (const auto& triplet : result) {
        cout << triplet[0] << " " << triplet[1] << " " << triplet[2] << endl;
    }
    return 0;
}