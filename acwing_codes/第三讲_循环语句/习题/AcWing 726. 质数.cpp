#include <cstdio>
#include <iostream>

using namespace std;

int main()
{
  int n;
  cin >> n;
  while (n -- )
  {
    int p;
    cin >> p;

    bool is_prime = true;
    for (int i = 2; i * i <= p; i ++ )
        if (p % i == 0)
        {
           is_prime = false;
           break;
        }
    if (is_prime) printf("%d is prime\n", p);
    else printf("%d is not prime\n", p);
  }

  return 0;
}