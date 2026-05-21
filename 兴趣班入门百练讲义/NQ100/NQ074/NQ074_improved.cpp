#include <iostream>
#include <cstring>
using namespace std;
int s[92][8], p[8], cnt=0;
void dfs(int r) {
    if(r>7) {
        for(int i=0;i<8;++i) s[cnt][i]=p[i];
        cnt++;
        return;
    }
    for(int c=1;c<=8;++c) {
        bool ok=1;
        for(int i=0;i<r;++i)
            if(p[i]==c||abs(p[i]-c)==abs(r-i)) { ok=0; break; } // 检查列和对角线冲突
        if(ok) { p[r]=c; dfs(r+1); } // 放置皇后并递归
    }
}
void pre() {
    memset(p,0,sizeof(p));
    cnt=0;
    dfs(0);
}
int main() {
    pre(); // 预处理所有8皇后解
    int T,n;
    cin>>T;
    while(T--) {
        cin>>n;
        if(n<1||n>92) { cout<<"Invalid input!\n"; continue; }
        for(int i=0;i<8;++i) cout<<s[n-1][i]; // 输出第n-1个解
        cout<<'\n';
    }
    return 0;
}
