# NQ014：最大值

> 题目来源：AcWing 614 | 题目ID：ACW614 | 第1章 程序设计的第一个脚印

## 题目描述
输入三个整数a、b、c，输出其中的最大者。

### 输入格式
一行，三个整数，用空格隔开。

### 输出格式
一个整数，即三个数中的最大值。

### 样例
**输入：**
```
7 14 106
```
**输出：**
```
106
```

## 解题思路
Python的max(a,b,c)直接接收多参数。C++需max({a,b,c})（C++11）或嵌套调用。

## 编程技巧
Python内置max/min/sum等。C++的<algorithm>提供类似功能。Python的设计哲学是"电池已包含"。

## 参考代码

### C++
```cpp
#include <iostream>
#include <algorithm>
using namespace std;
int main() { int a,b,c; cin>>a>>b>>c; cout<<max({a,b,c})<<endl; return 0; }
```

### Python
```python
a, b, c = map(int, input().split())
print(max(a, b, c))
```
