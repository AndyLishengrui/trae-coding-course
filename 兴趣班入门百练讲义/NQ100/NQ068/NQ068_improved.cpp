#include <iostream>
#include <cmath>
using namespace std;

const double kEpsilon = 1e-9;

// 定义函数 f(x) = x^3 - 5x^2 + 10x - 80
double f(double x) {
    return x * x * x - 5 * x * x + 10 * x - 80;
}

// 二分法求根
double binarySearch(double left, double right) {
    while (right - left > kEpsilon) {
        double mid = left + (right - left) / 2;
        if (f(mid) > 0) {
            right = mid; // 根在左半区间
        } else {
            left = mid; // 根在右半区间
        }
    }
    return (left + right) / 2; // 返回区间中点作为最终近似根
}

int main() {
    // 在区间 [0, 10] 内求根
    printf("%.9lf\n", binarySearch(0.0, 10.0));
    return 0;
}