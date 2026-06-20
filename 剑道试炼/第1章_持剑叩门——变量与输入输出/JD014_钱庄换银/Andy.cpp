#include <cstdio>

int main() {
    int n;
    scanf("%d", &n);
    printf("%d\n", n);
    // 面额：100, 50, 20, 10, 5, 2, 1
    int denoms[] = {100, 50, 20, 10, 5, 2, 1};
    for (int i = 0; i < 7; i++) {
        printf("%d nota(s) de R$ %d,00\n", n / denoms[i], denoms[i]);
        n %= denoms[i];  // 剩余金额
    }
    return 0;
}
