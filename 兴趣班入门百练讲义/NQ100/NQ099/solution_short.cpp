// NQ099 最省赛程 - 最优解实现
#include < cstring >
#include < iostream >
#include < queue >
#include < algorithm >
using namespace std;
const int N = 1010; //最大城市数量
const int M = 20200; //最大边数（无向图，需存双向边）
const int MAX_CAPACItY = 107;//最大油箱容量
const int INF = 0x3f3f3f3f;//无穷大，代表不可达状态
int oil_price[N]; //每个城市的单位油价
int expenses[N][MAX_CAPACItY];//expenses[city][fuel]：到达city且剩余fuel油量的最小花费
int head[N];
int ver[M];
int next_[M];//避免与std::next重名
int dist_[M];//道路消耗的油量，避免与std::dist重名
int tot = 0; //边的计数器
void add_edge(int u, int v, int d) {
 ver[tot] = v;
 dist_[tot] = d;
 next_[tot] = head[u];
 head[u] = tot++;
}
struct State {
 int city;
 int fuel;
 int cost;
 State(int c, int f, int co) : city(c), fuel(f), cost(co) {}
 bool operator < (const State& other) const {
  return cost > other.cost;
 }
};
// Dijkstra算法：计算从start到end，油箱容量为cap的最小油钱
int Dijkstra(int cap, int start, int end) {
 memset(expenses, 0x3f, sizeof(expenses));
 priority_queue < State > pq;
 expenses[start][0] = 0;
 pq.emplace(start, 0, 0);
 while (!pq.empty()) {
  auto curr = pq.top();
  pq.pop();
  int curr_city = curr.city;
  int curr_fuel = curr.fuel;
  int curr_cost = curr.cost;
  if (curr_cost > expenses[curr_city][curr_fuel]) {
   continue;
  }
  if (curr_city == end) {
   return curr_cost;
  }
  if (curr_fuel < cap) {
   int new_fuel = curr_fuel+1;
   int new_cost = curr_cost+oil_price[curr_city];
   if (new_cost < expenses[curr_city][new_fuel]) {
    expenses[curr_city][new_fuel] = new_cost;
    pq.emplace(curr_city, new_fuel, new_cost);
   }
  }
  for (int i = head[curr_city]; i != -1; i = next_[i]) {
   int next_city = ver[i];
   int fuel_needed = dist_[i];
   // 检查当前油量是否足够到达相邻城市
   if (curr_fuel >= fuel_needed) {
    int new_fuel = curr_fuel-fuel_needed;
    if (curr_cost < expenses[next_city][new_fuel]) {
     expenses[next_city][new_fuel] = curr_cost;
     pq.emplace(next_city, new_fuel, curr_cost);
    }
   }
  }
 }
 return-1;
}
int main() {
 ios::sync_with_stdio(false);
 cin.tie(nullptr);
 int n, m;
 cin > > n > > m;
 for (int i = 0; i < n;++i) {
  cin > > oil_price[i];
 }
 memset(head,-1, sizeof(head));
 tot = 0;
 for (int i = 0; i < m;++i) {
  int u, v, d;
  cin > > u > > v > > d;
  add_edge(u, v, d);
  add_edge(v, u, d);
 }
 int q;
 cin > > q;
 while (q--) {
  int C, S, E;
  cin > > C > > S > > E;
  int res = Dijkstra(C, S, E);
  if (res == -1) {
   cout < < "impossible\n";
  } else {
   cout < < res < < "\n";
  }
 }
 return 0;
}