#include <cstdio>
#include <iostream>

using namespace std;

int main()
{
    double n1, s1, p1;
    double n2, s2, p2;

    cin >> n1 >> s1 >> p1;
    cin >> n2 >> s2 >> p2;

    printf("VALOR A PAGAR: R$ %.2lf\n", s1 * p1 + s2 * p2);

    return 0;
}