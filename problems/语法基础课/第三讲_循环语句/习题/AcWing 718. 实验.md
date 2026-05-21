# AcWing 718. 实验

> ⚠ 此题暂未收录到XMUOJ公共题库，题面待补充
> 原题链接: https://www.acwing.com/problem/content/718/

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

  int c = 0, r = 0, f = 0;
  for (int i = 0; i < n; i ++ )
  {
    int k;
    char t;
    cin >> k >> t;
    if (t == 'C') c += k;
    else if (t == 'R') r += k;
    else f += k;
  }

  int s = c + r + f;
  printf("Total: %d animals\n", s);
  printf("Total coneys: %d\n", c);
  printf("Total rats: %d\n", r);
  printf("Total frogs: %d\n", f);
  printf("Percentage of coneys: %.2lf %%\n", (double)c / s * 100);
  printf("Percentage of rats: %.2lf %%\n", (double)r / s * 100);
  printf("Percentage of frogs: %.2lf %%\n", (double)f / s * 100);

  return 0;
}
```
