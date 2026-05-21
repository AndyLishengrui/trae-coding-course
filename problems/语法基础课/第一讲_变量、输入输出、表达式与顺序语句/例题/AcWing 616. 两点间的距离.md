# AcWing 616. 两点间的距离

> ⚠ 此题暂未收录到XMUOJ公共题库，题面待补充
> 原题链接: https://www.acwing.com/problem/content/616/

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
#include <cmath>

int main()
{
    double x1,y1,x2,y2;
    scanf("%lf%lf",&x1,&y1);
    scanf("%lf%lf",&x2,&y2);
    printf("%.4lf\n",sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)));

    return 0;
}
```
