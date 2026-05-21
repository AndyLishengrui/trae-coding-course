// NQ054 ACM纳新测试赛
#include <iostream>
#include <vector>
#include <cstdlib> // 引入abs函数所在的库
using namespace std;

int main() {
    int m, n;
    cin >> m >> n;
    vector<vector<int>> matrix(m, vector<int>(n)); // 使用vector定义一个m行n列的矩阵

    // 读取矩阵中的每个元素
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            cin >> matrix[i][j];
        }
    }

    int maxAbs = 0; // 用于记录最大绝对值
    int maxRow = 0, maxCol = 0; // 记录最大绝对值所在的行和列（从1开始计数）

    // 遍历矩阵，找到绝对值最大的元素及其位置
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (abs(matrix[i][j]) > maxAbs) {
                maxAbs = abs(matrix[i][j]);
                maxRow = i + 1;
                maxCol = j + 1;
            }
        }
    }

    // 输出结果：行号 列号 数值（注意行列号从1开始计数）
    cout << maxRow << " " << maxCol << " " << matrix[maxRow - 1][maxCol - 1];

    return 0;
}