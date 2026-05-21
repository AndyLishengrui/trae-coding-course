// NQ009 计算偶数平方和和奇数立方和
#include<iostream>
using namespace std;
int main(){
    int a,b;
    while(cin>>a>>b){  // 读取区间端点
        int s1=0,s2=0;  // s1:偶数平方和, s2:奇数立方和
        for(int i=a;i<=b;++i){
            if(i%2==0)s1+=i*i;  // 偶数平方累加
            else s2+=i*i*i;     // 奇数立方累加
        }
        cout<<s1<<" "<<s2<<'\n';  // 输出结果
    }
    return 0;
}