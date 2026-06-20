# AcWing 53. 最小的k个数 — 最小的 k 个数

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/53/

## 题目描述

输入 n 个整数，找出其中最小的 k 个数。注意输出数组内元素请按从小到大顺序排序。

### 输入格式

输入一个整数数组和一个整数 k。

数据范围：`1 ≤ k ≤ n ≤ 1000`

### 输出格式

输出最小的 k 个数，按从小到大排序。

### 样例

**输入:**
```
[1,2,3,4,5,6,7,8]
4
```

**输出:**
```
[1,2,3,4]
```

### 提示

注意输出格式。

## AC代码

```cpp
class Solution {
public:
    vector<int> getLeastNumbers_Solution(vector<int> input, int k) {
        //只保持前K个数
        priority_queue<int> heap;
        for (auto x: input) {
            heap.push(x);
            if (heap.size() > k) heap.pop();
        }
        //把堆的元素压入vector
        vector<int> res;
        while(heap.size()) res.push_back(heap.top()), heap.pop();
        //堆是大根堆，需要逆序
        reverse(res.begin(), res.end());
        return res;
    }
};
```
