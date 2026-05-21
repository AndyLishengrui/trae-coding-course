# AcWing 840. 模拟散列表 — 哈希试炼之模拟散列表

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/840/

## 题目描述

维护一个集合，支持如下几种操作：

“I x”，插入一个数 x；

“Q x”，询问数 x 是否在集合中出现过；

现在要进行 N 次操作，对于每个询问操作输出对应的结果。

**数据范围**：

1≤N≤10^5

−10^9≤x≤10^9

### 输入格式

第一行包含整数 N，表示操作数量。

接下来 N 行，每行包含一个操作指令，操作指令为“I x”，“Q x”中的一种。

### 输出格式

对于每个询问指令“Q x”，输出一个询问结果，如果 x 在集合中出现过，则输出“Yes”，否则输出“No”。

每个结果占一行。

### 样例

**输入:**
```
5
I 1
I 2
I 3
Q 2
Q 5
```

**输出:**
```
Yes
No
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

using namespace std;
const int N = 100007;//质数

int h[N], e[N], ne[N], idx;

void insert(int x)
{
  int k = (x % N + N) % N;//把负数映射成正数
  e[idx] = x, ne[idx] = h[k], h[k] = idx++;
}

bool find(int x)
{
  int k = (x % N + N) % N;//把负数映射成正数
  for (int i = h[k]; i!=-1; i=ne[i])
    if (e[i] == x) return true;

  return false;
}

int main()
{
    int n;
    cin>>n;

    memset(h, -1, sizeof h);//清空链表头数组

    while (n -- )
    {
     string op;//操作数
     int x;
     cin>>op>>x;//读入操作指令

     if (op=="I") insert(x);
     else {
       if (find(x)) puts("Yes");
       else puts("No");
     }
    }

    return 0;
}
```
