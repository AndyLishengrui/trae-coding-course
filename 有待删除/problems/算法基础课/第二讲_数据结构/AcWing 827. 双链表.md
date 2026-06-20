# AcWing 827. 双链表 — 双链表

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/827/

## 题目描述

实现一个双链表，双链表初始为空，支持5种操作：

(1) 在最左侧插入一个数；

(2) 在最右侧插入一个数；

(3) 将第k个插入的数删除；

(4) 在第k个插入的数左侧插入一个数；

(5) 在第k个插入的数右侧插入一个数

现在要对该链表进行M次操作，进行完所有操作后，从左到右输出整个链表。

数据范围

1≤M≤100000

所有操作保证合法。

注意:题目中第k个插入的数并不是指当前链表的第k个数。例如操作过程中一共插入了n个数，则按照插入的时间顺序，这n个数依次为：第1个插入的数，第2个插入的数，…第n个插入的数。

### 输入格式

第一行包含整数M，表示操作次数。

接下来M行，每行包含一个操作命令，操作命令可能为以下几种：

(1) “L x”，表示在链表的最左端插入数x。

(2) “R x”，表示在链表的最右端插入数x。

(3) “D k”，表示将第k个插入的数删除。

(4) “IL k x”，表示在第k个插入的数左侧插入一个数。

(5) “IR k x”，表示在第k个插入的数右侧插入一个数。

### 输出格式

共一行，将整个链表从左到右输出。

### 样例

**输入:**
```
10
R 7
D 1
L 3
IL 2 10
D 3
IL 2 7
L 8
R 9
IL 4 7
IR 2 2
```

**输出:**
```
8 7 7 3 2 9
```

### 提示

原题链接

Y总代码

Y总讲解

参考题解

## AC代码

```cpp
#include <iostream>

using namespace std;

const int N = 100010;//最大值

int e[N],l[N],r[N],idx;
//初始化
void init()
{
  //0表示head，1表示tail
  r[0] = 1, l[1] = 0;
  idx = 2;//一开始就有两个顶点e[0], e[1]
}
//在下标是k的点右边，插入x
void insert(int k, int x)
{
  e[idx] = x;//新节点
  r[idx] = r[k];
  l[idx] = k;

  l[r[k]] = idx;//修改原链表指针
  r[k]= idx++;
}
//删除第k个点
void remove(int k)
{
  r[l[k]]= r[k];//k左边点的右指针指向k右边的点
  l[r[k]]= l[k];//k右边点的左指针指向k左边的点
}

int main()
{
  int m; cin>>m;

  init();//初始化

  while (m --)
  {
   int k, x;

   string op;//操作字符
   cin>>op;

   //(1) “L x”，表示在链表的最左端插入数x。
   if (op == "L") 
   {
     cin >> x;
     insert(0,x);
   }
   else if(op == "R")
   {//(2) “R x”，表示在链表的最右端插入数x。
     cin >> x;
     insert(l[1],x);
   }
   else if (op == "D")
   {//(3) “D k”，表示将第k个插入的数删除。
     cin >> k;
    remove(k+1);
   }
   else if (op == "IL")
   {//(4) “IL k x”，表示在第k个插入的数左侧插入一个数。
     cin>>k>>x;
     insert(l[k+1],x);
   }
   else 
   {//(5) “IR k x”，表示在第k个插入的数右侧插入一个数。
     cin>>k>>x;
     insert(k+1,x);
   }

  }
  //打印双链表,1是tail
  for (int i = r[0]; i!=1; i = r[i]) cout << e[i] << ' ';
  cout << endl;

  return 0;
}
```
