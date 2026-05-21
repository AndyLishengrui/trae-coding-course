// NQ045 奇偶校验
#include <iostream>
#include <string>
using namespace std;
int main() {
    string s;
    while (cin >> s && s != "#") {
        int cnt = 0, len = s.size();
        for (int i = 0; i < len - 1; i++)
            if (s[i] == '1') cnt++;
        cnt %= 2;
        s[len - 1] = ((s[len - 1] == 'e' && cnt == 1) || (s[len - 1] == 'o' && cnt == 0)) ? '1' : '0';
        cout << s << endl;
    }
    return 0;
}