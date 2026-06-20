#include <cstdio>

/**
 * NQ1-12: 球的体积
 * V = (4/3) * pi * r^3, pi = 3.14159。
 * 时间: O(1) | 空间: O(1)
 */
int main() {
    int r;
    scanf("%d", &r);
    double volume = (4.0 / 3.0) * 3.14159 * r * r * r;
    printf("VOLUME = %.3lf\n", volume);
    return 0;
}
