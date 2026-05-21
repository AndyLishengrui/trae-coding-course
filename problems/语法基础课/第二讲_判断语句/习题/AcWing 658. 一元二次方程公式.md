# AcWing 658. 一元二次方程公式

> ⚠ 此题暂未收录到XMUOJ公共题库，题面待补充
> 原题链接: https://www.acwing.com/problem/content/658/

## 题目描述
> 待补充

### 输入格式
> 待补充

### 输出格式
> 待补充

### 样例
> 待补充

## AC代码

```cpp
#include <cstdio>
#include <iostream>
#include <cmath>

using namespace std;

int main()
{
  double a, b, c;
  cin >> a >> b >> c;

  double delta = b * b - 4 * a * c;
  if (delta < 0 || a == 0) printf("Impossivel calcular\n");
  else
  {
    delta = sqrt(delta);
    double x1 = (-b + delta) / (2 * a);
    double x2 = (-b - delta) / (2 * a);

    printf("R1 = %.5lf\n", x1);
    printf("R2 = %.5lf\n", x2);
  }

  return 0;
}
```
