# AcWing 716. 最大数和它的位置

> ⚠ 此题暂未收录到XMUOJ公共题库，题面待补充
> 原题链接: https://www.acwing.com/problem/content/716/

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
int a[100];

int main()
{
  int maxa = -1;
  int index = -1;
  for (int i = 0; i < 100; i ++) 
  {
    cin >> a[i];

    if (a[i] > maxa) 
    {
      maxa = a[i];
      index = i;
    }
  }

  cout << maxa << endl;
  cout << index+1 << endl;

  return 0;
}
```
