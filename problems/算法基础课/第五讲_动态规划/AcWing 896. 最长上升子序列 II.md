# AcWing 896. 最长上升子序列 II — 最长上升子序列(2)

**难度:** 困难 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/896/

## 题目描述

给定一个长度为N的数列，求数值严格单调递增的子序列的长度最长是多少。

### 输入格式

第一行包含整数N。

第二行包含N个整数，表示完整序列。

### 输出格式

输出一个整数，表示最大长度。

### 样例

**输入:**
```
7
3 1 2 1 8 5 6
```

**输出:**
```
4
```

### 提示

原题链接

## AC代码

```cpp
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 100007;

int n;
int a[N];
int q[N];//记录最长上升子序列的值

int main()
{
    scanf("%d", &n);
    //记录序列
    for (int i = 0; i <n; i++) scanf("%d", &a[i]);
    //使用q[N]存储最长上升子序列，用增量的方式更新里面的值
    int len = 0; //q的长度
    for (int i = 0; i < n; i++)
    {
      int l = 0, r = len;//q的下标
      while (l < r)
      {
        int mid = l + r + 1 >> 1;
        if (q[mid] < a[i]) l = mid;
        else r = mid -1;
      }//r就是找到的位置
      len = max(len,r+1);
      q[r+1] = a[i];
    }

    printf("%d\n",len);
    return 0;
}
```
