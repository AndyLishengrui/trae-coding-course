cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

// 定义长整型用于成本计算，确保不会溢出 (最大成本约为 12 * 12 * 5*10^5 < 10^8)
using LL = long long;
const LL INF = 1e18; // 足够大的无穷大值

const int MAXN = 12;
int N, M;
LL L[MAXN][MAXN]; // 邻接矩阵存储最小道路长度

/**
 * @brief 预处理图，读取输入并构建最小长度邻接矩阵L
 */
void preprocess_graph() {
    // 初始化 L 矩阵为无穷大
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            L[i][j] = INF;
        }
    }

    // 读取 M 条边并更新 L 矩阵，确保 L[u][v] 存储的是 u 和 v 之间最短的原始道路长度
    for (int k = 0; k < M; ++k) {
        int u, v;
        LL weight;
        if (!(cin >> u >> v >> weight)) return; 
        // 转换为 0-based indexing
        --u; --v;
        L[u][v] = min(L[u][v], weight);
        L[v][u] = min(L[v][u], weight);
    }
}

/**
 * @brief 对固定的根节点 R 执行修改版的 Prim 算法，计算最小总代价
 * @param R 0-based 根节点索引
 * @return 最小总代价
 */
LL solve_for_root(int R) {
    // 记录节点是否已连接
    vector<bool> is_connected(N, false);
    // 记录节点的深度 D[u] (从R到u的路径上的节点数，D[R]=1)
    vector<int> depth(N, 0);
    // 记录连接节点 v 到已连接集合 S 所需的最小代价
    vector<LL> min_edge_cost(N, INF);
    // 记录提供 min_edge_cost 的父节点
    vector<int> parent(N, -1);

    LL current_total_cost = 0;
    int connected_count = 0;

    // 1. 初始化根节点 R
    is_connected[R] = true;
    depth[R] = 1;
    connected_count = 1;

    // 初始化其他节点到 R 的最小连接代价
    for (int v = 0; v < N; ++v) {
        if (v == R) continue;
        
        // 初始代价 = 长度 L[R][v] * D[R] (即 1)
        if (L[R][v] != INF) {
            min_edge_cost[v] = L[R][v] * depth[R];
            parent[v] = R;
        }
    }

    // 2. Prim 算法主循环 (N-1 次迭代)
    while (connected_count < N) {
        
        LL min_c = INF;
        int v_star = -1;

        // 2a. 找到代价最小的未连接节点 v*
        for (int v = 0; v < N; ++v) {
            if (!is_connected[v]) {
                if (min_edge_cost[v] < min_c) {
                    min_c = min_edge_cost[v];
                    v_star = v;
                }
            }
        }

        // 如果找不到可连接的节点，说明图不连通
        if (v_star == -1 || min_c == INF) {
            return INF; 
        }

        // 2b. 连接 v*
        current_total_cost += min_c;
        is_connected[v_star] = true;
        connected_count++;

        // 2c. 确定 v* 的深度
        int u_star = parent[v_star];
        // u_star 保证不为 -1，因为 min_c 是有限值
        depth[v_star] = depth[u_star] + 1;
        
        // 2d. 更新未连接邻居 w 的连接代价
        LL depth_multiplier = depth[v_star];

        for (int w = 0; w < N; ++w) {
            if (!is_connected[w] && L[v_star][w] != INF) {
                // 新潜在代价 = 长度 L[v_star][w] * D[v_star]
                LL new_cost = L[v_star][w] * depth_multiplier;
                
                if (new_cost < min_edge_cost[w]) {
                    min_edge_cost[w] = new_cost;
                    parent[w] = v_star;
                }
            }
        }
    }

    return current_total_cost;
}


LL solve() {
    // 读取 N 和 M
    if (!(cin >> N >> M)) return 0;

    preprocess_graph();

    LL min_overall_cost = INF;

    // 遍历所有可能的起始点 R (0 到 N-1)
    for (int R = 0; R < N; ++R) {
        LL cost = solve_for_root(R);
        min_overall_cost = min(min_overall_cost, cost);
    }

    return min_overall_cost;
}

int main() {
    // 优化输入输出
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    LL result = solve();
    cout << result << endl;

    return 0;
}
