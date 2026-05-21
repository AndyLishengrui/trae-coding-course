#include <iostream>
#include <cstring>
using namespace std;
const int N = 6007; //最大是5842
int a[N];
bool is_humbernumber(int x)
{
    int res = x;
    while (res % 2 == 0) res /= 2;
    while (res % 3 == 0) res /= 3;
    while (res % 5 == 0) res /= 5;
    while (res % 7 == 0) res /= 7;
    return res == 1;
}
int main()
{
    memset(a, 0, sizeof(a)); //初始化
    int k = 1;
    //暴力枚举
    for (int i = 1; i < 20000000; i++)
    {
        //判断i是否是谦虚数
        if (is_humbernumber(i))
            a[k++] = i;
    }

    int q;
    cin >> q; //读入q组询问
    for (int j = 1; j <= q; j++)
    {
        int idx;
        cin >> idx;             //读入待查询的数
        cout << a[idx] << endl; //查表输出
    }

    return 0;
}
