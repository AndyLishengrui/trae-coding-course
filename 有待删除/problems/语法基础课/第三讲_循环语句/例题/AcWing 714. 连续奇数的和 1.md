# AcWing 714. 连续奇数的和 1

> ⚠ 此题暂未收录到XMUOJ公共题库，题面待补充
> 原题链接: https://www.acwing.com/problem/content/714/

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
    int x, y;
    cin >> x >> y;

    if (x > y) swap(x, y);

    int sum = 0;
    int i = x + 1;
    while (i < y)
    {
      if (i % 2) sum += i;
      i ++;
    }
    cout << sum << endl;

    return 0;
}
```
