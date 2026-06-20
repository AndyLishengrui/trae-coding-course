# AcWing 828. 模拟栈 — 模拟栈

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/828/

## 题目描述

实现一个栈，栈初始为空，支持四种操作：

(1) “push x” – 向栈顶插入一个数x；

(2) “pop” – 从栈顶弹出一个数；

(3) “empty” – 判断栈是否为空；

(4) “query” – 查询栈顶元素。

现在要对栈进行M个操作，其中的每个操作3和操作4都要输出相应的结果。

1≤M≤100000,

1≤x≤10^9

所有操作保证合法。

### 输入格式

第一行包含整数M，表示操作次数。

接下来M行，每行包含一个操作命令，操作命令为”push x”，”pop”，”empty”，”query”中的一种。

### 输出格式

对于每个”empty”和”query”操作都要输出一个查询结果，每个结果占一行。

其中，”empty”操作的查询结果为“YES”或“NO”，”query”操作的查询结果为一个整数，表示栈顶元素的值。

### 样例

**输入:**
```
10
push 5
query
push 6
pop
query
pop
empty
push 4
query
empty
```

**输出:**
```
5
5
YES
4
NO
```

### 提示

原题

## AC代码

```cpp
#include <iostream>

using namespace std;
const int N = 100010;

int m;
int stk[N], tt;//数组模拟栈

int main()
{
  cin>>m;
  while (m --)
  {
    string op;
    int x;

    cin>>op;
    if (op == "push")//栈顶指针+1，把数压入数组
    {
      cin >> x;
      stk[++tt] = x;//压入一个元素
    }
    else if (op == "pop") tt --;//修改栈顶指针即可
    else if (op == "empty") cout << (tt? "NO":"YES") <<endl;//tt>0表示非空
    else cout<<stk[tt]<<endl;//返回栈顶
  }
}
```
