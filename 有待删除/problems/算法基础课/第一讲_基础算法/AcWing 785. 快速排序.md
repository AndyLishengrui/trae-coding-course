# AcWing 785. 快速排序 — 快速排序

**难度:** 简单 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/785/

## 题目描述

给定你一个长度为n的整数数列。

请你使用快速排序对这个数列按照从小到大进行排序。

并将排好序的数列按顺序输出。

### 输入格式

输入共两行，第一行包含整数 n。

第二行包含 n 个整数（所有整数均在1--10^9范围内），表示整个数列。

(1≤n≤100000)

### 输出格式

输出共一行，包含 n 个整数，表示排好序的数列。

### 样例

**输入:**
```
5
3 1 2 4 5
```

**输出:**
```
1 2 3 4 5
```

### 提示

原题链接

## AC代码

```cpp
#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;

long long *numbers;

void quicksort(long long nums[], int left, int right)
{
    if (left >= right)
        return;
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
    //分治
    quicksort(nums, left, j);      //j左边的都是不比Target大的
    quicksort(nums, j + 1, right); // j右边的都比Target大
}
int main()
{
    //!cin\cout提速
    ios::sync_with_stdio(false); //来打消iostream的输入输出缓存
    cin.tie(0);                  //cin.tie(0)来解除cin与cout的绑定,0表示NULL

    int n;
    //创建动态数组
    cin >> n;
    numbers = new long long[n];
    for (int i = 0; i < n; i++)
        cin >> numbers[i];
    quicksort(numbers, 0, n - 1); //注意边界

    for (int i = 0; i < n; i++)
        cout << numbers[i] << " ";

    delete numbers;
    return 0;
}
```
