#include <iostream>
using namespace std;

const int N=10000007;

int n,k;
int a[N],q[N];//数组模拟队列
int hh=0,tt=-1;//hh队头,tt对尾

void initQueue(){
    hh=0; tt=-1;
}

int main()
{
    scanf("%d%d",&n,&k);
    for (int i=0; i<n; i++) scanf("%d",&a[i]);//读入数字

    //求滑动窗口内的最小值
    initQueue();//初始化队列,队列存储的是数组下标
    for (int i=0; i<n; i++)
    {
        //判断队头是否已经滑出窗口
        if (hh<=tt && i-k+1> q[hh]) hh++;//pop front删除队头
        //!单调队列，去掉所有降序的队尾点
        while (hh<=tt&& a[q[tt]]>= a[i]) tt--;//pop back删除队尾
        q[++tt] =i;//把当前i值入队列
        if (i>=k-1) //i在窗口内
          printf("%d ",a[q[hh]]);//队头就是最小值
    }
    puts("");

    //求滑动窗口内的最大值    
    initQueue();//初始化队列,队列存储的是数组下标
    for (int i=0; i<n; i++)
    {
        //判断队头是否已经滑出窗口
        if (hh<=tt && i-k+1> q[hh]) hh++;//pop front删除队头
        //!单调队列，去掉所有降序的队尾点
        while (hh<=tt&& a[q[tt]]<=a[i]) tt--;//pop back删除队尾
        q[++tt] =i;//把当前i值入队列
        if (i>=k-1) //i在窗口内
          printf("%d ",a[q[hh]]);//队头就是最大值
    }
    puts("");

}
