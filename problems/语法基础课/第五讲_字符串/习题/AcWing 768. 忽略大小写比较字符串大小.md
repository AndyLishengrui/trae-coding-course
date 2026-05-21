# AcWing 768. 忽略大小写比较字符串大小 — 忽略大小写比较字符串大小

**难度:** 简单 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/768/

## 题目描述

对两个字符串进行比较，忽略字母的大小写。比较方法：将两个字符串转换为统一大小写后，从左到右逐个字符比较；

若所有字符均相同，则视为相等；否则以第一个不同字符的 ASCII 值比较大小。

### 输入格式

输入共两行，每行包含一个字符串，字符串中仅可能包含字母和空格。
数据范围：每个字符串的长度范围为[0, 80]。

### 输出格式

输出一个字符：若第一个字符串（忽略大小写后）小于第二个，则输出 "<"；若大于，则输出 ">"；若相等，则输出 "="。

### 样例1

**输入:**
```
Hello
hello
```

**输出:**
```
=
```

### 样例2

**输入:**
```
How are you
How old are you
```

**输出:**
```
<
```

### 提示

提示：可先将字符串转换为统一字母大小写后，再利用标准字符串比较函数。

来源：语法题

## AC代码

```cpp
#include <cstdio>
#include <cstring>

int main()
{
    char a[100], b[100];

    fgets(a, 100, stdin);
    fgets(b, 100, stdin);

    if (a[strlen(a) - 1] == '\n') a[strlen(a) - 1] = 0;
    if (b[strlen(b) - 1] == '\n') b[strlen(b) - 1] = 0;

    for (int i = 0; a[i]; i ++ )
        if (a[i] >= 'A' && a[i] <= 'Z')
            a[i] += 32;

    for (int i = 0; b[i]; i ++ )
        if (b[i] >= 'A' && b[i] <= 'Z')
            b[i] += 32;

    int t = strcmp(a, b);
    if (t == 0) puts("=");
    else if (t > 0) puts(">");
    else puts("<");

    return 0;
}
```
