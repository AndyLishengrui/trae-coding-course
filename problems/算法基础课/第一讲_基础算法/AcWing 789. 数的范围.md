# AcWing 789. 数的范围 — 二分试炼之数的范围

**难度:** 简单 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/789/

## 题目描述

给定一个按照升序排列的长度为n的整数数组，以及 q 个查询。

对于每个查询，返回一个元素k的起始位置和终止位置（位置从0开始计数）。

如果数组中不存在该元素，则返回“-1 -1”。

数据范围
1≤n≤100000
1≤q≤10000
1≤k≤10000

### 输入格式

第一行包含整数n和q，表示数组长度和询问个数。

第二行包含n个整数（均在1~10000范围内），表示完整数组。

接下来q行，每行包含一个整数k，表示一个询问元素。

### 输出格式

共q行，每行包含两个整数，表示所求元素的起始位置和终止位置。

如果数组中不存在该元素，则返回“-1 -1”。

### 样例

**输入:**
```
6 3
1 2 2 3 3 4
3
4
5
```

**输出:**
```
3 4
5 5
-1 -1
```

### 提示

原题

## AC代码

```cpp
#include <iostream>
#include <algorithm>
using namespace std;
const int N = 100007;

int nums[N];

int main()
{

    // 第一行包含整数n和q，表示数组长度和询问个数。
    int n, q;
    scanf("%d%d", &n, &q);
    // 第二行包含n个整数（均在1~10000范围内），表示完整数组。
    for (int i = 0; i < n; i++)
        scanf("%d", &nums[i]);
    // 接下来q行，每行包含一个整数k，表示一个询问元素。
    while(q--){
      //读入要查找的数，并且二分查找其范围
      int k; 
      scanf("%d",&k);// 读入k

      int left = 0, right = n-1;//初始化left和right
      while (left < right) //模板2
      {
          int mid = left + right>>1;
          if (nums[mid]>=k) right = mid;//模板1,
          else left = mid +1;
      }
      //left就是左端点值
      //判断是否找得到
      if (nums[left]!=k) cout<<"-1 -1"<<endl;//找不到x
      else
      {
          cout<<left<<" ";
          //继续寻找右边界
          left=0, right=n-1;//重新初始化left,riight,进行第二次二分搜索
          while (left < right)
          {
              int mid = left+right+1>>1;
              if (nums[mid]<=k) left=mid;
              else right = mid -1;              
          }
          cout<<left<<endl;
      }
    }

    return 0;
}

// int bsearch_1(int left, int right)
// {
//     while (left < right)
//     {
//         int mid = left + right >> 1;
//         if (check(mid)) right = mid;
//         else left = mid + 1;
//     }
//     return left;
// }

// int bsearch_2(int left, int right)
// {
//     while (left < right)
//     {
//         int mid = left + right + 1 >> 1;
//         if (check(mid)) left = mid;
//         else right = mid - 1;
//     }
//     return left;
// }
```
