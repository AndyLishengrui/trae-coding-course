# AcWing 726. 质数

> ⚠ 此题暂未收录到XMUOJ公共题库，题面待补充
> 原题链接: https://www.acwing.com/problem/content/726/

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
  int n;
  cin >> n;
  while (n -- )
  {
    int p;
    cin >> p;

    bool is_prime = true;
    for (int i = 2; i * i <= p; i ++ )
        if (p % i == 0)
        {
           is_prime = false;
           break;
        }
    if (is_prime) printf("%d is prime\n", p);
    else printf("%d is not prime\n", p);
  }

  return 0;
}
```
