# AcWing 723. PUM

> ⚠ 此题暂未收录到XMUOJ公共题库，题面待补充
> 原题链接: https://www.acwing.com/problem/content/723/

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
    int n, m;
    cin >> n >> m;

    for (int i = 0, k = 1; i < n; i ++ )
    {
      for (int j = 0; j < m - 1; j ++ )
      {
        cout << k << ' ';
        k ++ ;
      }

      cout << "PUM" << endl;
      k ++ ;
    }

    return 0;  
}
```
