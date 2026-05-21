// NQ032 文本格式化
#include <iostream>
#include <string>
#include <cctype>
using namespace std;
int main() {
    string line;
    while (getline(cin, line)) {  // 逐行读取输入
        int len=line.size();
        if(len==0){  // 处理空行
            cout<<endl;
            continue;
        }
        line[0]=toupper(line[0]);  // 首字母大写
        for(int i=0;i<len-1;++i){  // 处理剩余字符
            if(line[i]==' ')line[i+1]=toupper(line[i+1]);  // 空格后首字母大写
            else line[i+1]=tolower(line[i+1]);  // 其他字母小写
        }
        cout<<line<<endl;  // 输出格式化后的文本
    }
    return 0;
}