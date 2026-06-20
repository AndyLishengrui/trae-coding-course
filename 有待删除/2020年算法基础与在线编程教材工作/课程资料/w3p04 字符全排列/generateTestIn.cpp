
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

// Êµï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½
int randTree(int n)
{
    for (int i = 2; i <= n; i++) {
        // ï¿½ï¿½ 2~n Ö®ï¿½ï¿½ï¿½Ã¿ï¿½ï¿½ï¿½ï¿½ i ï¿½ï¿½ 1~i-1 Ö®ï¿½ï¿½Äµï¿½ï¿½ï¿½ï¿½ï¿½ï¿½Ò»ï¿½ï¿½ï¿½ï¿½
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
    //ï¿½ï¿½Ê¼ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½Ä³ï¿½Ê¼Öµ
       srand((unsigned)time(0));
    
    //ï¿½ï¿½ï¿½ï¿½1ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½test.inï¿½Ä´ï¿½ï¿½ï¿½Ä£ï¿½ï¿½
    //   freopen("test.in","w",stdout);//ï¿½ï¿½ï¿½ï¿½ cout printf ï¿½ï¿½Ð©ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ test.inï¿½ï¿½ï¿½ï¿½È¥
    // Ð´ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½Ä¿ï¿½ï¿½ï¿½ï¿½Òªï¿½ï¿½Ò»ï¿½ÂµÄ²ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½
    // return 0;


    
    //ï¿½ï¿½ï¿½ï¿½10ï¿½ï¿½inï¿½Ä¼ï¿½ï¿½Ä´ï¿½ï¿½ï¿½Ä£ï¿½å£º
    for (int t = 1; t <= NUM; t++)
    {
        string inFileName;
        inFileName = getname(t, ".in");
        freopen(inFileName.c_str(),"w",stdout);
       
	   bool used[26]= {false};
       int Lenth= noZeroRandom(12);//×Ö·û´®³¤¶È1-6
       //Êä³ö³¤¶ÈÎª1-6µÄ²»ÖØ¸´×Ö·û´®£¬¶¼ÊÇÐ¡Ð´×ÖÄ¸ 
	   for (int k=1;k<=Lenth;k++)
	   {
	   	    int charIndex= random(26); 
	   	    while (used[charIndex])
			   {
			   	charIndex= random(26);
				}
			used[charIndex]=true;
			cout<<char('a'+charIndex);	 
		} 
		cout<<endl;
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
