#include <cstdio>
int main() {
    int a, b, c, d;
    scanf("%d%d%d%d", &a, &b, &c, &d);
    int start = a * 60 + b, end = c * 60 + d;
    if (end <= start) end += 24 * 60;
    int diff = end - start;
    printf("O JOGO DUROU %d HORA(S) E %d MINUTO(S)\n", diff / 60, diff % 60);
    return 0;
}
