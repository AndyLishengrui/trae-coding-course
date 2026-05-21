//这道题就是求卡特兰数
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

typedef long long LL;

const int N = 100007, mod = 1e9+7;

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

//用快速幂求逆元，求组合数
int main()
{
    int n; cin>>n;

    // C(n,2n) - C(n-1, 2n) = C(n,2n)/(n+1)

    int a = n * 2, b = n;//套用卡特兰数公式

    int res = 1;
    // 求C(b,a) 即 C(n,2n),公式的计算需要仔细消化理解
    for (int i = a; i > a-b; i--) res = (LL) res *i % mod;

    for (int i = 1; i<=b; i++) res = (LL) res * qmi(i, mod-2,mod) % mod;

    res = (LL) res  * qmi(n+1,mod-2,mod) % mod;

    cout <<res<<endl;

    return 0;

}