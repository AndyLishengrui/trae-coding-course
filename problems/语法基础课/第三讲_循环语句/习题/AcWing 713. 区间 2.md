# AcWing 713. 区间 2 — 区间 2

**难度:** 简单 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/713/

## 题目描述

读取 N 个整数 X1,X2,…,XN，判断这 N 个整数中有多少个在 [10,20] 的范围内，有多少个在范围外。

### 输入格式

第一行包含整数 N，表示共有 N 个整数需要进行判断。

接下来 N 行，每行包含一个整数 Xi。

数据范围

1≤N≤10000,

−10^7<Xi<10^7

### 输出格式

第一行输出`x in`，其中 x 为在范围内的整数的数量。第二行输出`y out`，其中 y 为在范围外的整数的数量。

### 样例

**输入:**
```
4
14
123
10
-25
```

**输出:**
```
2 in
2 out
```

### 提示

注意区间的开闭情况。

## AC代码

```cpp
#include <iostream>

using namespace std;

int main()
{
  int n;
  cin >> n;

  int x = 0, y = 0;
  while (n -- )
  {
    int t;
    cin >> t;
    if (t >= 10 && t <= 20) x ++ ;
    else y ++ ;
  }

  cout << x << " in" << endl;
  cout << y << " out" << endl;

  return 0;
}
```
