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
#define MaxCharNumber 12
char str[MaxCharNumber]={0};
char strPermutation[MaxCharNumber]={0};
bool used[MaxCharNumber]={false};
int lengthOfInput;
void permutation(int n)
{ 
    // 如果n的值为lengthofInput，表明从0--LengthofInput都已经排列好
    // 输出此种排列方案
    if (n==lengthOfInput)
    {
        strPermutation[n]=0;//结尾设置为空字符，然后用cout直接输出整个字符串
        cout<<strPermutation<<endl;
        return;
    }
    // 假定n-1已经排列好，现在选取一个字母加入排列的队列中
    // used[i]为true，表示该字符已经被选取
    for (int k =0; k<lengthOfInput;k++)
    {
        if (!used[k])
        {
            used[k]=true;
            //把当前选出的字符放到strPermuation中
            strPermutation[n]=str[k];
            permutation(n+1);
            used[k]=false;
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


int main(int argc, char *argv[])
{

    
    freopen(argv[1],"r",stdin);
    freopen(argv[2],"w",stdout);
    // permutation
	    cin>>str;
        lengthOfInput=strlen(str);
        sort(str,str+lengthOfInput);//调用sort排序
        permutation(0);
        
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
//}		
    return 0;
}
