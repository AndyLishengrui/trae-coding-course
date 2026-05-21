// NQ030 小球进盒子
#include <iostream>
using namespace std;
int main() {
    int R, B, C, D, E;  // R:红球数量, B:黑球数量, C:红球放入红盒得分, D:黑球放入黑盒得分, E:放入对方盒子得分
    cin >> R >> B >> C >> D >> E;
    if (C + D > 2 * E) {
        // C+D>2*E情况，红黑球都放自己盒子
        cout << R * C + B * D;
    } else {
        // C+D<=2*E情况，交换盒子可能得分更高
        if (R > B) {
            // 红比黑多，红黑球交换盒子后，剩余红球放红盒
            cout << B * E + B * E + (R - B) * C;
        } else if (B > R) {
            // 黑比红多，红黑球交换盒子后，剩余黑球放黑盒
            cout << R * E + R * E + (B - R) * D;
        } else {
            // 红和黑相等，红黑球交换盒子
            cout << R * 2 * E;
        }
    }
    return 0;
}