# AcWing 9. 分组背包问题

> ⚠ 此题暂未收录到XMUOJ公共题库，题面待补充
> 原题链接: https://www.acwing.com/problem/content/9/

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
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 107;

int n,m;
int v[N][N], w[N][N], s[N];
int f[N];

int main()
{
    cin >> n >> m;
    //直接把数据存到数组里
    for (int i = 1; i <=n; i ++)
    {
      cin >> s[i];
      for (int j = 0; j < s[i]; j++)
        cin >> v[i][j] >> w[i][j];
    }
    //三重循环，计算最大值
    for (int i = 1; i <=n; i ++)
      for (int j = m; j >= 0; j--)
       for (int k = 0; k < s[i]; k++)
          if (v[i][k] <= j)
            f[j] = max(f[j],f[j-v[i][k]] + w[i][k]);

    cout<<f[m]<<endl;
    return 0;
}
```
