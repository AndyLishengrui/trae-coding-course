// NQ031 解密问题
// 对输入的文本进行解密，将大写字母左移5位
#include <iostream>
#include <string>
using namespace std;

int main() {
    string line;
    bool is_awaiting = false;  // 标记是否正在等待解密文本
    
    while (getline(cin, line)) {
        if (line == "ENDOFINPUT") break;  // 遇到结束标志，退出循环
        if (line == "START") {
            is_awaiting = true;  // 遇到开始标志，准备接收解密文本
            continue;
        }
        if (is_awaiting) {
            // 对文本进行解密处理
            for (char& c : line) {
                if (c >= 'A' && c <= 'Z') {
                    // 左移5位等价于右移21位（26-5=21）
                    c = 'A' + (c - 'A' + 21) % 26;
                }
            }
            cout << line << endl;  // 输出解密后的文本
            is_awaiting = false;  // 重置标志
        }
    }
    return 0;
}