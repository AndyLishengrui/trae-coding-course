#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;
const int N = 100007;
int n;
int numbers[N],tmp[N];

void mergeSort(int nums[], int left, int right)
{
    if (left>=right) return;

    int mid = left+(right-left)/2;//防止溢出

    mergeSort(nums,left,mid), mergeSort(nums,mid+1,right);//先调用归并排序
    //合二为一
    int k=0, i=left, j=mid+1;//左右两部分数组的起点

    while(i<=mid && j<=right) //扫描还未抵达终点
      if (nums[i]<=nums[j])//把小的放到tmp数组里面
        tmp[k++] = nums[i++];
        else tmp[k++] = nums[j++];

    while(i<=mid) tmp[k++]=nums[i++];//把左边剩余的部分插入tmp
    while(j<=right) tmp[k++]=nums[j++];//把右边剩余的部分插入tmp

    //把tmp的部分复制回数组
    for (i=left,k=0; i<=right; i++, k++) nums[i]=tmp[k];

}
int main()
{
    //数据大，使用printf和scanf
    scanf("%d",&n);
    for (int i = 0; i<n ;i++) scanf("%d",&numbers[i]);

    mergeSort(numbers,0,n-1);

    for (int i=0; i<n ;i++) printf("%d ",numbers[i]);

    return 0;
}
