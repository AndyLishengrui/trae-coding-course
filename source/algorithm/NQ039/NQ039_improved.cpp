// NQ039 合法标识符
#include <cctype>
#include <iostream>
#include <string>
using namespace std;

int main() {
    int n;
    cin >> n;
    while (n--) {
        string s;
        cin >> s;
        if (isdigit(static_cast<unsigned char>(s[0]))) {
            cout << "no" << endl;
            continue;
        }
        bool valid = true;
        for (char c : s) {
            unsigned char uc = static_cast<unsigned char>(c);
            if (!(isdigit(uc) || isalpha(uc) || c == '_')) {
                valid = false;
                break;
            }
        }
        cout << (valid ? "yes" : "no") << endl;
    }
    return 0;
}