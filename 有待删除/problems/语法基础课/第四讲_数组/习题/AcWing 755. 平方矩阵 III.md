# AcWing 755. 平方矩阵 III — 平方矩阵 III

**难度:** 简单 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/755/

## 题目描述

输入整数 N，输出一个 N 阶的二维数组 M，这个 N 阶二维数组满足 M[i][j] = 2^(i+j)。

具体形式可参考样例。

### 输入格式

输入包含多行，每行包含一个整数 N。当输入行为 N = 0 时，表示输入结束，且该行无需作任何处理。

数据范围0≤N≤15

### 输出格式

对于每个输入整数 N，输出一个满足要求的 N 阶二维数组。每个数组占 N 行，每行包含 N 个用空格隔开的整数，输出完毕后需再输出一个空行。

### 样例

**输入:**
```
1
2
3
4
5
0
```

**输出:**
```
1

1 2
2 4

1 2 4
2 4 8
4 8 16

1 2 4 8
2 4 8 16
4 8 16 32
8 16 32 64

1 2 4 8 16
2 4 8 16 32
4 8 16 32 64
8 16 32 64 128
16 32 64 128 256
```

### 提示

注意输出格式。

## AC代码

```cpp
#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    int n;
    while (cin >> n, n)
    {
      for (int i = 0; i < n; i ++ )
      {
        for (int j = 0; j < n; j ++ )
        {
          int v = 1;
          for (int k = 0; k < i + j; k ++ ) v *= 2;
          cout << v << ' ';
        }
        cout << endl;
      }

      cout << endl;
    }

    return 0;
}
```
