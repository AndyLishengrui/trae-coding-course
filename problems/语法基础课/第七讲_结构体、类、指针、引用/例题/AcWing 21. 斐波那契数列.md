# AcWing 21. 斐波那契数列 — 斐波那契数列

**难度:** 简单 | **时间限制:** 1000ms | **内存限制:** 64MB

> 原题链接: https://www.acwing.com/problem/content/21/

## 题目描述

输入一个整数`n`，要求斐波那契数列的第`n`项。

假定从`0`开始，第`0`项为`0`。

### 输入格式

输入一个整数`n`。

数据范围：`0 ≤ n ≤ 39`

### 输出格式

返回斐波那契数列的第`n`项。

### 样例

**输入:**
```
5
```

**输出:**
```
5
```

### 提示

注意输出格式。

## AC代码

```cpp
class Solution {
public:
    int Fibonacci(int n) {
        if (n <= 1) return n;
        return Fibonacci(n - 1) + Fibonacci(n - 2);
    }
};
```
