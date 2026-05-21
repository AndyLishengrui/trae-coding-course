// NQ004 球体体积计算
#include<iostream>
#include<iomanip>
#include<cmath>
using namespace std;
#define PI 3.1415926
int main(){
    int n;cin>>n;  // 读取测试用例数量
    while(n--){
        double r;cin>>r;  // 读取球体半径
        double v=(4.0/3.0)*PI*pow(r,3);  // 计算体积
        cout<<fixed<<setprecision(3)<<v<<'\n';  // 输出保留三位小数
    }
    return 0;
}