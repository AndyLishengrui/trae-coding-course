# AcWing 899. 编辑距离 — 编辑距离

**难度:** 困难 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/899/

## 题目描述

给定n个长度不超过10的字符串以及m次询问，每次询问给出一个字符串和一个操作次数上限。

对于每次询问，请你求出给定的n个字符串中有多少个字符串可以在上限操作次数内经过操作变成询问给出的字符串。

每个对字符串进行的单个字符的插入、删除或替换算作一次操作。

数据范围1≤n,m≤1000

### 输入格式

第一行包含两个整数n和m。

接下来n行，每行包含一个字符串，表示给定的字符串。

再接下来m行，每行包含一个字符串和一个整数，表示一次询问。

字符串中只包含小写字母，且长度均不超过10。

### 输出格式

输出共m行，每行输出一个整数作为结果，表示一次询问中满足条件的字符串个数。

### 样例

**输入:**
```
3 2
abc
acd
bcd
ab 1
acbd 2
```

**输出:**
```
1
3
```

### 提示

原题链接

## AC代码

```cpp
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 1007;

string a[N];
int f[N][N];
int n,m;

int edit_distance(string a, string b)
{
  a = " "+ a, b = " "+ b;//前置加一个空格，让处理的下标从1开始
  int la = a.length(), lb = b.length();

  //初始化变化为空串的操作数
  for (int i = 0; i <= la; i++) f[i][0] = i;
  for (int i = 0; i <= lb; i++) f[0][i] = i;
  // 动态规划递推
  for (int i = 1; i <= la; i++)
   for (int j = 1; j <= lb; j++)
   {
     f[i][j] = min(f[i-1][j]+1, f[i][j-1]+1);
     f[i][j] = min(f[i][j], f[i-1][j-1]+(a[i]!=b[j]));
   }
  return f[la][lb];

}

int main()
{
    cin>>n>>m;
    //讀入n個字符串
    for(int i = 0; i < n; i++) cin>>a[i];

    while (m -- )
    {
      string b;
      cin>>b;
      int steps;
      cin>>steps;
      //统计有多少a[i]与b的编辑距离小于steps
      int res = 0;
      for (int i = 0; i <n; i++) {
        if (edit_distance(a[i],b) <= steps) res ++;
      }
      cout<<res<<endl;
    }
    return 0;
}
```
