#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// 四元组求和函数
vector<vector<int>> four_sum(vector<int>& nums, int target) {
    vector<vector<int>> res;
    // 排序数组
    sort(nums.begin(), nums.end());
    int n = nums.size();
    
    // 四重循环，后两重用双指针
    for (int i = 0; i < n; ++i) {
        // 跳过重复的i值
        if (i > 0 && nums[i] == nums[i-1]) {
            continue;
        }
        
        for (int j = i + 1; j < n; ++j) {
            // 跳过重复的j值
            if (j > i + 1 && nums[j] == nums[j-1]) {
                continue;
            }
            
            // 双指针算法
            int k = j + 1;
            int l = n - 1;
            
            while (k < l) {
                // 跳过重复的k值
                if (k > j + 1 && nums[k] == nums[k-1]) {
                    ++k;
                    continue;
                }
                
                // 移动l指针到合适的位置
                while (k < l - 1 && nums[i] + nums[j] + nums[k] + nums[l-1] >= target) {
                    --l;
                }
                
                // 检查是否找到和为目标值的四元组
                int current_sum = nums[i] + nums[j] + nums[k] + nums[l];
                if (current_sum == target) {
                    res.push_back({nums[i], nums[j], nums[k], nums[l]});
                    ++k;
                } else if (current_sum < target) {
                    ++k;
                } else {
                    --l;
                }
            }
        }
    }
    
    return res;
}

int main() {
    int target, n;
    while (cin >> target >> n) {
        vector<int> nums(n);
        for (int i = 0; i < n; ++i) {
            cin >> nums[i];
        }
        
        // 寻找四元组
        vector<vector<int>> res = four_sum(nums, target);
        
        // 对结果排序
        sort(res.begin(), res.end());
        
        // 输出结果
        for (auto& quadruplet : res) {
            for (int i = 0; i < 4; ++i) {
                if (i > 0) {
                    cout << " ";
                }
                cout << quadruplet[i];
            }
            cout << endl;
        }
    }
    return 0;
}