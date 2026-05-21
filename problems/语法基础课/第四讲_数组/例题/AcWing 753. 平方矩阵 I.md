# AcWing 753. 平方矩阵 I — 平方矩阵 I

**难度:** 简单 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/753/

## 题目描述

输入整数 N，输出一个 N 阶的回字形状二维数组。

数组的最外层为 1，次外层为 2，以此类推。

### 输入格式

输入包含多行，每行包含一个整数 N。

当输入行为 N = 0 时，表示输入结束，且该行无需作任何处理。

数据范围0≤N≤100

### 输出格式

对于每个输入整数 N，输出一个满足要求的 N 阶二维数组。每个数组占 N 行，每行包含 N 个用空格隔开的整数。每个数组输出完毕后，输出一个空行。

### 样例

**输入:**
```
1
2
3
4
0
```

**输出:**
```
1

1 1
1 1

1 1 1
1 2 1
1 1 1

1 1 1 1
1 2 2 1
1 2 2 1
1 1 1 1
```

### 提示

注意输出格式。

## AC代码

```cpp
#include <iostream>

using namespace std;

int main()
{
    int n;
    while (cin >> n, n)
    {
      for (int i = 1; i <= n; i ++ )
      {
        for (int j = 1; j <= n; j ++ )
        {
         int up = i, down = n - i + 1, left = j, right = n - j + 1;
         cout << min(min(up, down), min(left, right)) << ' ';
        }
        cout << endl;
      }

      cout << endl;
    }

    return 0;
}
```
