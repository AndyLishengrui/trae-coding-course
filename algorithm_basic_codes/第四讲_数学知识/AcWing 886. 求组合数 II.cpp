#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

typedef long long LL;
const int N = 100007, mod = 1e9+7;

int fact[N], infact[N];//逆元

int qmi(int a, int k, int p)  // 求a^k mod p
{
    int res = 1 % p;
    while (k)
    {
        if (k & 1) res = (LL)res * a % p;
        a = (LL)a * a % p;
        k >>= 1;
    }
    return res;
}

int main()
{
    fact[0]=infact[0]=1;
    for (int i = 1; i < N; i ++ )
    {
      fact[i] = (LL)fact[i-1] * i % mod;//求组合数分子
      infact[i] = (LL)infact[i-1] * qmi(i, mod-2, mod) % mod;//求逆元
    }

    int n;
    scanf("%d", &n);
    while (n -- )
    {
      int a,b;
      scanf("%d%d", &a, &b);
      printf("%d\n",(LL)fact[a] * infact[b] % mod * infact[a-b] % mod);//套用组合数公式
    }

    return 0;
}