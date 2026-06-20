#include <cstdio>
int main() {
    double x;
    scanf("%lf", &x);
    if (x <= 2000) { printf("Isento\n"); return 0; }
    x -= 2000;
    double t = 0;
    if (x > 0) { double v = x < 1000 ? x : 1000; t += v * 0.08; x -= v; }
    if (x > 0) { double v = x < 1500 ? x : 1500; t += v * 0.18; x -= v; }
    if (x > 0) t += x * 0.28;
    printf("R$ %.2lf\n", t);
    return 0;
}
