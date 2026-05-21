// NQ035 二进制字符串奇偶位互换
// 将二进制字符串的相邻两位（奇偶位）互换位置
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    int test_case_count;
    cin >> test_case_count;  // 读取测试用例数量
    
    while (test_case_count--) {  // 遍历每个测试用例
        string binary_str;
        cin >> binary_str;  // 读取二进制字符串
        
        // 每两位互换位置（奇偶位互换）
        // 遍历步长为2，每次处理i和i+1位置的字符
        for (int i = 0; i < binary_str.length() - 1; i += 2) {
            swap(binary_str[i], binary_str[i + 1]);
        }
        
        cout << binary_str << endl;  // 输出互换后的二进制字符串
    }
    
    return 0;
}