#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;

int n, m;
long long dp[12][1 << 11];
vector<int> valid[1 << 11];

// Check if mask has all consecutive runs of 1-bits with even length
bool checkEven(int mask) {
    int cnt = 0;
    while (mask) {
        if (mask & 1) {
            cnt++;
        } else {
            if (cnt & 1) return false;
            cnt = 0;
        }
        mask >>= 1;
    }
    return (cnt & 1) == 0;
}

void solve() {
    int fullMask = (1 << n) - 1;
    // Precompute valid transitions: from state j, which states k are valid
    for (int j = 0; j <= fullMask; j++) {
        valid[j].clear();
        for (int k = 0; k <= fullMask; k++) {
            if (j & k) continue; // horizontal domino on filled cell
            if (!checkEven(fullMask ^ (j | k))) continue; // remaining cells must be vertically tileable
            valid[j].push_back(k);
        }
    }

    memset(dp, 0, sizeof(dp));
    dp[0][0] = 1;
    for (int col = 0; col < m; col++) {
        for (int j = 0; j <= fullMask; j++) {
            if (dp[col][j] == 0) continue;
            for (int k : valid[j]) {
                dp[col + 1][k] += dp[col][j];
            }
        }
    }
    printf("%lld\n", dp[m][0]);
}

int main() {
    while (scanf("%d %d", &n, &m) == 2) {
        if (n == 0 && m == 0) break;
        solve();
    }
    return 0;
}
