# AcWing 84. 求1+2+…+n — 求 1+2+...+n

**难度:** 简单 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/84/

## 题目描述

求`1+2+...+n`，要求不能使用乘除法、for、while、if、else、switch、case 等关键字及条件判断语句 (A?B : C)。

### 输入格式

输入一个整数`n`。

数据范围：`1 ≤ n ≤ 50000`

### 输出格式

输出`1+2+...+n`的结果。

### 样例

**输入:**
```
10
```

**输出:**
```
55
```

### 提示

注意输出格式。

## AC代码

```cpp
class Solution {
public:
    int getSum(int n) {
        int res = n;
        n > 0 && (res += getSum(n - 1));
        return res;
    }
};
```
