# AcWing 794. 高精度除法 — 高精度除法

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/794/

## 题目描述

给定两个非负整数A，B，请你计算 A / B的商和余数。

数据范围：

1≤A的长度≤100000,

1≤B≤10000

B 一定不为0

### 输入格式

共两行，第一行包含整数A，第二行包含整数B。

### 输出格式

共两行，第一行输出所求的商，第二行输出所求余数。

### 样例

**输入:**
```
7
2
```

**输出:**
```
3
1
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
#include <algorithm>

using namespace std;
const int N = 1e6 + 7;

//C= A/b 余数为r
vector<int> div(vector<int> &A, int b, int &r){
    vector<int> C;
    r=0;//余数
    for(int i=A.size()-1; i>=0; i--){
        r = r* 10 + A[i];//从最高位开始，当前余数r需要上一次运算的r乘10
        C.push_back(r/b);
        r %= b;
    }
    reverse(C.begin(), C.end());//定义的数是最低位在C[0],因此需要取逆
    while(C.size()>1 && C.back()==0) C.pop_back();//去掉C开头的0字符
    return C;
}

int main()
{
    //输入为字符串
    string a;
    int b;//输入的b比较小，作为一个整体处理
    vector<int> A;

    cin >> a >> b; // a="786654"
    //倒序存储A，B，a[0]乃是最低位
    for (int i = a.size() - 1; i >= 0; i--)
        A.push_back(a[i] - '0');

    int r;
    auto C=div(A,b,r);//使用auto自动辨别变量类型

    for (int i = C.size() - 1; i >= 0; i--)
            cout << C[i]; //打印C
            cout<<endl<<r<<endl;//打印余数
    return 0;
}
```
