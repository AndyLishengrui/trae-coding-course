#include < iostream >
#include < cstdio >
#include < cstring >
#include < algorithm >
#include < queue >
using namespace std;
#define For(i, a, b) for (int i = a; i < b; i++)
#define N 507//最大是500
struct Stone {
 int x, y, status;//x,y为石柱的基块坐标；stadus:0为站立 1为横躺 2为竖躺
 Stone(int a, int b, int c) {x = a, y = b, status = c;}
 Stone() : x(0), y(0),status(0){};
};
int direction[4][3][3] = {
 {{-2, 0, 2}, {-1, 0, 1}, {-1, 0, 0}},
 {{1, 0, 2}, {1, 0, 1}, {2, 0, 0}},
 {{0,-2, 1}, {0,-1, 0}, {0,-1, 2}},
 {{0, 1, 1}, {0, 2, 0}, {0, 1, 2}}
};
Stone moveStone(Stone &p, int udlf) {
 int dx = direction[udlf][p.status][0];
 int dy = direction[udlf][p.status][1];
 int newstatus = direction[udlf][p.status][2];
 return Stone(p.x+dx, p.y+dy, newstatus);
}
int n, m;
char area[N][N];
int dist[N][N][3];
queue < Stone > q; //BFS使用的队列
Stone start, target, qHead;//起点，终点，队列中的头坐标
bool isInside(int x, int y) {
 return x >= 0 && x < n && y >= 0 && y < m;
}
bool isValid(Stone node) {
 if (!isInside(node.x, node.y) || area[node.x][node.y] == '#')
 return false;//不在范围内
 if (node.status == 2 && (!isInside(node.x+1, node.y) || area[node.x+1][node.y] == '#'))
 return false;//竖躺碰到禁区
 if (node.status == 1 && (!isInside(node.x, node.y+1) || area[node.x][node.y+1] == '#'))
 return false;
 if (node.status == 0 && area[node.x][node.y] == 'E')
 return false;
 return true;
}
bool isVisited(Stone node) {
 return dist[node.x][node.y][node.status] != -1;
}
char readChar() {
 char c = getchar();
 while (c != '#' && c != '.' && c != 'X' && c != 'O' && c != 'E')
 c = getchar();
 return c;
}
void BuildMap(int n, int m) {
 memset(area, '#', sizeof(area));//初始化为禁区
 memset(dist,-1, sizeof(dist));//初始化
 For(i, 0, n) For(j, 0, m) area[i][j] = readChar();
 For(i, 0, n) For(j, 0, m) {
  char c = area[i][j];
  if (c == 'X') {
   start.x = i, start.y = j, start.status = 0, area[i][j] = '.';//找到起点，站立
   if (isInside(i,j+1) && area[i][j+1] == 'X')
   start.status = 1, area[i][j+1] = '.';//横躺
   if (isInside(i+1,j) && area[i+1][j] == 'X')
   start.status = 2, area[i+1][j] = '.';//竖躺
  }
  if (c == 'O')
  target.x = i, target.y = j, target.status = 0;//必须站立才能过关
 }
}
int bfs(Stone &s) {
 while (q.size())
 q.pop();//清空队列
 q.push(s);
 dist[s.x][s.y][s.status] = 0;//起始点步数为0
 while (q.size()) {
  qHead = q.front();
  q.pop();
  For(i, 0, 4) {
   Stone next = moveStone(qHead, i);
   if (!isValid(next)) continue;
   if (!isVisited(next)) {
    dist[next.x][next.y][next.status] = dist[qHead.x][qHead.y][qHead.status]+1;
    q.push(next);
    if (next.x == target.x && next.y == target.y && next.status == target.status)
    return dist[next.x][next.y][next.status];
   }
  }
 }
 return-1;
}
int main() {
 while (cin > > n > > m && n) {
  BuildMap(n, m);
  int res = bfs(start);
  if (res == -1)
  cout < < "Impossible" < < endl;
  else
  cout < < res < < endl;
 }
}