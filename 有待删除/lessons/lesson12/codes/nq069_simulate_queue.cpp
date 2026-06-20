#include <iostream>
using namespace std;
const int N = 1000007;
int q[N], hh, tt=-1;

int main(){
  int m;
  cin>>m;
  while (m--)
  {
    int x;

    string op;
    cin>>op;

    if (op == "push") {
      //(1) “push x” – 向队尾插入一个数x；
      cin>>x;
      q[++tt] =x;
    } else if (op == "pop")// (2) “pop” – 从队头弹出一个数；
      hh++;
      else if (op == "empty") // (3) “empty” – 判断队列是否为空；
      cout<<(hh<=tt?"NO":"YES")<<endl;
      else cout<<q[tt]<<endl;// (4) “query” – 查询队头元素。
  }

  return 0;
}