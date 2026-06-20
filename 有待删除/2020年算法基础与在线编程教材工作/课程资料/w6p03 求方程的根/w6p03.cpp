// code by Andy
#include <iostream>
using namespace std;

//! f(0)==-80; f(10)==1000-500+100-80=520
double f(double x) 
    { return x * x * x - 5 * x * x + 10 * x - 80; }

double bsearch_d1(double l, double r) {
  double eps = 1e-11;  //小数点后面9位，精度为(9+2)
  while (r - l > eps) {
    double mid = (l + r) / 2;
    if (f(mid) > 0)
      r = mid;  //去掉右区间
    else
      l = mid;  //去掉左区间
  }
  return l;
}

int main() {
  //! 二分区间[0.0,10.0]
  printf("%.9lf\n", bsearch_d1(0.0, 10.0));
  return 0;
}
