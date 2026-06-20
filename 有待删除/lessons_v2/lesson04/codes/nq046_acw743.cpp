#include <cstdio>
int main() {
    int l; char t;
    scanf("%d %c", &l, &t);
    double sum = 0, x;
    for (int i = 0; i < 12; i++)
        for (int j = 0; j < 12; j++) {
            scanf("%lf", &x);
            if (i == l) sum += x;
        }
    printf("%.1lf\n", t == 'S' ? sum : sum / 12);
    return 0;
}
