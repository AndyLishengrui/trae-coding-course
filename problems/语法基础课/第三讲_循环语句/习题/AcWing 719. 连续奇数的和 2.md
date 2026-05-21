# AcWing 719. 连续奇数的和 2

> ⚠ 此题暂未收录到XMUOJ公共题库，题面待补充
> 原题链接: https://www.acwing.com/problem/content/719/

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
#include <algorithm>

using namespace std;

int main()
{
  int n;
  cin >> n;

  while (n -- )
  {
    int x, y;
    cin >> x >> y;

    if (x > y) swap(x, y);

    int s = 0;
    for (int i = x + 1; i < y; i ++ )
        if (i % 2)
           s += i;
    cout << s << endl;       
  }

  return 0;
}
```
