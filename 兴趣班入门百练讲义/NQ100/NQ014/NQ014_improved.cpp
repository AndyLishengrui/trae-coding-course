// NQ014 凤凰花开吃杨梅
#include <iostream>
using namespace std;
int calc(int n){
    int res=1;  // 第n天剩下1个
    for(int i=n-1;i>0;--i){
        res=(res+1)*2;  // 逆推前一天的数量
    }
    return res;
}
int main(){
    int x;
    while(cin>>x){
        cout<<calc(x)<<'\n';  // 计算并输出
    }
    return 0;
}