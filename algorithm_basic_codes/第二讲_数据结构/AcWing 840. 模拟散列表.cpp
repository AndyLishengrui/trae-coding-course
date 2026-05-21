#include <iostream>
#include <cstring>

using namespace std;
const int N = 100007;//质数

int h[N], e[N], ne[N], idx;

void insert(int x)
{
  int k = (x % N + N) % N;//把负数映射成正数
  e[idx] = x, ne[idx] = h[k], h[k] = idx++;
}

bool find(int x)
{
  int k = (x % N + N) % N;//把负数映射成正数
  for (int i = h[k]; i!=-1; i=ne[i])
    if (e[i] == x) return true;

  return false;
}

int main()
{
    int n;
    cin>>n;

    memset(h, -1, sizeof h);//清空链表头数组

    while (n -- )
    {
     string op;//操作数
     int x;
     cin>>op>>x;//读入操作指令

     if (op=="I") insert(x);
     else {
       if (find(x)) puts("Yes");
       else puts("No");
     }
    }

    return 0;
}