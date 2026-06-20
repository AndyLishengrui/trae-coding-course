# AcWing 762. 字符串匹配 — 字符串匹配

**难度:** 简单 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/762/

## 题目描述

给定两个长度相同的字符串 a 和字符串 b。如果在某个位置 i 上，满足字符串 a 上的字符 a[i] 和字符串 b 上的字符 b[i] 相同，那么这个位置上的字符就是匹配的。

如果两个字符串的匹配位置的数量与字符串总长度的比值大于或等于 k，则称两个字符串是匹配的。现在请你判断给定的两个字符串是否匹配。

### 输入格式

第一行包含一个浮点数 k，第二行包含字符串 a，第三行包含字符串 b。输入的字符串中不包含空格。
数据范围：0 < k ≤ 1，字符串的长度不超过 100。

### 输出格式

如果两个字符串匹配，则输出`yes`。否则，输出`no`。

### 样例

**输入:**
```
0.4
aaaa
abed
```

**输出:**
```
no
```

### 提示

注意输出格式。

## AC代码

```cpp
#include <iostream>

using namespace std;

int main()
{
    double k;
    string a, b;
    cin >> k >> a >> b;

    int cnt = 0;
    for (int i = 0; i < a.size(); i ++ )
        if (a[i] == b[i])
            cnt ++ ;

    if ((double)cnt / a.size() >= k) puts("yes");
    else puts("no");

    return 0;
}
```
