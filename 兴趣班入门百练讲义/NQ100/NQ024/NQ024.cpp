//NQ024 珠穆朗玛峰测距
#include <cmath>
#include <cstdio>

int main() {
  int c;
  double x, y, m, n;
  scanf("%d", &c);  // 输入有c行测试数据
  while (c--) {
    scanf("%lf %lf %lf %lf", &x, &y, &m, &n);
    //欧几里得两点间的距离公式sqrt((x - m)^2 + (y - n)^2)
    printf("%.1lf\n",
           sqrt(x * x + y * y + m * m + n * n - 2 * m * x - 2 * n * y));
  }
  return 0;
}