#include <cstdio>

/**
 * NQ1-06: 油耗
 * 行驶距离(km) / 消耗汽油量(L) = 每升公里数。
 * 时间: O(1) | 空间: O(1)
 */
int main() {
    double distance, fuel;
    scanf("%lf%lf", &distance, &fuel);
    printf("%.3lf km/l\n", distance / fuel);
    return 0;
}
