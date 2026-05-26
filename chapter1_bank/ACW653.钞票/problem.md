# NQ008：钞票

> 题目来源：AcWing 653 | 题目ID：ACW653 | 第1章 程序设计的第一个脚印

## 题目描述
给定金额N，用最少的钞票数量支付。面额：100,50,20,10,5,2,1。

### 输入格式
一个整数N。

### 输出格式
第一行输出N。然后7行，按面额从大到小输出"X nota(s) de R$ Y,00"。

### 样例
**输入：**
```
576
```
**输出：**
```
576
5 nota(s) de R$ 100,00
1 nota(s) de R$ 50,00
1 nota(s) de R$ 20,00
0 nota(s) de R$ 10,00
1 nota(s) de R$ 5,00
0 nota(s) de R$ 2,00
1 nota(s) de R$ 1,00
```

## 解题思路
贪心算法雏形：从最大面额开始，每次尽可能多地使用当前面额。count = N // face_value; N %= face_value。Python用列表+循环消除重复代码。

## 编程技巧
Python用列表+循环消除重复代码：for v in [100,50,20,10,5,2,1]。C++中消除重复是重要的工程思维。

## 参考代码

### C++
```cpp
#include <cstdio>
int main() { int n,s[]={100,50,20,10,5,2,1}; scanf("%d",&n); printf("%d\n",n); for(int i=0;i<7;i++){printf("%d nota(s) de R$ %d,00\n",n/s[i],s[i]);n%=s[i];} return 0; }
```

### Python
```python
n = int(input())
print(n)
for v in [100,50,20,10,5,2,1]:
    print(f"{n // v} nota(s) de R$ {v},00")
    n %= v
```
