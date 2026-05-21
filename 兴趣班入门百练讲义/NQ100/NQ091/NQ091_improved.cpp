#include <cstring>
#include <iostream>
using namespace std;
// 骑士的8个可能移动方向
struct Point {
    int r, c;
} dir[8] = {{-2, -1}, {-2, 1}, {-1, -2}, {-1, 2},
    {1, -2}, {1, 2}, {2, -1}, {2, 1}};
Point path[30];       // 存储路径
int n, m;             // n是行数，m是列数
bool visited[30][30]; // 标记格子是否被访问过
bool dfs(int r, int c, int step) {
    if (step == n * m) {
        return true; // 找到路径
    }
    if (r < 0 || r >= n || c < 0 || c >= m || visited[r][c]) {
        return false;
    }
    visited[r][c] = true;
    path[step] = {r, c};
    // 尝试8个可能的移动方向
    for (int i = 0; i < 8; ++i) {
        int nr = r + dir[i].r;
        int nc = c + dir[i].c;
        if (dfs(nr, nc, step + 1)) {
            return true;
        }
    }
    visited[r][c] = false; // 回溯
    return false;
}
int main() {
    int t;
    cin >> t;
    for (int tt = 1; tt <= t; ++tt) {
        cout << "#" << tt << ":" << endl;
        cin >> m >> n; // m是列数，n是行数
        memset(visited, false, sizeof(visited));
        bool found = false;
        // 尝试从每个格子开始搜索
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (dfs(i, j, 0)) {
                    found = true;
                    for (int k = 0; k < n * m; ++k) {
                        char row = 'A' + path[k].r;
                        int col = path[k].c + 1; // 列号从1开始
                        cout << row << col;
                    }
                    break;
                }
            }
            if (found)
                break;
        }
        if (!found) {
            cout << "none";
        }
        cout << endl;
    }
    return 0;
}
