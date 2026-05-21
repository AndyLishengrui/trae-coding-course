// NQ030 小球进盒子
#include <iostream>
using namespace std;
int R, B, r, b, A;
int main() {
  cin >> R >> B >> r >> b >> A;
  if (r + b > 2 * A) {
    // r+b>2*A情况，红黑球都放自己盒子
    cout << R * r + B * b;
    return 0;
  } else  // r+b<2*A情况
  {
    if (R > B) {
      //红比黑多，红黑球交换盒子后，剩余红球放红盒
      cout << B * A + B * A + (R - B) * r;
      return 0;
    }
    if (B > R) {
      //黑比红多，红黑球交换盒子后，剩余黑球放黑盒
      cout << R * A + R * A + (B - R) * b;
      return 0;
    }
    if (B == R) {
      // 红和黑相等，红黑球交换盒子
      cout << R * 2 * A;
      return 0;
    }
  }
  return 0;
}