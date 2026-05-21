// NQ019 最大公约数
#include <iostream>
using namespace std;
int gcd(int a,int b){return b?gcd(b,a%b):a;}  // 欧几里得算法
int main(){
    int n;
    cin>>n;  // 读取测试用例数量
    while(n--){
        int a,b;
        cin>>a>>b;  // 读取两个整数
        cout<<gcd(a,b)<<'\n';  // 计算并输出
    }
    return 0;
}