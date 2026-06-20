# NQ009：时间转换

> 题目来源：AcWing 654 | 题目ID：ACW654 | 第1章 程序设计的第一个脚印

## 题目描述
将总秒数N转换为HH:MM:SS格式。

### 输入格式
一个整数N，表示总秒数。

### 输出格式
HH:MM:SS格式的时间。

### 样例
**输入：**
```
556
```
**输出：**
```
0:9:16
```

## 解题思路
时 = N/3600，分 = N%3600/60，秒 = N%60。Python的divmod()可同时获得商和余数。

## 编程技巧
Python的divmod(a,b)返回(商,余数)元组。链式调用：h,r=divmod(n,3600); m,s=divmod(r,60)。

## 参考代码

### C++
```cpp
#include <cstdio>
int main() { int n; scanf("%d",&n); printf("%d:%d:%d",n/3600,n%3600/60,n%60); return 0; }
```

### Python
```python
n = int(input())
h, r = divmod(n, 3600)
m, s = divmod(r, 60)
print(f"{h}:{m}:{s}")
```
