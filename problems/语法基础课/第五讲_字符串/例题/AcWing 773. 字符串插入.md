# AcWing 773. 字符串插入 — 字符串插入

**难度:** 简单 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/773/

## 题目描述

有两个不包含空白字符的字符串 str 和 substr，str 的字符个数不超过 10，substr 的字符个数为 3。

将 substr 插入到 str 中 ASCII 码最大的那个字符后面，若有多个最大则只考虑第一个。

### 输入格式

输入包括若干行，每一行为一组测试数据，格式为 str substr。

### 输出格式

对于每一组测试数据，输出插入之后的字符串。

### 样例

**输入:**
```
abcab eee
12343 555
```

**输出:**
```
abceeeab
12345553
```

### 提示

注意输出格式。

来源：语法题

## AC代码

```cpp
#include <iostream>
#include <cstring>
using namespace std;
int main()
{
    string a,b;
    while(cin>>a>>b){

        int p=0;
        for (int i=0;i<a.size();i++)
            if (a[i]>a[p]) p=i;//找到最大的位置

        cout<<a.substr(0,p+1)+b+a.substr(p+1)<<endl;

    }
    return 0;
}
```
