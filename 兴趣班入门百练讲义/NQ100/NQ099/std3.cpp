// 作者：秦淮岸灯火阑珊
// 链接：https://www.acwing.com/solution/acwing/content/973/
// 来源：AcWing
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
#include <cstring>
#include <iostream>
#include <algorithm>
#include <queue>

using namespace std;
const int N=1010;
const int M=10100;
int wn[N],head[N],Next[2*M],ver[2*M],dis[2*M],ans[N][102];
bool vis[N][102];
int c,s,e,n,m,t,tot=-1;
void add(int x,int y,int z)//链式前向星
{
    ver[++tot]=y;//这条边到达的点
    Next[tot]=head[x];//链接
    dis[tot]=z;//权值
    head[x]=tot;//标记x起点
}
struct node
{
    int u,f,w;
    node(int x,int y,int z):u(x),f(y),w(z) {}
    friend bool operator < (node a,node b)
    {
        return a.w>b.w;//权值从小到大排序,记住是小根堆
    }
};
priority_queue <node> q;
bool check1(int u,int f)
{
    if(f+1<=c && !vis[u][f+1] && (ans[u][f+1]>ans[u][f]+wn[u]))//如果油还在油箱限制内,且这买油一定更好的话
        return 1;
    return 0;
}
bool check2(int f,int v,int p,int w)
{
    if(f>=p && !vis[v][f-p] && ans[v][f-p]>w)//如果说当前这个点没有访问过,且当前剩余油大于路径花费油
        return 1;
    return 0;
}
int BFS()
{
    while(!q.empty())
        q.pop();
    memset(vis,false,sizeof(vis));
    memset(ans,0x3f,sizeof(ans));
    ans[s][0]=0;
    q.push(node(s,0,0));//s为起点,0为剩余油量,0为权值
    while(!q.empty())
    {
        node now=q.top();
        q.pop();
        int u=now.u;
        int f=now.f;
        int w=now.w;
        vis[u][f]=true;//访问过了
        if(u==e)//到达终点了
            return w;
        if(check1(u,f))//判断
        {
            ans[u][f+1]=ans[u][f]+wn[u];//加上一升油的钱
            q.push(node(u,f+1,ans[u][f+1]));//购买一升油的状态
        }
        for(int i=head[u]; i; i=Next[i])//遍历
        {
            int v=ver[i],p=dis[i];
            if(check2(f,v,p,w))//判断
            {
                ans[v][f-p]=w;//耗费油
                q.push(node(v,f-p,w));
            }
        }
    }
    return -1;
}
int main()
{
    ios::sync_with_stdio(false);
    cin>>n>>m;
    for(int i=0; i<n; i++)
        cin>>wn[i];
    for(int i=1; i<=m; i++)
    {
        int x,y,z;
        cin>>x>>y>>z;
        add(x,y,z);
        add(y,x,z);//无向图两条边
    }
    cin>>t;
    while(t--)
    {
        cin>>c>>s>>e;
        int ans=BFS();
        if(ans==-1)
            printf("impossible\n");//无解
        else
            printf("%d\n",ans);
    }
    return 0;
}
