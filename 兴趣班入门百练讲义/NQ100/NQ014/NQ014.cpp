//NQ014 凤凰花开吃杨梅
#include <iostream>
using namespace std;
int f(int n) //f函数输入天数n 返回最初的杨梅数p
{
    int res = 1;
    //上一天的杨梅数为这一天的加1再乘以2，循环n-1次
    for (int i = n - 1; i > 0; --i) 
        res = (res + 1) * 2;
    return res;
}
int main()
{
    int x;
    while (cin>>x)//输入
    	cout<<f(x)<<endl;//输出
    return 0;
}