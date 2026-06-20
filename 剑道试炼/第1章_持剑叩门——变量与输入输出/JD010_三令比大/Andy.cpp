#include <cstdio>

int main() {
    int a, b, c;
    scanf("%d%d%d", &a, &b, &c);
    // 找三个数中的最大值
    int max_val = a;
    if (b > max_val) max_val = b;
    if (c > max_val) max_val = c;
    printf("Max = %d\n", max_val);
    return 0;
}
