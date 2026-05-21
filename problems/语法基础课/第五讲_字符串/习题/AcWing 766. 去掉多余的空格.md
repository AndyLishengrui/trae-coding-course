# AcWing 766. 去掉多余的空格 — 去掉多余的空格

**难度:** 简单 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/766/

## 题目描述

输入一个字符串，字符串中可能包含多个连续的空格，请将多余的空格去掉，只留下一个空格。

### 输入格式

共一行，包含一个字符串。
数据范围：输入字符串的长度不超过 200。保证输入字符串的开头和结尾没有空格。

### 输出格式

输出去掉多余空格后的字符串，占一行。

### 样例

**输入:**
```
Hello   world.This is  c language.
```

**输出:**
```
Hello world.This is c language.
```

### 提示

注意输出格式。

## AC代码

```cpp
#include <iostream>

using namespace std;

int main()
{
    string s;
    while (cin >> s) cout << s << ' ';

    return 0;
}
```
