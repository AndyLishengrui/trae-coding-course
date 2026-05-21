// NQ025 胜利会师
#include <iomanip>
#include <iostream>
using namespace std;
int main() {
  int t;
  cin >> t;

  cout << fixed << setprecision(3);//输出格式设置为保留三位小数
  
  while (t--) {
    float u, v, w, l;
    cin >> u >> v >> w >> l; //读入4个浮点数
    cout << w * l / (u + v) << endl; //输出计算结果
  }
  return 0;
}