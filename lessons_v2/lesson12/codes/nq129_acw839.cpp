#include <iostream>
#include <algorithm>
#include <string.h>

using namespace std;

const int N = 100007;

// hp是heap pointer的缩写，表示堆数组中下标到第k个插入的映射
// ph是pointer heap的缩写，表示第k个插入到堆数组中的下标的映射
// hp和ph数组是互为反函数的
int h[N],ph[N],hp[N],cnt;

void heap_swap(int a, int b)
{
  swap(ph[hp[a]],ph[hp[b]]);//堆数组的下标
  swap(hp[a],hp[b]);//下标与第几个插入元素的映射
  swap(h[a],h[b]);//堆元素
}

void down(int u)
{
  int t = u;
  if (u*2<=cnt && h[u*2]<h[t]) t = u*2;//u*2左儿子
  if (u*2+1 <= cnt && h[u*2+1]<h[t]) t = u*2+1;// u*2+1右儿子
  if (u != t)
  {
    heap_swap(u,t);
    down(t);
  }
}

void up(int u)
{
  while (u/2 && h[u] < h[u/2])
  {
    heap_swap(u,u/2);
    u >>= 1;
  }
}

int main()
{
  int n,m=0;
  scanf("%d",&n);
  while(n --) 
  {
    char op[5];
    int k,x;
    scanf("%s",op);
    //在堆最后一个元素插入元素
    if (!strcmp(op,"I"))
    {
      scanf("%d",&x);
      cnt ++;
      m++;
      ph[m] = cnt, hp[cnt] = m;
      h[cnt] = x;
      up(cnt); //插入后执行up(cnt)
    }
    else if (!strcmp(op,"PM")) printf("%d\n",h[1]);//堆顶是最小值
    else if (!strcmp(op,"DM"))
    {
      heap_swap(1,cnt);
      cnt --;
      down(1); //删除最小值后执行down(1)
    }
    else if (!strcmp(op,"D"))
    {
      scanf("%d",&k);//删除第k个元素
      k = ph[k];//取第k个元素下标
      heap_swap(k,cnt);//与最后一个元素交换
      cnt--;
      up(k);
      down(k);
    }
    else {
      scanf("%d%d",&k,&x);//修改第k个数
      k = ph[k];
      h[k] = x;
      up(k);
      down(k);
    }
  }
  return 0;
}