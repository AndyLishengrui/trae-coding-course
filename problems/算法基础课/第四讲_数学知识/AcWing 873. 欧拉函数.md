# AcWing 873. 欧拉函数 — 欧拉函数

**难度:** 中等 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/873/

## 题目描述

给定 n 个正整数 ai，求出每个数的欧拉函数。欧拉函数 ϕ(N) 表示 1∼N 中与 N 互质的数的个数。

### 输入格式

第一行包含整数 n。接下来 n 行，每行包含一个正整数 ai。

### 输出格式

共 n 行，其中第 i 行输出 ai的欧拉函数。

### 样例

**输入:**
```
3
3
6
8
```

**输出:**
```
2
2
4
```

### 提示

利用质因数分解以及公式 ϕ(N) = N × Π(1 - 1/p) 计算欧拉函数。

参考题解

Y总讲解

Y总代码

## AC代码

```cpp
//Andy代码，参考Y总
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

int main()
{
    int n; cin>>n;
    while (n -- )
    {
      int a; cin>>a;
      int res = a;
      //分解质因子,用题目公式直接计算
      for (int i = 2; i <= a /i; i++)
      if (a % i == 0)
      {
        res = res /i * (i-1);//取整，调换*与/的次序
        while (a % i == 0) a /=i;
      }

      if (a > 1) res = res /a *(a-1);

      cout<< res<<endl;
    }
    return 0;
}
```
