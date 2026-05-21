# AcWing 772. 只出现一次的字符 — 只出现一次的字符

**难度:** 简单 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/772/

## 题目描述

给你一个只包含小写字母的字符串。请你判断是否存在只在字符串中出现过一次的字符。如果存在，输出满足条件的字符中位置最靠前的那个。如果没有，输出 no。

### 输入格式

共一行，包含一个由小写字母构成的字符串。数据保证字符串的长度不超过 100000。

### 输出格式

输出满足条件的第一个字符。如果没有，则输出 no。

### 样例

**输入:**
```
abcabcd
```

**输出:**
```
d
```

### 提示

注意输出格式。

来源：语法题

## AC代码

```cpp
#include <iostream>
#include <cstring>

using namespace std;

int cnt[26];
char str[100010];

int main()
{
    cin >> str;

    for (int i = 0; str[i]; i ++ ) cnt[str[i] - 'a'] ++ ;

    for (int i = 0; str[i]; i ++ )
        if (cnt[str[i] - 'a'] == 1)
        {
          cout << str[i] << endl;
          return 0;
        }

        puts("no");

    return 0;    
}
```
