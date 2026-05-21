// NQ002 字符比大小
#include<algorithm>
#include<iostream>
using namespace std;
int main(){
    int n;cin>>n;  // 读取数据组数
    string s;
    while(n--){  // 处理每组数据
        cin>>s;  // 读取字符串
        sort(s.begin(),s.end());  // 对字符串排序
        // 输出前三个字符
        cout<<s[0]<<' '<<s[1]<<' '<<s[2]<<'\n';  
    }
    return 0;
}
