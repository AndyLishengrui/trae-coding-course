#include <cmath>
#include <iostream>
using namespace std;

int main() {
    int t; cin >> t;
    while (t--) {
        double s, u; scanf("%lf%lf", &s, &u);
        double v = 1.0 / tan(atan(1.0/s) - atan(1.0/u));  // 计算v值
        double res = v*u - s*u - v*s;  // 计算最终结果
        printf("%.0lf\n", res);
    }
    return 0;
}