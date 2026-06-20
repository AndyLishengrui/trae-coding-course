#include <cstdio>

/**
 * NQ1-08: 钞票
 * 贪心: 用最少钞票数支付金额N。面额: 100,50,20,10,5,2,1。
 * 时间: O(1) | 空间: O(1)
 */
int main() {
    int n;
    int bills[] = {100, 50, 20, 10, 5, 2, 1};
    scanf("%d", &n);
    printf("%d\n", n);
    for (int i = 0; i < 7; i++) {
        printf("%d nota(s) de R$ %d,00\n", n / bills[i], bills[i]);
        n %= bills[i];
    }
    return 0;
}
