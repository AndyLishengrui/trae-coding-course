# AcWing 5. 多重背包问题 II

> ⚠ 此题暂未收录到XMUOJ公共题库，题面待补充
> 原题链接: https://www.acwing.com/problem/content/5/

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
//采用二进制优化，把s的个数分租
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 25007, M = 2007;//2000= 2^11 ,因此2000*11=22000，取25007即可

int n,m;
int v[N],w[N];
int f[M];

int main()
{
    cin>>n>>m;
    // 二进制优化，把s按照二进制分组，问题变为01背包的问题
    int cnt = 0;//分组的组别
    for (int i = 1; i <=n; i++)
    {
      int a, b, s;
      cin>>a>>b>>s;
      //把s进行二进制拆分，重新计算v和w
      int k = 1;//2的0次方
      while(k <= s)
      {
        cnt ++; //s分为的第几组
        v[cnt] = a * k;//体积
        w[cnt] = b * k;//权重
        s -= k;
        k *= 2; 
      }
      if (s > 0)
      {
        cnt ++;
        v[cnt] = a * s;
        w[cnt] = b * s;
      }
    }
    // 01背包
    n = cnt; //个数设置为组数
    for (int i = 1; i <=n; i++)
      for (int j = m; j >= v[i]; j--)
        f[j] = max(f[j], f[j-v[i]]+w[i]);

    cout<<f[m]<<endl;

    return 0;
}
```
