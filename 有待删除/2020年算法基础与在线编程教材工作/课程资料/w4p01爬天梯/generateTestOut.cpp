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
#pragma comment(linker, "/STACK:1073741824000")
using namespace std;
int N;
int stairs(int n)
{
    if( n < 0)
        return 0;
    if( n == 0 )
        return 1;
    return stairs(n-1) + stairs(n-2);
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
    freopen("9.in","r",stdin);//���� cin scanf ��Щ���������� test.in�ж�ȡ
    freopen("9.out","w",stdout);//���� cout printf ��Щ������������ test.out����ȥ
    
    // GW123
	 cin >> N;
    cout << stairs(N) << endl;
//    
//    for (int tt = 1; tt <= NUM; tt++)
//    {
//        string inFileName,outFileName;//�ļ���
//        inFileName = getname(tt, ".in");
//        outFileName = getname(tt,".out");
//        freopen(inFileName.c_str(),"r",stdin);
//        freopen(outFileName.c_str(),"w",stdout);
//
//
//}		
    return 0;
}
