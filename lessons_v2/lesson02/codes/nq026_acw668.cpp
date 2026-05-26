#include <cstdio>

int main()
{
    int a, b, c, d;
    scanf("%d%d%d%d", &a, &b, &c, &d);

    int start = a * 60 + b;
    int end = c * 60 + d;

    int spent_time = end - start;
    if (spent_time <= 0) spent_time += 1440;

    printf("O JOGO DUROU %d HORA(S) E %d MINUTO(S)", spent_time / 60, spent_time % 60);

    return 0;

}