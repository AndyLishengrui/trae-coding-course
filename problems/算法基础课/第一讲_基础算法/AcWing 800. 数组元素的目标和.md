# AcWing 800. 数组元素的目标和 — 数组元素的目标和

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/800/

## 题目描述

给定两个升序排序的有序数组A和B，以及一个目标值x。数组下标从0开始。
请你求出满足A[i] + B[j] = x的数对(i, j)。

数据保证有唯一解。

数据范围：

数组长度不超过100000。

同一数组内元素各不相同。

1≤数组元素≤10^9

### 输入格式

第一行包含三个整数n，m，x，分别表示A的长度，B的长度以及目标值x。

第二行包含n个整数，表示数组A。

第三行包含m个整数，表示数组B。

### 输出格式

共一行，包含两个整数 i 和 j。

### 样例

**输入:**
```
4 5 6
1 2 4 7
3 4 6 8 9
```

**输出:**
```
1 1
```

### 提示

原题链接

## AC代码

```cpp
#include <iostream>
#include <algorithm>
using namespace std;
const int N=100007;
int n,m,x;
int numA[N],numB[N];

int main(){
       //读入n,m,x其中x为目标和
   scanf("%d%d%d",&n,&m,&x);
   for (int i=0; i<n; i++) scanf("%d",&numA[i]);
   for (int j=0; j<m; j++) scanf("%d",&numB[j]);
   //双指针查找和

   for (int i=0, j= m-1; i<n; i++){
       //check(i,j)
       while (j>=0 && numA[i]+numB[j]>x) j--;
       if (numA[i]+numB[j]==x)//判断是否和相等
       {
         printf("%d %d\n",i,j);
        break;
       }
   }
    return 0;
}
```
