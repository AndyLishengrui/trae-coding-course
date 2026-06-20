#include <cstdio>

int main() {
    double s, l;
    scanf("%lf%lf", &s, &l);
    // 每升草料汁能跑的里数 = 总路程 / 消耗量
    printf("%.3f km/l\n", s / l);
    return 0;
}
