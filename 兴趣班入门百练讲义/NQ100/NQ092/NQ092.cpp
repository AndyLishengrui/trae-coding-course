// NQ092 骑士林克的怜悯(2)
#include <bits/stdc++.h>
using namespace std;
#define FOR(i, a, b) for (int i = a; i <= b; i++)
// 搜索8个马跳跃的方向
const int dx[8] = {1, 2, 2, 1, -1, -2, -2, -1};
const int dy[8] = {2, 1, -1, -2, -2, -1, 1, 2};

char g[160][160];
int n, m, d[160][160];

#define pii pair<int, int>
pii start, target;
queue<pii> q;

bool check(int x, int y) {  //在范围内;且不是障碍物;第一次被访问
  return x>=1 && x<=n && y>=1 && y<=m && g[x][y]!='*'&&d[x][y]==-1;
}

void setST(void)  //找起点和终点
{
  FOR(i, 1, n) FOR(j, 1, m) {
    if (g[i][j] == 'K') {
      start.first = i;
      start.second = j;
    }
    if (g[i][j] == 'H') {
      target.first = i;
      target.second = j;
    }
  }
}
int bfs(void) {
  memset(d, -1, sizeof(d));
  q.push(make_pair(start.first, start.second));  //压入起点
  d[start.first][start.second] = 0;
  while (q.size()) {
    pii pHead = q.front();
    q.pop();
    FOR(i, 0, 7) {
      int x = pHead.first + dx[i], y = pHead.second + dy[i];  //拓展
      if (check(x, y))                                        //满足条件
      {
        d[x][y] = d[pHead.first][pHead.second] + 1;
        q.push(make_pair(x, y));
        if (x == target.first && y == target.second)  //到达终点了
          return d[x][y];
      }
    }
  }
  return -1;  //然而并没有无解情况
}
int main() {
  scanf("%d%d\n", &m, &n);  //*谨慎读入！
  FOR(i, 1, n)
  scanf("%s", g[i] + 1);  //!读入从字符1开始
  setST();                //*锁定起点和终点
  cout << bfs();
  return 0;
}