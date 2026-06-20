#include <cstdio>
int main() {
    for (int i = 0; i < 100; i++) {
        double x;
        scanf("%lf", &x);
        if (x <= 10) printf("A[%d] = %.1f\n", i, x);
    }
    return 0;
}
