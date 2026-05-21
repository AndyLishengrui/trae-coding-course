#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;
const int N=510, M=100010;
int n1,n2,m;
int h[N],e[N],ne[N],idx;//数组存储图,使用链表
int match[N];
bool visited[N];//判重
void add(int a, int b){
  e[idx]=b, ne[idx]=h[a], h[a]=idx++; //数组模拟链表add操作
}
bool find(int x)//深搜
{
  for (int i=h[x]; i!=-1; i=ne[i])//枚举所有边相连的顶点
  {
    int j=e[i];//取顶点下标
    if (!visited[j]) {
      visited[j]=true;
      if (match[j]==0 || find(match[j]))//未匹配，或者可以找到下家
      {
        match[j]=x; return true;
      }
    }
  }
 return false; 
}

int main()
{
  scanf("%d%d%d",&n1,&n2,&m);
  memset(h,-1,sizeof h);
  while(m--) {
   int a,b;//读入点
    scanf("%d%d",&a,&b);
    add(a,b);    
  }
  int res=0;//最大匹配数，也就是统计完全匹配的数量
  for(int i=1; i<=n1;i++) {
    memset(visited,false,sizeof visited);
    if (find(i)) res++;
  }
  printf("%d\n",res);

}