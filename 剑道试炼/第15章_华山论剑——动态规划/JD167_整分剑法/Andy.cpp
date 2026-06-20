#include <cstdio>
using namespace std;

const int MOD = 1000000007;
const int MAXN = 1010;
int dp[MAXN]; // dp[j] = number of ways to partition j

int main() {
    int n;
    scanf("%d", &n);
    dp[0] = 1;
    // For each value i from 1 to n, treat as complete knapsack
    for (int i = 1; i <= n; i++) {
        for (int j = i; j <= n; j++) {
            dp[j] = (dp[j] + dp[j - i]) % MOD;
        }
    }
    printf("%d\n", dp[n]);
    return 0;
}
