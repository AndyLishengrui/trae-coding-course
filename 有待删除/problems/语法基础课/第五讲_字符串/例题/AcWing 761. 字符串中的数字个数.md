# AcWing 761. 字符串中的数字个数 — 字符串中的数字个数

**难度:** 简单 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/761/

## 题目描述

输入一行字符（长度不超过 100），请你统计一下其中的数字字符的个数。

### 输入格式

输入一行字符。字符中可能包含空格。

### 输出格式

输出一个整数，表示该行字符中数字字符的个数。

### 样例

**输入:**
```
I am 18 years old this year.
```

**输出:**
```
2
```

### 提示

注意读取整行字符，并统计每个数字字符。

来源：语法题

## AC代码

```cpp
#include <cstdio>

int main()
{
    char str[101];

    fgets(str, 101, stdin);

    int cnt = 0;
    for (int i = 0; str[i]; i ++ )
        if (str[i] >= '0' && str[i] <= '9')
           cnt ++ ;

    printf("%d\n", cnt);

    return 0;
}
```
