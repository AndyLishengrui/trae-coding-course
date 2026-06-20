
#include <bits/stdc++.h>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <string>
#include <sstream>
#include <ctime>
using namespace std;
const int NUM = 10;

string getname(int i, string a)
{
    stringstream ss;
    ss << i << a;
    return ss.str();
}


int main()
{
    
    //只读入一组测试数据test.in，生成test.out的代码模板：
 //   freopen("test.in","r",stdin);//设置 cin scanf 这些输入流都从 test.in中读取
 //   freopen("test.out","w",stdout);//设置 cout printf 这些输出流都输出到 test.out里面去
    // 待测程序，即标程,放在这里
    
    //------------------------------我是分割线---------------------------------------
    
    //循环读入1.in-- 10.in    
    //循环读入10个in文件，生成10个out的代码模板：
    for (int tt = 1; tt <= NUM; tt++)
    {
        string inFileName,outFileName;//文件名
        inFileName = getname(tt, ".in");
        outFileName = getname(tt,".out");
        freopen(inFileName.c_str(),"r",stdin);
        freopen(outFileName.c_str(),"w",stdout);
    
    // 待测程序，即标程,放在这里
    // GW074 
    int N;
    scanf("%d",&N);
    for(int a = 2; a <= N; ++a)//a范围[2,N]
        for (int b = 2; b<=a-1; ++b) //b范围[2,a-1]
            for (int c=b; c<=a-1; ++c)//c范围[b,a-1]
                for(int d = c; d<=a-1; ++d)//d范围[c,a-1]
            if( a*a*a == b*b*b + c*c*c +d*d*d)
                printf("Cube = %d, Triple = (%d,%d,%d)\n", a, b, c,d);

    // _sleep(2*1000);//延时2秒 
       
    }

    return 0;
}
