#include <iostream>
#include <cctype> // 引入cctype库以使用toupper和tolower函数
using namespace std;

int main() {
    string line;
    while (getline(cin, line)) {
        // 转换首字母为大写
        line[0] = toupper(line[0]);

        // 双哨兵：检查每个字符和其后的字符
        for (size_t i = 0; i < line.length() - 1; ++i) { // 确保不越界
            char curr = line[i];
            char next = line[i + 1];

            // 如果当前字符是空格，并且下一个字符是小写，则转换为大写
            if (isspace(curr) && islower(next)) {
                line[i + 1] = toupper(next);
            }
            // 如果当前字符不是空格，并且下一个字符是大写，则转换为小写
            else if (!isspace(curr) && isupper(next)) {
                line[i + 1] = tolower(next);
            }
        }

        cout << line << endl;
    }
    return 0;
}