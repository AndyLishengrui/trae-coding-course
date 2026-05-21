#include <iostream>

using namespace std;

// 台阶问题是一个经典的动态规划问题，其解法对应于斐波那契数列的变种。
// 设 dp[i] 表示到达第 i 级台阶的不同走法总数。
// 递推关系：dp[i] = dp[i-1] + dp[i-2]。

// N 的最大值限制
const int MAX_N = 40;

// 使用 long long 存储结果，尽管对于 N=40 来说 int 足够，但 long long 提供了额外的溢出安全性。
long long dp[MAX_N + 1];

/**
 * @brief 预计算所有 N (1 <= N <= 40) 的上台阶方案数。
 */
void Precalculate() {
    // 基础情况 (Base Cases):
    // N=1: 1 种走法 ([1])
    dp[1] = 1;

    // N=2: 2 种走法 ([1, 1], [2])
    dp[2] = 2;

    // 动态规划递推计算
    for (int i = 3; i <= MAX_N; ++i) {
        // 到达 i 级，要么从 i-1 走 1 步，要么从 i-2 走 2 步。
        dp[i] = dp[i - 1] + dp[i - 2];
    }
}

/**
 * @brief 处理测试用例，读取 Q 和 N，并输出结果。
 */
void Solve() {
    // 预计算 DP 结果
    Precalculate();

    int q;
    // 读取测试实例的个数 q
    if (!(cin >> q)) {
        return;
    }

    while (q--) {
        int n;
        // 读取台阶数 N
        if (!(cin >> n)) {
            break;
        }

        // 根据题目约束 1 <= N <= 40，直接输出预计算的结果。
        if (n >= 1 && n <= MAX_N) {
            cout << dp[n] << "\n";
        }
    }
}

int main() {
    // 提升 I/O 效率
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    Solve();

    return 0;
}