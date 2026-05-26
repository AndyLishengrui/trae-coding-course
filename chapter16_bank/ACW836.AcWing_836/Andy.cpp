#include <iostream>
using namespace std;
const int N = 100007;
int p[N];
int n;

//返回x的father节点+路径压缩
int find(int x)
{
  if (p[x] != x) p[x] = find(p[x]);
  return p[x];
}
void merge(int a, int b)
{
  p[find(a)] = find(b);
}
void query(int a, int b)
{
   if (find(a) == find(b)) puts("Yes");
    else puts("No");
}
int main()
{ 
   int  m;
   cin>>n>>m;//输入n
  //创造并查集数
  for (int i = 1; i <=n; i++) p[i] = i;
  while (m--)
  {
    char op;
    int a,b;
    cin>>op;
    cin>>a>>b;
    if (op == 'M') merge(a,b);
    else if (op == 'Q') query(a,b);
  }
  return 0;
}
