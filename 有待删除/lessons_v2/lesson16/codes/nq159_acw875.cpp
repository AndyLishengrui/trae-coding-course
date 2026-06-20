#include <iostream>
#include <algorithm>
using namespace std;
typedef long long LL;
int qmi(int a, int b, int p)
{
    int res = 1; //初始值为1
    while (b)
    {
        if (b & 1)                 //b的最末尾为1
            res = (LL)res * a % p; //必须用long long防止溢出
        b >>= 1;                   //去掉b最低位
        a = (LL)a * a % p;
    }
    return res;
}

int main()
{
    int n;
    scanf("%d", &n); //数据很大，需要用LL读入
    while (n--)
    {
        int a, b, p;
        scanf("%d%d%d", &a, &b, &p); //读入a b p

        printf("%d\n", qmi(a, b, p)); //计算快速幂
    }
    return 0;
}
