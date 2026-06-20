# AcWing 815. 打印字符串 — 打印字符串

**难度:** 简单 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/815/

## 题目描述

给定字符串，编写函数 void print(char str[]) （Python 用 print_str()）打印该字符串。

### 输入格式

一行一个字符串。

数据范围：`1 ≤ 长度 ≤ 100`

### 输出格式

一行表示打印出的字符串。

### 样例

**输入:**
```
I love AcWing.
```

**输出:**
```
I love AcWing.
```

### 提示

注意输出格式。

来源：语法题

## AC代码

```cpp
#include <cstdio>

void print(char str[])
{
    printf("%s", str);
}

int main()
{
    char str[110];
    fgets(str, 101, stdin);

    print(str);

    return 0;
}
```
