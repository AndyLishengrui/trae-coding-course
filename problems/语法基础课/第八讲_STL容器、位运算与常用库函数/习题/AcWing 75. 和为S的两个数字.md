# AcWing 75. 和为S的两个数字

> ⚠ 此题暂未收录到XMUOJ公共题库，题面待补充
> 原题链接: https://www.acwing.com/problem/content/75/

## 题目描述
> 待补充

### 输入格式
> 待补充

### 输出格式
> 待补充

### 样例
> 待补充

## AC代码

```cpp
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
```
