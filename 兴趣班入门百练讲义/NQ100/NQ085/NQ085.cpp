#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;
const int N = 1007;
const int INF = 0x3f3f3f3f;
int n, a[N][N], f[N][N];
int main() {
    cin >> n;
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= i; ++j) {
            cin >> a[i][j];
        }
    }
    memset(f, -INF, sizeof(f));
    f[1][1] = a[1][1];  // 边界条件：第一个位置的和就是它本身
    for (int i = 2; i <= n; ++i) {
        for (int j = 1; j <= i; ++j) {
            f[i][j] = max(f[i-1][j-1], f[i-1][j]) + a[i][j];  // 动态规划：取上方或左上方的最大值
        }
    }
    int res = -INF;
    for (int j = 1; j <= n; ++j) {
        res = max(res, f[n][j]);  // 找到最后一行的最大值
    }
    cout << res << endl;
    return 0;
}