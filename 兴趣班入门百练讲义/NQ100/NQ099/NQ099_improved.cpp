#include <iostream>
#include <vector>
#include <queue>
#include <climits>
using namespace std;

const int MAX_N = 1010;
const int MAX_CAPACITY = 107;

struct Edge {
    int to, distance;
    Edge(int t, int d) : to(t), distance(d) {};
};

vector<vector<Edge>> adj(MAX_N);
int oil_price[MAX_N];
int expenses[MAX_N][MAX_CAPACITY];
bool visited[MAX_N][MAX_CAPACITY];

struct Node {
    int city, fuel, money;
    Node(int c, int f, int m) : city(c), fuel(f), money(m) {};
    bool operator<(const Node& other) const {
        return money > other.money; // 小根堆
    }
};

priority_queue<Node> pq;

int dijkstra(int cap, int start, int target, int n) {
    // 初始化
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j <= cap; ++j) {
            expenses[i][j] = INT_MAX;
            visited[i][j] = false;
        }
    }
    
    // 清空优先队列
    while (!pq.empty()) pq.pop();
    
    // 起点状态
    expenses[start][0] = 0;
    pq.push(Node(start, 0, 0));
    
    while (!pq.empty()) {
        Node current = pq.top();
        pq.pop();
        
        int city = current.city;
        int fuel = current.fuel;
        int money = current.money;
        
        if (city == target) return money;
        if (visited[city][fuel]) continue;
        visited[city][fuel] = true;
        
        // 尝试加一升油
        if (fuel < cap) {
            int new_fuel = fuel + 1;
            int new_money = money + oil_price[city];
            if (new_money < expenses[city][new_fuel]) {
                expenses[city][new_fuel] = new_money;
                pq.push(Node(city, new_fuel, new_money));
            }
        }
        
        // 尝试前往相邻城市
        for (Edge edge : adj[city]) {
            int next = edge.to;
            int req_fuel = edge.distance;
            if (fuel >= req_fuel) {
                int new_fuel = fuel - req_fuel;
                if (money < expenses[next][new_fuel]) {
                    expenses[next][new_fuel] = money;
                    pq.push(Node(next, new_fuel, money));
                }
            }
        }
    }
    
    return -1; // 无法到达
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, m;
    cin >> n >> m;
    
    for (int i = 0; i < n; ++i) {
        cin >> oil_price[i];
    }
    
    for (int i = 0; i < m; ++i) {
        int u, v, d;
        cin >> u >> v >> d;
        adj[u].emplace_back(v, d);
        adj[v].emplace_back(u, d);
    }
    
    int q;
    cin >> q;
    while (q--) {
        int c, s, e;
        cin >> c >> s >> e;
        int res = dijkstra(c, s, e, n);
        if (res == -1) {
            cout << "impossible" << endl;
        } else {
            cout << res << endl;
        }
    }
    
    return 0;
}