# AcWing 764. 输出字符串 — 输出字符串

**难度:** 简单 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/764/

## 题目描述

给定字符串 a，请按照如下要求构造字符串 b：
对于 a 的每个位置 i（从第 1 个字符到倒数第二个字符），令 b[i] 为字符，其 ASCII 值等于 a[i] 和 a[i+1] 的 ASCII 值之和；
最后 b 的最后一个字符的 ASCII 值等于 a 的最后一个字符和第一个字符的 ASCII 值之和。
输出字符串 b。

### 输入格式

输入共一行，包含字符串 a（字符串长度范围：3 ~ 100），其中每个字符的 ASCII 值均不超过 63（例如空格、!、"、#、...、?）。

### 输出格式

输出一行，表示字符串 b。

### 样例

**输入:**
```
1 2 3
```

**输出:**
```
QRRSd
```

### 提示

提示：读取整行字符串，然后依次计算相邻两个字符 ASCII 值之和，最后一个字符与第一个字符相加。

来源：语法题

## AC代码

```cpp
#include <iostream>

using namespace std;

int main()
{
    string a, b;
    getline(cin, a);

    for (int i = 0; i < a.size(); i ++ ) b += (char)(a[i] + a[(i + 1) % a.size()]);

    cout << b << endl;

    return 0;
}
```
