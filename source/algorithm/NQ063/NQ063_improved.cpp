#include <iostream>
using namespace std;
const int MAX_N = 40;
long long dp[MAX_N + 1];
void Precalculate() {
    dp[1] = 1;
    dp[2] = 2;
    for (int i = 3; i <= MAX_N; ++i)
        dp[i] = dp[i-1] + dp[i-2]; // 动态规划：第i级台阶的走法数=前一级+前两级
}
int main() {
    Precalculate();
    int q;
    cin >> q;
    while (q--) {
        int n;
        cin >> n;
        if (n >= 1 && n <= MAX_N)
            cout << dp[n] << '\n';
    }
    return 0;
}