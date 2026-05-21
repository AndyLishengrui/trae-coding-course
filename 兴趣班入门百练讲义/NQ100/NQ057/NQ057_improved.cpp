#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int n;
    while (cin >> n) {
        // 灯泡亮着的数量等于n以内的完全平方数个数
        // 即n的平方根的整数部分
        cout << (int)sqrt(n) << endl;
    }
    return 0;
}