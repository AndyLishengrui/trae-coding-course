#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

const int MAX_N = 1007;
int d[MAX_N][MAX_N]; // 记忆化数组：d[i][j]表示从(i,j)出发的最长滑行路径长度
int h[MAX_N][MAX_N]; // 高度矩阵
int R, C;

// 四个方向的偏移量：左、上、右、下
int dx[] = {0, -1, 0, 1};
int dy[] = {-1, 0, 1, 0};

int dfs(int i, int j) {
    if (d[i][j] != -1) return d[i][j]; // 记忆化剪枝
    
    int max_len = 1; // 初始长度为1（当前位置）
    
    for (int k = 0; k < 4; ++k) {
        int ni = i + dx[k];
        int nj = j + dy[k];
        
        // 检查边界并确保高度递减
        if (ni >= 1 && ni <= R && nj >= 1 && nj <= C && h[i][j] > h[ni][nj]) {
            int len = dfs(ni, nj) + 1;
            max_len = max(max_len, len);
        }
    }
    
    return d[i][j] = max_len; // 记忆化存储结果
}

int main() {
    cin >> R >> C;
    
    memset(h, 0x3f, sizeof(h)); // 边界处理
    for (int i = 1; i <= R; ++i) {
        for (int j = 1; j <= C; ++j) {
            cin >> h[i][j];
        }
    }
    
    memset(d, -1, sizeof(d)); // 初始化记忆化数组
    
    int ans = 0;
    for (int i = 1; i <= R; ++i) {
        for (int j = 1; j <= C; ++j) {
            ans = max(ans, dfs(i, j));
        }
    }
    
    cout << ans << endl;
    return 0;
}
