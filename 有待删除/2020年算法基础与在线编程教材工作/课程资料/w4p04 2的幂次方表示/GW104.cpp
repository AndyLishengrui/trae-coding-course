#include <iostream>
using namespace std;

inline int GetBit(int n,int i)
{
	return (n >> i ) & 1;
}
void printDigital(int n)
{
    //从低位到高位，枚举输入n的每一位
    //整数为16位,所以取15--0位
    bool isFirstTerm=true;
    for (int i = 15; i >=0 ; --i)
    {
          //该位为1，不为0，需要输出
        if(GetBit(n,i))
        {
            if(!isFirstTerm)
            {
                cout<<"+";
            } else 
                isFirstTerm=false;   
            //如果i为0，表示只有最低位是1，直接输出2(0)
            if (i==0)
                cout<<"2(0)";
            else
            if (i==1)
                cout<<"2";
            else
            {          
            //对于读到的每一位，输出二进制的新表达式
                cout<<"2(";
                printDigital(i);//why?
                cout<<")";
            }
        };
}
}

int main ()
{
    int N;
    cin>>N;
    printDigital(N);
    return 0;
}
