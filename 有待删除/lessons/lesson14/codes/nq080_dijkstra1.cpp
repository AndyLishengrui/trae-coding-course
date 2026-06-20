#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 510;//500*500
const int INF = 0x3f3f3f3f;

int g[N][N]; 
int dist[N];
bool st[N];

int n,m;

int Dijkstra()
{
  memset(dist,0x3f, sizeof dist);//初始化距离  0x3f代表无限大

  dist[1] = 0; //第一个点到自身的距离为0

  //有n个点，迭代n次
  for (int i = 0; i<n; i++)
  {
    int t = -1;//当前访问点的编号初始为-1

    for (int j = 1; j <= n; j++) //从点1到点n开始计算dist
      if (!st[j] && (t == -1 || dist[t] > dist[j]))
        t = j;// 更新点t，直到找到dist最小的点

    st[t]= true;//标记此点确定

    for (int j = 1; j <=n; j++)//每个点都要遍历所有点一遍
       dist[j] = min( dist[j], dist[t]+ g[t][j]);//遍历所有的点，求从点t到点j的最小值
   }


   if (dist[n] == INF) return -1;
   return dist[n];//返回第n个点的最短距离
}

int main()
{
  cin>>n>>m;

  memset(g, 0x3f, sizeof g);

  while (m--)
  {
    int x,y,z;
    cin>>x>>y>>z;
    g[x][y] = min( g[x][y],z);//取重边和自环的最小值，保留一条边
  }
  cout<<Dijkstra()<<endl;

  return 0;
}