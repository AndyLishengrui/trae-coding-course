// code by Guo Wei
#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
int a[100007]; //输入数据
int b[100007]; //临时数组
//把从小到大合并，改为从大到小合并
void Merge(int a[],int low,int mid, int high,int tmp[])
//从大到小合并[low,mid], [mid+1,high] 
{
	int pTmp = 0;
	int p1 = low,p2 = mid+1;
	while( p1 <= mid && p2 <= high) {
		if( a[p1] > a[p2]) //把大的摆前面，存入tmp数组
			tmp[pTmp++] = a[p1++];
		else 
			tmp[pTmp++] = a[p2++];
	}
	while( p1 <= mid) //把p1剩下的拷贝到tmp数组
		tmp[pTmp++] = a[p1++];	
	while( p2 <= high)//把p2剩下的拷贝到tmp数组
		tmp[pTmp++] = a[p2++];
    //把tmp数组的拷贝回a里面
	for(int i = 0;i < high-low+1; ++i)
		a[low+i] = tmp[i];
}
//逆序数可能很多，用long long存储count
long long Count(int a[],int low,int mid, int high)
//根据merge改写，左边是[low,mid],右边是[mid+1,high] 
{
	long long result = 0;
	int p1 = low,p2 = mid+1;
	while( p1 <= mid && p2 <= high) {
		if( a[p1] > a[p2]) {
			result += high-p2+1;
			++p1;
		}
		else 
			++p2;
	}
	return result;
}

long long MergeSortAndCount(int a[],int low,int high,int  tmp[])
{
	long long result = 0;
	if( low < high) {
		int mid = low + (high-low)/2;
        //算mid左边和右边的逆序数，并且从大到小排序
		result += MergeSortAndCount(a,low,mid,tmp);  
		result += MergeSortAndCount(a,mid+1,high,tmp);
        //计算从左边和右边各取一个数得到的逆序数，左边和右边都是从大到小排序的 
        result += Count(a,low,mid,high); 
        Merge(a,low,mid,high,tmp); //从大到小合并，确保排序 
	}
	return result;
}
int main()
{
	int n;
	scanf("%d",&n);
	for(int i = 0;i < n; ++i)
		scanf("%d",&a[i]);
	printf("%lld",MergeSortAndCount(a,0,n-1,b));
	return 0;
}
