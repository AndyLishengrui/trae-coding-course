//完全参考Y总代码
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 10;

//数组num[i]的[l,r]各个数转换为十进制数
int get(vector<int> num, int l, int r)
{
  int res = 0;
  for (int i = l; i >= r; i--) res = res * 10 + num[i];
  return res;
}
//计算10的x次方
int power10(int x)
{
  int res = 1;
  while (x --) res *=10;
  return res;
}

int count(int n, int x)
{
  if (!n) return 0;

  vector<int> num;
  //n转换为数组
  while (n)
  {
    num.push_back(n % 10);
    n /= 10;
  }
  n = num.size();//存储几位数

  int res = 0;
  for (int i = n -1 - !x; i >=0; i--)
  {
    if (i < n - 1)
    {
      res += get(num, n-1, i+1) * power10(i);
      if (!x) res -= power10(i);//去掉首字母为0的情况
    }

    if (num[i] == x) res += get(num,i-1,0) + 1;
    else if (num[i]>x) res+=power10(i);
  }
  return res;
}

int main()
{
    int a,b;
    while (cin>>a>>b, a)
    {
      if (a>b) swap(a,b);
      for (int i = 0; i <=9; i++)//计算前缀和的思想
        cout<<count(b,i)- count(a-1,i) <<' ';
      cout <<endl;
    }
    return 0;
}