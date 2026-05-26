#include <iostream>
#include <cstring>

using namespace std;
const int N = 100007;
int p[N],Size[N];
int n;

//返回x的father节点+路径压缩
int find(int x)
{
  if (p[x] != x) p[x] = find(p[x]);
  return p[x];
}
void merge(int a, int b)
{
  Size[find(b)] += Size[find(a)];
  p[find(a)] = find(b);
}
void query(int a, int b)
{
   if (find(a) == find(b)) puts("Yes");
    else puts("No");
}
int count(int x)
{
  return Size[find(x)];
}
int main()
{ 
   int  m;
   cin>>n>>m;//输入n
  //创造并查集数
  for (int i = 1; i <=n; i++) p[i] = i , Size[i] = 1;
  while (m--)
  {
    string op;
    int a,b;
    cin>>op;
    if (op == "C") 
    { 
      cin>>a>>b;
      if (find(a) == find(b)) continue;//已经在同一个集合里，跳过merge操作
      merge(a,b);
    }
    else if (op == "Q1") cin>>a>>b, query(a,b);
    else cin>>a, cout<<count(a)<<endl;;
  }
  return 0;
}
