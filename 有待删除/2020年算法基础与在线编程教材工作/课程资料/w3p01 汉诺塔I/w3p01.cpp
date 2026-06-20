#include <iostream>
using namespace std;
void move(char start, char target) {
  //把盘子从start移动到target，只需要直接打印移动路径
  cout << start << "->" << target << endl;
  return;
}
//将start上的n个盘子，以other为中转，移动到target
void Hanoi(int n, char start, char other, char target)
{
  if (n == 1) {  //只需移动一个盘子
    move(start, target);
    return;  //递归终止
  }
  Hanoi(n - 1, start, target, other);  //先将n-1个盘子从start移动到other
  move(start, target);                 //把第n个盘子移动到target
  Hanoi(n - 1, other, start, target);  //最后将n-1个盘子从other移动到target
  return;
}
int main() {
  int n;
  cin >> n;                 //输入盘子数目
  Hanoi(n, 'A', 'B', 'C');  //用字符A,B,C代表柱子编号
  return 0;
}
