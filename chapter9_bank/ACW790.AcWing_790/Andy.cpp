#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    double number;
    scanf("%lf", &number);
    double left = -10000, right = 10000;
    while (right - left >= 1e-8)
    {
        double mid = (right + left) / 2; //二分
        if (mid * mid * mid >= number)
            right = mid;
        else
            left = mid;
    }
    //输出left
    printf("%lf", left);
}
