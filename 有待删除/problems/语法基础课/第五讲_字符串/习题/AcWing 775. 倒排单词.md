# AcWing 775. 倒排单词 — 倒排单词

**难度:** 简单 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/775/

## 题目描述

编写程序，读入一行英文（只包含字母和空格，单词间以单个空格分隔），将所有单词的顺序倒排并输出，依然以单个空格分隔。

### 输入格式

输入为一个字符串（字符串长度至多为 100）。

### 输出格式

输出为按要求排序后的字符串。

### 样例

**输入:**
```
I am a student
```

**输出:**
```
student a am I
```

### 提示

注意输出格式。

## AC代码

```cpp
#include <iostream>

using namespace std;

int main()
{
    string str[100];

    int n = 0;
    while (cin >> str[n]) n ++ ;

    for (int i = n - 1; i >= 0; i -- ) cout << str[i] << ' ';
    cout << endl;

    return 0;
}
```
