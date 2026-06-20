# AcWing 769. 替换字符 — 替换字符

**难度:** 简单 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/769/

## 题目描述

给定一个由大小写字母构成的字符串。把该字符串中特定的字符全部用字符 # 替换。请你输出替换后的字符串。

### 输入格式

输入共两行。
第一行包含一个长度不超过 30 的字符串。
第二行包含一个字符，表示要替换的特定字符。

### 输出格式

输出共一行，为替换后的字符串。

### 样例

**输入:**
```
hello
l
```

**输出:**
```
he##o
```

### 提示

注意输出格式。

来源：语法题

## AC代码

```cpp
#include <cstdio>
#include <iostream>

using namespace std;

int main()
{
    char str[31];
    scanf("%s", str);

    char c;
    scanf("\n%c", &c);

    for (int i = 0; str[i]; i ++ )
        if (str[i] == c)
            str[i] = '#';

    puts(str);

    return 0;
}
```
