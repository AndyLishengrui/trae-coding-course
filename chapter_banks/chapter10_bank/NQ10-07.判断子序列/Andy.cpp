#include <iostream>
#include <cstdio>
using namespace std;
const int N = 1e5+7;//我的风格
int a[N],b[N];

int main()
{
  int n,m;
  scanf("%d%d",&n,&m);
  for (int i = 0; i<n; i++) scanf("%d",&a[i]);
  for (int i = 0; i<m; i++) scanf("%d",&b[i]);

  int p = 0;//指向a数组的指针
  for (int i = 0; i < m; i++)
  {
    if (p < n && a[p] == b[i]) p++;
  }
  //完全匹配
  if (p==n) puts("Yes");
  else puts("No");

  return 0;

}
