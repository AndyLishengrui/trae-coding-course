#include <cstdio>

/**
 * NQ1-11: 简单计算
 * 根据产品编号、数量和单价，计算总价。
 * 时间: O(1) | 空间: O(1)
 */
int main() {
    int code, quantity;
    double price;
    scanf("%d%d%lf", &code, &quantity, &price);
    printf("VALOR A PAGAR: R$ %.2lf\n", quantity * price);
    return 0;
}
