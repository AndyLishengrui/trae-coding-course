#include <cstdio>
#include <algorithm>
using namespace std;

const int MAXV = 1010;
int dp[MAXV];

int main() {
    int N, V;
    scanf("%d%d", &N, &V);
    for (int g = 0; g < N; g++) {
        int S;
        scanf("%d", &S);
        int gv[1010], gw[1010];
        for (int i = 0; i < S; i++) {
            scanf("%d%d", &gv[i], &gw[i]);
        }
        // For each group, try each item (at most one per group)
        for (int j = V; j >= 0; j--) {
            for (int i = 0; i < S; i++) {
                if (j >= gv[i]) {
                    dp[j] = max(dp[j], dp[j - gv[i]] + gw[i]);
                }
            }
        }
    }
    printf("%d\n", dp[V]);
    return 0;
}
