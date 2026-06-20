# NQ010：简单乘积

> 题目来源：AcWing 605 | 题目ID：ACW605 | 第1章 程序设计的第一个脚印

## 题目描述
读取两个整数，输出"PROD = "后跟它们的乘积。

### 输入格式
两行，每行一个整数。

### 输出格式
输出"PROD = X"。

### 样例
**输入：**
```
3
9
```
**输出：**
```
PROD = 27
```

## 解题思路
和第1题结构完全相同，只需把+改成*，添加"PROD = "前缀。

## 编程技巧
修改已有代码比从零开始更高效。用AI把L1的代码改成乘法版本。

## 参考代码

### C++
```cpp
#include <iostream>
using namespace std;
int main() { int a,b; cin>>a>>b; cout<<"PROD = "<<a*b<<endl; return 0; }
```

### Python
```python
a = int(input())
b = int(input())
print(f"PROD = {a * b}")
```
