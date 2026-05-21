//NQ021 废强重建
#include <iostream>
using namespace std;
const int N=107;//墙最大宽度<100
int main()
{
    int n, a[N];

    while (cin >> n, n > 0)
    {
        int avg = 0; //平均值
        for (int i = 0; i < n; i++)
        {
            cin >> a[i];
            avg += a[i];
        }
        avg = avg / n; //求平均值
        int res = 0;   //统计小于平均值的列中砖块的空缺数
        for (int i = 0; i < n; i++)
        {
            if (a[i] < avg)
                res += avg - a[i];
        }
        cout << res << endl  << endl;//数据之间有空行
    }
    return 0;
}
