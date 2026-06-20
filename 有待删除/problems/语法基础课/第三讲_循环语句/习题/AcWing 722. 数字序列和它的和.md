# AcWing 722. 数字序列和它的和

> ⚠ 此题暂未收录到XMUOJ公共题库，题面待补充
> 原题链接: https://www.acwing.com/problem/content/722/

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
  int n, m;
  while (cin >> n >> m, n > 0 && m > 0)
  {
    if (n > m) swap(n, m);

    int sum = 0;
    for (int i = n; i <= m; i ++ )
    {
      cout << i << ' ';
      sum += i;
    }

    cout << "Sum=" << sum << endl;
  }

  return 0;
}
```
