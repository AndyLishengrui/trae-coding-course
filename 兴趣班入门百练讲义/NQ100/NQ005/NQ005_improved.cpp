// NQ005 实数绝对值
#include<iostream>
#include<iomanip>
#include<cmath>
using namespace std;
int main(){
    double x;
    while(cin>>x){  // 循环读取输入
        double v=fabs(x);  // 计算绝对值
        cout<<fixed<<setprecision(2)<<v<<'\n';  // 输出保留两位小数
    }
    return 0;
}