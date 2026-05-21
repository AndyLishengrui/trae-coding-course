# AcWing 614. 最大值

> ⚠ 此题暂未收录到XMUOJ公共题库，题面待补充
> 原题链接: https://www.acwing.com/problem/content/614/

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
  int a, b, c;
  cin >> a >> b >> c;

  int t = (a + b + abs(a - b)) / 2;
  int r = (t + c + abs(t - c)) / 2;

  cout << r << " eh o maior" << endl;

  return 0;

}
```
