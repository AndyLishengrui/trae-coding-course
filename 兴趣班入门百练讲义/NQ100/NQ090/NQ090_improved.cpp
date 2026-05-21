#include <algorithm>
#include <cstring>
#include <iostream>
using namespace std;
const int MAX_W = 27;
const int MAX_H = 27;
const int MAX_M = 407;
const int INF = 0x3f3f3f3f;
int minMax[MAX_W][MAX_H][MAX_M]; // 记忆化数组：minMax[w][h][cnt]表示将w×h的矩形切成cnt+1块时的最小最大面积
int dfs(int w, int h, int cnt) {
    if (w * h < cnt + 1)
        return INF; // 无法分割
    if (cnt == 0)
        return w * h; // 不需要切
    if (minMax[w][h][cnt] != -1)
        return minMax[w][h][cnt]; // 记忆化剪枝
    int minMArea = INF;
    // 尝试竖切
    for (int i = 1; i < w; ++i) {
        for (int k = 0; k <= cnt; ++k) {
            int left = dfs(i, h, k);
            int right = dfs(w - i, h, cnt - 1 - k);
            minMArea = min(minMArea, max(left, right));
        }
    }
    // 尝试横切
    for (int j = 1; j < h; ++j) {
        for (int k = 0; k <= cnt; ++k) {
            int top = dfs(w, j, k);
            int bottom = dfs(w, h - j, cnt - 1 - k);
            minMArea = min(minMArea, max(top, bottom));
        }
    }
    return minMax[w][h][cnt] = minMArea; // 记忆化存储
}
int main() {
    int W, H, M;
    while (cin >> W >> H >> M) {
        if (W == 0 && H == 0)
            break;
        memset(minMax, -1, sizeof(minMax));
        cout << dfs(W, H, M - 1) << endl;
    }
    return 0;
}