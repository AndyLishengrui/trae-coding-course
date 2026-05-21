# AcWing 712. 正数

> ⚠ 此题暂未收录到XMUOJ公共题库，题面待补充
> 原题链接: https://www.acwing.com/problem/content/712/

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
    int cnt = 0;

    for (int i = 0; i < 6; i ++ )
    {
      double x;
      cin >> x;

      if (x > 0) cnt ++ ;
    }

    cout << cnt << " positive numbers" << endl;

    return 0;
}
```
