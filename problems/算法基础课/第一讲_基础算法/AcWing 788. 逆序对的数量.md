# AcWing 788. 逆序对的数量 — 逆序对的数量

**难度:** 简单 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/788/

## 题目描述

给定一个长度为n的整数数列，请你计算数列中的逆序对的数量。

逆序对的定义如下：对于数列的第 i 个和第 j 个元素，如果满足 i < j 且 a[i] > a[j]，则其为一个逆序对；否则不是。

数据范围：1≤n≤100000

### 输入格式

第一行包含整数n，表示数列的长度。

第二行包含 n 个整数，表示整个数列。

### 输出格式

输出一个整数，表示逆序对的个数。

### 样例

**输入:**
```
6
2 3 4 5 6 1
```

**输出:**
```
5
```

## AC代码

```cpp
#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;
typedef long long LL;

const int N = 100007;
int n;
int numbers[N],tmp[N];
//最大的数可能会是 n^2/2 
 LL mergeSort(int nums[], int left, int right)
{
    if (left>=right) return 0; //如果左指针越过右指针，则返回

    int mid = left+(right-left)/2;//防止溢出

    LL result = mergeSort(nums,left,mid)+mergeSort(nums,mid+1,right);//先调用归并排序
    //合二为一
    int k=0, i=left, j=mid+1;//左右两部分数组的起点

    while(i<=mid && j<=right) //扫描还未抵达终点
      if (nums[i]<=nums[j])//把小的放到tmp数组里面
        tmp[k++] = nums[i++];
        else {
            //计算逆序对的个数mid-i+1
            result += mid -i +1;
            tmp[k++] = nums[j++];
        }

    while(i<=mid) tmp[k++]=nums[i++];//把左边剩余的部分插入tmp
    while(j<=right) tmp[k++]=nums[j++];//把右边剩余的部分插入tmp

    //把tmp的部分复制回数组
    for (i=left,k=0; i<=right; i++, k++) nums[i]=tmp[k];

    return result;

}
int main()
{
    //数据大，使用printf和scanf
    scanf("%d",&n);
    for (int i = 0; i<n ;i++) scanf("%d",&numbers[i]);

   cout<<mergeSort(numbers,0,n-1)<<endl;


    return 0;
}
```
