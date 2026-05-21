#include <iostream>
#include <string>
using namespace std;

string longestPalindrome(string s) {
    string res;
    int n = s.size();
    
    for (int i = 0; i < n; i++) {
        // 奇数长度回文子串扩展
        int l = i, r = i;
        while (l >= 0 && r < n && s[l] == s[r]) {
            l--;
            r++;
        }
        if (res.size() < r - l - 1) {
            res = s.substr(l + 1, r - l - 1);
        }
        
        // 偶数长度回文子串扩展
        l = i, r = i + 1;
        while (l >= 0 && r < n && s[l] == s[r]) {
            l--;
            r++;
        }
        if (res.size() < r - l - 1) {
            res = s.substr(l + 1, r - l - 1);
        }
    }
    return res;
}

int main() {
    string s;
    cin >> s;
    cout << longestPalindrome(s) << endl;
    return 0;
}