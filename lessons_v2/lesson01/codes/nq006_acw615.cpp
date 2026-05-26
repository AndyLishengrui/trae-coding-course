#include <cstdio>

int main()
{
    double x, y;
    scanf("%lf%lf", &x, &y);
    printf("%.3lf km/l", x / y);

    return 0;
}