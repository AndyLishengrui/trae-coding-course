# AcWing 835. Trie字符串统计 — Trie字符串统计

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/835/

## 题目描述

维护一个字符串集合，支持两种操作：

“I x”向集合中插入一个字符串x；“Q x”询问一个字符串在集合中出现了多少次。共有N个操作，输入的字符串总长度不超过105105，字符串仅包含小写英文字母。

数据范围：

1≤N≤2∗10^4

### 输入格式

第一行包含整数N，表示操作数。

接下来N行，每行包含一个操作指令，指令为”I x”或”Q x”中的一种。

### 输出格式

对于每个询问指令”Q x”，都要输出一个整数作为结果，表示x在集合中出现的次数。

每个结果占一行。

### 样例

**输入:**
```
5
I abc
Q abc
Q ab
I ab
Q ab
```

**输出:**
```
1
0
1
```

### 提示

原题

## AC代码

```cpp
#include <iostream>
using namespace std;

const int N = 100007;
int son[N][26];     //输入数据只有小写字母26个
int pcount[N]; //字符串结束标记
int idx;            //Trie树一共有多少个节点
char str_op[2], str[N];
void insert(char str[])
{
    int parent = 0;
    for (int i = 0; str[i]; i++) //字符串最后一个为\0
    {
        int value = str[i] - 'a';
        if (!son[parent][value])
            son[parent][value] = ++idx;
        parent = son[parent][value]; //设置为父节点，接着执行插入
    }
    pcount[parent]++; //插入字符串的最后一个字母打上标记
}

int query(char str[])
{
    int parent = 0;
    for (int i = 0; str[i]; i++)
    {
        int value = str[i] - 'a';
        if (!son[parent][value])
            return 0; //查找不到，返回0
        parent = son[parent][value];
    }
    return pcount[parent]; //返回结束标记，0表示查找不到
}

int main()
{
    // 第一行包含整数N，表示操作数。
    int n;
    cin >> n;
    // 接下来N行，每行包含一个操作指令，指令为”I x”或”Q x”中的一种。
    while (n--)
    {
        cin >> str_op >> str;
        if (str_op[0] == 'I')
            insert(str);           //插入str
        else if (str_op[0] == 'Q') //查询并且输出
            cout << query(str) << endl;
    }

    return 0;
}
```
