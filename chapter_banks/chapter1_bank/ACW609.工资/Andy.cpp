#include <cstdio>

/**
 * NQ1-05: 工资
 * 员工编号、月工作时数、时薪，计算工资总额。
 * 时间: O(1) | 空间: O(1)
 */
int main() {
    int number, hours;
    double rate;
    scanf("%d%d%lf", &number, &hours, &rate);
    printf("NUMBER = %d\n", number);
    printf("SALARY = U$ %.2lf\n", hours * rate);
    return 0;
}
