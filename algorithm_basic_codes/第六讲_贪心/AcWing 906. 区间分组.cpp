#include <iostream>
#include <cstring>
#include <algorithm>
#include <queue>
#include <utility>

using namespace std;

const int N = 100007;

pair<int,int> range[N];
int n;
int main()
{
    cin>>n;
    for (int i = 0; i < n; i ++ )
    {
      int a , b;
      cin>>a>>b;

      range[i]={a,b};
    }
    //排序
    sort(range,range+n);
    //用小根堆维护max_r
    priority_queue<int, vector<int>, greater<int>> heap;

    for (int i = 0; i < n; i ++ )
    {
      if (heap.empty() || heap.top() >= range[i].first)
      {
        heap.push(range[i].second);//创建新分组
      }
      else
      {
        heap.pop(); //更新mar_r
        heap.push(range[i].second);//右端点入堆
      }
    }
    cout<<heap.size()<<endl;

    return 0;
}