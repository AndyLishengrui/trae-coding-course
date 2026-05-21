#include <iostream>
#include <vector>
#include <queue>
#include <bitset>
using namespace std;

const int MAXM = 30007;
vector<int> adj[MAXM];  // 邻接表
int inDegree[MAXM];     // 入度数组
int topoOrder[MAXM];    // 拓扑序列
int cnt;                // 拓扑序列长度
bitset<MAXM> reachable[MAXM];  // 可达性集合

void topoSort(int n) {
    queue<int> q;
    for (int i = 1; i <= n; ++i) {
        if (inDegree[i] == 0) q.push(i);
    }
    cnt = 0;
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        topoOrder[++cnt] = u;
        for (int v : adj[u]) {
            if (--inDegree[v] == 0) q.push(v);
        }
    }
}

void calcReachable(int n) {
    for (int i = cnt; i >= 1; --i) {
        int u = topoOrder[i];
        reachable[u].set(u);
        for (int v : adj[u]) {
            reachable[u] |= reachable[v];
        }
    }
}

int main() {
    int n, m;
    cin >> n >> m;
    for (int i = 1; i <= n; ++i) {
        adj[i].clear();
        inDegree[i] = 0;
        reachable[i].reset();
    }
    for (int i = 1; i <= m; ++i) {
        int x, y;
        cin >> x >> y;
        adj[x].push_back(y);
        inDegree[y]++;
    }
    topoSort(n);
    calcReachable(n);
    for (int i = 1; i <= n; ++i) {
        cout << reachable[i].count() << endl;
    }
    return 0;
}