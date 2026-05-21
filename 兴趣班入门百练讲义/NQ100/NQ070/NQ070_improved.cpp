#include <cstdio>
#include <algorithm>
using namespace std;

const int MAXN = 100010;
int g[MAXN];

int main() {
    int n, m;
    scanf("%d", &n);
    
    g[0] = -1000000000;
    for (int i = 1; i <= n; ++i) {
        scanf("%d", &g[i]);
    }
    g[n+1] = 1000000000;
    
    scanf("%d", &m);
    while (m--) {
        int t;
        scanf("%d", &t);
        
        int l = lower_bound(g + 1, g + n + 1, t) - g;
        int r = upper_bound(g + 1, g + n + 1, t) - g;
        if (l <= n) l--;
        
        if (l == n + 1) {
            printf("%d\n", g[n]);
        } else if (r == 1) {
            printf("%d\n", g[1]);
        } else {
            if (t - g[l] > g[r] - t) {
                printf("%d\n", g[r]);
            } else {
                printf("%d\n", g[l]);
            }
        }
    }
    return 0;
}