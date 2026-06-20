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
#define spacesize 4 
double inputnumber[spacesize+1];
#define EPS 1e-6
bool isZero(double x)
{
    return fabs(x)<=EPS;
}
bool count24(double a[],int n)//用数组里a的n个数计算24
{
    //数组大小为1，这时候只需要判断a[0]是否是24即可，若不是表示这个计算序列得不到24.
	if( n == 1 ) {
		if(isZero( a[0] - 24) )
			return true;
		else
			return false;
	}
    //n>1 把问题规模缩小为n-1
	//取出两个数，执行+-*/，生成新的实数，原来的数中剩下n-2个。 
	//因为+与*满足交换律,所以共有6种情况需要计算
	//每种情况都导致一个新数的诞生，把这个新数加回到n-2个数中
	//问题转换为计算n-1个数的算24点问题
	
	//枚举取出两个数
  	//输入数组a[0--n-1]
	// a[i],a[j]为当前取的两个数
	for (int i = 0;i<n-1;i++) //从0取到n-2个数 
	  for (int j =i+1;j<n;j++) //从i+1开始取到n-1
	  {
	  	//创建temp数组，存储n-1个要处理的数 
			double temp[n-1]={0};
			int iTemp=0;
			for (int k=0;k<n;k++)
			   if((k!=i)&&(k!=j)) temp[iTemp++]=a[k];
			//iTemp++执行了n-2次,所以temp[iTemp]就是当前最后一个元素，指向第n-1个数
			//分六种情况求temp[iTemp]的值
			//1. +
			temp[iTemp] = a[i] + a[j];
			if (count24(temp,n-1)) return true;
			
			//2. *
			temp[iTemp] = a[i] * a[j];
			if (count24(temp,n-1)) return true;
			 
		    //3. -
			temp[iTemp] = a[i] - a[j];
			if (count24(temp,n-1)) return true;
			//4. -
			temp[iTemp] = a[j] - a[i];
			if (count24(temp,n-1)) return true;
			//5. /
			if(!isZero(a[j]))
			{
				temp[iTemp] = a[i]/a[j];
			if (count24(temp,n-1)) return true;
			}
			//6. /
			if(!isZero(a[i]))
			{
				temp[iTemp] = a[j]/a[i];
			if (count24(temp,n-1)) return true;
			}
	   }// for 枚举两个数 
    return false;
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

    
//    //只锟斤拷锟斤拷一锟斤拷锟斤拷锟斤拷锟斤拷锟絫est.in锟斤拷锟斤拷锟斤拷test.out锟侥达拷锟斤拷模锟藉：
    freopen("10.in","r",stdin);//锟斤拷锟斤拷 cin scanf 锟斤拷些锟斤拷锟斤拷锟斤拷锟斤拷锟斤拷 test.in锟叫讹拷取
    freopen("10.out","w",stdout);//锟斤拷锟斤拷 cout printf 锟斤拷些锟斤拷锟斤拷锟斤拷锟斤拷锟斤拷锟斤拷 test.out锟斤拷锟斤拷去
    
    // GW078
	 while(true)
    {
        //判断是否输入是连续n个0
        bool isEndInput=true;
        for (int i = 0;i<spacesize;i++)
        {
          cin>>inputnumber[i];
          if(!isZero(inputnumber[i])) isEndInput=false;  
        }
        if (isEndInput) break;
        //调用count24计算结果
        if (count24(inputnumber,spacesize)) 
            cout<<"YES"<<endl;
            else   
            cout<<"NO"<<endl;
    }
//    
//    for (int tt = 1; tt <= NUM; tt++)
//    {
//        string inFileName,outFileName;//锟侥硷拷锟斤拷
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
