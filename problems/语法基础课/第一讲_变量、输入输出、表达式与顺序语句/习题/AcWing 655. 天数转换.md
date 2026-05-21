# AcWing 655. 天数转换

> ⚠ 此题暂未收录到XMUOJ公共题库，题面待补充
> 原题链接: https://www.acwing.com/problem/content/655/

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

    cout << n / 365 << " ano(s)" << endl;
    cout << n % 365 / 30 << " mes(es)" << endl;
    cout << n % 365 % 30 << " dia(s)" << endl;

    return 0;
}
```
