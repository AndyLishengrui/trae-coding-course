#include <iostream>

using namespace std;
const int N = 1000007;
int n, m;

int a[N], s[N];

int main()
{
    scanf("%d%d", &n, &m);
    for (int i = 1; i <= n; i++)
        scanf("%d", &a[i]);
    s[0] = 0; //刻意初始化s[0]为0 ，此句可以不写，写也无妨
    for (int i = 1; i <= n; i++)
        s[i] = s[i - 1] + a[i]; //打表法
    //m次询问
    while (m--)
    {
        int l, r;
        scanf("%d%d", &l, &r);
        printf("%d\n", s[r] - s[l - 1]); //求区间和，直接从s中读取数值
    }

    return 0;
}
