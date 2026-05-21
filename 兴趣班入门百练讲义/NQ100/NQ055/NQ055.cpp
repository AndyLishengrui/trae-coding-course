#include <iostream>
using namespace std;

// 求两个数的最大公约数（Greatest Common Divisor）
int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

// 求两个数的最小公倍数（Least Common Multiple）
int lcm(int a, int b) {
    return (a * b) / gcd(a, b);
}

int main() {
    int n;
    while (cin >> n) { // 读取测试样例的个数
        if (n == 0) break; // 如果输入为0，则结束程序（根据实际需求可能需要修改）
        int result = 1; // 初始化结果为1，因为LCM乘法会很快增长
        int num;
        for (int i = 0; i < n; i++) {
            cin >> num; // 读取每个数
            result = lcm(result, num); // 计算当前结果和新读入数的LCM
        }
        cout << result << endl; // 输出最终结果
    }
    return 0;
}
