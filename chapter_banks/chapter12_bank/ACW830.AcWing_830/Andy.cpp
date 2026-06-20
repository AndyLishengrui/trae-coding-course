#include <iostream>
using namespace std;
const int N=100007;
int n;
int stk[N],tt;//数组模拟栈实现单调栈
int main ()
{
    cin>> n;
    for (int i=0; i< n; i++){
        int x; cin>>x;
        while (tt && stk[tt]>= x)//tt为空，并且单调栈顶元素比x大
          tt--;//出栈，这些数永远不会用到
          if (tt) cout<<stk[tt]<<' '; //栈顶就是比x小的元素，直接输出
           else cout<<-1<<' '; //x左边没有任何数比它小
           //入栈
           stk[++tt] = x;
    }
    return 0;
}
