#include <iostream>
#include <string>
using namespace std;

int main() {
    int t;
    cin >> t;

    while (t--) {
        string s;
        cin >> s;
        int len = s.size();

        // 密码长度大于或等于8，且不要超过16
        if (len < 8 || len > 16) {
            cout << "NO" << endl;
            continue; // 使用continue跳过当前不安全的密码，并继续检查下一个
        }

        bool hasLowerCase = false;
        bool hasUpperCase = false;
        bool hasDigit = false;
        bool hasSpecialChar = false;

        for (char c : s) {
            // 检查字符类型
            hasLowerCase = hasLowerCase || (c >= 'a' && c <= 'z');
            hasUpperCase = hasUpperCase || (c >= 'A' && c <= 'Z');
            hasDigit = hasDigit || (c >= '0' && c <= '9');
            hasSpecialChar = hasSpecialChar || (c == '~' || c == '!' || c == '@' || c == '#' ||
                                               c == '$' || c == '%' || c == '^');
        }

        // 密码中的字符应该包含四种字符中至少三种
        if ((hasLowerCase + hasUpperCase + hasDigit + hasSpecialChar) >= 3) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }

    return 0;
}