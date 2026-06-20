# AcWing 839. 模拟堆 — 模拟堆

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/839/

## 题目描述

维护一个集合，初始时集合为空，支持如下几种操作：

“I x”，插入一个数x；“PM”，输出当前集合中的最小值；“DM”，删除当前集合中的最小值（数据保证此时的最小值唯一）；“D k”，删除第k个插入的数；“C k x”，修改第k个插入的数，将其变为x；现在要进行N次操作，对于所有第2个操作，输出当前集合的最小值。

1≤N≤10^5

−109≤x≤10^9

数据保证合法。

### 输入格式

第一行包含整数N。

接下来N行，每行包含一个操作指令，操作指令为”I x”，”PM”，”DM”，”D k”或”C k x”中的一种。

### 输出格式

对于每个输出指令“PM”，输出一个结果，表示当前集合中的最小值。

每个结果占一行。

### 样例

**输入:**
```
8
I -10
PM
I -10
D 1
C 2 8
I 6
PM
DM
```

**输出:**
```
-10
6
```

### 提示

原题链接

Y总讲解

## AC代码

```cpp
#include <iostream>
#include <algorithm>
#include <string.h>

using namespace std;

const int N = 100007;

// hp是heap pointer的缩写，表示堆数组中下标到第k个插入的映射
// ph是pointer heap的缩写，表示第k个插入到堆数组中的下标的映射
// hp和ph数组是互为反函数的
int h[N],ph[N],hp[N],cnt;

void heap_swap(int a, int b)
{
  swap(ph[hp[a]],ph[hp[b]]);//堆数组的下标
  swap(hp[a],hp[b]);//下标与第几个插入元素的映射
  swap(h[a],h[b]);//堆元素
}

void down(int u)
{
  int t = u;
  if (u*2<=cnt && h[u*2]<h[t]) t = u*2;//u*2左儿子
  if (u*2+1 <= cnt && h[u*2+1]<h[t]) t = u*2+1;// u*2+1右儿子
  if (u != t)
  {
    heap_swap(u,t);
    down(t);
  }
}

void up(int u)
{
  while (u/2 && h[u] < h[u/2])
  {
    heap_swap(u,u/2);
    u >>= 1;
  }
}

int main()
{
  int n,m=0;
  scanf("%d",&n);
  while(n --) 
  {
    char op[5];
    int k,x;
    scanf("%s",op);
    //在堆最后一个元素插入元素
    if (!strcmp(op,"I"))
    {
      scanf("%d",&x);
      cnt ++;
      m++;
      ph[m] = cnt, hp[cnt] = m;
      h[cnt] = x;
      up(cnt); //插入后执行up(cnt)
    }
    else if (!strcmp(op,"PM")) printf("%d\n",h[1]);//堆顶是最小值
    else if (!strcmp(op,"DM"))
    {
      heap_swap(1,cnt);
      cnt --;
      down(1); //删除最小值后执行down(1)
    }
    else if (!strcmp(op,"D"))
    {
      scanf("%d",&k);//删除第k个元素
      k = ph[k];//取第k个元素下标
      heap_swap(k,cnt);//与最后一个元素交换
      cnt--;
      up(k);
      down(k);
    }
    else {
      scanf("%d%d",&k,&x);//修改第k个数
      k = ph[k];
      h[k] = x;
      up(k);
      down(k);
    }
  }
  return 0;
}
```
