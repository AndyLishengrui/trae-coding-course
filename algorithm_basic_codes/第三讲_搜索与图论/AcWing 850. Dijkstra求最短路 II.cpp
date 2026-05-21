#include <algorithm>
#include <cstring>
#include <iostream>
#include <queue>

using namespace std;

typedef pair<int, int> PII;

const int N = 1e6 + 10;

int n, m;                          //行，列
int h[N], w[N], e[N], ne[N], idx;  //数组模拟链表
int dist[N];                       //距离矩阵
bool st[N];                        //状态矩阵

//建边函数（数组模拟链表)
void add(int a, int b, int c) {
  e[idx] = b, w[idx] = c, ne[idx] = h[a], h[a] = idx++;
}

//改进版，使用小根堆
int dijkstra() {
  //初始化距离矩阵
  memset(dist, 0x3f, sizeof dist);
  dist[1] = 0;
  //调用优先队列，以及greater算子，创建小根堆
  priority_queue<PII, vector<PII>, greater<PII>> heap;

  //按照距离排序，因此第一个元素是距离，第二个元素是顶点编号
  heap.push({0, 1});

  // BFS计算最短距离
  while (heap.size()) {
    //取堆头元素
    auto t = heap.top();
    heap.pop();

    // 取顶点编号、顶点距离
    int ver = t.second, distance = t.first;

    // 顶点遍历过就跳过，不展开改顶点
    if (st[ver]) continue;
    st[ver] = true;

    //遍历所有相邻顶点
    for (int i = h[ver]; i != -1; i = ne[i]) {
      int j = e[i];
      //判断dist[ver]+w[i]是否比原来顶点j的距离大
      if (dist[j] > dist[ver] + w[i]) {
        dist[j] = dist[ver] + w[i];  //更新顶点j的距离值
        heap.push({dist[j], j});     //把更小的距离值入堆
      }
    }
  }
  //如果第n点距离值没被更新，表明不可达
  if (dist[n] == 0x3f3f3f3f) return -1;
  //返回点n的距离值
  return dist[n];
}

int main() {
  //读入行n，列m
  scanf("%d%d", &n, &m);
  //把邻接链表的头指针化为-1，表明当前为空，不指向任何链表
  memset(h, -1, sizeof h);
  //处理m条边
  while (m--) {
    int a, b, c;
    scanf("%d%d%d", &a, &b, &c);
    add(a, b, c);//调用add建图
  }
  //调用改进版的dijkstra()
  cout << dijkstra() << endl;

  return 0;
}