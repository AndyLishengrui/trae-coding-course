# AcWing 663. 简单排序 — 简单排序

**难度:** 简单 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/663/

## 题目描述

读取三个整数并按升序对它们进行排序。

### 输入格式

共一行，包含三个整数。

数据范围

−100≤输入整数≤100,输入整数各不相同。

### 输出格式

首先，将三个整数按升序顺序输出，每行输出一个整数。

然后，输出一个空行。

紧接着，将三个整数按原输入顺序输出，每行输出一个整数。

### 样例

**输入:**
```
7 21 -14
```

**输出:**
```
-14
7
21

7
21
-14
```

### 提示

注意输出格式。

## AC代码

```cpp
#include <iostream>

using namespace std;

int main()
{
    int a, b, c;
    cin >> a >> b >> c;

    int x = a, y = b, z = c;

    if (b < a)
    {
      int t = a;
      a = b;
      b = t;
    }
    if (c < a)
    {
      int t = a;
      a = c;
      c = t;
    }
    if (c < b)
    {
      int t = b;
      b = c;
      c = t;
    }

    cout << a << endl << b << endl << c << endl << endl;
    cout << x << endl << y << endl << z << endl;

    return 0;
}
```
