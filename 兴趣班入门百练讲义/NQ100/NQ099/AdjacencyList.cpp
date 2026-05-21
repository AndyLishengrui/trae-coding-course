#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

//Head 与 Next数组存储的是"ver数组的下标“，0表示指向空。
//Ver数组存储的是每条边的终点
//使用数组实现邻接表，无向图
const int N = 1010;                                          //顶点数
const int M = 10100;                                         //边的数目
int head[N], Next[2 * M], ver[2 * M], dist[2 * M], tot = -1; //邻接表
void add(int x, int y, int z)
{
    ver[++tot] = y;      //这条边到达的点
    Next[tot] = head[x]; //链接
    head[x] = tot;       //标记x起点
    //具体数据
    dist[tot] = z; //权值
}
void printU(int u)
{
    //! 访问从u出发的所有边，遍历的代码如下,当next[i]为0的时候遍历结束
    cout<<u<<" : ";
    for (int i = head[u]; i; i = Next[i]) //遍历相邻顶点v
    {
        int v = ver[i], d = dist[i];
        cout << "(" << u << "," << v << "," << d << ") ";
    }
}
int main()
{
    add(1, 2, 77);
    add(2, 3, 777);
    add(2, 5, 77777);
    add(3, 5, 77777);
    add(5, 4, 7777);
    add(5, 1, 7);
    for (int u = 1; u <= 5; u++)
    {
        printU(u);
        cout << endl;
    }

    return 0;
}
