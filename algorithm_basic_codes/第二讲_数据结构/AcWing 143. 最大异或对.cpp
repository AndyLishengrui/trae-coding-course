#include <iostream>
#include <algorithm>

using namespace std;
const int N = 1000007, M = 3000000;

int n;
int son[M][2], idx;//Trie树，只有2个分支0,1
int a[N];

//插入并且创建Trie分支
void insert(int x)
{
  int p = 0;
  for (int i = 30; ~i; i--)//一共31位
  {
    //找到下一个儿子的地址
    int &s = son[p][x>>i & 1];
    if (!s) s = ++idx; //在数组模拟的链表中创建新节点
    p = s;
  }
}
//查找最大的异或数
int query(int x)
{
  int res = 0, p = 0;
  for (int i = 30; ~i; i--)
  {
    int s = x >> i & 1;
    if (son[p][!s])//异或，所以找与s不同的分支
    {
      res += 1 << i;//设置答案的第i位
      p = son[p][!s];
    } else p = son[p][s];
  }

  return res;

}
int main()
{
  cin>>n;
  for (int i = 0; i < n; i++){  
    cin>> a[i]; insert(a[i]);//创建trie树
  }

  int res = 0;
  for (int i = 0; i<n ; i++) res = max(res, query(a[i]));

  cout<<res<<endl;

  return 0;

}