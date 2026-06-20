#include <cstdio>

/**
 * NQ1-03: 圆的面积
 * 给定半径 r，计算面积。pi = 3.14159。
 * 时间: O(1) | 空间: O(1)
 */
int main() {
    double r;
    scanf("%lf", &r);
    printf("A=%.4lf\n", 3.14159 * r * r);
    return 0;
}
