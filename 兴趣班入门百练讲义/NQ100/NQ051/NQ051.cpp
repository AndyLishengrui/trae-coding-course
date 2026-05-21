//NQ051 数组元素交换
#include <iostream>
#include <algorithm>
using namespace std;
const int N = 10007;
int a[N], m, p; //数组,最小值,最小值下标
int main()
{
  int n;
  while (cin >> n, n > 0)
  {
    m = INT_MAX;//初始化为最大值
    p = 0;//数字下标初始化为第一项
    for (int i = 0; i < n; i++)
    {
      cin >> a[i];//读入数据
      if (m > a[i]) m = a[i],p = i;//记录最小值和相应下标
    }
    swap(a[0], a[p]);//交换
    for (int i = 0; i < n; i++) 
        if(i<n-1) cout << a[i] << " "; else cout<<a[i]<<endl;
  }
  return 0;
}
