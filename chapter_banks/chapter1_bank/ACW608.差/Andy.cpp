#include <cstdio>

/**
 * NQ1-02: 差
 * 读取四个整数A,B,C,D，计算A*B-C*D。
 * 时间: O(1) | 空间: O(1)
 */
int main() {
    int a, b, c, d;
    scanf("%d%d%d%d", &a, &b, &c, &d);
    printf("DIFERENCA = %d\n", a * b - c * d);
    return 0;
}
