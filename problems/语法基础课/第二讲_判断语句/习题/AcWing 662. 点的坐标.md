# AcWing 662. 点的坐标

> ⚠ 此题暂未收录到XMUOJ公共题库，题面待补充
> 原题链接: https://www.acwing.com/problem/content/662/

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
    double x, y;
    cin >> x >> y;

    if (x > 0 && y > 0) cout << "Q1" << endl;
    else if (x < 0 && y > 0) cout << "Q2" << endl;
    else if (x < 0 && y < 0) cout << "Q3" << endl;
    else if (x > 0 && y < 0) cout << "Q4" << endl;
    else
    {
      if (!x && !y) cout << "Origem" << endl;
      else if (!y) cout << "Eixo X" << endl;
      else cout << "Eixo Y" << endl;
    }
  return 0;  
}
```
