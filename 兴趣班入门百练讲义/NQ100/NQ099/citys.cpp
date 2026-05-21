// 作者：yxc
// 链接：https://www.acwing.com/blog/content/405/
// 来源：AcWing

#include <algorithm>
#include <cstring>
#include <iostream>
#include <queue>
using namespace std;
#define For(i, a, b) for (int i = a; i < b; i++)

const int N = 1007, M = 10007, C = 107;

int head[N],next[2*M],e[M], w[N], idx;
int price[N];  //价格
int dist[N][C];
bool st[N][C];  // 存储每个点的最短路是否已经确定

struct Ver {
    int d, u, c;  //定义一个顶点结构体
    bool operator<(const Ver &W) const {
        return d > W.d;  //把小于号重载位大于号
    }
};

void add(int a, int b, int c) {
    e[idx] = b, w[idx] = c, next[idx] = head[a], head[a] = idx++;
}

// 求1号点到n号点的最短路，如果不存在则返回-1
int bfs(int c, int start, int end) {
    priority_queue<Ver> heap;  //小根堆

    memset(dist, 0x3f, sizeof dist);
    memset(st, false, sizeof st);  //点的访问状态
    heap.push({0, start, 0});  //从起点出发，初始油量是0（起点开始买油)

    while (heap.size()) {
        auto t = heap.top();
        heap.pop();

        if (t.u == end) return t.d;  //找到最小值
        //判断状态是否搜索过
        if (st[t.u][t.c]) continue;  //直接continue
        st[t.u][t.c] = true;
        //开始判断两种类型的边
        //需要买油（每次买1升)
        if (t.c < c) {
            if (dist[t.u][t.c + 1] > t.d + price[t.u]) {
                dist[t.u][t.c + 1] = t.d + price[t.u];  //加一升油
                heap.push({dist[t.u][t.c + 1], t.u,
                           t.c + 1});  //把顶点加入堆，终点是t.u
            }
        }

        //枚举所有的临边
        for (int i = head[t.u]; i; i = next[i]) {
            int j = e[i];     //得到当前边
            if (t.c >= w[i])  //油够用，改变可走
            {
                if (dist[j][t.c - w[i]] > t.d) {
                    //入堆
                    dist[j][t.c - w[i]] = t.d;
                    heap.push({t.d, j, t.c - w[i]});
                }
            }
        }
    }
    return -1;
}

int main() {
     freopen("2.in","r",stdin);
    // freopen("1o.out","w",stdout);

    ios::sync_with_stdio(false);  //加速cin cout
    int n, m;
    cin >> n >> m;
    // cout<<n<<m;

    For(i, 0, n) {
        cin >> price[i];
        // cout<<price[i]<<" ";
    }

    memset(head, -1, sizeof(head));
    while (m--) {
        int a, b, c;
        cin >> a >> b >> c;
        add(a, b, c), add(b, a, c);  //无向图加两遍边
    }
    // cout<<"finish reading input"<<endl;
    // //读入询问
    int query;
    cin >> query;
    while (query--) {
        int c, start, end;
        cin >> c >> start >> end;
        int t = bfs(c, start, end);
        if (t == -1)
            cout << "impossible" << endl;
        else
            cout << t << endl;
    }

    return 0;
}
