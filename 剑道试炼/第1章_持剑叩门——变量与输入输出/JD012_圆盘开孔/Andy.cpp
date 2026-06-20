#include <cstdio>
#define PI 3.14159

int main() {
    double a, b, c;
    scanf("%lf%lf%lf", &a, &b, &c);
    // 五个图形的面积
    printf("TRIANGULO: %.3f\n", a * c / 2);       // 三角形
    printf("CIRCULO: %.3f\n", PI * c * c);         // 圆形
    printf("TRAPEZIO: %.3f\n", (a + b) * c / 2);  // 梯形
    printf("QUADRADO: %.3f\n", b * b);             // 正方形
    printf("RETANGULO: %.3f\n", a * b);            // 长方形
    return 0;
}
