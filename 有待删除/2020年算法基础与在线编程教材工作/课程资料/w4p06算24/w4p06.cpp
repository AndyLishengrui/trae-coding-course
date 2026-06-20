#include <algorithm>
#include <cstring>
#include <iostream>
#include <vector>
using namespace std;
// 输入的数组a，计算结果res
bool count24(vector<int> a, double res) {
  //递归出口
  if (a.empty()) {
    return fabs(res - 24) < 0.000001;
  }
  // 枚举所有选取运算元素的组合数
  for (int i = 0; i < a.size(); i++) {
    vector<int> b(a);        //拷贝a
    b.erase(b.begin() + i);  //取数组a的前i个元素
    //数组a的第i个元素,与res产生4种运算的结果
    if (count24(b, res + a[i]) || count24(b, res - a[i]) ||
        count24(b, res * a[i]) || count24(b, res / a[i]))
      return true;
  }
  return false;
}
int main() {
  //读入4个数
  vector<int> a(4);
  //判断是否全为0
  while (cin >> a[0] >> a[1] >> a[2] >> a[3] && a[0] | a[1] | a[2] | a[3]) {
    //递归计算24
    if (count24(a, 0.0))
      cout << "YES" << endl;
    else
      cout << "NO" << endl;
  }
  return 0;
}