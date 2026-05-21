// NQ016 十六进制加法
#include <iostream>
#include <iomanip>
using namespace std;
int main() {
    long long a,b;
    cout<<uppercase<<setbase(16);  // 大写十六进制输出
    while(cin>>hex>>a>>b){  // 十六进制读取
        long long sum=a+b;
        if(sum<0)cout<<"-"<<-sum<<'\n';  // 处理负数
        else cout<<sum<<'\n';  // 输出结果
    }
    return 0;
}