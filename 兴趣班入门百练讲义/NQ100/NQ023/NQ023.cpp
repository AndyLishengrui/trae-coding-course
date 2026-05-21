//NQ023 桌球比赛
#include <iostream>
#include <string>
using namespace std;
int main() {
  int m;
  // 不断从标准输入读入整数m，直到输入结束
  while (cin >> m) {
    int cntR = 0, cntY = 0;
    char c;  // 读入m个字符
    // 循环m次，读入一个字符
    while (m--) {
      cin >> c;
      // 如果字符是'R'，则红色计数加1
      if (c == 'R') cntR++;
      // 如果字符是'Y'，则黄色计数加1
      if (c == 'Y') cntY++;
      // 如果字符是'B'
      if (c == 'B') {
        // 如果红色计数等于7，则输出"Red"
        if (cntR == 7)
          cout << "Red" << endl;
        // 否则输出"Yellow"
        else
          cout << "Yellow" << endl;
      }
      // 如果字符是'L'
      if (c == 'L') {
        // 如果黄色计数等于7，则输出"Yellow"
        if (cntY == 7)
          cout << "Yellow" << endl;
        // 否则输出"Red"
        else
          cout << "Red" << endl;
      }
    }
  }
  return 0;
}