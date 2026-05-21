// NQ006 成绩分区
#include<iostream>
using namespace std;
int main(){
    double s;
    while(cin>>s){  // 循环读取输入
        if(s<0||s>100)cout<<"Wrong Score!\n";
        else if(s>=90)cout<<"A:[90,100]\n";  // A级
        else if(s>=80)cout<<"B:[80,90)\n";   // B级
        else if(s>=70)cout<<"C:[70,80)\n";   // C级
        else if(s>=60)cout<<"D:[60,70)\n";   // D级
        else cout<<"E:[0,60)\n";             // E级
    }
    return 0;
}