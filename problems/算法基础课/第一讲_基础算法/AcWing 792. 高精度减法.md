# AcWing 792. 高精度减法 — 高精度减法

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/792/

## 题目描述

给定两个正整数，计算它们的差，计算结果可能为负数。

1≤整数长度≤100000

### 输入格式

共两行，每行包含一个整数。

### 输出格式

共一行，包含所求的差。

### 样例

**输入:**
```
32
11
```

**输出:**
```
21
```

### 提示

原题链接

Y总讲解

参考题解

Y总代码

## AC代码

```cpp
#include <iostream>
#include <cstring>
#include <vector>
using namespace std;
const int N = 1e6 + 7;
bool isGreater(vector<int> &A, vector<int> &B)
{
    if (A.size() != B.size()) //比较大小
        return A.size() > B.size();
    //否则大小相等，逐位比较大小
    for (int i = A.size() - 1; i >= 0; i--)
        if (A[i] != B[i])
            return A[i] > B[i];
    return true; //每个数字都相同，长度相同，两数相等
}
//C= A-B
vector<int> sub(vector<int> &A, vector<int> &B)
{
    vector<int> C;
    //A是比较大的数
    int t = 0; //第一轮减法进位为0
    for (int i = 0; i < A.size(); i++)
    {
        t = A[i] - t;
        if (i < B.size())
            t -= B[i];              //A[i]-B[i] + t
        C.push_back((t + 10) % 10); //得到对应位
        if (t < 0)
            t = 1;
        else
            t = 0; //判断是否借一位
    }
    //去掉开头的0
    while (C.size() > 1 && C.back()==0) C.pop_back();

    return C;
}

int main()
{
    //输入为字符串
    string a, b;
    vector<int> A, B;

    cin >> a >> b; // a="786654"
    //倒序存储A，B，a[0]乃是最低位
    for (int i = a.size() - 1; i >= 0; i--)
        A.push_back(a[i] - '0');
    for (int i = b.size() - 1; i >= 0; i--)
        B.push_back(b[i] - '0');
    //判断A与B的大小
    if (isGreater(A, B))
    {
        auto C = sub(A, B);
        for (int i = C.size() - 1; i >= 0; i--)
            cout << C[i]; //打印C
    }
    else
    {
        auto C = sub(B, A);
        cout << "-";
        for (int i = C.size() - 1; i >= 0; i--)
            cout << C[i]; //打印C
    }
    return 0;
}
```
