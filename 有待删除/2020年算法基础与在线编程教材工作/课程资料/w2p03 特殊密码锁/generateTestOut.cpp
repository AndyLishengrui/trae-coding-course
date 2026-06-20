
#include <bits/stdc++.h>
#include <cstdlib>
#include <ctime>
#include <string>
#include <sstream>
#include <ctime>
#include <memory>  
#include <cstring>  
#include <iostream>  
using namespace std;
int oriLock;
int lock;
int destLock;
inline void SetBit(int & n,int i,int v)
{
	if(v) 
		n |= (1 << i);
	else
		n &= ~(1 << i);
}
inline void FlipBit(int & n,int i)
{
	n ^= (1 << i);
}
inline int GetBit(int n,int i)
{
	return (n >> i) & 1;
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
	char oriLights[5]; //最初灯矩阵，一个比特表示一盏灯
    char lights[5];  //不停变化的灯矩阵
    char pressed[5];  //结果按钮矩阵
    char switchs;  //某一行的开关状态
    
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
    // GW0101

    char line[40];
	destLock = lock = oriLock = 0;
	cin >> line;
	int N = strlen(line);
	for(int i = 0; i < N; ++i)
		SetBit(oriLock,i, line[i] - '0');
	cin >> line;
	for(int i = 0; line[i]; ++i)
		SetBit(destLock,i, line[i] - '0');
	int minTimes = 1 << 30;
	for(int p = 0; p < 2; ++p) { //p代表最左边按钮 
		lock = oriLock;
		int times = 0;
		int curButton = p;
		for(int i = 0; i < N; ++i) {
			if(curButton) {
				++ times;
				if( i > 0)
					FlipBit(lock,i-1);
				FlipBit(lock,i);
				if( i < N-1)
					FlipBit(lock,i+1);
			}
			if( GetBit(lock,i) != GetBit(destLock,i))  
				curButton = 1;
			else 
				curButton = 0;
		}
		if( lock == destLock) 
			minTimes = min(minTimes ,times);
	}
	if( minTimes == 1 << 30)
		cout << "impossible" << endl;
	else
		cout << minTimes << endl;
    // _sleep(2*1000);//延时2秒 
       
    }

    return 0;
}
