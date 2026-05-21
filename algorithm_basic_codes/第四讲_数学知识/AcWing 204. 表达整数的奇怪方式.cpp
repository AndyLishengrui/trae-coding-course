#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

//LL版exgcd
typedef long long LL;
LL exgcd(LL a, LL b, LL &x, LL &y)  // 扩展欧几里得算法, 求x, y，使得ax + by = gcd(a, b)
{
    if (!b)
    {
        x = 1; y = 0;
        return a;
    }
    LL d = exgcd(b, a % b, y, x);
    y -= (a / b) * x;
    return d;
}

int main()
{
    int n; cin>>n;
    bool flag = true;
    //读入第一个方程
    LL a1,m1;
    cin>>a1>>m1;

    for (int i = 0; i < n -1; i ++ )//合并方程
    {
      LL a2,m2;
      cin >> a2 >> m2;//读入第二个方程

      LL k1, k2;//求系数
      LL d = exgcd(a1, a2, k1, k2);

      if ((m2-m1) % d)
      {
        flag = false;
        break;
      }

      //求新的k1参数和m1参数
      k1 *= (m2-m1)/d;
      LL t = a2/d;
      k1 = (k1 %t + t) % t;//求最小余数

      m1 = a1 * k1 + m1;
      a1 = abs(a1 /d * a2);
    }

    if (flag)
    {
      cout << (m1 % a1 + a1) % a1 <<endl;//求最小余数
    }
    else puts("-1");

    return 0;
}