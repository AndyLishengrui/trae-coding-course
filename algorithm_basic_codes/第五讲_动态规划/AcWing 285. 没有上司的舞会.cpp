#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

const int N = 6007;

int n;
int happy[N];
//邻接表
int h[N],e[N], ne[N],idx;
int f[N][2];
bool has_father[N];//判断是否是根节点
void add(int a, int b)
{
    e[idx] = b, ne[idx] = h[a], h[a] = idx ++;
}


void dfs(int u)
{
    f[u][1] = happy[u];
    for (int i = h[u]; i!= -1; i = ne[i])
    {
        int j = e[i];
        dfs(j);
        f[u][0] += max(f[j][0], f[j][1]);
        f[u][1] += f[j][0];
    }
}


int main()
{
    scanf("%d",&n);
    for (int i = 1; i <=n; i++) scanf("%d",&happy[i]);

    memset(h,-1,sizeof h);
    for (int i = 0; i < n-1; i++)
    {
        int a,b;
        scanf("%d%d", &a, &b);
        has_father[a] = true;
        add(b,a);
    }
    //判断有多少根节点
    int root = 1;
    while (has_father[root]) root++;
    dfs(root);
    //只有两种情况，是否选择根节点
    printf("%d\n",max(f[root][0], f[root][1]));
    return 0;
}