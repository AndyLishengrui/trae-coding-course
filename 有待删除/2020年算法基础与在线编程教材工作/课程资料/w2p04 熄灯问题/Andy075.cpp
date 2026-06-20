#include <iostream>
#include <cstring>
using namespace std;
#define Row 5
#define Column 6
bool lights[Row+2][Column+2]; //数组多一个边界，让按钮的操作只需要处理一种状况
bool lightstates[Row+2][Column+2];//存储中间状态
bool pressed[Row+2][Column+2]; //需要按的数组 

bool btnPress(int i,int j)
{
    if ((i>Row+2)||(j>Column+2)||(i<0)||(j<0)) return false;//下标越界
    //取反中，下，上，左，右的状态
    lightstates[i][j]=!lightstates[i][j];
    lightstates[i-1][j]=!lightstates[i-1][j];
    lightstates[i+1][j]=!lightstates[i+1][j];
    lightstates[i][j-1]=!lightstates[i][j-1];
    lightstates[i][j+1]=!lightstates[i][j+1];
    //记录按下的按钮
    pressed[i][j]=true;
    return true;
} 
bool isLightOn(int i,int j)
{
    return lightstates[i][j];
}
//判断是否整行都熄灯
bool isWholeRowDown(int RowNo)
{
    for (int j=1;j<=Column;j++)
    {
           if (isLightOn(RowNo,j)) return false;
    }
    return true;
}
//修改灯的状态
void initStates()
{
    memset(lightstates,0,sizeof(lightstates));
    memset(pressed,0,sizeof(pressed));
    memcpy(lightstates,lights,sizeof(lightstates));
}
int main() {  
    int t;  cin >> t;
    int round=0;
    while(t--) {
    //输入样例
    for(int i = 1;i <= Row; ++i)
        for (int j=1;j<=Column;++j) 
          cin>> lights[i][j];


    //枚举第一行的按键状况，从什么都不按，到全部按
    for(int ii=0;ii<64;++ii)
    {
        //重置状态数值
        initStates();
    //遍历第一行按钮的状态000000,000001,000010,000011,000100
        int temp[Column+2];
        int num=ii,n=1;
        while (num!=0){
            temp[n]=num%2;//倒序存储数值
            num/=2;
            n++;}
        for(n=n-1;n>=1;n--)
        {
            //按下相应的按钮
            if(temp[n]==1)
            btnPress(1,n);
        }
        //处理其余的行，让第一行到倒数第二行的灯全部都熄灭
        for (int jj=2;jj<=Row;++jj)
        for (int cc=1;cc<=Column;++cc)
            {
                if (isLightOn(jj-1,cc)) btnPress(jj,cc);
            }
        //检查最后一行的状态
        //判断最后一行是否全部熄灭，如果是，退出循环，输出按钮方案，否则枚举下一种按键的情况
        if (isWholeRowDown(Row))  break;
    }
    //输出按钮状态
    cout<<"PUZZLE #"<<++round<<endl;
    // cout<<"Button Pressed:"<<endl;
    for(int i = 1;i <= Row; ++i)
    {
        for (int j=1;j<=Column;++j) 
          cout<<pressed[i][j]<<" ";
        cout<<endl;
    }
    }

    return 0;
}
