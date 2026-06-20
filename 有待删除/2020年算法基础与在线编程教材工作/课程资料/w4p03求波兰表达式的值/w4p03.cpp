#include <cmath>
#include <iostream>
#include <string>
using namespace std;
double p() {
  string str;
  cin >> str;  //读入下一个表达式
  switch (str[0]) {
    case '+':
      return p() + p();
      break;
    case '-':
      return p() - p();
      break;
    case '*':
      return p() * p();
      break;
    case '/':
      return p() / p();
    default:
      return stof(str);  //把字符串转换为浮点数
      break;
  }
}
int main() {
  printf("%lf", p());
  return 0;
}
