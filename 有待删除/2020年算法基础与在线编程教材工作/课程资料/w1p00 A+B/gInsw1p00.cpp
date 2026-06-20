
#include <bits/stdc++.h>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <string>
#include <sstream>
#include <ctime>
#define For(a, begin, end) for (register int a = begin; a < end; ++a)
#define Clear(a, b) memset(a, b, sizeof(a))
using namespace std;
template <typename AAA>
inline void CMax(AAA &u, AAA v)
{
    if (v > u)
        u = v;
} //把最大值存在u里面

int random(int n)
{
    return (long long)rand() * rand() % n;
}
int NoZeroRandom(int n)
{
    int result = random(n);
    while (result == 0)
        result = random(n);
    return result;
}

int randNM()
{
    int n = random(100000) + 1;
    int m = 1000000000;

    for (int i = 1; i <= n; i++)
    {
        cout << random(2 * m + 1) - m << endl;
    }
}

int randRangeLR(int n, int m)
{
    for (int i = 1; i <= m; i++)
    {
        int l = random(n) + 1;
        int r = random(n) + 1;
        if (l > r)
            swap(l, r);
        printf("%d %d\n", l, r);
    }
}
char randChar()
{
    return char('a' + random(26));
}

int randTree(int n)
{
    for (int i = 2; i <= n; i++)
    {
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
void printGrid2str(int lines)
{
    string readstr;
    For(i, 0, lines)
    {
        string s;
        cin >> s;
        cout << s << endl;
    }
}

int main()
{
    srand((unsigned)time(0));
    //    freopen("test.in","r",stdin);
    //  弱数据
    For(t, 1, 11)
    {

        string inFileName;
        inFileName = getname(t, ".in");
        freopen(inFileName.c_str(), "w", stdout);
        // 输出tt组询问
        // 第一行包含两个整数n和m。
        int n = NoZeroRandom(10000000); //a的大小
        int m = NoZeroRandom(10000000); 
        //累计数的起点
        cout << n << " "<<m<<endl;
    }// end of for
    return 0;
}
