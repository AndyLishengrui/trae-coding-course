#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;
//无向图
const int N=100007,M=200007;//两倍的边
int n,m;
int h[N],e[M],ne[M],idx;
int color[N];//0表示未访问，1表示颜色1，2表示颜色2.

void add(int a, int b){
  e[idx]=b, ne[idx]=h[a], h[a]=idx++; //数组模拟链表add操作
}

bool dfs(int u, int c){
  color[u]=c;

  for (int i=h[u]; i!=-1; i=ne[i])
  {
    int j=e[i]; //取i对应的另外一个顶点编号
    if (!color[j]) {
       if (!dfs(j,3-c)) return false;//颜色是1或者2切换，所以用3-color可以交换两种颜色
    }
    else if (color[j]==c) return false;//端点颜色相同
  }
  return true;  
}
int main(){

  scanf("%d%d",&n,&m);
  memset(h,-1,sizeof h);//初始化头结点
  //建图
  while (m--)
  {
     int a,b;
     scanf("%d%d",&a,&b);
     add(a,b); add(b,a);
  }
  bool flag = true;//表示染色有矛盾
  for (int i=1; i<=n; i++)
    if (!color[i]) {
      if (!dfs(i,1))
      {
        flag = false;
        break;
      }
    } 
  if (flag) puts("Yes"); else puts ("No");

  return 0;
}