//NQ021 废强重建
#include <iostream>
using namespace std;
const int N=107;
int main(){
    int n,a[N];
    while(cin>>n,n>0){
        int avg=0;
        for(int i=0;i<n;i++){
            cin>>a[i];
            avg+=a[i];
        }
        avg/=n;  // 计算平均值
        int res=0;
        for(int i=0;i<n;i++){
            if(a[i]<avg)res+=avg-a[i];  // 统计空缺数
        }
        cout<<res<<'\n'<<'\n';  // 输出结果，空行分隔
    }
    return 0;
}
