#include <cstdio>

int main() {
    int n;
    scanf("%d", &n);
    // 总秒数转换为 时:分:秒
    int h = n / 3600;
    int m = (n % 3600) / 60;
    int s = n % 60;
    printf("%d:%d:%d\n", h, m, s);
    return 0;
}
