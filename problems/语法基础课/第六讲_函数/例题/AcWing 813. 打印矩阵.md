# AcWing 813. 打印矩阵 — 打印矩阵

**难度:** 简单 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/813/

## 题目描述

给定一个 row x col 的二维数组 a，请编写一个函数 void print2D(int a[][N], int row, int col)，

打印数组构成的 row 行，col 列的矩阵。

注意，每打印完一整行需要输出一个回车。

### 输入格式

第一行包含两个整数 row, col。
接下来 row 行，每行包含 col 个整数，表示完整二维数组 a。

数据范围：`1 ≤ row ≤ 100`，`1 ≤ col ≤ 100`

### 输出格式

共 row 行，每行 col 个整数，表示打印出的矩阵。

### 样例

**输入:**
```
3 4
1 3 4 5
2 6 9 4
1 4 7 5
```

**输出:**
```
1 3 4 5
2 6 9 4
1 4 7 5
```

### 提示

注意输出格式。

来源：语法题

## AC代码

```cpp
#include <iostream>

using namespace std;

void print2D(int a[][100], int row, int col)
{
    for (int i = 0; i < row; i ++ )
    {
      for (int j = 0; j < col; j ++ )
          cout << a[i][j] << ' ';
      cout << endl;    
    }
}

int main()
{
    int a[100][100];

    int row, col;

    cin >> row >> col;
    for (int i = 0; i < row; i ++ )
        for (int j = 0; j < col; j ++ )
            cin >> a[i][j];

    print2D(a, row, col);        

    return 0;
}
```
