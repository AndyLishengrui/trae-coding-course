#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int n;
int w[20][20];
long long dp[1 << 16][16];

int main() {
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            scanf("%d", &w[i][j]);

    int full = (1 << n) - 1;
    memset(dp, 0x3f, sizeof(dp));
    dp[1][0] = 0; // start at vertex 0

    for (int mask = 0; mask <= full; mask++) {
        for (int i = 0; i < n; i++) {
            if (!(mask & (1 << i))) continue;
            if (dp[mask][i] >= 0x3f3f3f3f3f3f3f3fLL) continue;
            for (int j = 0; j < n; j++) {
                if (mask & (1 << j)) continue;
                int nmask = mask | (1 << j);
                dp[nmask][j] = min(dp[nmask][j], dp[mask][i] + w[i][j]);
            }
        }
    }
    printf("%lld\n", dp[full][n - 1]);
    return 0;
}
