#include <iostream>
#include <algorithm>
using namespace std;
const int N = 7;//只需要判断3个数
int a[N];
int main()
{
  int n; cin>>n;//读入n
  while (n--){//n组数据
    cin>>a[0];//读入第一个数，这个数存储最大值
    for (int i = 1; i <= 2; i++)
    {
      cin >> a[i];//读入数据
      if (a[0]<a[i]) swap(a[0],a[i]);//a[0]存储最大值
    }
    cout<<(a[0]<a[1]+a[2]?"OK":"NO")<<endl;//输出可否构成三角形
  }
  return 0;
}
