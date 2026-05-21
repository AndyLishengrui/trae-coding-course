//题解:https://www.acwing.com/solution/content/11231/
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

int exgcd(int a, int b, int &x, int &y)  // 扩展欧几里得算法, 求x, y，使得ax + by = gcd(a, b)
{
    if (!b)
    {
        x = 1; y = 0;
        return a;
    }
    int d = exgcd(b, a % b, y, x);
    y -= (a / b) * x;
    return d;
}

int main()
{
    int n;
    scanf("%d", &n);
    while (n -- )
    {
      int a,b,m;
      scanf("%d%d%d", &a, &b, &m);
      int x,y;
      int d = exgcd(a,m,x,y);
      if( b % d == 0) {
        int t = b/d;
        printf("%d\n", ((long long) x * t % (m/d)+(m/d))%(m/d));
      }
      else 
        puts("impossible");
    }

    return 0;
}