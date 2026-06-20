
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
    while (result < 1)
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
       
    for (int t = 3; t <= 10; t++)
    {
        string inFileName;
        inFileName = getname(t, ".in");
        freopen(inFileName.c_str(),"w",stdout);
       
        int T,n;        
        n = NoZeroRandom(10000);
      
        vector<int> a;
        for (int i=0; i<n; i++) a.push_back(NoZeroRandom(100000000));      

        vector<int> b(a);//拷贝一份a
        
        sort(a.begin(), a.end());
        a.erase(unique(a.begin(),a.end()),a.end());
        n = a.size();
        int x = NoZeroRandom(n-1), y = NoZeroRandom(n-1), z = NoZeroRandom(n-1);
        int target = a[x] + a[y] + a[z];//三数之和
        //输出target,n
        cout<<target<<" "<<b.size()<<endl;
        //输出数组
        for(auto x:b) cout<<x<<" ";
        
    }
    return 0;
}
