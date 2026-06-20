#include <cstdio>

/**
 * NQ1-09: 时间转换
 * 将总秒数N转换为时:分:秒格式。
 * 时间: O(1) | 空间: O(1)
 */
int main() {
    int n;
    scanf("%d", &n);
    int hours = n / 3600;
    int minutes = (n % 3600) / 60;
    int seconds = n % 60;
    printf("%d:%d:%d\n", hours, minutes, seconds);
    return 0;
}
