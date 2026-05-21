# AcWing 659. 区间 — 区间

**难度:** 简单 | **时间限制:** 1000ms | **内存限制:** 256MB

> 原题链接: https://www.acwing.com/problem/content/659/

## 题目描述

给定一个浮点数，请你判断该数字属于以下哪个区间：[0, 25], (25, 50], (50, 75], (75, 100]。

如果给定的数值小于 0 或大于 100，则程序输出`Fora de intervalo`，表示超出范围。

开区间 (a, b)：在实数 a 和实数 b 之间的所有实数，但不包含 a 和 b。

闭区间 [a, b]：在实数 a 和实数 b 之间的所有实数，包含 a 和 b。

### 输入格式

输入一个浮点数。

### 输出格式

判断输入数值位于哪个区间，按格式`Intervalo x`输出，其中 x 为区间范围 [0, 25], (25, 50], (50, 75], (75, 100] 中的一个。

如果数值位于所有区间之外，则输出`Fora de intervalo`。

### 样例

**输入:**
```
25.01
```

**输出:**
```
Intervalo (25, 50]
```

### 提示

注意区间的开闭情况。

## AC代码

```cpp
#include <iostream>

using namespace std;

int main()
{
    double x;
    cin >> x;

    if (x >= 0 && x <= 25) cout << "Intervalo [0,25]" << endl;
    else if (x > 25 && x <= 50) cout << "Intervalo (25,50]" << endl;
    else if (x > 50 && x <= 75) cout << "Intervalo (50,75]" << endl;
    else if (x > 75 && x <= 100) cout << "Intervalo (75,100]" << endl;
    else cout << "Fora de intervalo" << endl;

    return 0;

}
```
