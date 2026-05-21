// NQ042 最长无重复子串
#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;
int lengthOfLongestSubstring(string s) {
    unordered_map<char, int> count;  // 字符计数
    int res = 0;  // 最长长度
    int j = 0;  // 左指针
    for (int i = 0; i < s.size(); i++) {
        char c = s[i];
        count[c]++;
        // 处理重复字符
        while (count[c] > 1) {
            count[s[j]]--;
            j++;
        }
        res = max(res, i - j + 1);
    }
    return res;
}
int main() {
    string s;
    cin >> s;
    cout << lengthOfLongestSubstring(s) << endl;
    return 0;
}