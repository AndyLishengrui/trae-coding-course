
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
int noZeroRandom(int n)
{
	long result =random(n);
	while (result==0)
		result=random(n);
	return result;
}

int randNM()
{
    int n = random(100000) + 1;
    int m = 1000000000;


    for (int i = 1; i <= n; i++) {
        cout<<random(2 * m + 1) - m<<endl;;
    }
}

int randRangeLR(int n, int m)
{
for (int i = 1; i <= m; i++) {
    int l = random(n) + 1;
    int r = random(n) + 1;
    if (l > r) swap(l, r);
    printf("%d %d\n", l, r);
}
}
char randChar()
{
    return char('a'+random(26));
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


    
    //����10��in�ļ��Ĵ���ģ�壺
    for (int t = 1; t <= NUM; t++)
    {
        string inFileName;
        inFileName = getname(t, ".in");
        freopen(inFileName.c_str(),"w",stdout);
       
    cout<<noZeroRandom(20000)<<endl; 
//        if(caseNumber<=1) caseNumber=random(30);
//        cout<<caseNumber<<endl;

//    for (int it=0;it<10;it++)
//          cout<<s[t-1]<<endl;;
    
//        
//       for (int i=1;i<=3;i++)
//                cout<<randChar()<<" ";
//    cout<<endl;
//        // cout<<"-1 -1 -1 -1"<<endl;

    }
    return 0;
}
