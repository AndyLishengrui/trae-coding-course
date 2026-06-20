#include <cstdio>
int main() {
    double s;
    scanf("%lf", &s);
    int p;
    if (s <= 400) p = 15;
    else if (s <= 800) p = 12;
    else if (s <= 1200) p = 10;
    else if (s <= 2000) p = 7;
    else p = 4;
    double r = s * p / 100;
    printf("Novo salario: %.2lf\nReajuste ganho: %.2lf\nEm percentual: %d %%\n", s + r, r, p);
    return 0;
}
