#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 100007, M= N*2;//无向图

int n;
int h[N], e[M], ne[M], idx;
int ans = N;
bool st[N];//顶点n是否访问

void add(int a, int b)  // 添加一条边a->b
{
    e[idx] = b, ne[idx] = h[a], h[a] = idx ++ ;
}

int dfs(int u)
{
  st[u] = true;

  int size = 0;//去掉i节点后，i子树的最大子树节点数
  int sum = 0;//i子树的节点总数
  for (int i = h[u]; i!=-1; i=ne[i])
  {
    int j = e[i];
    if (st[j]) continue;

    int s = dfs(j);//返回j子树的大小
    size = max(size,s);
    sum += s;//计算所有子树和
  }

  size = max(size, n - sum - 1);//i子树和与 非i子树部分的和，取最大值
  ans = min(ans,size);

  return sum+1;//加上i节点本身
}

int main()
{
    cin>>n;
    memset(h, -1, sizeof h);
    for (int i = 0; i < n-1; i ++ )
    {
      int a,b;
      cin>>a>>b;
      add(a, b),add(b,a);//无向边
    }
    dfs(1);
    cout<<ans<<endl;
    return 0;
}