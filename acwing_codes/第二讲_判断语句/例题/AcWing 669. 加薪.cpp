#include <cstdio>

int main()
{
    double salary;
    scanf("%lf", &salary);

    double x;

    if (salary <= 400) x = 0.15;
    else if (salary <= 800) x = 0.12;
    else if (salary <= 1200) x = 0.1;
    else if (salary <= 2000) x = 0.07;
    else x = 0.04;

    printf("Novo salario: %.2lf\n", salary * (1 + x));
    printf("Reajuste ganho: %.2lf\n", salary * x);
    printf("Em percentual: %.0lf %%", x * 100);

    return 0;

}