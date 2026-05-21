//NQ046 悬垂问题
#include <iostream>
using namespace std;
int main() {
  double top; 
  while (cin >> top, top != 0) {
    double res=0;
    //求比差数列的和
    int cnt;
    //按照题目模拟题意做判断
    for (cnt = 1; res < top; cnt++) 
      res += 1.0 / (2.0 * cnt);
    cout << cnt-1 << (cnt-1==1?" block" :" blocks")<< endl;
  }
  return 0;
}
