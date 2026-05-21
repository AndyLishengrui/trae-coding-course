#include <iostream>

using namespace std;

const int N = 100010;//最大值

int e[N],l[N],r[N],idx;
//初始化
void init()
{
  //0表示head，1表示tail
  r[0] = 1, l[1] = 0;
  idx = 2;//一开始就有两个顶点e[0], e[1]
}
//在下标是k的点右边，插入x
void insert(int k, int x)
{
  e[idx] = x;//新节点
  r[idx] = r[k];
  l[idx] = k;

  l[r[k]] = idx;//修改原链表指针
  r[k]= idx++;
}
//删除第k个点
void remove(int k)
{
  r[l[k]]= r[k];//k左边点的右指针指向k右边的点
  l[r[k]]= l[k];//k右边点的左指针指向k左边的点
}

int main()
{
  int m; cin>>m;

  init();//初始化

  while (m --)
  {
   int k, x;

   string op;//操作字符
   cin>>op;

   //(1) “L x”，表示在链表的最左端插入数x。
   if (op == "L") 
   {
     cin >> x;
     insert(0,x);
   }
   else if(op == "R")
   {//(2) “R x”，表示在链表的最右端插入数x。
     cin >> x;
     insert(l[1],x);
   }
   else if (op == "D")
   {//(3) “D k”，表示将第k个插入的数删除。
     cin >> k;
    remove(k+1);
   }
   else if (op == "IL")
   {//(4) “IL k x”，表示在第k个插入的数左侧插入一个数。
     cin>>k>>x;
     insert(l[k+1],x);
   }
   else 
   {//(5) “IR k x”，表示在第k个插入的数右侧插入一个数。
     cin>>k>>x;
     insert(k+1,x);
   }

  }
  //打印双链表,1是tail
  for (int i = r[0]; i!=1; i = r[i]) cout << e[i] << ' ';
  cout << endl;

  return 0;
}