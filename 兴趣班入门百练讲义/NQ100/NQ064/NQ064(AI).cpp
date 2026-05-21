#include <iostream>
#include <vector>
using namespace std;

// 计算第year年的公主猫总数
int calculateCats(int year) {
    // 前4年的猫数量等于年份
    if (year < 5) return year;
    
    // 动态规划数组，存储每年的猫数量
    vector<int> dp(year + 1);
    dp[0] = 0; // 第0年不计入统计
    
    // 初始化前4年的猫数量
    for (int i = 1; i <= 4; ++i) {
        dp[i] = i;
    }
    
    // 从第5年开始，使用递推关系计算
    // 递推公式：当前年猫数量 = 前一年 + 前三年
    for (int i = 5; i <= year; ++i) {
        dp[i] = dp[i - 1] + dp[i - 3];
    }
    
    return dp[year];
}

int main() {
    int n, m;
    cin >> n; // 输入测试实例个数
    
    // 处理每个测试实例
    while (n--) {
        cin >> m; // 输入年份
        cout << calculateCats(m) << endl;
    }
    
    return 0;
}