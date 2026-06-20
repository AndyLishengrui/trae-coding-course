#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;

const int MAXN = 6010;
vector<int> children[MAXN];
int h[MAXN];
long long dp[MAXN][2]; // dp[u][0]: u doesn't attend, dp[u][1]: u attends
bool hasBoss[MAXN];

void dfs(int u) {
    dp[u][0] = 0;
    dp[u][1] = h[u];
    for (int v : children[u]) {
        dfs(v);
        dp[u][0] += max(dp[v][0], dp[v][1]);
        dp[u][1] += dp[v][0];
    }
}

int main() {
    int n;
    scanf("%d", &n);
    for (int i = 1; i <= n; i++)
        scanf("%d", &h[i]);

    memset(hasBoss, 0, sizeof(hasBoss));
    for (int i = 0; i < n - 1; i++) {
        int l, k;
        scanf("%d %d", &l, &k);
        children[k].push_back(l);
        hasBoss[l] = true;
    }

    int root = -1;
    for (int i = 1; i <= n; i++)
        if (!hasBoss[i]) { root = i; break; }

    dfs(root);
    printf("%lld\n", max(dp[root][0], dp[root][1]));
    return 0;
}
