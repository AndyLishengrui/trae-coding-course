#include <cstdio>

int main() {
    int n;
    while (scanf("%d", &n) == 1 && n) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++)
                printf("%lld ", 1LL << (i + j));
            printf("\n");
        }
        printf("\n");
    }
    return 0;
}
