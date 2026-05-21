#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 1007;

string a[N];
int f[N][N];
int n,m;

int edit_distance(string a, string b)
{
  a = " "+ a, b = " "+ b;//前置加一个空格，让处理的下标从1开始
  int la = a.length(), lb = b.length();

  //初始化变化为空串的操作数
  for (int i = 0; i <= la; i++) f[i][0] = i;
  for (int i = 0; i <= lb; i++) f[0][i] = i;
  // 动态规划递推
  for (int i = 1; i <= la; i++)
   for (int j = 1; j <= lb; j++)
   {
     f[i][j] = min(f[i-1][j]+1, f[i][j-1]+1);
     f[i][j] = min(f[i][j], f[i-1][j-1]+(a[i]!=b[j]));
   }
  return f[la][lb];

}

int main()
{
    cin>>n>>m;
    //讀入n個字符串
    for(int i = 0; i < n; i++) cin>>a[i];

    while (m -- )
    {
      string b;
      cin>>b;
      int steps;
      cin>>steps;
      //统计有多少a[i]与b的编辑距离小于steps
      int res = 0;
      for (int i = 0; i <n; i++) {
        if (edit_distance(a[i],b) <= steps) res ++;
      }
      cout<<res<<endl;
    }
    return 0;
}