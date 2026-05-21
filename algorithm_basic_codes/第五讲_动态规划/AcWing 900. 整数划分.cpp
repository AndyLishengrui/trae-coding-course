#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 1007, mod = 1e9+7;

int n;
int f[N];//完全背包,体积是i的方案数

int main()
{
    cin>>n;
    f[0] = 1;

    for (int i = 1; i <= n; i++)
      for (int j = i; j <=n; j++)
        f[j] = (f[j] + f[j-i]) % mod;

    cout <<f[n]<<endl;
}