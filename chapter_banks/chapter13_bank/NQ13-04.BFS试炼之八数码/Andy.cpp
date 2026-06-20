#include <iostream>
#include <cstring>
#include <algorithm>
#include <unordered_map>
#include <queue>

using namespace std;

/**
 * NQ13-04: BFS试炼之八数码
 * 搜索与回溯 | AcWing 845
 * 时间: O(n!) | 空间: O(n)
 */

int bfs(string start)
{
  string end = "12345678x";

  queue<string> q;
  unordered_map<string,int> d;//字符串映射到整数

  q.push(start);
  d[start] = 0;//map的用法

  //方向向量
  int dx[4] = {1,-1,0,0},dy[4]={0,0,1,-1};

  //广搜
  while(q.size())
  {
    auto t = q.front();
    q.pop();

    int distance = d[t];
    if (t==end) return distance;//找到目标

    //查询x在字符串中的下标
    int k = t.find('x');
    int x = k / 3, y = k % 3;//转换为宫格坐标

    for (int i = 0; i < 4; i ++ )
    {
      int a = x + dx[i], b = y + dy[i];

      if (a >= 0 && a < 3 && b >= 0 && b < 3)
      {
        swap(t[k], t[a*3+b]);//移动x的位置
        if (!d.count(t))
        {
          d[t] = distance + 1;
          q.push(t);//压入队列
        }
        swap(t[k],t[a*3+b]);//还原现场
      }
    }
  }
  return -1;

}

int main()
{
    string c, start;
    //去掉空格
    for (int i = 0; i < 9; i ++ )
    {
      cin>>c;
      start += c;
    }

    cout<<bfs(start)<<endl;
}
