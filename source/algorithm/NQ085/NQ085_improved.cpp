#include <iostream>
#include <algorithm>
using namespace std;
const int N = 1007;
int n, a[N][N], f[N][N];
int main() {
    cin >> n;
    for (int i = 1; i <= n; ++i)
        for (int j = 1; j <= i; ++j)
            cin >> a[i][j];
    f[1][1] = a[1][1]; // 边界条件：顶点的路径和为自身
    for (int i = 2; i <= n; ++i)
        for (int j = 1; j <= i; ++j)
            f[i][j] = max(f[i-1][j-1], f[i-1][j]) + a[i][j]; // 取上方或左上方的最大值
    int res = 0;
    for (int j = 1; j <= n; ++j)
        res = max(res, f[n][j]); // 最后一行的最大值即为答案
    cout << res << endl;
    return 0;
}