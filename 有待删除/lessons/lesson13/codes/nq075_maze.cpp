#include <algorithm>
#include <iostream>
#include <queue>
#include <cstring>
using namespace std;

typedef pair<int, int> PII;  // Y总风格pair<int,int>声明

const int N = 107;

int n, m;
int g[N][N],d[N][N];  

//广搜
int bfs() {

  queue<PII> q;      //队列

  memset(d,-1,sizeof d);
  d[0][0]=0;
  q.push({0,0});

  // 四个方向向量
  int dx[] = {-1, 0, 1, 0}, dy[] = {0, 1, 0, -1};

  while (q.size()) 
  { //队列为空的时候退出广搜
    auto t = q.front();  //取队头
    q.pop();             //弹出队头

    //搜索四个方向
    for (int i = 0; i < 4; i++)
    {
      int x = t.first + dx[i], y = t.second + dy[i];  //待搜索的新坐标点

      if (x < 0 || x >= n || y < 0 || y >= m || g[x][y] != 0 || d[x][y]!=-1) continue;

      d[x][y] = d[t.first][t.second]+1;

      q.push({x, y});//入队


    }
  }

  return d[n-1][m-1];
}

int main() {

    cin >> n >> m;

    for (int i = 0; i < n; i++) 
      for (int j = 0; j <m; j++)
        cin >> g[i][j];

    cout << bfs() << endl;

  return 0;
}