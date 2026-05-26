# NQ001：A + B

> 题目来源：AcWing 1 | 题目ID：ACW001 | 第1章 程序设计的第一个脚印

## 题目描述
输入两个整数A和B，计算它们的和。这是学习编程的第一道题。

### 输入格式
一行，两个整数A和B，用空格隔开。

### 输出格式
一个整数，即A+B的结果。

### 样例
**输入：**
```
3 4
```
**输出：**
```
7
```

## 解题思路
这是编程中最简单的题目，但它包含了所有程序的基本骨架：读入数据→计算→输出结果。C++用cin/cout，Python用input/print。两种语言体现了静态类型和动态类型的设计哲学差异。

## 编程技巧
Python的map(int, input().split())是处理空格分隔整数输入的标准写法。C++的cin >> a >> b自动跳过空白字符。

## 参考代码

### C++
```cpp
#include <iostream>
using namespace std;
int main() { int a, b; cin >> a >> b; cout << a + b << endl; return 0; }
```

### Python
```python
a, b = map(int, input().split())
print(a + b)
```
