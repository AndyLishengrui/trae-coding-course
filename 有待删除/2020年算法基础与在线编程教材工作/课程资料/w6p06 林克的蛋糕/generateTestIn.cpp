
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
int NoZeroRandom(int n) {
    int result=random(n);
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


int randTree(int n)
{
    for (int i = 2; i <= n; i++) {
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
       srand((unsigned)time(0));
        //   freopen("test.in","w",stdout);
        //   第一行包含两个正整数N和F，1 ≤ N, F ≤ 10 000，表示蛋糕的数量和朋友的数量。
   
    for (int t = 1; t <= NUM; t++)
    {
        string inFileName;
        inFileName = getname(t, ".in");
        freopen(inFileName.c_str(),"w",stdout);
       

        int N,F;
        N=NoZeroRandom(10000);
        F=NoZeroRandom(10000);
        cout<<N<<" "<<F<<endl;
        // 第二行包含N个1到10000之间的整数，表示每个蛋糕的半径。
        for (int i=1;i<=N;i++)
        {
          cout<<NoZeroRandom(10000)<<" ";
        }
        cout<<endl;

    }
    return 0;
}
