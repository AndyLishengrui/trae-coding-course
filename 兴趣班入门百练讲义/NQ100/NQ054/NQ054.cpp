// NQ054 ACM纳新测试赛
#include <iostream>
#include <cstdlib> // 引入abs函数所在的库
using namespace std;

int main() {
    int m, n;
    cin >> m >> n;
    int a[m][n];  // 定义一个m行n列的数组

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            cin >> a[i][j];
        }
    }

    int maxAbs = 0; // 用于记录最大绝对值
    int max_m, max_n;

    for (int i = 0; i < m; i++) {  // 找到数组中绝对值最大的数，并记录其位置
        for (int j = 0; j < n; j++) {
            if (abs(a[i][j]) > maxAbs) { // 使用abs函数比较绝对值
                maxAbs = abs(a[i][j]);
                max_m = i + 1;
                max_n = j + 1;
            }
        }
    }

    // 输出结果，注意数组下标，并且直接输出分数值而不是绝对值
    cout << max_m << " " << max_n << " " << a[max_m - 1][max_n - 1];

    return 0;
}