# AcWing 776. 字符串移位包含问题 — 字符串移位包含问题

**难度:** 简单 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/776/

## 题目描述

对于一个字符串来说，定义一次循环移位操作为：将字符串的第一个字符移动到末尾形成新的字符串。

给定两个字符串 s1 和 s2，要求判定其中一个字符串是否是另一字符串通过若干次循环移位后的新字符串的子串。

例如`CDAA`是由`AABCD`两次移位后产生的新串`BCDAA`的子串，而`ABCD`与`ACBD`则不能通过多次移位来得到其中一个字符串是新串的子串。

### 输入格式

共一行，包含两个字符串，中间由单个空格隔开。字符串只包含字母和数字，长度不超过 30。

### 输出格式

如果一个字符串是另一字符串通过若干次循环移位产生的新串的子串，则输出`true`，否则输出`false`。

### 样例

**输入:**
```
AABCD CDAA
```

**输出:**
```
true
```

## AC代码

```cpp
#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    string a, b;

    cin >> a >> b;
    if (a.size() < b.size()) swap(a, b);

    for (int i = 0; i < a.size(); i ++ )
    {
      a = a.substr(1) + a[0];
      for (int j = 0; j + b.size() <= a.size(); j ++ )
        {
          int k = 0;
          for (; k < b.size(); k ++ )
              if (a[j + k] != b[k])
                  break;
          if (k == b.size())
          {
            puts("true");
            return 0;
          }
        }
    }

    puts("false");

    return 0;
}
```
