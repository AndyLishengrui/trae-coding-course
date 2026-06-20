
#include <bits/stdc++.h>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <string>
#include <sstream>
#include <ctime>

using namespace std;

int random(int n) {
    return (long long)rand() * rand() % n;
}


// ����1 ���������������
// ������100000������ֵ��1000000000�ڵ�����

int randNM()
{
    int n = random(100000) + 1;
    int m = 1000000000;


    for (int i = 1; i <= n; i++) {
        cout<<random(2 * m + 1) - m<<endl;;
    }
}

// ����2 �������������
int randRangeLR(int n, int m)
{
for (int i = 1; i <= m; i++) {
    int l = random(n) + 1;
    int r = random(n) + 1;
    if (l > r) swap(l, r);
    printf("%d %d\n", l, r);
}
}

// ʵ�������������
int randTree(int n)
{
    for (int i = 2; i <= n; i++) {
        // �� 2~n ֮���ÿ���� i �� 1~i-1 ֮��ĵ������һ����
        int fa = random(i - 1) + 1;
        int val = random(1000000000) + 1;
        printf("%d %d %d\n", fa, i, val);
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
    //��ʼ����������ĳ�ʼֵ
       srand((unsigned)time(0));
    
    //����1����������test.in�Ĵ���ģ��
    //   freopen("test.in","w",stdout);//���� cout printf ��Щ������������ test.in����ȥ
    // д������������Ŀ����Ҫ��һ�µĲ�������
    // return 0;

//------------------------------���Ƿָ���---------------------------------------
    
    //����10��in�ļ��Ĵ���ģ�壺
    for (int t = 11; t <= 20; t++)
    {
        string inFileName;
        inFileName = getname(t, ".in");
        freopen(inFileName.c_str(),"w",stdout);
    //  cout<<t+3<<endl;
        int caseNumber= random(10000);
//       if(caseNumber<=3) caseNumber=random(30);
        cout<<caseNumber<<endl;

//    for (int it=3;it<=13;it++)
//    {     
//        cout<<it<<endl;
//        // cout<<"-1 -1 -1 -1"<<endl;
//    }
	}	
    return 0;
}
