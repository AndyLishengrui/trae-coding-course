#include <iostream>
using namespace std;

// 求最大公约数（GCD）
int gcd(int a, int b) {
    return b == 0 ? a : gcd(b, a % b);
}

// 求最小公倍数（LCM）
int lcm(int a, int b) {
    return (a * b) / gcd(a, b);
}

int main() {
    int n;
    while (cin >> n && n > 0) {
        int result = 1;
        for (int i = 0; i < n; i++) {
            int num;
            cin >> num;
            result = lcm(result, num); // 累积计算LCM
        }
        cout << result << endl;
    }
    return 0;
}