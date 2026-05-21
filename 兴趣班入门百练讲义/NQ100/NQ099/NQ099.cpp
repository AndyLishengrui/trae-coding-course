//NQ099 最省赛程
#include <cstring>
#include <iostream>
#include <algorithm>
#include <queue>

using namespace std;

//使用数组实现邻接表，无向图
const int N = 1010;          //顶点数
const int M = 10100;         //边的数目
const int maxCapacity = 107; //油箱容量
int oilPrice[N], expenses[N][maxCapacity];
int head[N], Next[2 * M], ver[2 * M], dist[2 * M], tot = -1; //邻接表
bool visited[N][maxCapacity];
void add(int x, int y, int z)
{
    ver[++tot] = y;      //这条边到达的点
    Next[tot] = head[x]; //链接
    head[x] = tot;       //标记x起点
    //具体数据
    dist[tot] = z;       //权值
}
//! 访问从u出发的所有边，遍历的代码如下,当next[i]为0的时候遍历结束
//todo:    for(int i=head[u]; i; i=Next[i])//遍历相邻顶点v
//todo:     {
//todo:         int v = ver[i], d = dist[i];
//todo:     }
struct node
{
    int city, fuel, money; //城市，赛车油量，累计花费
    node(int x, int y, int z) : city(x), fuel(y), money(z) {}
    friend bool operator<(node a, node b)
    {
        return a.money > b.money; //权值从小到大排序,记住是小根堆
    }
};
priority_queue<node> q;

bool buyOneOil(int city, int fuel, int c)
{
    //如果油还在油箱限制内,且这买油一定更好的话
    if (fuel + 1 <= c && !visited[city][fuel + 1] && 
        (expenses[city][fuel + 1] > expenses[city][fuel] + oilPrice[city]))
        return true;
    else
        return false;
}

bool isNextRoad(int fuel, int cityid, int d, int money)
{
    //剩余油大于路径花费油、下一个状态未被访问过、并且花费更便宜
    if (fuel >= d && !visited[cityid][fuel - d] && 
        expenses[cityid][fuel - d] > money) 
        return true;
    else
        return false;
}
//全局遍历列表
int n, m;
//Dijkstra算法
int BFS(int currentCapacity, int start, int target)
{
    while (!q.empty())
        q.pop();
    memset(visited, false, sizeof(visited));
    memset(expenses, 0x3f, sizeof(expenses));

    //从起点开始搜索
    expenses[start][0] = 0;
    q.push(node(start, 0, 0)); //s为起点,0为剩余油量,0为权值
    while (!q.empty())
    {
        node qHead = q.top();
        q.pop();
        int city = qHead.city;
        int fuel = qHead.fuel;
        int money = qHead.money;
        visited[city][fuel] = true; //访问过了
        if (city == target)         //到达终点了
            return money;

        if (buyOneOil(city, fuel, currentCapacity)) //判断
        {
            //? 加上一升油的钱
            expenses[city][fuel + 1] = expenses[city][fuel] + oilPrice[city]; 
            //? 购买一升油的状态
            q.push(node(city, fuel + 1, expenses[city][fuel + 1]));           
        }

        for (int i = head[city]; i; i = Next[i]) //遍历相邻城市
        {
            int nextCity = ver[i], d = dist[i];    //此路径消耗油量d
            if (isNextRoad(fuel, nextCity, d, money))  //判断
            {
                expenses[nextCity][fuel - d] = money; //耗费油
                q.push(node(nextCity, fuel - d, money));
            }
        } // end of for
    } // end of While
    return -1;
}// end of BFS
int main()
{
    ios::sync_with_stdio(false);

    cin >> n >> m;

    //代表N个城市的单位油价，第i个数即为第i个城市的油价Pi
    for (int i = 0; i < n; i++)
        cin >> oilPrice[i];
    //每行包括三个整数u,v,d，表示城市u与城市v之间存在道路，且赛车从u到v需要消耗的油量为d。
    for (int i = 1; i <= m; i++)
    {
        int u, v, d;
        cin >> u >> v >> d;
        add(u, v, d); //无向图(u,v)
        add(v, u, d); //无向图(v,u)
    }
    //整数q，代表问题数量（q<100)
    int questions;
    cin >> questions;
    while (questions--)
    {
        // 每行包含三个整数C、S、E，分别表示赛车油箱容量、起点城市S、终点城市E
        int c, s, e;
        cin >> c >> s >> e;
        int expenses = BFS(c, s, e);
        if (expenses == -1)
            printf("impossible\n"); //无解
        else
            printf("%d\n", expenses);
    }
    return 0;
}
