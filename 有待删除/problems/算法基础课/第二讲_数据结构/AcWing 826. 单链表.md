# AcWing 826. 单链表 — 单链表

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/826/

## 题目描述

实现一个单链表，链表初始为空，支持三种操作：

(1) 向链表头插入一个数；

(2) 删除第k个插入的数后面的数；

(3) 在第k个插入的数后插入一个数

现在要对该链表进行M次操作，进行完所有操作后，从头到尾输出整个链表。

1≤M≤100000

所有操作保证合法。

注意:题目中第k个插入的数并不是指当前链表的第k个数。例如操作过程中一共插入了n个数，则按照插入的时间顺序，这n个数依次为：第1个插入的数，第2个插入的数，…第n个插入的数。

### 输入格式

第一行包含整数M，表示操作次数。

接下来M行，每行包含一个操作命令，操作命令可能为以下几种：

(1) “H x”，表示向链表头插入一个数x。

(2) “D k”，表示删除第k个输入的数后面的数（当k为0时，表示删除头结点）。

(3) “I k x”，表示在第k个输入的数后面插入一个数x（此操作中k均大于0）。

### 输出格式

共一行，将整个链表从头到尾输出。

### 样例

**输入:**
```
10
H 9
I 1 1
D 1
D 0
H 6
I 3 6
I 4 5
I 4 5
I 3 4
D 6
```

**输出:**
```
6 4 6 5
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

const int N = 100010;

// head 表示头节点的下标， e[N]表示节点i的值
// ne[N]表示节点i的next指针是多少，idx存储当前已经用到了哪个节点
int head, e[N], ne[N], idx;

void init()
{
    head = -1;//一开始设置为-1
    idx = 0;//当前用到了0个节点
}

//将x插入到头节点
void add_to_head(int x)
{
  e[idx]=x, ne[idx] = head, head = idx, idx ++;
}
//将x插到下标是k的点后面
void add(int k, int x)
{
  e[idx]=x, ne[idx]=ne[k], ne[k] = idx, idx ++;
}
//将下标是k的点后面的点删掉
void remove(int k)
{
  ne[k] = ne[ne[k]];
  //idx--;
}
int main()
{
  int m; cin>>m;

  init();//初始化

  while (m --)
  {
   int k, x;
   char op;//操作字符

   cin>>op;
   if (op == 'H') 
   {
     cin >> x;
     add_to_head(x);
   }
   else if (op == 'D')
   {
     cin >> k;
     if (!k) head = ne[head];//删除头节点
     else remove(k-1);
   }
   else 
   {
     cin >> k >> x;
     add(k-1, x);
   }
  }
  //打印单链表
  for (int i = head; i!=-1; i = ne[i]) cout << e[i] << ' ';
  cout << endl;
}
```
