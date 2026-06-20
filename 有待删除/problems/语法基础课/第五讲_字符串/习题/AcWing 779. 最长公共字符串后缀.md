# AcWing 779. 最长公共字符串后缀 — 最长公共字符串后缀

**难度:** 简单 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/779/

## 题目描述

给出若干个字符串，输出这些字符串的最长公共后缀。

### 输入格式

由不超过 5 组输入组成。每组输入的第一行是一个整数`N`。

`N`为 0 时表示输入结束，否则后面会继续有`N`行输入，每行是一个字符串（字符串内不含空白符）。

每个字符串的长度不超过 200。

### 输出格式

每组数据输出一行结果，为`N`个字符串的最长公共后缀（可能为空）。

### 样例

**输入:**
```
3
baba
baba
cba
2
cc
cc
2
aa
bb
0
```

**输出:**
```
ba
cc
```

### 提示

注意输出格式。

## AC代码

```cpp
#include <iostream>

using namespace std;

const int N = 200;

int n;
string str[N];

int main()
{
    while (cin >> n, n)
    {
      int len = 1000;
      for (int i = 0; i < n; i ++ )
      {
        cin >> str[i];
        if (len > str[i].size()) len = str[i].size();
      }

      while (len)
      {
        bool success = true;
        for (int i = 1; i < n; i ++ )
        {
          bool is_same = true;
          for (int j = 1; j <= len; j ++ )
              if (str[0][str[0].size() - j] != str[i][str[i].size() - j])
              {
                is_same = false;
                break;
              }
          if (!is_same)
          {
            success = false;
            break;
          }
        }

        if (success) break;
        len -- ;
      }

      cout << str[0].substr(str[0].size() - len) << endl;
    }

    return 0;
}
```
