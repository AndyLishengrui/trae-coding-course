#include <cstdio>

int main()
{
    double x;
    scanf("%lf", &x);

    double sum = 0;
    if (x > 2000)
    {
      double y = 3000;
      if (x < 3000) y = x;
      sum += (y - 2000) * 0.08;
    }
    if (x > 3000)
    {
      double y = 4500;
      if (x < 4500) y = x;
      sum += (y - 3000) * 0.18;
    }
    if (x > 4500) sum += (x - 4500) * 0.28;

    if (sum == 0) printf("Isento");
    else printf("R$ %.2lf\n", sum);

    return 0;

}