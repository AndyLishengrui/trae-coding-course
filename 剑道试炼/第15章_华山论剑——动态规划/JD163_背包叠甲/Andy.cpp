#include <cstdio>
#include <algorithm>
using namespace std;

const int MAXV = 2010;
int dp[MAXV];
int vbuf[20010], wbuf[20010];

int main() {
    int N, V;
    scanf("%d%d", &N, &V);
    int cnt = 0;
    for (int i = 0; i < N; i++) {
        int v, w, s;
        scanf("%d%d%d", &v, &w, &s);
        // Binary split: decompose s into powers of 2
        int k = 1;
        while (k <= s) {
            vbuf[cnt] = k * v;
            wbuf[cnt] = k * w;
            cnt++;
            s -= k;
            k *= 2;
        }
        if (s > 0) {
            vbuf[cnt] = s * v;
            wbuf[cnt] = s * w;
            cnt++;
        }
    }
    // 0-1 knapsack over decomposed items
    for (int i = 0; i < cnt; i++) {
        for (int j = V; j >= vbuf[i]; j--) {
            dp[j] = max(dp[j], dp[j - vbuf[i]] + wbuf[i]);
        }
    }
    printf("%d\n", dp[V]);
    return 0;
}
