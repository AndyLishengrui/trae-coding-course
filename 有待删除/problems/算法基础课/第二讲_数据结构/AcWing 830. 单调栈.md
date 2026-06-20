# AcWing 830. 单调栈 — 单调栈

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/830/

## 题目描述

给定一个长度为N的整数数列，输出每个数左边第一个比它小的数，如果不存在则输出-1。

1≤N≤10^5

1≤数列中元素≤10^9

### 输入格式

第一行包含整数N，表示数列长度。

第二行包含N个整数，表示整数数列。

### 输出格式

共一行，包含N个整数，其中第i个数表示第i个数的左边第一个比它小的数，如果不存在则输出-1。

### 样例

**输入:**
```
5
3 4 2 7 5
```

**输出:**
```
-1 3 -1 2 2
```

### 提示

原题链接

参考题解

Y总讲解

Y总代码

## AC代码

```cpp
#include <iostream>
using namespace std;
const int N=100007;
int n;
int stk[N],tt;//数组模拟栈实现单调栈
int main ()
{
    cin>> n;
    for (int i=0; i< n; i++){
        int x; cin>>x;
        while (tt && stk[tt]>= x)//tt为空，并且单调栈顶元素比x大
          tt--;//出栈，这些数永远不会用到
          if (tt) cout<<stk[tt]<<' '; //栈顶就是比x小的元素，直接输出
           else cout<<-1<<' '; //x左边没有任何数比它小
           //入栈
           stk[++tt] = x;
    }
    return 0;
}
```
