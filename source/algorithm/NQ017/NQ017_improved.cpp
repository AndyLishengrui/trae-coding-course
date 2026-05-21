// NQ017 计算绩点
#include <iostream>
#include <iomanip>
using namespace std;
int main() {
    float s,c,g,tc=0.0,tg=0.0;
    int q;
    cin>>q;
    while(q--){
        cin>>s>>c;
        // 根据成绩计算绩点
        if(s>=90)g=4.0;
        else if(s>=85)g=3.7;
        else if(s>=81)g=3.3;
        else if(s>=78)g=3.0;
        else if(s>=75)g=2.7;
        else if(s>=72)g=2.3;
        else if(s>=68)g=2.0;
        else if(s>=64)g=1.7;
        else if(s>=60)g=1.0;
        else g=0.0;
        tc+=c;tg+=g*c;  // 累加学分和加权绩点
    }
    cout<<fixed<<setprecision(4)<<tg/tc<<'\n';  // 输出加权平均绩点
    return 0;
}