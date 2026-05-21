# AcWing 68. 0到n-1中缺失的数字 — 0 到 n-1 中缺失的数字

**难度:** 简单 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/68/

## 题目描述

一个长度为n−1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0到n−1之内。

在范围00到n−1的n个数字中有且只有一个数字不在该数组中，请找出这个数字。

### 输入格式

第一行输入整数 n；

第二行输入 n-1 个整数，数字之间以空格隔开。

数据范围

1≤n≤1000

### 输出格式

输出一个整数，表示缺失的数字。

### 样例

**输入:**
```
[0,1,2,4]
```

**输出:**
```
3
```

## AC代码

```cpp
class Solution {
public:
    int getMissingNumber(vector<int>& nums) {
        if (nums.empty()) return 0;

        int l = 0, r = nums.size() -1;
        while (l < r)
        {
            int mid = l + r >> 1;
            if (nums[mid] != mid) r = mid;
            else l = mid + 1;
        }

        if (nums[r] == r) r++;
        return r;
    }
};
```
