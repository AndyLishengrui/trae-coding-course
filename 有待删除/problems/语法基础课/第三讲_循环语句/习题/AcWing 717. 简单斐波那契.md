# AcWing 717. 简单斐波那契

> ⚠ 此题暂未收录到XMUOJ公共题库，题面待补充
> 原题链接: https://www.acwing.com/problem/content/717/

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
  int n;
  cin >> n;

  int a = 0, b = 1;

  for (int i = 0; i < n; i ++ )
  {
    cout << a << ' ';
    int c = a + b;
    a = b;
    b = c;
  }

  cout << endl;

  return 0;
}
```
