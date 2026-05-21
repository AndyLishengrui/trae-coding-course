# AcWing 665. 倍数

> ⚠ 此题暂未收录到XMUOJ公共题库，题面待补充
> 原题链接: https://www.acwing.com/problem/content/665/

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
    int a, b;
    cin >> a >> b;

    if (a % b == 0 || b % a == 0 ) cout << "Sao Multiplos" << endl;
    else cout << "Nao sao Multiplos" << endl;

    return 0;
}
```
