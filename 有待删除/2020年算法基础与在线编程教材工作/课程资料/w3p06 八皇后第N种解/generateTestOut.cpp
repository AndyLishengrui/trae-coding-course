
#include <bits/stdc++.h>
#include <cstdlib>
#include <ctime>
#include <string>
#include <sstream>
#include <memory>  
#include <cstring>  
#include <iostream>
#include <bitset>
#include <algorithm>
#include <functional>

using namespace std;
int queenSpace[92][8];//八皇后的解空间数组，每一行是一种皇后的摆法
int solution[8];// solution存储皇后的一组解,solution[0]存储皇后第0行的位置，solution[i]存储皇后第i行的位置
int solutionNUmber=0;//可行解的计数器

void queen(int n)
{
    //递归出口，n从0开始到7全部遍历完毕
    if (n>7)
    {
        for (int k=0; k<8;k++)
            queenSpace[solutionNUmber][k]= solution[k];
        solutionNUmber++;
        return;
    }
    //假定n-1个皇后已经全部摆好，现在准备摆第n个皇后
    //意味着solution[0]--solution[n-1]已经有值了
    for (int i = 1; i <= 8; i++) //尝试0-7列位置，摆放第n个皇后
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
const int NUM = 10;

string getname(int i, string a)
{
    stringstream ss;
    ss << i << a;
    return ss.str();
}


int main()
{

    
    //只锟斤拷锟斤拷一锟斤拷锟斤拷锟斤拷锟斤拷锟絫est.in锟斤拷锟斤拷锟斤拷test.out锟侥达拷锟斤拷模锟藉：
    freopen("10.in","r",stdin);//锟斤拷锟斤拷 cin scanf 锟斤拷些锟斤拷锟斤拷锟斤拷锟斤拷锟斤拷 test.in锟叫讹拷取
    freopen("10.out","w",stdout);//锟斤拷锟斤拷 cout printf 锟斤拷些锟斤拷锟斤拷锟斤拷锟斤拷锟斤拷锟斤拷 test.out锟斤拷锟斤拷去
    // 锟斤拷锟斤拷锟斤拷颍锟斤拷锟斤拷,锟斤拷锟斤拷锟斤拷锟斤拷
    int T,q,j;
    memset(solution,0,sizeof(solution));
    solutionNUmber=0;
    queen(0);
    cin>>T;//T组测试数据
    for (int i=0;i<T;i++)
    {
        cin>>q;
        for(j=0;j<8;j++)
         cout<<queenSpace[q-1][j];
         cout<<endl;

    }
    
//    for (int tt = 7; tt <= NUM; tt++)
//    {
//        string inFileName,outFileName;//锟侥硷拷锟斤拷
//        inFileName = getname(tt, ".in");
//        outFileName = getname(tt,".out");
//        freopen(inFileName.c_str(),"r",stdin);
//        freopen(outFileName.c_str(),"w",stdout);
//    
    // 锟斤拷锟斤拷锟斤拷颍锟斤拷锟斤拷,锟斤拷锟斤拷锟斤拷锟斤拷
    // Hanoi(1)
//		int n;
//	    cin >> n; //杈撳叆鐩樺瓙鏁扮洰 
//        Hanoi(n,'A','B','C');
//        fclose (stdin);
//        fclose (stdout);
//    }

    return 0;
}
