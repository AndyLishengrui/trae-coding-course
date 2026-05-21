// NQ036 合并字符串初阶
#include <cstring>
#include <iostream>
using namespace std;
int main() {
  int t;
  cin >> t;   //读入t组数据
  getchar();  //去掉换行符
  while (t--) {
    string a, b;
    getline(cin, a);       //读入第一行
    getline(cin, b);       //读入第二行
    int p = a.size() / 2;  //取中点
    //合并字符串
    cout << a.substr(0, p) + b + a.substr(p) << endl;
  }
  return 0;
}
