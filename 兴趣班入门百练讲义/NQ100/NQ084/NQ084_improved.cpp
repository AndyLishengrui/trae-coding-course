#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;
bool isIsomorphic(const string& s, const string& t) {
    if (s.size() != t.size()) return false;
    unordered_map<char, char> s_to_t, t_to_s;
    for (int i = 0; i < s.size(); i++) {
        char c1 = s[i], c2 = t[i];
        if (s_to_t.count(c1)) {
            if (s_to_t[c1] != c2) return false;  // 检查映射是否一致
        } else {
            if (t_to_s.count(c2)) return false;  // 检查是否有重复映射
            s_to_t[c1] = c2;
            t_to_s[c2] = c1;
        }
    }
    return true;
}
int main() {
    int n;
    cin >> n;
    while (n--) {
        string s, t;
        cin >> s >> t;
        cout << (isIsomorphic(s, t) ? "true" : "false") << endl;
    }
    return 0;
}