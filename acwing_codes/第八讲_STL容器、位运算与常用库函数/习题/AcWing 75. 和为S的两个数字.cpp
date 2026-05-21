class Solution {
public:
    vector<int> findNumbersWithSum(vector<int>& nums, int target) {
        //哈希表
        unordered_set<int> s;
        for (auto x:nums){
            if (s.count(target-x)) return {x, target-x};//在x之前哈希表里有target-x这个数，则输出
            s.insert(x);//把x插入哈希表
        }
    }
};