#include <cstdio>
int main() {
    int x, y;
    scanf("%d%d", &x, &y);
    double p;
    if (x == 1) p = 4.0;
    else if (x == 2) p = 4.5;
    else if (x == 3) p = 5.0;
    else if (x == 4) p = 2.0;
    else p = 1.5;
    printf("Total: R$ %.2lf\n", p * y);
    return 0;
}
