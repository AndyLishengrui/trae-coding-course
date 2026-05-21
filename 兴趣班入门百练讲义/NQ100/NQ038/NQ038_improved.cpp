// NQ038 统计数字字符个数
#include <cctype>
#include <iostream>
#include <string>
using namespace std;

int main() {
    int test_case_num;
    cin >> test_case_num;
    cin.ignore();  // 清除换行符
    
    while (test_case_num--) {
        string input_line;
        getline(cin, input_line);
        
        int digit_count = 0;
        for (char c : input_line) {
            if (isdigit(static_cast<unsigned char>(c))) digit_count++;  // 统计数字字符
        }
        
        cout << digit_count << endl;
    }
    
    return 0;
}