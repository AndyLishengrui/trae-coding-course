
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


// 范例1 随机生成整数序列
// 不超过100000个绝对值在1000000000内的整数

int randNM()
{
    int n = random(100000) + 1;
    int m = 1000000000;


    for (int i = 1; i <= n; i++) {
        cout<<random(2 * m + 1) - m<<endl;;
    }
}

// 范例2 随机生成区间列
int randRangeLR(int n, int m)
{
for (int i = 1; i <= m; i++) {
    int l = random(n) + 1;
    int r = random(n) + 1;
    if (l > r) swap(l, r);
    printf("%d %d\n", l, r);
}
}

// 实例：随机生成树
int randTree(int n)
{
    for (int i = 2; i <= n; i++) {
        // 从 2~n 之间的每个点 i 向 1~i-1 之间的点随机连一条边
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
    //初始化随机函数的初始值
       srand((unsigned)time(0));
    
    //创建1个测试数据test.in的代码模板
    //   freopen("test.in","w",stdout);//设置 cout printf 这些输出流都输出到 test.in里面去
    // 写代码生成与题目输入要求一致的测试数据
    // return 0;

//------------------------------我是分割线---------------------------------------
    
    //创建10个in文件的代码模板：
    for (int t = 1; t <= NUM; t++)
    {
        string inFileName;
        inFileName = getname(t, ".in");
        freopen(inFileName.c_str(),"w",stdout);
       
       // 写代码生成与题目输入要求一致的测试数据
       //案例数 1-100
       int caseNumber= random(20);
       if(caseNumber<=0) caseNumber=random(20);
       cout<<caseNumber<<endl;

       for (int i=1;i<=caseNumber;i++)
       {
        for (int n=1;n<=5;n++)
          for (int m=1;m<=6;m++)
          {
                cout<<random(2)<<" ";
                if(m>=6) cout<<endl;
          }
        }      
        // cout<<"-1 -1 -1 -1"<<endl;

    }
    return 0;
}