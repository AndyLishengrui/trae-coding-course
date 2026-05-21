# AcWing 720. 连续整数相加

> ⚠ 此题暂未收录到XMUOJ公共题库，题面待补充
> 原题链接: https://www.acwing.com/problem/content/720/

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
    int a, n;
    cin >> a;
    while (cin >> n, n <= 0);

    int s = 0;
    for (int i = 0; i < n; i ++) s += a + i;

    cout << s << endl;

    return 0;
}
```
