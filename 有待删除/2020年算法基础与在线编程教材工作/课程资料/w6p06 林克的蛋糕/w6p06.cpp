// code by Andy 2021.04.01
#include <algorithm>
#include <iostream>
using namespace std;
const double PI = 3.1415926535898;
double cakes[10010];
const double eps = 1e-6;  // 1e- (k+2), k为保留k位小数
int N, F;

// Check(mid)函数的设计
bool Check(double x) {
  if (x < eps) return true;
  int cnt = 0;                   //可以分到蛋糕的人数
  for (int i = 0; i < N; i++) {  //扫描所有蛋糕的体积
    int pieces = cakes[i] / x;   //计算此块蛋糕可以分成几块
    cnt += pieces;               //统计拿到蛋糕的人数
    if (cnt >= F) return true;   //超过总人数，返回true
  }
  return false;
}

double bsearch_d1(double l, double r) {
  while (r - l > eps) {
    double mid = (l + r) / 2;
    if (Check(mid))  //判断按照当前的mid的大小切蛋糕是否够分
      l = mid;       //去右区间查找更大的mid
    else
      r = mid;  //去左区间查找更小的mid
  }
  return l;
}

int main() {
  ios::sync_with_stdio(false);  //输入输出提速
  cin >> N >> F;
  F++;  //多一个人——林克的设计者
  int a;
  double maxCake = 0;
  for (int i = 0; i < N; ++i) {
    cin >> a;                          //读入的半径值
    cakes[i] = (double)a * a;          //存储蛋糕的半径的平方
    maxCake = max(maxCake, cakes[i]);  //计算最大值
  }

  // 二分查找范围[0，最大蛋糕的体积]
  // 即 [ 0, maxCake]
  double l = 0, r = maxCake;
  double res = bsearch_d1(l, r);
  printf("%.3lf\n", res * PI);  //输出保留3位小数
  return 0;
}
