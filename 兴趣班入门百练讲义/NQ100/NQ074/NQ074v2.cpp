#include <cstring>
#include <iostream>
using namespace std;

int res[92][8];
int path[8];

// 将cnt作为参数传递，并返回最终值
int dfs(int n, int cnt) {
    if (n > 7) {
        for (int k = 0; k < 8; k++) res[cnt][k] = path[k];
        return cnt + 1;  // 返回下一个解的计数器
    }
    for (int i = 1; i <= 8; i++) {
        int k;
        for (k = 0; k < n; k++)
            if ((path[k] == i) || abs(path[k] - i) == abs(n - k)) break;
        if (k == n) {
            path[n] = i;
            cnt = dfs(n + 1, cnt);  // 更新计数器
        }
    }
    return cnt;  // 返回当前解的计数器
}

int main() {
    int T, n;
    memset(path, 0, sizeof(path));
    int totalSolutions = dfs(0, 0);  // 从0开始计数，获取总解数
    cin >> T;
    while (T--) {
        cin >> n;
        if (n < 1 || n > totalSolutions) {
            cout << "Invalid input!" << endl;  // 检查n的有效性
            continue;
        }
        for (int i = 0; i < 8; i++) cout << res[n - 1][i];  // 输出第n个解
        cout << endl;
    }
    return 0;
}