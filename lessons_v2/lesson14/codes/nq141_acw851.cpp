#include <queue>
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 100007;

int n,m;
int h[N], e[N], w[N], ne[N], idx;
int q[N], dist[N];
bool st[N];

void add(int a, int b, int c)  // 添加一条边a->b，边权为c
{
    e[idx] = b, w[idx] = c, ne[idx] = h[a], h[a] = idx ++ ;
}

int spfa()  // 求1号点到n号点的最短路距离，如果从1号点无法走到n号点则返回-1
{
    int hh = 0, tt = 0;
    memset(dist, 0x3f, sizeof dist);
    dist[1] = 0;
    q[tt ++ ] = 1;
    st[1] = true;

    while (hh != tt)
    {
        int t = q[hh ++ ];
        if (hh == N) hh = 0;
        st[t] = false;

        for (int i = h[t]; i != -1; i = ne[i])
        {
            int j = e[i];
            if (dist[j] > dist[t] + w[i])
            {
                dist[j] = dist[t] + w[i];
                if (!st[j])     // 如果队列中已存在j，则不需要将j重复插入
                {
                    q[tt ++ ] = j;
                    if (tt == N) tt = 0;
                    st[j] = true;
                }
            }
        }
    }

    if (dist[n] == 0x3f3f3f3f) return -1;
    return dist[n];
}

int main()
{
    scanf("%d%d", &n, &m);
    memset(h, -1, sizeof h);
    while (m -- )
    {
      int a, b, c;
      scanf("%d%d%d", &a, &b, &c);
      add(a, b, c);
    }

    int t = spfa();

    if (t == -1) puts("impossible");
    else printf("%d\n",t);

    return 0;
}