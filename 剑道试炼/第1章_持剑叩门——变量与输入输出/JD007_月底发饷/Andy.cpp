#include <cstdio>

int main() {
    int id, days;
    double rate;
    scanf("%d", &id);       // 第一行：工号
    scanf("%d%lf", &days, &rate);  // 第二行：出工天数和每日工钱
    // 输出工号和实发金额
    printf("NUMBER = %d\n", id);
    printf("SALARY = U$ %.2f\n", days * rate);
    return 0;
}
