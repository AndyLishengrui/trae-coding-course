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
double PolishNotation() 
{
    char str[32];
    cin>>str; //读入下一个表达式
    switch (str[0])
    {
    case '+': return PolishNotation() + PolishNotation();
        break;
    case '-': return PolishNotation() - PolishNotation();
        break;
    case '*': return PolishNotation() * PolishNotation();
        break;
    case '/':return PolishNotation() / PolishNotation();
    default:
        return atof(str); //把字符串转换为浮点数
    break;
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

    
//    //ֻ����һ���������test.in������test.out�Ĵ���ģ�壺
    freopen("11.in","r",stdin);//���� cin scanf ��Щ���������� test.in�ж�ȡ
    freopen("11.out","w",stdout);//���� cout printf ��Щ������������ test.out����ȥ
    
    // GW079
	printf("%lf",PolishNotation()); 
    
//    for (int tt = 1; tt <= NUM; tt++)
//    {
//        string inFileName,outFileName;//�ļ���
//        inFileName = getname(tt, ".in");
//        outFileName = getname(tt,".out");
//        freopen(inFileName.c_str(),"r",stdin);
//        freopen(outFileName.c_str(),"w",stdout);
//        
//          
//
//
//}		
    return 0;
}
