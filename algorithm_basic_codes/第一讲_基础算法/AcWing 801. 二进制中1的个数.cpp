#include <iostream>
using namespace std;
inline int lowbit(int &x)
{
    return x & -x;//x的二进制的最后一个1所构成的整数
}
int main()
{
    int n, x;
    cin >> n;
    while (n--)
    {
        //读入一个数，并且计算1的个数，并且输出
        cin >> x;
        int res = 0;//计数变量
        while (x)
            x -= lowbit(x), res++; //使用,表达式，简化代码去括号
        cout << res << " ";        //输出运算结果
    }
    return 0;
}
