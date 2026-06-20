#include <cstdio>

/**
 * NQ1-13: 面积
 * 计算三个图形面积: 直角三角形、圆、梯形。
 * 时间: O(1) | 空间: O(1)
 */
int main() {
    double a, b, c;
    scanf("%lf%lf%lf", &a, &b, &c);
    const double PI = 3.14159;
    printf("TRIANGULO: %.3lf\n", a * c / 2.0);          // 直角三角形
    printf("CIRCULO: %.3lf\n", PI * c * c);              // 圆
    printf("TRAPEZIO: %.3lf\n", (a + b) * c / 2.0);     // 梯形
    return 0;
}
