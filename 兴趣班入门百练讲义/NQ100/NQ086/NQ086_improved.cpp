#include <iostream>
#include <algorithm>
using namespace std;

const int MAX_N = 1007;
const int MAX_M = 1007;

int main() {
    int n, m;
    cin >> n >> m;
    
    int volume[MAX_N], value[MAX_N];
    for (int i = 1; i <= n; ++i) {
        cin >> volume[i] >> value[i];
    }
    
    int dp[MAX_M] = {0}; // dp[j] 表示背包容量为j时的最大价值
    
    // 遍历每个物品，逆序更新dp数组以避免重复选择
    for (int i = 1; i <= n; ++i) {
        for (int j = m; j >= volume[i]; --j) {
            dp[j] = max(dp[j], dp[j - volume[i]] + value[i]);
        }
    }
    
    cout << dp[m] << endl;
    return 0;
}
