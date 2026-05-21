# AcWing 660. 零食

> ⚠ 此题暂未收录到XMUOJ公共题库，题面待补充
> 原题链接: https://www.acwing.com/problem/content/660/

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
    int x, y;
    scanf("%d%d", &x, &y);

    double price;
    if (x == 1) price = 4;
    else if (x == 2) price = 4.5;
    else if (x == 3) price = 5;
    else if (x == 4) price = 2;
    else price = 1.5;

    printf("Total: R$ %.2lf\n", price * y);

    return 0;
}
```
