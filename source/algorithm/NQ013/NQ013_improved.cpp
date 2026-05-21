// NQ013 倒数数列求和
#include <iostream>
#include <iomanip>
using namespace std;
const int MAX_N=10007;
double a[MAX_N];  // 存储前i项和的数组
int main() {
    a[1]=1.0;  // 第一项为1
    for(int i=2;i<MAX_N;++i){
        if(i%2!=0)a[i]=a[i-1]+1.0/i;  // 奇数项：加
        else a[i]=a[i-1]-1.0/i;       // 偶数项：减
    }
    cout<<fixed<<setprecision(2);  // 保留两位小数
    int n,q;
    while(cin>>q){
        while(q--){
            cin>>n;
            cout<<a[n]<<'\n';  // 查表输出
        }
    }
    return 0;
}