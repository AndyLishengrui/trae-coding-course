// NQ100 滚石柱 - 改进版
#include <iostream>
#include <vector>
#include <queue>
#include <cstring>
using namespace std;

const int MAX_N = 507;

struct Stone {
    int x, y, status; // x,y为石柱的基块坐标；status:0为站立 1为横躺 2为竖躺
    Stone(int a = 0, int b = 0, int c = 0) : x(a), y(b), status(c) {}
};

// 四种方向 UP=0, DOWN=1, LEFT=2, RIGHT=3
// 每种状态的坐标以方块的左上顶点的格子为基准点
int direction[4][3][3] = {
    {{-2, 0, 2}, {-1, 0, 1}, {-1, 0, 0}},  // UP
    {{1, 0, 2}, {1, 0, 1}, {2, 0, 0}},      // DOWN
    {{0, -2, 1}, {0, -1, 0}, {0, -1, 2}},   // LEFT
    {{0, 1, 1}, {0, 2, 0}, {0, 1, 2}}        // RIGHT
};

char area[MAX_N][MAX_N];
int dist[MAX_N][MAX_N][3];
int n, m;
Stone start, target;

bool isInside(int x, int y) {
    return x >= 0 && x < n && y >= 0 && y < m;
}

bool isValid(Stone node) {
    // 检查基准点是否合法
    if (!isInside(node.x, node.y) || area[node.x][node.y] == '#') {
        return false;
    }
    
    // 检查不同状态下的其他格子
    if (node.status == 1) { // 横躺，需要检查右侧格子
        if (!isInside(node.x, node.y + 1) || area[node.x][node.y + 1] == '#') {
            return false;
        }
    } else if (node.status == 2) { // 竖躺，需要检查下方格子
        if (!isInside(node.x + 1, node.y) || area[node.x + 1][node.y] == '#') {
            return false;
        }
    }
    
    // 终点必须是站立状态
    if (node.x == target.x && node.y == target.y && node.status != 0) {
        return false;
    }
    
    return true;
}

Stone moveStone(Stone p, int dir) {
    int dx = direction[dir][p.status][0];
    int dy = direction[dir][p.status][1];
    int newStatus = direction[dir][p.status][2];
    return Stone(p.x + dx, p.y + dy, newStatus);
}

void buildMap() {
    memset(area, '#', sizeof(area));
    memset(dist, -1, sizeof(dist));
    
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> area[i][j];
        }
    }
    
    // 寻找起点和终点
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (area[i][j] == 'X') {
                start = Stone(i, j, 0);
                area[i][j] = '.';
                
                // 检查是否是横躺或竖躺
                if (isInside(i, j + 1) && area[i][j + 1] == 'X') {
                    start.status = 1;
                    area[i][j + 1] = '.';
                } else if (isInside(i + 1, j) && area[i + 1][j] == 'X') {
                    start.status = 2;
                    area[i + 1][j] = '.';
                }
            } else if (area[i][j] == 'O') {
                target = Stone(i, j, 0);
            }
        }
    }
}

int bfs() {
    queue<Stone> q;
    q.push(start);
    dist[start.x][start.y][start.status] = 0;
    
    while (!q.empty()) {
        Stone current = q.front();
        q.pop();
        
        // 检查是否到达终点
        if (current.x == target.x && current.y == target.y && current.status == 0) {
            return dist[current.x][current.y][current.status];
        }
        
        // 尝试四个方向
        for (int dir = 0; dir < 4; ++dir) {
            Stone next = moveStone(current, dir);
            
            if (isValid(next) && dist[next.x][next.y][next.status] == -1) {
                dist[next.x][next.y][next.status] = dist[current.x][current.y][current.status] + 1;
                q.push(next);
            }
        }
    }
    
    return -1; // 无法到达
}

int main() {
    while (cin >> n >> m && n) {
        buildMap();
        int result = bfs();
        if (result == -1) {
            cout << "Impossible" << endl;
        } else {
            cout << result << endl;
        }
    }
    return 0;
}