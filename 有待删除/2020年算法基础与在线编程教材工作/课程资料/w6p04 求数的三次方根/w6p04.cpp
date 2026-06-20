#include <iostream>
using namespace std;

int main()
{
    double number;
    scanf("%lf", &number);
    double l = -10000, r = 10000;//初始化搜索范围
    while (r - l >= 1e-8) //保留6为小数(6+2=8)
    {
        double mid = (r + l) / 2; //取中值
        if (mid * mid * mid >= number) //check函数
            r = mid;
        else
            l = mid;
    }
    //输出左区间l
    printf("%lf", l);
}
