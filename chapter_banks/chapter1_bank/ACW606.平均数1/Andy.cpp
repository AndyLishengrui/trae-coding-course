#include <cstdio>

/**
 * NQ1-04: 平均数1
 * 加权平均分：A权重3.5，B权重7.5。
 * 时间: O(1) | 空间: O(1)
 */
int main() {
    double a, b;
    scanf("%lf%lf", &a, &b);
    printf("MEDIA = %.5lf\n", (a * 3.5 + b * 7.5) / 11.0);
    return 0;
}
