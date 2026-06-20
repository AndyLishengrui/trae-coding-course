#include <cstdio>
int main() {
    int a, b;
    scanf("%d%d", &a, &b);
    // 计算比武持续小时数
    int res;
    if (a < b) res = b - a;
    else if (a == b) res = 24;
    else res = 24 - a + b;
    printf("%d\n", res);
    return 0;
}
