#include <iostream>
#include <algorithm>
using namespace std;
const int N=100007;
int n,m,x;
int numA[N],numB[N];

int main(){
       //读入n,m,x其中x为目标和
   scanf("%d%d%d",&n,&m,&x);
   for (int i=0; i<n; i++) scanf("%d",&numA[i]);
   for (int j=0; j<m; j++) scanf("%d",&numB[j]);
   //双指针查找和

   for (int i=0, j= m-1; i<n; i++){
       //check(i,j)
       while (j>=0 && numA[i]+numB[j]>x) j--;
       if (numA[i]+numB[j]==x)//判断是否和相等
       {
         printf("%d %d\n",i,j);
        break;
       }
   }
    return 0;
}