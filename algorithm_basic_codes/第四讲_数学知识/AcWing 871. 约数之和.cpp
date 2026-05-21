#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

typedef long long LL;

const int N = 110, mod = 1e9+7;//大数取mod

int main()
{
    int n; cin>>n;

    unordered_map<int,int> primes;//存质因数与个数

    while (n -- )
    {
      //读入a，分解质因数
      int a; cin>>a;
      for (int i = 2; i <= a / i; i++)
        while(a % i == 0)
        {
          a /= i;//统计因子i的个数
          primes[i]++;
        }

      if (a > 1) primes[a]++;//剩下的最后一个因子
    }
    //根据公式计算约数之和
    LL res = 1;
    for (auto x:primes) 
    {
      int p = x.first, a = x.second;
      LL t = 1;
      while (a --) t = (t * p + 1) % mod;
      res = res * t % mod;
    }

    cout<<res<<endl;

    return 0;
}