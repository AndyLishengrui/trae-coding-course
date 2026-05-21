#include <iostream>
#include <algorithm>

using namespace std;

const int N = 100007;//Andy风格

int h[N],heapSize;

int n,m;

void down(int u)
{
  int t = u;
  if (2 * u <= heapSize && h[t] > h[2*u]) t = 2*u;

  if (2 * u + 1 <= heapSize && h[t] > h[2*u+1]) t = 2*u+1;

  if (u!=t)
  {
    swap(h[u], h[t]);
    down(t);
  }
}

int main() {
  cin>>n>>m;
  heapSize = n;
  //i从1开始
  for (int i = 1; i<=n; i++)
  scanf("%d",&h[i]);
  for (int i = n/2; i; i--) down(i);//初始化堆

  while (m--)
  {
    cout<<h[1]<<" ";
    h[1] = h[heapSize--];
    down(1);
  }
  return 0;
}