#include <iostream>
using namespace std;
// x苹果个数 y盘子个数
int f(int x, int y) {
  if (y > x)         //盘子数大于苹果数
    return f(x, x);  //去掉多余的空盘子

  if (x == 0)  //没苹果了，只有1种摆法，返回1
    return 1;

  if (y <= 0)  //没盘子了，无解，返回0
    return 0;

  // 空一个盘子的摆法 + 每个盘子至少有一个苹果的摆法
  return f(x, y - 1) + f(x - y, y);
}
int main() {
  int t, x, y;
  cin >> t;
  while (t--) {
    cin >> x >> y;  //读入苹果个数，盘子个数
    cout << f(x, y) << endl;
  }
  return 0;
}
