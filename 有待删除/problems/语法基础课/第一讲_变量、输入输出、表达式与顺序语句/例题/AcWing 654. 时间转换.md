# AcWing 654. 时间转换

> ⚠ 此题暂未收录到XMUOJ公共题库，题面待补充
> 原题链接: https://www.acwing.com/problem/content/654/

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
#include <cstdio>

int main()
{
  int n;
  scanf("%d",&n);
  printf("%d:%d:%d", n / 3600, n % 3600 / 60, n % 60);

  return 0;
}
```
