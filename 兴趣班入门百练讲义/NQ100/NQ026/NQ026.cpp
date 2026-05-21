//NQ026 公式变代码
#include <cmath>
#include <iostream>
using namespace std;
int main() {
  int t;  // t组数据
  cin >> t;
  while (t--) {
    double s, u;
    // 输入s和u的值
    scanf("%lf%lf", &s, &u);
    // 计算v的值
    double v = 1.0 / tan(atan(1.0 / s) - atan(1.0 / u));
    // 计算res的值
    double res = v * u - s * u - v * s;
    // 输出res的值，保留整数部分
    printf("%.0lf\n", res);
  }
  return 0;
}