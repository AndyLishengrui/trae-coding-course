// NQ011 构造数列并求和
#include <cmath>
#include <iostream>
using namespace std;
int main() {
  int n, m;
  float res, a;
  while (cin >> n >> m)  //读入n,m直到文件末尾
  {
    res = 0;  //累加结果
    a = n;    //初始化数列第1项
    for (int i = 1; i <= m; i++) {
      res += a;
      a = sqrt(a);  //构造数列下一项
    }
    // 输出结果,保留两位小数
    printf("%.2f\n", res);
  }
  return 0;
}
