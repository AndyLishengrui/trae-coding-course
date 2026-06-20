# AcWing 872. 最大公约数 — 最大公约数

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/872/

## 题目描述

给定`n`对正整数`ai, bi`，请你求出每对数的最大公约数。

### 输入格式

第一行包含整数`n`。

接下来`n`行，每行包含一个整数对`ai, bi`。

**数据范围**

`1≤n≤10^5`

`1≤ai, bi≤2×10^9`

### 输出格式

输出共`n`行，每行输出一个整数对的最大公约数。

### 样例

**输入:**
```
2
3 6
4 6
```

**输出:**
```
3
2
```

### 提示

原题链接

Y总讲解

参考题解

Y总代码

## AC代码

```cpp
#include <iostream>
using namespace std;

// 利用性质：gcd(a , b) == gcd(b,a mod b)
int gcd(int a, int b){
    return b? gcd(b, a%b) :a;
}

int main()
{
    int n;
    cin>>n;
    while (n--){
        int a,b;
        cin>>a>>b;
        cout<<gcd(a,b)<<endl;
    }
    return 0;
}
```
