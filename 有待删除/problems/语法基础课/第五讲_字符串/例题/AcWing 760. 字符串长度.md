# AcWing 760. 字符串长度 — 字符串长度

**难度:** 简单 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/760/

## 题目描述

给定一行长度不超过100的非空字符串，求出其实际长度（包括空格）。

### 输入格式

输入一行字符串，注意字符串中可能包含空格。

### 输出格式

输出一个整数，表示该字符串的长度。

### 样例

**输入:**
```
I love Beijing.
```

**输出:**
```
15
```

### 提示

注意读取整行，包括空格。

来源：语法题

## AC代码

```cpp
#include <cstdio>

int main()
{
    char str[101];

    fgets(str, 101, stdin);

    int len = 0;
    for (int i = 0; str[i] && str[i] != '\n'; i ++ ) len ++ ;

    printf("%d\n", len);

    return 0;
}
```
