# AcWing 672. 税

> ⚠ 此题暂未收录到XMUOJ公共题库，题面待补充
> 原题链接: https://www.acwing.com/problem/content/672/

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
    double x;
    scanf("%lf", &x);

    double sum = 0;
    if (x > 2000)
    {
      double y = 3000;
      if (x < 3000) y = x;
      sum += (y - 2000) * 0.08;
    }
    if (x > 3000)
    {
      double y = 4500;
      if (x < 4500) y = x;
      sum += (y - 3000) * 0.18;
    }
    if (x > 4500) sum += (x - 4500) * 0.28;

    if (sum == 0) printf("Isento");
    else printf("R$ %.2lf\n", sum);

    return 0;

}
```
