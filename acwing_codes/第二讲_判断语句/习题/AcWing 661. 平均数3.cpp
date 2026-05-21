#include <cstdio>
#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    double n1, n2, n3, n4;
    scanf("%lf%lf%lf%lf", &n1, &n2, &n3, &n4);

    double x = (n1 * 2 + n2 * 3 + n3 * 4 + n4) / 10;

    printf("Media: %.1lf\n", x + 1e-8);
    if (x >= 7) printf("Aluno aprovado.\n");
    else if (x < 5) printf("Aluno reprovado.\n");
    else
    {
      printf("Aluno em exame.\n");
      double y;
      scanf("%lf", &y);
      printf("Nota do exame: %.1lf\n", y + 1e-8);
      double z = (x + y) / 2;
      if (z >= 5) printf("Aluno aprovado.\n");
      else printf("Aluno reprovado.\n");
      printf("Media final: %.1lf\n", z + 1e-8);
    }

    return 0;
}