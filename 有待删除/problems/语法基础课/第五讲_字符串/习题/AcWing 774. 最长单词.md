# AcWing 774. 最长单词 — 最长单词

**难度:** 简单 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/774/

## 题目描述

一个以`.`结尾的简单英文句子，单词之间用单个空格分隔，没有缩写形式和其它特殊形式，求句子中的最长单词。

### 输入格式

输入一行字符串，表示这个简单英文句子，长度不超过 500。

### 输出格式

该句子中最长的单词。如果多于一个，则输出第一个。

### 样例

**输入:**
```
I am a student of Peking University.
```

**输出:**
```
University
```

### 提示

注意输出格式。

## AC代码

```cpp
#include <iostream>

using namespace std;

int main()
{
    string res, str;

    while (cin >> str)
    {
      if (str.back() == '.') str.pop_back();
      if (str.size() > res.size()) res = str;
    }

    cout << res << endl;

    return 0;
}
```
