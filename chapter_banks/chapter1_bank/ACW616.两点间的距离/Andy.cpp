#include <cstdio>
#include <cmath>

/**
 * NQ1-07: 两点间的距离
 * 欧几里得距离: sqrt((x1-x2)^2 + (y1-y2)^2)。
 * 时间: O(1) | 空间: O(1)
 */
int main() {
    double x1, y1, x2, y2;
    scanf("%lf%lf%lf%lf", &x1, &y1, &x2, &y2);
    double dx = x1 - x2;
    double dy = y1 - y2;
    printf("%.4lf\n", sqrt(dx * dx + dy * dy));
    return 0;
}
