//NQ071 手撕农夫与牛问题
#include <iostream>
#include <algorithm>
using namespace std;

int N,Stalls[100005],C;

bool isContainAllcows(int distance)
{
    int count =1,tempStall=Stalls[0];
    for (int i=1;i<N;i++)
    {//判断当前隔间是否可以放牛
       if(Stalls[i]-tempStall>distance)
         { //把1头牛逐个放入当前畜栏的隔间
            count++;
            tempStall=Stalls[i];
            //判断是否C头牛都放完
            if (count>=C)
            return true;
         }
    }
    //循环结束，count技术还不到C,表明有剩下牛
    return false;
}

//搜索区间[0,n),左闭右闭,升序
int binarySearch(int nums[], int n) {
    int left = nums[0], right = nums[n-1]-nums[0];//查找空间
    while(left<right) { //如果left==right 例如 [10,10)循环退出
        int mid = left + (right - left) / 2;
        //mid为要测试的Distance值
        if (isContainAllcows(mid)) 
             left=mid+1; //在右边区间找更大的距离值
         else
            right=mid;   //在左边区间找可行的距离值      
    }
    return left; 
}

int main()
{
    scanf("%d%d",&N,&C);
    for(int i=0;i<N;i++) scanf("%d",&Stalls[i]);
    sort(Stalls,Stalls+N);
    int D= binarySearch(Stalls,N);
    printf("%d\n",D);
    
    return 0;
}