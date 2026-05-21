#include <cstring>
#include <iostream>
#include <queue>
using namespace std;
// 骑士的8个可能移动方向
const int dx[8] = {1, 2, 2, 1, -1, -2, -2, -1};
const int dy[8] = {2, 1, -1, -2, -2, -1, 1, 2};
char g[160][160]; // 棋盘
int n, m;         // n是行数，m是列数
int d[160][160];  // d[x][y]表示从起点到(x,y)的最短步数
struct Point {
    int x, y;
    Point(int x = 0, int y = 0) : x(x), y(y) {}
} start, target;
queue<Point> q;
bool check(int x, int y) {
    return x >= 1 && x <= n && y >= 1 && y <= m && g[x][y] != '*' && d[x][y] == -1;
}
void findStartAndTarget() {
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            if (g[i][j] == 'K') {
                start.x = i;
                start.y = j;
            }
            if (g[i][j] == 'H') {
                target.x = i;
                target.y = j;
            }
        }
    }
}
int bfs() {
    memset(d, -1, sizeof(d));
    q.push(start);
    d[start.x][start.y] = 0;
    while (!q.empty()) {
        Point current = q.front();
        q.pop();
        for (int i = 0; i < 8; ++i) {
            int nx = current.x + dx[i];
            int ny = current.y + dy[i];
            if (check(nx, ny)) {
                d[nx][ny] = d[current.x][current.y] + 1;
                q.push(Point(nx, ny));
                if (nx == target.x && ny == target.y) {
                    return d[nx][ny];
                }
            }
        }
    }
    return -1;
}
int main() {
    cin >> m >> n; // 注意输入顺序：m是列数，n是行数
    for (int i = 1; i <= n; ++i) {
        cin >> (g[i] + 1); // 从g[i][1]开始存储
    }
    findStartAndTarget();
    cout << bfs() << endl;
    return 0;
}