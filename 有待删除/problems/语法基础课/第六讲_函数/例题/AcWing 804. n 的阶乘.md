# AcWing 804. n 的阶乘

> ⚠ 此题暂未收录到XMUOJ公共题库，题面待补充
> 原题链接: https://www.acwing.com/problem/content/804/

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

int fact(int n)
{
  int res = 1;
  for (int i = 1; i <= n; i ++ )
      res *= i;
  return res;    
}

int main()
{
   int n;
   cin >> n;

   cout << fact(n) << endl;

   return 0;
}
```
