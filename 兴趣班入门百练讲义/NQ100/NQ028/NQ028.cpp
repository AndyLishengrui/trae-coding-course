// NQ028 统计0-1矩阵中1的数量
#include <iostream>
using namespace std;

int main() {
  int t;
  // 输入测试用例数量
  cin >> t;
  while (t--) {
    int a, b, x, cnt = 0;
    // 输入矩阵的行数和列数
    cin >> a >> b;
    // 遍历矩阵的每个元素
    for (int i = 1; i <= a; i++)
      for (int j = 1; j <= b; j++) {
        // 输入当前元素的值
        cin >> x;
        // 如果当前元素值为1，则计数器加1
        if (x == 1) cnt++;
      }
    // 输出计数器的值，即矩阵中值为1的元素个数
    cout << cnt << endl;
  }
  return 0;
}