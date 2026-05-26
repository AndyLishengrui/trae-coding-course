# NQ006：油耗

> 题目来源：AcWing 615 | 题目ID：ACW615 | 第1章 程序设计的第一个脚印

## 题目描述
输入行驶距离(km)和消耗汽油量(L)，计算每升汽油行驶的公里数。

### 输入格式
两行：距离(float)和汽油量(float)。

### 输出格式
保留3位小数，后跟" km/l"。

### 样例
**输入：**
```
500
35.0
```
**输出：**
```
14.286 km/l
```

## 解题思路
燃油效率 = 距离 / 油耗。使用浮点数除法。输出保留3位小数。

## 编程技巧
C++中整数除法会截断。如果距离是int需要先转double。Python中/自动浮点。

## 参考代码

### C++
```cpp
#include <cstdio>
int main() { double x,y; scanf("%lf%lf",&x,&y); printf("%.3lf km/l\n",x/y); return 0; }
```

### Python
```python
x = float(input())
y = float(input())
print(f"{x / y:.3f} km/l")
```
