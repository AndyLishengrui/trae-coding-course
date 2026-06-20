# AcWing 653. 钞票

> ⚠ 此题暂未收录到XMUOJ公共题库，题面待补充
> 原题链接: https://www.acwing.com/problem/content/653/

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
  int n;
  scanf("%d", &n);
  printf("%d\n", n);

  printf("%d nota(s) de R$ 100,00\n", n / 100 );
  n %= 100;
  printf("%d nota(s) de R$ 50,00\n", n / 50 );
  n %= 50;
  printf("%d nota(s) de R$ 20,00\n", n / 20 );
  n %= 20;
  printf("%d nota(s) de R$ 10,00\n", n / 10 );
  n %= 10;
  printf("%d nota(s) de R$ 5,00\n", n / 5 );
  n %= 5;
  printf("%d nota(s) de R$ 2,00\n", n / 2 );
  n %= 2;
  printf("%d nota(s) de R$ 1,00\n", n);

return 0;
}
```
