# AcWing 664. 三角形

> ⚠ 此题暂未收录到XMUOJ公共题库，题面待补充
> 原题链接: https://www.acwing.com/problem/content/664/

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

using namespace std;

int main()
{
    double a, b, c;
    cin >> a >> b >> c;
    if(a + b > c && a + c > b && b + c > a)
      printf("Perimetro = %.1lf\n", a + b + c);
    else
      printf("Area = %.1lf\n",(a + b) * c / 2);

      return 0;
}
```
