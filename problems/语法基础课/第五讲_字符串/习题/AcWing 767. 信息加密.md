# AcWing 767. 信息加密 — 信息加密

**难度:** 简单 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/767/

## 题目描述

对给定的字符串进行加密处理，加密规则如下：
1. 小写字母：a→b, b→c, …, z→a；
2. 大写字母：A→B, B→C, …, Z→A；
3. 数字：0→1, 1→2, …, 9→0；
4. 其他字符不变。
输出加密后的字符串。

### 输入格式

输入共一行，包含一个字符串，注意字符串中可能包含空格。
数据范围：字符串长度不超过100。

### 输出格式

输出一行，即加密后的字符串。

### 样例

**输入:**
```
Hello! How are you!
```

**输出:**
```
Ifmmp! Ipx bsf zpv!
```

### 提示

注意按照规则进行字符替换，保持空格等其他字符不变。

来源：语法题

## AC代码

```cpp
#include <iostream>
#include <cstring>
using namespace std;

int main(){

    string s;
    getline(cin,s);//读入一行

    for (auto &c:s)//使用auto注意&c直接引用字符串直接修改
      if (c>='a' && c<='z') 
          c = 'a'+ (c-'a'+1) % 26;//取模运算
         else if (c>='A' && c<='Z') 
          c = 'A' + (c-'A'+1) % 26;

    cout<<s<<endl;//输出结果
}
```
