// Andy 2021.06.04
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 100000007;

int primes[N],cnt;
bool st[N];
void get_primes(int n)  // 线性筛质数
{
    for (int i = 2; i <= n; i ++ )
    {
        if (!st[i]) primes[cnt ++ ] = i;
        for (int j = 0; primes[j] <= n / i; j ++ )
        {
            st[primes[j] * i] = true;
            if (i % primes[j] == 0) break;
        }
    }
}


int main()
{
    int n; cin>>n;
    get_primes(n);
    cout<<cnt<<endl;
    return 0;
}