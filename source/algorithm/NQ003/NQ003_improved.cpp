// NQ003 计算线段长度
#include<iostream>
#include<iomanip>
#include<cmath>
using namespace std;
int main(){
    int n;cin>>n;  // 读取测试用例数量
    while(n--){
        double x1,y1,x2,y2;
        cin>>x1>>y1>>x2>>y2;  // 读取两点坐标
        double dx=x1-x2,dy=y1-y2;
        double d=sqrt(dx*dx+dy*dy);  // 计算欧几里得距离
        cout<<fixed<<setprecision(2)<<d<<'\n';  // 输出保留两位小数
    }
    return 0;
}