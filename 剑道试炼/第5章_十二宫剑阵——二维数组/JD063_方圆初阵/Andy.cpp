#include <cstdio>

int min(int a, int b) { return a < b ? a : b; }

int main() {
    int n;
    while (scanf("%d", &n) == 1 && n) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int v = min(min(i, j), min(n - 1 - i, n - 1 - j));
                printf("%3d", v + 1);
            }
            printf("\n");
        }
        printf("\n");
    }
    return 0;
}
