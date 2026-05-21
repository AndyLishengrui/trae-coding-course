#include <cstring>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;
bool topoSort(int n, vector<vector<int>>& adj, vector<int>& inDegree, vector<int>& topoOrder) {
    queue<int> q;
    // 将所有入度为0的点加入队列
    for (int i = 1; i <= n; ++i) {
        if (inDegree[i] == 0) {
            q.push(i);
        }
    }
    int idx = 0;
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        topoOrder[idx++] = u;
        // 遍历所有邻接点，更新入度
        for (int v : adj[u]) {
            if (--inDegree[v] == 0) {
                q.push(v);
            }
        }
    }
    return idx == n; // 检查是否所有点都被访问到
}
int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> adj(n + 1);
    vector<int> inDegree(n + 1, 0);
    vector<int> topoOrder(n);
    for (int i = 0; i < m; ++i) {
        int a, b;
        cin >> a >> b;
        adj[a].push_back(b);
        inDegree[b]++;
    }
    if (topoSort(n, adj, inDegree, topoOrder)) {
        for (int i = 0; i < n; ++i) {
            cout << topoOrder[i] << " ";
        }
        cout << endl;
    } else {
        cout << -1 << endl;
    }
    return 0;
}
