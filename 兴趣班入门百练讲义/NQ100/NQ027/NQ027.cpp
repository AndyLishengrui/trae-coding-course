//NQ027 丑数
#include <iostream>
using namespace std;

//判断一个整数是否是丑数（只包含质因子2、3和5的数）
bool isUgly(int num) {
  if (num <= 0) return false;
  //去掉因子2
  while (num % 2 == 0) num /= 2;
  //去掉因子3
  while (num % 3 == 0) num /= 3;
  //去掉因子5
  while (num % 5 == 0) num /= 5;
  //如果余数为1，则为丑数
  return num == 1;
}
int main() {
  int n;
  while (cin >> n)
    if (isUgly(n))
      cout << "true" << endl;
    else
      cout << "false" << endl;
  return 0;
}
