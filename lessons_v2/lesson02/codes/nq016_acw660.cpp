#include <cstdio>

int main()
{
    int x, y;
    scanf("%d%d", &x, &y);

    double price;
    if (x == 1) price = 4;
    else if (x == 2) price = 4.5;
    else if (x == 3) price = 5;
    else if (x == 4) price = 2;
    else price = 1.5;

    printf("Total: R$ %.2lf\n", price * y);

    return 0;
}