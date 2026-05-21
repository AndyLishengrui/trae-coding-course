//NQ094 全面反击
#include <algorithm>
#include <bitset>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <queue>
using namespace std;
#define MAXM 30007
int n, m, degree[MAXM], a[MAXM];  //存储入度、拓扑序的顶点
int edge[MAXM], Next[MAXM], head[MAXM], tot, cnt;
bitset<MAXM> f[MAXM];  //使用bit

void add(int x, int y) {  // 在邻接表中添加一条有向边
  edge[++tot] = y, Next[tot] = head[x], head[x] = tot;
  degree[y]++;  //入度++
}
// 拓扑排序
void topsort() {
  queue<int> q;  //队列
  for (int i = 1; i <= n; i++)
    if (degree[i] == 0)  //所有入度为0的顶点入栈
      q.push(i);
  //栈不空的时候拓扑排序
  while (q.size()) {
    int x = q.front();
    q.pop();
    a[++cnt] = x;  //保存拓扑过程中的顶点
    // 拓展顶点x
    for (int i = head[x]; i; i = Next[i]) {
      int y = edge[i];
      --degree[y];  //入度减1
      if (degree[y] == 0) q.push(y);
    }
  }  // end of while
}  // end of topsort

void calReachableNodes() {
  //逆序统计
  for (int i = cnt; i; i--) {
    int x = a[i];  //取拓扑排序过程中的顶点
    f[x][x] = 1;   //当前顶点设置为访问过
    for (int i = head[x]; i; i = Next[i]) {
      int y = edge[i];
      f[x] |= f[y];  //求并集合
    }
  }
}

int main() {
  cin >> n >> m;  // 点数、边数
  for (int i = 1; i <= m; i++) {
    int x, y;
    cin >> x >> y;
    add(x, y);  //建图
  }
  topsort();            //拓扑排序，顶点存储在全局数组a中
  calReachableNodes();  //逆序计算可达顶点数
  for (int i = 1; i <= n; i++) cout << f[i].count() << endl;
}
