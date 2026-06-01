#include <iostream>
#include <queue>

using namespace std;

int main()
{
    int n; cin>>n;
    //优先队列，使用greater作比较函数,把默认的大根堆变为小根堆
    priority_queue<int, vector<int>,greater<int>> heap;
    //把读入数据压入堆
    while (n--)
    {
        int x; cin>>x;
        heap.push(x);
    }

    int res = 0;
    while(heap.size() > 1)
    {
        int x = heap.top(); heap.pop();
        int y = heap.top(); heap.pop();
        res += x + y;//累计合并值
        heap.push(x+y);//把当前合并的值压入堆
    }

    cout<<res<<endl;

    return 0;
}
