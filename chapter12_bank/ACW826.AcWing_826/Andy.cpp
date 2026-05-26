#include <iostream>

using namespace std;

const int N = 100010;

// head 表示头节点的下标， e[N]表示节点i的值
// ne[N]表示节点i的next指针是多少，idx存储当前已经用到了哪个节点
int head, e[N], ne[N], idx;

void init()
{
    head = -1;//一开始设置为-1
    idx = 0;//当前用到了0个节点
}

//将x插入到头节点
void add_to_head(int x)
{
  e[idx]=x, ne[idx] = head, head = idx, idx ++;
}
//将x插到下标是k的点后面
void add(int k, int x)
{
  e[idx]=x, ne[idx]=ne[k], ne[k] = idx, idx ++;
}
//将下标是k的点后面的点删掉
void remove(int k)
{
  ne[k] = ne[ne[k]];
  //idx--;
}
int main()
{
  int m; cin>>m;

  init();//初始化

  while (m --)
  {
   int k, x;
   char op;//操作字符

   cin>>op;
   if (op == 'H') 
   {
     cin >> x;
     add_to_head(x);
   }
   else if (op == 'D')
   {
     cin >> k;
     if (!k) head = ne[head];//删除头节点
     else remove(k-1);
   }
   else 
   {
     cin >> k >> x;
     add(k-1, x);
   }
  }
  //打印单链表
  for (int i = head; i!=-1; i = ne[i]) cout << e[i] << ' ';
  cout << endl;
}
