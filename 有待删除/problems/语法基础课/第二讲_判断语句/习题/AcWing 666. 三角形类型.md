# AcWing 666. 三角形类型

> ⚠ 此题暂未收录到XMUOJ公共题库，题面待补充
> 原题链接: https://www.acwing.com/problem/content/666/

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
#include <iostream>

using namespace std;

int main()
{
    double a, b, c;
    cin >> a >> b >> c;

    if (b > a)
    {
      double t = a;
      a = b;
      b = t;
    }
    if (c > a)
    {
      double t = a;
      a = c;
      c = t;
    }
    if (c > b)
    {
      double t = b;
      b = c;
      c = t;
    }

    if (a >= b + c) cout << "NAO FORMA TRIANGULO" << endl;
    else
    {
      if (a * a == b * b + c * c) cout << "TRIANGULO RETANGULO" << endl;
      if (a * a > b * b + c * c) cout << "TRIANGULO OBTUSANGULO" << endl;
      if (a * a < b * b + c * c) cout << "TRIANGULO ACUTANGULO" << endl;
      if (a == b && b == c) cout << "TRIANGULO EQUILATERO" << endl;
      else if (a == b || a == c || b == c) cout << "TRIANGULO ISOSCELES" << endl;
    }

   return 0; 
}
```
