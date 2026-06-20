// NQ005: 工资
#include <cstdio>

int main() {
    int number, hour;
    double money;
    scanf("%d%d%lf", &number, &hour, &money);
    printf("NUMBER = %d\n", number);
    printf("SALARY = U$ %.2lf\n", hour * money);
    return 0;
}
