#include <iostream>
#include <cstring>
using namespace std;

int main() {
    const int kMaxColumn = 30;
    int dp[kMaxColumn + 1];
    memset(dp, 0, sizeof(dp));
    dp[0] = 1; // 空墙面
    dp[2] = 3; // 3x2 墙面的基础铺法
    
    // 递推计算偶数列的铺法数
    for (int i = 4; i <= kMaxColumn; i += 2) {
        dp[i] = 4 * dp[i - 2] - dp[i - 4];
    }
    
    int n;
    while (cin >> n && n != -1) {
        cout << dp[n] << endl;
    }
    
    return 0;
}