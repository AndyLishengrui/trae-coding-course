# AcWing 727. 菱形

> ⚠ 此题暂未收录到XMUOJ公共题库，题面待补充
> 原题链接: https://www.acwing.com/problem/content/727/

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
#include <cmath>

using namespace std;

int main()
{
  int n;
  cin >> n;

  int cx = n / 2, cy = n / 2;
  for (int i = 0; i < n; i ++ )
  {
    for (int j = 0; j < n; j ++ )
        if (abs(i - cx) + abs(j - cy) <= n / 2) cout << '*';
        else cout << ' ';
    cout << endl;    
  }

  return 0;
}
```
