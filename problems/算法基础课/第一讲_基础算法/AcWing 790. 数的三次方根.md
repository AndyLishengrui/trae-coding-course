# AcWing 790. 数的三次方根 — 数的三次方根

**难度:** 简单 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/790/

## 题目描述

给定一个浮点数n，求它的三次方根。

数据范围:−10000≤n≤10000

### 输入格式

共一行，包含一个浮点数n。

### 输出格式

共一行，包含一个浮点数，表示问题的解。

注意，结果保留6位小数。

### 样例

**输入:**
```
1000.00
```

**输出:**
```
10.000000
```

### 提示

原题链接

## AC代码

```cpp
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    double number;
    scanf("%lf", &number);
    double left = -10000, right = 10000;
    while (right - left >= 1e-8)
    {
        double mid = (right + left) / 2; //二分
        if (mid * mid * mid >= number)
            right = mid;
        else
            left = mid;
    }
    //输出left
    printf("%lf", left);
}
```
