#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;
typedef long long LL;

const int N = 100007;
int n;
int numbers[N],tmp[N];
//最大的数可能会是 n^2/2 
 LL mergeSort(int nums[], int left, int right)
{
    if (left>=right) return 0; //如果左指针越过右指针，则返回

    int mid = left+(right-left)/2;//防止溢出

    LL result = mergeSort(nums,left,mid)+mergeSort(nums,mid+1,right);//先调用归并排序
    //合二为一
    int k=0, i=left, j=mid+1;//左右两部分数组的起点

    while(i<=mid && j<=right) //扫描还未抵达终点
      if (nums[i]<=nums[j])//把小的放到tmp数组里面
        tmp[k++] = nums[i++];
        else {
            //计算逆序对的个数mid-i+1
            result += mid -i +1;
            tmp[k++] = nums[j++];
        }

    while(i<=mid) tmp[k++]=nums[i++];//把左边剩余的部分插入tmp
    while(j<=right) tmp[k++]=nums[j++];//把右边剩余的部分插入tmp

    //把tmp的部分复制回数组
    for (i=left,k=0; i<=right; i++, k++) nums[i]=tmp[k];

    return result;

}
int main()
{
    //数据大，使用printf和scanf
    scanf("%d",&n);
    for (int i = 0; i<n ;i++) scanf("%d",&numbers[i]);

   cout<<mergeSort(numbers,0,n-1)<<endl;


    return 0;
}