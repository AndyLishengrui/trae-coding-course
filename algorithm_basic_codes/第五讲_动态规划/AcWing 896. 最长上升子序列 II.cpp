#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 100007;

int n;
int a[N];
int q[N];//记录最长上升子序列的值

int main()
{
    scanf("%d", &n);
    //记录序列
    for (int i = 0; i <n; i++) scanf("%d", &a[i]);
    //使用q[N]存储最长上升子序列，用增量的方式更新里面的值
    int len = 0; //q的长度
    for (int i = 0; i < n; i++)
    {
      int l = 0, r = len;//q的下标
      while (l < r)
      {
        int mid = l + r + 1 >> 1;
        if (q[mid] < a[i]) l = mid;
        else r = mid -1;
      }//r就是找到的位置
      len = max(len,r+1);
      q[r+1] = a[i];
    }

    printf("%d\n",len);
    return 0;
}