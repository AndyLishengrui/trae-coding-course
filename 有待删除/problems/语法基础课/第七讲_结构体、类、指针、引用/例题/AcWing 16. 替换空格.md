# AcWing 16. 替换空格 — 替换空格

**难度:** 简单 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/16/

## 题目描述

请实现一个函数，把字符串中的每个空格替换成`%20`。

### 输入格式

输入一个字符串。

数据范围：`0 ≤ 输入字符串的长度 ≤ 1000`

### 输出格式

输出替换后的字符串。

### 样例

**输入:**
```
We are happy.
```

**输出:**
```
We%20are%20happy.
```

### 提示

注意输出格式。

## AC代码

```cpp
class Solution {
public:
    string replaceSpaces(string &str) {
        string res;
        for (auto c : str)
            if (c == ' ' ) res += "%20";
            else res += c;
        return res;
    }
};
```
