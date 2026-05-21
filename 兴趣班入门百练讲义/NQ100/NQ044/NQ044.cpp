//NQ044密码安全问题
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
        if (len < 8 || len > 16) {
            cout << "NO" << endl;
            continue;
        }
        int j[4] = {0};
        bool valid = true;
        for (char c : s) {
            bool a = islower(c);
            bool b = isupper(c);
            bool d = (c == '~' || c == '!' || c == '@' || c == '#' || c == '$' || c == '%' || c == '^');
            if (!a && !b && !isdigit(c) && !d) {
                valid = false;
                break;
            }
            if (a) j[0] = 1;
            if (b) j[1] = 1;
            if (isdigit(c)) j[2] = 1;
            if (d) j[3] = 1;
        }
        if (!valid) {
            cout << "NO" << endl;
            continue;
        }
        if (j[0] + j[1] + j[2] + j[3] >= 3)
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }
    return 0;
}