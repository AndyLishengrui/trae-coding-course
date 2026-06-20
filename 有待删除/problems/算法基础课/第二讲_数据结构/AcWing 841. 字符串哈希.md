# AcWing 841. 字符串哈希 — 哈希试炼之字符串哈希

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/841/

## 题目描述

给定一个长度为`n`的字符串，再给定`m`个询问，每个询问包含四个整数`l1`,`r1`,`l2`,`r2`。

请你判断`[l1, r1]`和`[l2, r2]`这两个区间所包含的字符串子串是否完全相同。

字符串中只包含大小写英文字母和数字。

### 输入格式

第一行包含整数`n`和`m`，表示字符串长度和询问次数。

第二行包含一个长度为`n`的字符串，字符串中只包含大小写英文字母和数字。

接下来`m`行，每行包含四个整数`l1`,`r1`,`l2`,`r2`，表示一次询问所涉及的两个区间。

注意，字符串的位置从 1 开始编号。

### 输出格式

对于每个询问输出一个结果，如果两个字符串子串完全相同则输出`Yes`，否则输出`No`。

每个结果占一行。

**数据范围**1≤`n`,`m`≤10^5

### 样例

**输入:**
```
8 3
aabbaabb
1 3 5 7
1 3 6 8
1 2 1 2
```

**输出:**
```
Yes
No
Yes
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
//P进制其中P取131，Hash的边界取2^64，因此用unsigned long long来存储省掉mod的操作
typedef unsigned long long ULL;
const int N = 100007, P = 131;
int n, m;               //n为待匹配字符串长度
char str[N];            //str搜索范围
ULL hashTable[N], p[N]; // hashTable存放字符串的前缀值,p为P进制的基数组
ULL gethashId(int left, int right)
{
    return hashTable[right] - hashTable[left - 1] * p[right - left + 1];
}
//初始化P进制的基数组
void initP(int n)
{
    p[0] = 1; //这里是1不是0.最低位的基是1
    for (int i = 1; i <= n; i++)
    {
        p[i] = p[i - 1] * P;
    }
}
int main()
{
    // 第一行包含整数n和m，表示字符串长度和询问次数。
    // 第二行包含一个长度为n的字符串，字符串中只包含大小写英文字母和数字。
    // 接下来m行，每行包含四个整数l1,r1,l2,r2，表示一次询问所涉及的两个区间。
    // 注意，字符串的位置从1开始编号。
    cin >> n >> m >> str + 1; //字符串从1开始存储，cin会在末尾加上\0
    // cout<<str+1<<endl;
    //初始化P进制的基数组
    initP(n);
    //预处理前缀hash表
    for (int i = 1; i <= n; i++)
        hashTable[i] = hashTable[i - 1] * P + str[i];
    //处理m个询问
    while (m--)
    {
        int l1, r1, l2, r2;
        cin >> l1 >> r1 >> l2 >> r2;
        //哈希值相等就认为字串相等,不重复的hash映射
        if (gethashId(l1, r1) == gethashId(l2, r2))
            cout << "Yes" << endl;
        else
            cout << "No" << endl;
    }
    return 0;
}
```
