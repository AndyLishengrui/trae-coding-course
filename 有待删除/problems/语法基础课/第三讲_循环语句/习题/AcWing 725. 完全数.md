# AcWing 725. 完全数

> ⚠ 此题暂未收录到XMUOJ公共题库，题面待补充
> 原题链接: https://www.acwing.com/problem/content/725/

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
    int x;
    cin >> x;

    int s = 0;
    for (int i = 1; i * i <= x; i ++ )
        if (x % i == 0)
        {
          if (i < x) s += i;
          if (i != x / i && x / i < x) s += x / i;
        }

    if (s == x) printf("%d is perfect\n", x);
    else printf("%d is not perfect\n", x);
  }

  return 0;
}
```
