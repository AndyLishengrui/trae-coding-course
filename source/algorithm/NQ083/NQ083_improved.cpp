#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
const int MAX_LENGTH = 1007;
int longest_common_subsequence(const string& s1, const string& s2) {
    int dp[MAX_LENGTH][MAX_LENGTH];
    int len1 = s1.length();
    int len2 = s2.length();
    for (int i = 0; i <= len1; i++) {
        dp[i][0] = 0;
    }
    for (int j = 0; j <= len2; j++) {
        dp[0][j] = 0;
    }
    for (int i = 1; i <= len1; i++) {
        for (int j = 1; j <= len2; j++) {
            if (s1[i - 1] == s2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;  // 字符相同，长度加1
            } else {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);  // 字符不同，取最大值
            }
        }
    }
    return dp[len1][len2];
}
int main() {
    string s1, s2;
    while (cin >> s1 >> s2) {
        int result = longest_common_subsequence(s1, s2);
        cout << result << endl;
    }
    return 0;
}
