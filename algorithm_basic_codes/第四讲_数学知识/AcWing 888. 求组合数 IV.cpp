//套用Y总模板，分解质因数、线性筛法、高精度乘法
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 5007;

int primes[N],cnt;//分解质因数
int sum[N];
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

int get(int n, int p)//求n中有几个p
{
  int res = 0;
  while (n)
  {
    res += n /p;
    n /= p;
  }
  return res;
}

//高精度乘法
vector<int> mul(vector<int> &A, int b)  // C = A * b, A >= 0, b >= 0
{
    vector<int> C;

    int t = 0;
    for (int i = 0; i < A.size() || t; i ++ )
    {
        if (i < A.size()) t += A[i] * b;
        C.push_back(t % 10);
        t /= 10;
    }

    while (C.size() > 1 && C.back() == 0) C.pop_back();

    return C;
}

int main()
{
    int a,b; cin>>a>>b;
    //分解质因数
    get_primes(a);

    for (int i = 0; i < cnt; i++)
    {
      int p = primes[i];
      sum[i] = get(a,p) - get(a-b,p) - get(b,p);//组合数公式计算质因数Prime[i]的个数
    }

    //高精度乘法
    vector<int> res;
    res.push_back(1);
    for (int i = 0; i < cnt; i++)
      for (int j = 0; j < sum[i]; j++)
        res = mul(res,primes[i]);//连乘sum[i]个primes[i]
    //输出高精度数
    for (int i = res.size()-1 ; i >=0; i--) cout<<res[i];
    puts("");

    return 0;
}