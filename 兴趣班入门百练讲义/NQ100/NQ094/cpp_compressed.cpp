#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<bitset>
#include<queue>
using namespace std;

int n, m, deg[30010], a[30010];
int ver[30010], Next[30010], head[30010], tot, cnt;
bitset<30010> f[30010];

// 添加边到邻接表
void add(int x, int y) {
    ver[++tot] = y, Next[tot] = head[x], head[x] = tot;
    deg[y]++;
}

// 拓扑排序
void topsort() {
    queue<int> q;
    for (int i = 1; i <= n; i++)
        if (deg[i] == 0) q.push(i);
    while (q.size()) {
        int x = q.front(); q.pop();
        a[++cnt] = x;
        for (int i = head[x]; i; i = Next[i]) {
            int y = ver[i];
            if (--deg[y] == 0) q.push(y);
        }
    }
}

// 计算每个节点的可达节点数量
void calc() {
    for (int i = cnt; i; i--) {
        int x = a[i];
        f[x][x] = 1; // 每个节点可以到达自己
        for (int i = head[x]; i; i = Next[i]) {
            int y = ver[i];
            f[x] |= f[y]; // 合并邻接节点的可达集合
        }
    }
}

int main() {
    cin >> n >> m; // 读取节点数和边数
    for (int i = 1; i <= m; i++) {
        int x, y;
        scanf("%d%d", &x, &y);
        add(x, y);
    }
    topsort();
    calc();
    for (int i = 1; i <= n; i++) printf("%d\n", f[i].count());
}
