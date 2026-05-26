#include <iostream>
#include <cstring>
#include <algorithm>
#include <queue>

using namespace std;

const int N = 100007;//有向图

int n,m;
int h[N], e[N], ne[N], idx;
int d[N];

void add(int a, int b)  // 添加一条边a->b
{
    e[idx] = b, ne[idx] = h[a], h[a] = idx ++ ;
}

int bfs()
{
  memset(d,-1,sizeof d);
  queue<int> q;
  d[1] = 0;//起始点
  q.push(1);

  while (q.size())
  {
    auto t = q.front();
    q.pop();

    for (int i = h[t]; i!=-1; i = ne[i])
    {
      int j = e[i];
      if (d[j]==-1)
      {
        d[j] = d[t]+1; //层次加1
        q.push(j);
      }
    }
  }
  return d[n];
}

int main()
{
    cin>>n>>m;
    memset(h, -1, sizeof h);

    for (int i = 0; i < m; i++)
    {
      int a, b;
      cin>>a>>b;
      add(a,b);
    }

    cout<<bfs()<<endl;
    return 0;
}
