# NQ007：两点间的距离

> 题目来源：AcWing 616 | 题目ID：ACW616 | 第1章 程序设计的第一个脚印

## 题目描述
给定两点坐标P1(x1,y1)和P2(x2,y2)，计算欧几里得距离。

### 输入格式
一行，四个浮点数x1 y1 x2 y2。

### 输出格式
距离，保留4位小数。

### 样例
**输入：**
```
1.0 7.0 5.0 9.0
```
**输出：**
```
4.4721
```

## 解题思路
欧几里得距离 = √((x1-x2)² + (y1-y2)²)。需要使用数学库：C++的cmath/sqrt，Python的math.sqrt。

## 编程技巧
C++需要#include<cmath>并链接-lm。Python的import math后math.sqrt()简洁明了。注意用double不用float（精度更高）。

## 参考代码

### C++
```cpp
#include <cstdio>
#include <cmath>
int main() { double x1,y1,x2,y2; scanf("%lf%lf%lf%lf",&x1,&y1,&x2,&y2); printf("%.4lf\n",sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))); return 0; }
```

### Python
```python
import math
x1, y1, x2, y2 = map(float, input().split())
print(f"{math.sqrt((x1-x2)**2 + (y1-y2)**2):.4f}")
```
