#include <iostream>
#include <algorithm>
#include <queue>
#include <cstring>

using namespace std;
#define For(a, begin, end) for (int a = (begin); a < (end); a++)
const int N = 1000007;

int n, m;
int head[N], edge[N], nextVertex[N], idx; //邻接表
int q[N], d[N]; //队列，入度

void add(int a, int b)
{    
    edge[idx] = b;
    nextVertex[idx] = head[a];
    head[a] = idx++;
}

bool topsort()
{
    int qHeadIdx = 0, qTailIdx = -1; //队头，队尾
    //从前往后遍历入度为0的点，插入队列
    for (int i = 1; i <= n; i++)
        if (!d[i])
            q[++qTailIdx] = i; //数组模拟队列，入队是尾指针+1
    while (qHeadIdx <= qTailIdx) //如果头指针小于尾指针
    {
        int t = q[qHeadIdx++]; //取队列头元素，，出队只是把头指针往后移动一位
        //遍历t的临边，空指针初始化为-1
        for (int i = head[t]; i != -1; i = nextVertex[i])
        {
            int j = edge[i]; //取到出边
            d[j]--;   //入度减一
            if (d[j] == 0)
                q[++qTailIdx] = j; //如若入度为0，压入队列
        }
    }
    //判断是否所有顶点都入队
    //也就是头指针qTailIdx是否等于n-1,即所有点都进入队列了
    return qTailIdx==n-1;
}
int main()
{

    cin >> n >> m;            //读入n,m
    memset(head, -1, sizeof(head)); //初始化Head数组指向-1顶点

    For(i, 0, m)
    {
        int a, b;
        cin >> a >> b;
        add(a, b); //插入边
        d[b]++;    //更新入度
    }

    if (topsort())
    {//数组队列里面的元素就是拓扑序
      for (int i =0; i<n; i++) printf("%d ",q[i]);
    }
    else
        puts("-1");
    return 0;
}
