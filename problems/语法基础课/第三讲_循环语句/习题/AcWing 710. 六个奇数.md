# AcWing 710. 六个奇数

> ⚠ 此题暂未收录到XMUOJ公共题库，题面待补充
> 原题链接: https://www.acwing.com/problem/content/710/

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
    int x;
    cin >> x;

    if (x % 2 == 0) x ++ ;

    for (int i = 0; i < 6; i ++ ) cout << x + i * 2 << endl;

    return 0;
}
```
