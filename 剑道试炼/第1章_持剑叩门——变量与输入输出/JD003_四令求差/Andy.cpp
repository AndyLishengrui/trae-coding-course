#include <cstdio>

int main() {
    int a, b, c, d;
    scanf("%d%d%d%d", &a, &b, &c, &d);
    // 先各自相乘，再求差
    printf("DIFFERENCE = %d\n", a * b - c * d);
    return 0;
}
