// NQ036 合并字符串初阶
#include <iostream>
#include <string>
using namespace std;

int main() {
    int t;
    cin >> t;  // 读入测试用例数量
    getchar();  // 去掉换行符
    
    while (t--) {
        string a, b;
        getline(cin, a);  // 读入第一行
        getline(cin, b);  // 读入第二行
        
        int p = a.size() / 2;  // 取中点
        // 合并字符串：a的前p个字符 + b + a的后部分
        cout << a.substr(0, p) + b + a.substr(p) << endl;
    }
    
    return 0;
}