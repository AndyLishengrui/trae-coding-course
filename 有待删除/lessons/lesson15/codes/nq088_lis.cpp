#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;
// f[i]定义为以s[i]结尾的最长的子序列
// 集合：所有以第i个数结尾的上升子序列集合
// 属性: Max 上升子序列长度的最大值
const int N = 10007;
int n;
int a[N], f[N];
//状态计算
int main()
{
    cin >> n;
    for (int i = 1; i <= n; i++)
        cin >> a[i]; //从1开始初始化

    for (int i = 1; i <= n; i++)
    {

        f[i] = 1;                   // a[i]只有一个元素，所以f[i]=1;
        for (int j = 1; j < i; j++) //求i之前的f[j]
            if (a[j] < a[i])
                f[i] = max(f[i], f[j] + 1);
    }

    int res = 1;
    for (int i = 1; i <= n; i++)
        res = max(res, f[i]);
    cout << res << endl;
    return 0;
}