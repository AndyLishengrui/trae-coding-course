//Andy代码，参考Y总
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

typedef long long LL;

const int N = 1000007;

int primes[N],cnt;
int euler[N];
int st[N];

void get_eulers(int n)  // 线性筛法求1~n的欧拉函数
{
    euler[1] = 1;
    for (int i = 2; i <= n; i ++ )
    {
        if (!st[i])
        {
            primes[cnt ++ ] = i;//找到一个质数
            euler[i] = i - 1; //质数i的欧拉函数个数为i-1
        }
        //线性筛法，每次都/掉一个i
        for (int j = 0; primes[j] <= n / i; j ++ )
        {
            int t = primes[j] * i;
            st[t] = true;
            if (i % primes[j] == 0)
            {
                euler[t] = euler[i] * primes[j];
                break;
            }
            euler[t] = euler[i] * (primes[j] - 1);
        }
    }
}

int main()
{
    int n; cin>>n;

    get_eulers(n);

    LL res = 0;
    for (int i = 1; i <=n; i++) res += euler[i];
    cout<<res<<endl;

    return 0;
}