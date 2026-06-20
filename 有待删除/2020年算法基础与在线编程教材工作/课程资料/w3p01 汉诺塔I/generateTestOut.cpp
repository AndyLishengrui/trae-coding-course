//BL2814 ��������  by Guo Wei
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
void Hanoi(int n, char src,char mid,char dest)
//将src座上的n个盘子，以mid座为中转，移动到dest座
{
    if( n == 1) {	//只需移动一个盘子
        cout << src << "->" << dest << endl;
    //直接将盘子从src移动到dest即可  
        return ;	//递归终止
    }
        Hanoi(n-1,src,dest,mid); //先将n-1个盘子从src移动到mid
        cout << src << "->" << dest << endl;
        //再将一个盘子从src移动到dest
        Hanoi(n-1,mid,src,dest); //最后将n-1个盘子从mid移动到dest
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

    
    //ֻ����һ���������test.in������test.out�Ĵ���ģ�壺
    freopen("10.in","r",stdin);//���� cin scanf ��Щ���������� test.in�ж�ȡ
    freopen("10.out","w",stdout);//���� cout printf ��Щ������������ test.out����ȥ
    // ������򣬼����,��������
    int n;
 	cin >> n; //输入盘子数目 
    Hanoi(n,'A','B','C');   
    //------------------------------���Ƿָ���---------------------------------------
    
    //ѭ������1.in-- 10.in    
    //ѭ������10��in�ļ�������10��out�Ĵ���ģ�壺
//    for (int tt = 7; tt <= NUM; tt++)
//    {
//        string inFileName,outFileName;//�ļ���
//        inFileName = getname(tt, ".in");
//        outFileName = getname(tt,".out");
//        freopen(inFileName.c_str(),"r",stdin);
//        freopen(outFileName.c_str(),"w",stdout);
//    
    // ������򣬼����,��������
    // Hanoi(1)
//		int n;
//	    cin >> n; //输入盘子数目 
//        Hanoi(n,'A','B','C');
//        fclose (stdin);
//        fclose (stdout);
//    }

    return 0;
}
