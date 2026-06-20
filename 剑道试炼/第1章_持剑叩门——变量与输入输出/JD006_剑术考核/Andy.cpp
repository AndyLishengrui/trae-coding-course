#include <cstdio>

int main() {
    double a, b;
    scanf("%lf%lf", &a, &b);
    // 加权平均 = (剑术*3.5 + 心法*7.5) / 11
    printf("Average = %.5f\n", (a * 3.5 + b * 7.5) / 11);
    return 0;
}
