//BL2814 拨钟问题  by Guo Wei
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
int oriClocks[9];
int clocks[9];
const char * moves[9] = { "ABDE","ABC","BCEF","ADG","BDEFH","CFI","DEGH","GHI","EFHI" };
int moveTimes[9] = {0};
int result[9];
int minTimes = 1 << 30;
void resetClocks()
{
	memset(oriClocks,0,sizeof(oriClocks));
//	memset(clocks,0,sizeof(clocks));
	memset(moveTimes,0,sizeof(moveTimes));
	memset(result,0,sizeof(result));
}
void Enum(int n) 
{
	if( n >= 9 ) {
		memcpy(clocks,oriClocks,sizeof(clocks));
		int totalTimes = 0;
		for( int i = 0;i < 9 ; ++ i ) { //依次进行9种移动
			if( moveTimes[i] ) { 
				for( int k = 0; moves[i][k]; ++k) {
					clocks[moves[i][k]-'A'] = (clocks[moves[i][k]-'A'] + moveTimes[i]) % 4;
					totalTimes += moveTimes[i];
				}
			}
		}
		int i;
		for( i = 0;i < 9; ++i )
			if( clocks[i])
				break;
		if( i == 9) {
			if( minTimes > totalTimes) {
				minTimes = totalTimes;
				memcpy(result,moveTimes,sizeof(result)); 
			} 
		}
		return ;
	}
	for( int i = 0;i < 4; ++ i ) {
		moveTimes[n] = i;
		Enum(n+1);
	}
	return ;
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

    
    //只读入一组测试数据test.in，生成test.out的代码模板：
//    freopen("10.in","r",stdin);//设置 cin scanf 这些输入流都从 test.in中读取
//    freopen("10.out","w",stdout);//设置 cout printf 这些输出流都输出到 test.out里面去
    // 待测程序，即标程,放在这里
//        resetClocks();
//    	for( int i = 0;i < 9 ; ++i )
//		cin >> oriClocks[i];
//			Enum(0);
//		for( int i = 0; i < 9; ++i )
//			for( int k = 0; k < result[i] ; ++ k ) 
//			cout << i+1 << " ";
    
    //------------------------------我是分割线---------------------------------------
    
    //循环读入1.in-- 10.in    
    //循环读入10个in文件，生成10个out的代码模板：
//    for (int tt = 1; tt <= NUM; tt++)
//    {
//        string inFileName,outFileName;//文件名
//        inFileName = getname(tt, ".in");
//        outFileName = getname(tt,".out");
//        freopen(inFileName.c_str(),"r",stdin);
//        freopen(outFileName.c_str(),"w",stdout);
//    
    // 待测程序，即标程,放在这里
    // GW102
        resetClocks();
    	for( int i = 0;i < 9 ; ++i )
		cin >> oriClocks[i];
			Enum(0);
		for( int i = 0; i < 9; ++i )
			for( int k = 0; k < result[i] ; ++ k ) 
			cout << i+1 << " ";
     _sleep(2*1000);//延时2秒 
       
//    }

    return 0;
}
