#include <iostream>

using namespace std;
const int N = 100010;

int m;
int stk[N], tt;//数组模拟栈

int main()
{
  cin>>m;
  while (m --)
  {
    string op;
    int x;

    cin>>op;
    if (op == "push")//栈顶指针+1，把数压入数组
    {
      cin >> x;
      stk[++tt] = x;//压入一个元素
    }
    else if (op == "pop") tt --;//修改栈顶指针即可
    else if (op == "empty") cout << (tt? "NO":"YES") <<endl;//tt>0表示非空
    else cout<<stk[tt]<<endl;//返回栈顶
  }
}