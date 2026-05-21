// NQ023 桌球比赛
#include <iostream>
using namespace std;
int main() {
    int m;
    while(cin>>m){
        int r=0,y=0;
        char c;
        while(m--){
            cin>>c;
            if(c=='R')r++;  // 统计红球
            else if(c=='Y')y++;  // 统计黄球
            else if(c=='B')cout<<(r==7?"Red":"Yellow")<<'\n';  // B指令
            else if(c=='L')cout<<(y==7?"Yellow":"Red")<<'\n';  // L指令
        }
    }
    return 0;
}