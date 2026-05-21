#include <iostream>
#include <string>
#include <cctype>
using namespace std;

void checkPassword() {
    string s;
    if (!(cin >> s)) return;
    
    int len = s.size();
    if (len < 8 || len > 16) {
        cout << "NO" << endl;
        return;
    }
    
    int type[4] = {0}; // 0:小写, 1:大写, 2:数字, 3:特殊符号
    bool valid = true;
    
    for (char c : s) {
        if (islower(c)) type[0] = 1;
        else if (isupper(c)) type[1] = 1;
        else if (isdigit(c)) type[2] = 1;
        else if (c == '~' || c == '!' || c == '@' || c == '#' || c == '$' || c == '%' || c == '^') type[3] = 1;
        else {
            valid = false;
            break;
        }
    }
    
    if (!valid) {
        cout << "NO" << endl;
        return;
    }
    
    if (type[0] + type[1] + type[2] + type[3] >= 3)
        cout << "YES" << endl;
    else
        cout << "NO" << endl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int t;
    cin >> t;
    while (t--) {
        checkPassword();
    }
    
    return 0;
}