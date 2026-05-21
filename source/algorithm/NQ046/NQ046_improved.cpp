#include <iostream>
using namespace std;

int main() {
    double top;
    while (cin >> top && top != 0) {
        double res = 0;
        int cnt;
        // 计算调和级数的和，直到超过top
        for (cnt = 1; res < top; cnt++) {
            res += 1.0 / (2.0 * cnt);
        }
        // 输出结果，注意单复数形式
        int blocks = cnt - 1;
        cout << blocks << (blocks == 1 ? " block" : " blocks") << endl;
    }
    return 0;
}