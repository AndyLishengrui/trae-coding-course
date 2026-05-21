#include <algorithm>
#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;
    while (cin >> s) {
        char max_char = *max_element(s.begin(), s.end());  // 找到最大字符
        for (char c : s) {
            cout << c;
            if (c == max_char) {
                cout << "(max)";
            }
        }
        cout << endl;
    }
    
    return 0;
}