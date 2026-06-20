# AcWing 338. 计数问题 — 计数问题

**难度:** 困难 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/338/

## 题目描述

给定两个整数 a 和 b，求 a 和 b 之间的所有数字中0~9的出现次数。

例如，a=1024，b=1032，则 a 和 b 之间共有9个数如下：

1024 1025 1026 1027 1028 1029 1030 1031 1032

其中‘0’出现10次，‘1’出现10次，‘2’出现7次，‘3’出现3次等等…

数据范围0<a,b<100000000

### 输入格式

输入包含多组测试数据。

每组测试数据占一行，包含两个整数 a 和 b。

当读入一行为0 0时，表示输入终止，且该行不作处理。

### 输出格式

每组数据输出一个结果，每个结果占一行。

每个结果包含十个用空格隔开的数字，第一个数字表示‘0’出现的次数，第二个数字表示‘1’出现的次数，以此类推。

### 样例

**输入:**
```
1 10
44 497
346 542
1199 1748
1496 1403
1004 503
1714 190
1317 854
1976 494
1001 1960
0 0
```

**输出:**
```
1 2 1 1 1 1 1 1 1 1
85 185 185 185 190 96 96 96 95 93
40 40 40 93 136 82 40 40 40 40
115 666 215 215 214 205 205 154 105 106
16 113 19 20 114 20 20 19 19 16
107 105 100 101 101 197 200 200 200 200
413 1133 503 503 503 502 502 417 402 412
196 512 186 104 87 93 97 97 142 196
398 1375 398 398 405 499 499 495 488 471
294 1256 296 296 296 296 287 286 286 247
```

### 提示

原题链接

## AC代码

```cpp
//完全参考Y总代码
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 10;

//数组num[i]的[l,r]各个数转换为十进制数
int get(vector<int> num, int l, int r)
{
  int res = 0;
  for (int i = l; i >= r; i--) res = res * 10 + num[i];
  return res;
}
//计算10的x次方
int power10(int x)
{
  int res = 1;
  while (x --) res *=10;
  return res;
}

int count(int n, int x)
{
  if (!n) return 0;

  vector<int> num;
  //n转换为数组
  while (n)
  {
    num.push_back(n % 10);
    n /= 10;
  }
  n = num.size();//存储几位数

  int res = 0;
  for (int i = n -1 - !x; i >=0; i--)
  {
    if (i < n - 1)
    {
      res += get(num, n-1, i+1) * power10(i);
      if (!x) res -= power10(i);//去掉首字母为0的情况
    }

    if (num[i] == x) res += get(num,i-1,0) + 1;
    else if (num[i]>x) res+=power10(i);
  }
  return res;
}

int main()
{
    int a,b;
    while (cin>>a>>b, a)
    {
      if (a>b) swap(a,b);
      for (int i = 0; i <=9; i++)//计算前缀和的思想
        cout<<count(b,i)- count(a-1,i) <<' ';
      cout <<endl;
    }
    return 0;
}
```
