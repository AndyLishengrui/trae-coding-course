# AcWing 67. 数字在排序数组中出现的次数 — 数字在排序数组中出现的次数

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/67/

## 题目描述

统计一个数字在排序数组中出现的次数。例如输入排序数组 [1, 2, 3, 3, 3, 3, 4, 5] 和数字 3，由于 3 在这个数组中出现了 4 次，因此输出 4。

### 输入格式

输入一个排序数组和一个整数。

数据范围：数组长度 `[0, 1000]`。

### 输出格式

输出该数字在数组中出现的次数。

### 样例

**输入:**
```
[1, 2, 3, 3, 3, 3, 4, 5]
3
```

**输出:**
```
4
```

### 提示

来源：剑指 Offer

## AC代码

```cpp
class Solution {
public:
    int getNumberOfK(vector<int>& nums , int k) {
        if (nums.empty()) return 0;

        int l = 0, r = nums.size() -1;
        while (l < r) {
            int mid = l + r >> 1;
            if (nums[mid] < k) l = mid + 1;
            else r = mid;
        }

        if (nums[l] !=k) return 0;

        int left = l;

        l = 0, r = nums.size() -1;
        while (l < r) {
            int mid = l + r + 1 >>1;
            if (nums[mid] <= k) l = mid;
            else r = mid -1;
        }

        return r -left+1;

    }
};
```
