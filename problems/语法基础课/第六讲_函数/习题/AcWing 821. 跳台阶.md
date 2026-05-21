# AcWing 821. 跳台阶 — 跳台阶

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/821/

## 题目描述

一个楼梯有 n 级台阶，每次可走一级或两级，求从第 0 级走到第 n 级的方案数。

### 输入格式

一行一个整数 n。

数据范围：`1 ≤ n ≤ 15`

### 输出格式

一个整数表示方案数。

### 样例

**输入:**
```
5
```

**输出:**
```
8
```

### 提示

注意输出格式。

来源：语法题

## AC代码

```cpp
#include <iostream>

using namespace std;

int n;
int ans;

void f(int k)
{
  if (k == n) ans ++ ;
  else if (k < n)
  {
    f(k + 1);
    f(k + 2);
  }
}

int main()
{
    cin >> n;
    f(0);
    cout << ans << endl;

    return 0;
}
```
