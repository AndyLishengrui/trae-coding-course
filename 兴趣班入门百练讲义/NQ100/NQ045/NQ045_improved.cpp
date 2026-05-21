#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;
    while (cin >> s && s != "#") {
        int cnt = 0, len = s.size();
        // 统计前len-1位中'1'的个数
        for (int i = 0; i < len - 1; i++)
            if (s[i] == '1') cnt++;
        
        int parity = cnt % 2; // 计算奇偶性
        // 根据校验类型设置校验位
        s[len - 1] = ((s[len - 1] == 'e' && parity == 1) || (s[len - 1] == 'o' && parity == 0)) ? '1' : '0';
        cout << s << endl;
    }
    return 0;
}