//容斥原理
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

typedef long long LL;

const int N = 20;

int n,m;
int p[N];

int main()
{
    cin>>n>>m;
    for (int i = 0; i < m; i++) cin >>p[i];

    int res = 0;
    //用i的二进制数来枚举集合的选取情况
    for (int i = 1; i < 1<<m; i++)
    {
      int t = 1, cnt =0;
      for (int j = 0; j < m; j++)
        if (i >>j & 1)
        {
          cnt ++;//计算二进制中1的个数
          if ((LL) t * p[j] > n)
          { 
            t = -1;
            break;
          }
          t *= p[j]; //分母
        }
        if (t != -1)
        {
          if (cnt % 2) res += n / t;
          else res -= n / t;
        }
    }
    cout <<res<<endl;

    return 0;
}