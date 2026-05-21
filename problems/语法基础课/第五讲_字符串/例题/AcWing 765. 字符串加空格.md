# AcWing 765. 字符串加空格 — 字符串加空格

**难度:** 简单 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/765/

## 题目描述

给定一个字符串，在字符串的每个字符之间都加一个空格。输出修改后的新字符串。

### 输入格式

共一行，包含一个字符串。注意字符串中可能包含空格。
数据范围：`1 ≤ 字符串长度 ≤ 100`

### 输出格式

输出增加空格后的字符串。

### 样例

**输入:**
```
test case
```

**输出:**
```
t e s t   c a s e
```

### 提示

注意输出格式。

来源：剑指Offer、语法题

## AC代码

```cpp
#include <iostream>

using namespace std;

int main()
{
    string a;
    getline(cin, a);

    string b;
    for (auto c : a) b = b + c + ' ';

    b.pop_back();

    cout << b << endl;

    return 0;
}
```
