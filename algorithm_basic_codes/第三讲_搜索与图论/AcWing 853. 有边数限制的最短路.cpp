#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;
const int N = 507, M = 100007;

struct edge {
  int a, b,w;
} edges[M];

int dist[N],backup[N];//备份数组，防止迭代的时候串联
int n,m,k;//k代表最短路径最多包含k条边

int bellman_ford(){
  memset(dist,0x3f,sizeof dist);//初始化为无穷大0x3f3f3f3f;
  dist[1] = 0;//顶点1为起点，搜索到顶点n的最短路径
  for (int i = 0; i<k; i++)
  {
    memcpy(backup,dist,sizeof dist);//备份dist数组

    for (int j = 0; j<m; j++) {//遍历所有边
    int a = edges[j].a, b=edges[j].b, w=edges[j].w;
    dist[b] = min(dist[b],backup[a]+w);//松弛操作

    }
  }

  if (dist[n] > 0x3f3f3f3f /2) return -1;
  else return dist[n];

}

int main()
{
    scanf("%d%d%d", &n,&m,&k);
    for (int i = 0; i < m; i ++ ) {
      int a, b, w;
      scanf("%d%d%d", &a,&b,&w);
      edges[i]={a,b,w};//直接用数组存储边和边权
    }

    int res = bellman_ford(); //调用bf算法
    if (res == -1) puts("impossible");
    else cout<<res;

    return 0;
}