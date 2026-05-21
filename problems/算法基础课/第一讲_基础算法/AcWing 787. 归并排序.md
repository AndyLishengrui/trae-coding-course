# AcWing 787. 归并排序 — 归并排序

**难度:** 简单 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/787/

## 题目描述

给定你一个长度为n的整数数列。

请你使用归并排序对这个数列按照从小到大进行排序。

并将排好序的数列按顺序输出。

### 输入格式

输入共两行，第一行包含整数 n。

第二行包含 n 个整数（所有整数均在1~109109范围内），表示整个数列。

数据范围:1≤n≤100000

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

Andy讲解(2021)

原题链接

## AC代码

```cpp
#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;
const int N = 100007;
int n;
int numbers[N],tmp[N];

void mergeSort(int nums[], int left, int right)
{
    if (left>=right) return;

    int mid = left+(right-left)/2;//防止溢出

    mergeSort(nums,left,mid), mergeSort(nums,mid+1,right);//先调用归并排序
    //合二为一
    int k=0, i=left, j=mid+1;//左右两部分数组的起点

    while(i<=mid && j<=right) //扫描还未抵达终点
      if (nums[i]<=nums[j])//把小的放到tmp数组里面
        tmp[k++] = nums[i++];
        else tmp[k++] = nums[j++];

    while(i<=mid) tmp[k++]=nums[i++];//把左边剩余的部分插入tmp
    while(j<=right) tmp[k++]=nums[j++];//把右边剩余的部分插入tmp

    //把tmp的部分复制回数组
    for (i=left,k=0; i<=right; i++, k++) nums[i]=tmp[k];

}
int main()
{
    //数据大，使用printf和scanf
    scanf("%d",&n);
    for (int i = 0; i<n ;i++) scanf("%d",&numbers[i]);

    mergeSort(numbers,0,n-1);

    for (int i=0; i<n ;i++) printf("%d ",numbers[i]);

    return 0;
}
```
