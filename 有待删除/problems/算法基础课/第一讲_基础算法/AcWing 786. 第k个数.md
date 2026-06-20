# AcWing 786. 第k个数 — 快速选择第k个数

**难度:** 简单 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/786/

## 题目描述

给定一个长度为n的整数数列，以及一个整数k，请用快速选择算法求出数列的第k小的数是多少。

### 输入格式

第一行包含两个整数 n 和 k。

第二行包含 n 个整数（所有整数均在1--10^9范围内），表示整数数列。

数据范围:1≤n≤100000,1≤k≤n

### 输出格式

输出一个整数，表示数列的第k小数。

### 样例

**输入:**
```
5 3
2 4 1 5 3
```

**输出:**
```
3
```

### 提示

Andy讲解(2021)

原题链接

## AC代码

```cpp
#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;

long long *numbers;

long long quickFind(long long nums[], int left, int right, int k)
{
    if (left == right)
        return nums[left]; //只有一个元素，左开右闭
    //选取分割数
    long long target = nums[left]; //选取第一个快排的分割数
    int i = left - 1, j = right + 1;
    while (i < j)
    {
        do
            i++;
        while (nums[i] < target); //i指针定位
        do
            j--;
        while (nums[j] > target); //j指针定位
        if (i < j)
            swap(nums[i], nums[j]); //交换
    }
    //判断i与k的关系
    int sumofLeft = j - left + 1; //计算左边区间数字个数，用于与k比较

    if (k <= sumofLeft)              //分治
        quickFind(nums, left, j, k); //j左边的都是不比Target大的
    else
        quickFind(nums, j + 1, right, k - sumofLeft); // j右边的都比Target大
}
int main()
{
    //!cin\cout提速
    ios::sync_with_stdio(false); //来打消iostream的输入输出缓存
    cin.tie(0);                  //cin.tie(0)来解除cin与cout的绑定,0表示NULL

    int n, k;
    //创建动态数组
    cin >> n >> k;
    numbers = new long long[n];
    for (int i = 0; i < n; i++)
        cin >> numbers[i];
    //查找第k小数，输出之
    cout << quickFind(numbers, 0, n - 1, k) << endl; //注意边界

    delete numbers;
    return 0;
}
```
