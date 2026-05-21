// NQ001 求连续整数和
#include <iostream>  
using namespace std; 
int main() {
  int a, n;  
  cin >> a;  
  // 逗号运算符会先执行cin >> n，然后判断n的值
  while (cin >> n, n <= 0)
    ;  // 空循环体，不做任何操作
  int res = 0;  // res用于存储连续整数和
  // 从a开始，累加n个整数到res中，每次循环a自增
  for (int i = 0; i < n; i++) res += a++;
  cout << res << endl;  
  return 0;  
}