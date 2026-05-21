// NQ007 日期计算
#include <iostream>
using namespace std;
inline bool isLeap(int y) {//判断是否是闰年
  return (y % 4 == 0 && y % 100 != 0 || y % 400 == 0);
}
//计算第几天
int DayInYear(int y, int m, int d) {
  int days[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
  if (isLeap(y)) days[1] = 29;
  for (int i = 0; i < m - 1; ++i) {
    d += days[i];
  }
  return d;
}
int main() {
  int y, m, d;
  char p, q;
  while (scanf("%d%c%d%c%d", &y, &p, &m, &q, &d) != EOF) {
    printf("%d\n", DayInYear(y, m, d));  //输出第几天
  }
  return 0;
}
