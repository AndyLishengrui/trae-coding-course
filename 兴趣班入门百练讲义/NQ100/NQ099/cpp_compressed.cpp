// NQ099 最省赛程 - 最优解实现
#include <cstring>
#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;

const int N = 1010;          // 最大城市数量
const int M = 20200;         // 最大边数（无向图，需存双向边）
const int MAX_CAPACITY = 107; // 最大油箱容量
const int INF = 0x3f3f3f3f;  // 无穷大，代表不可达状态

int oil_price[N];             // 每个城市的单位油价
int expenses[N][MAX_CAPACITY]; // expenses[city][fuel]：到达city且剩余fuel油量的最小花费

// 邻接表结构（无向图）
int head[N];
int ver[M];
int next_[M];  // 避免与std::next重名
int dist_[M];  // 道路消耗的油量，避免与std::dist重名
int tot = 0;   // 边的计数器

// 添加无向边
void add_edge(int u, int v, int d) {
    ver[tot] = v;
    dist_[tot] = d;
    next_[tot] = head[u];
    head[u] = tot++;
}

// 状态结构体：当前城市、剩余油量、累计花费
struct State {
    int city;
    int fuel;
    int cost;
    State(int c, int f, int co) : city(c), fuel(f), cost(co) {}
    
    // 优先队列排序规则：小根堆，花费小的优先出队
    bool operator<(const State& other) const {
        return cost > other.cost;
    }
};

// Dijkstra算法：计算从start到end，油箱容量为cap的最小油钱
int Dijkstra(int cap, int start, int end) {
    // 初始化花费数组为无穷大
    memset(expenses, 0x3f, sizeof(expenses));
    priority_queue<State> pq;

    // 初始状态：起点城市，油量0，花费0（需在起点加油才能出发）
    expenses[start][0] = 0;
    pq.emplace(start, 0, 0);

    while (!pq.empty()) {
        auto curr = pq.top();
        pq.pop();

        int curr_city = curr.city;
        int curr_fuel = curr.fuel;
        int curr_cost = curr.cost;

        // 如果当前状态花费大于已知最优解，直接跳过（冗余状态）
        if (curr_cost > expenses[curr_city][curr_fuel]) {
            continue;
        }

        // 到达终点，返回当前最小花费
        if (curr_city == end) {
            return curr_cost;
        }

        // 操作1：在当前城市加1升油（不超过油箱容量）
        if (curr_fuel < cap) {
            int new_fuel = curr_fuel + 1;
            int new_cost = curr_cost + oil_price[curr_city];
            if (new_cost < expenses[curr_city][new_fuel]) {
                expenses[curr_city][new_fuel] = new_cost;
                pq.emplace(curr_city, new_fuel, new_cost);
            }
        }

        // 操作2：尝试前往相邻城市
        for (int i = head[curr_city]; i != -1; i = next_[i]) {
            int next_city = ver[i];
            int fuel_needed = dist_[i];
            // 检查当前油量是否足够到达相邻城市
            if (curr_fuel >= fuel_needed) {
                int new_fuel = curr_fuel - fuel_needed;
                // 移动仅消耗油量，不产生新花费
                if (curr_cost < expenses[next_city][new_fuel]) {
                    expenses[next_city][new_fuel] = curr_cost;
                    pq.emplace(next_city, new_fuel, curr_cost);
                }
            }
        }
    }

    // 无法到达终点
    return -1;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    // 读取每个城市的油价
    for (int i = 0; i < n; ++i) {
        cin >> oil_price[i];
    }

    // 初始化邻接表
    memset(head, -1, sizeof(head));
    tot = 0;

    // 读取道路信息
    for (int i = 0; i < m; ++i) {
        int u, v, d;
        cin >> u >> v >> d;
        add_edge(u, v, d);
        add_edge(v, u, d);
    }

    int q;
    cin >> q;
    while (q--) {
        int C, S, E;
        cin >> C >> S >> E;
        int result = Dijkstra(C, S, E);
        if (result == -1) {
            cout << "impossible\n";
        } else {
            cout << result << "\n";
        }
    }

    return 0;
}
