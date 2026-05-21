# AcWing 812. 打印数字 — 打印数字

**难度:** 简单 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/812/

## 题目描述

输入一个长度为 n 的数组 a 和一个整数 size，请编写一个函数 void print(int a[], int size)，打印数组 a 中的前 size 个数。

注意：对于 Python 语言，print 是内置函数，所以本题中使用 print1D() 这个函数名，来避免跟内置函数产生冲突。

### 输入格式

第一行包含两个整数 n 和 size。
第二行包含 n 个整数 a[i]，表示整个数组。

数据范围：`1 ≤ n ≤ 1000`，`1 ≤ size ≤ n`

### 输出格式

共一行，包含 size 个整数，表示数组的前 size 个数。

### 样例

**输入:**
```
5 3
1 2 3 4 5
```

**输出:**
```
1 2 3
```

### 提示

注意输出格式。

来源：语法题

## AC代码

```cpp
#include <iostream>

using namespace std;

const int N = 1010;

void print(int a[], int size)
{
    for (int i = 0; i < size; i ++ )
        cout << a[i] << ' ';
    cout << endl;    

}

int main()
{
    int n, size;
    int a[N];

    cin >> n >> size;
    for (int i = 0; i < n; i ++ ) cin >> a[i];

    print(a, size);

    return 0;
}
```
