# AcWing 613. 面积

> ⚠ 此题暂未收录到XMUOJ公共题库，题面待补充
> 原题链接: https://www.acwing.com/problem/content/613/

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

int main()
{
  double a, b, c;  
  scanf("%lf%lf%lf", &a, &b, &c);

  printf("TRIANGULO: %.3lf\n", a * c / 2);
  printf("CIRCULO: %.3lf\n", 3.14159 * c * c);
  printf("TRAPEZIO: %.3lf\n", (a + b) * c / 2);
  printf("QUADRADO: %.3lf\n", b * b);
  printf("RETANGULO: %.3lf\n", a * b);

  return 0;
}
```
