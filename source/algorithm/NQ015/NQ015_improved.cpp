// NQ015 辩论赛评分
#include <iostream>
#include <iomanip>
using namespace std;
int main() {
    cout<<fixed<<setprecision(2);  // 保留两位小数
    int n;
    while(cin>>n){
        int q=n;
        float min=101.0,max=-1.0,sum=0.0,s;  // 初始化最小值、最大值和总和
        while(q--){
            cin>>s;
            if(s<min)min=s;  // 更新最小值
            if(s>max)max=s;  // 更新最大值
            sum+=s;  // 累加总分
        }
        cout<<(sum-max-min)/(n-2)<<'\n';  // 计算并输出平均分
    }
    return 0;
}