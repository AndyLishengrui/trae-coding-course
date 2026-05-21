#include <iostream>
#include <cstring>
using namespace std;
bool p[100];
bool used[100];
int a[100];
int n, now = 0;
void dfs(int deep) {
    if (deep == n + 1 && p[a[1] + a[n]]) {
        for (int i = 1; i <= n; i++) {
            cout << a[i];
            if (i != n) cout << " ";
        }
        cout << endl;
        return;
    }
    for (int i = 2; i <= n; i++) {
        if (!used[i] && p[i + a[deep - 1]]) {
            used[i] = true;
            a[deep] = i;
            dfs(deep + 1);  // 递归搜索下一个位置
            used[i] = false;  // 回溯
        }
    }
}
int main() {
    // 预处理质数表
    memset(p, false, sizeof(p));
    p[2] = p[3] = p[5] = p[7] = p[11] = true;
    p[13] = p[17] = p[19] = p[23] = p[29] = true;
    p[31] = p[37] = true;
    bool first_case = true;
    while (cin >> n) {
        a[1] = 1;  // 第一个元素固定为1
        if (!first_case) {
            cout << endl;
        }
        first_case = false;
        cout << "Case " << ++now << ":" << endl;
        memset(used, false, sizeof(used));
        dfs(2);  // 从第二个位置开始DFS
    }
    return 0;
}