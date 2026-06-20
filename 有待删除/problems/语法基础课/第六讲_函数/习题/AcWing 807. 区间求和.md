# AcWing 807. 区间求和 — 区间求和

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/807/

## 题目描述

给定一个长度为 n 的整数数组和 q 个区间查询，每个查询给出左右下标 l 和 r（数组下标从 0 开始），请你求出该区间内所有数字的和。

### 输入格式

第一行输入整数 n (1 ≤ n ≤ 10^5)；第二行输入 n 个整数，数字之间以空格隔开；第三行输入整数 q (1 ≤ q ≤ 10^5)；接下来 q 行，每行包含两个整数 l 和 r (0 ≤ l ≤ r < n)，表示一个区间查询。

### 输出格式

输出 q 行，每行输出一个整数，表示对应区间内所有数字之和。

### 样例

**输入:**
```
5
1 2 3 4 5
3
0 2
1 3
0 4
```

**输出:**
```
6
9
15
```

### 提示

可以预处理前缀和数组来在 O(1) 时间内求出每个区间的和。

## AC代码

```cpp
#include <iostream>

using namespace std;

int sum(int l, int r)
{
  int s = 0;
  for (int i = l; i <= r; i ++ ) s += i;
  return s;
}

int main()
{
    int l, r;
    cin >> l >> r;
    cout << sum(l, r) << endl;

    return 0;
}
```
