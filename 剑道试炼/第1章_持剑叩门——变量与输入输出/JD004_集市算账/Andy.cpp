#include <cstdio>

int main() {
    int id, qty;
    double price;
    scanf("%d%d", &id, &qty);     // 第一行：编号和数量
    scanf("%lf", &price);          // 第二行：单价
    // 总价 = 数量 × 单价
    printf("TOTAL = %.2f\n", qty * price);
    return 0;
}
