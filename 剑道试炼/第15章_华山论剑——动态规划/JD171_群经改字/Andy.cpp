#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int n, m;
char dict[1010][22];
int dlen[1010];

int editDist(const char *a, int alen, const char *b, int blen) {
    static int f[22][22];
    for (int i = 0; i <= alen; i++) f[i][0] = i;
    for (int j = 0; j <= blen; j++) f[0][j] = j;
    for (int i = 1; i <= alen; i++)
        for (int j = 1; j <= blen; j++) {
            f[i][j] = min(f[i - 1][j] + 1, f[i][j - 1] + 1);
            if (a[i - 1] == b[j - 1])
                f[i][j] = min(f[i][j], f[i - 1][j - 1]);
            else
                f[i][j] = min(f[i][j], f[i - 1][j - 1] + 1);
        }
    return f[alen][blen];
}

int main() {
    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; i++) {
        scanf("%s", dict[i]);
        dlen[i] = strlen(dict[i]);
    }
    for (int q = 0; q < m; q++) {
        char query[22];
        int limit;
        scanf("%s %d", query, &limit);
        int qlen = strlen(query);
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            if (editDist(query, qlen, dict[i], dlen[i]) <= limit)
                cnt++;
        }
        printf("%d\n", cnt);
    }
    return 0;
}
