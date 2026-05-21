#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;
int main() {
    int n;
    cin >> n;
    vector<int> heights(n);
    for (int i = 0; i < n; ++i) {
        cin >> heights[i];
    }
    vector<int> dp(n, 1); // dp[i] 表示以第i个元素结尾的最长不上升子序列的长度
    // 动态规划计算最长不上升子序列
    for (int i = 1; i < n; ++i) {
        for (int j = 0; j < i; ++j) {
            if (heights[i] <= heights[j]) {
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
    }
    cout << *max_element(dp.begin(), dp.end()) << endl;
    return 0;
}