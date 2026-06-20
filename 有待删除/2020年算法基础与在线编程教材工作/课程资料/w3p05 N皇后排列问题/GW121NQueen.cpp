#include <iostream>
#include <cstring>
#include <cstdlib>
using namespace std;
int N;//读入的皇后个数
// solution存储皇后的一组解,solution[0]存储皇后第0行的位置
//solution[i-1]存储第i皇后的位置
int *solution;
 
void queen(int n)
{
    //递归出口，n从0开始到N-1全部遍历完毕
    if (n==N)
    {
       for (int k=0; k<N;k++)
       cout<<solution[k];
       cout<<endl;
        return;
    }
    //假定n-1个皇后已经全部摆好，现在准备摆第n个皇后
    //意味着solution[0]--solution[n-1]已经有值了
    for (int i = 1; i <= N; i++) //尝试0-N列位置，摆放第n个皇后
    {
        int k;
        for (k = 0; k < n; k++)
            if ((solution[k]==i) || //发现同列，跳出
                abs(solution[k]-i)==abs(n-k)) //对角线，跳出
                break;
        if (k==n) 
        {
            solution[n]=i;//把当前第n个皇后放在第i个位置上
            queen(n+1);
        }
    }
        
}
int main()
{
    //全局变量N皇后
   cin>>N;
   solution = new int[N];
   queen(0);
   delete [] solution;
   return 0;
}
