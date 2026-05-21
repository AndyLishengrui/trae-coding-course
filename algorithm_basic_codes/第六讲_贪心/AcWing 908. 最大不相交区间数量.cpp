#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 100007;

struct Range
{
  int l , r;
  bool operator< (const Range & R) const
  {
    return r < R.r;//重载比较符，根据r排序
  }
} range[N];

int main()
{
    int n;
    scanf("%d", &n);
    //读入区间
    for (int i = 0; i <n; i++)
    {
      int l,r;
      scanf("%d%d", &l, &r);
      range[i] = {l,r};
    }
    //按照右端点排序
    sort(range,range+n);
    //根据右端点计算覆盖的区间个数
    int res = 0, ed = -2e9;//已统计区间的右端点
    for (int i = 0; i < n; i ++ )
     if (range[i].l > ed)
     {
       res ++;
       ed = range[i].r;
     }
     printf("%d\n", res);

     return 0;
}