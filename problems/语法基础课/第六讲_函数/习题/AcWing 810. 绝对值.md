# AcWing 810. 绝对值

> ⚠ 此题暂未收录到XMUOJ公共题库，题面待补充
> 原题链接: https://www.acwing.com/problem/content/810/

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

int abs(int x)
{
  if (x > 0) return x;
  return -x;
}

int main()
{
    int x;
    cin >> x;
    cout << abs(x) << endl;

    return 0;
}
```
