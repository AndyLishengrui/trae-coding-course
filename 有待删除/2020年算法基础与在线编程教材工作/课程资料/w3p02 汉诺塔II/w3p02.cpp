#include <iostream>
using namespace std;

//把id号盘子从start移动到target
void move(int id, char start, char target) { 
  cout << id << ":" << start << "->" << target << endl;
  return;
}

//将start上的n个盘子，以other为中转，移动到target
void Hanoi(int n, int id, char start, char other, char target) {
  if (n == 1) {  //只需移动一个盘子
    move(id, start, target);
    return;  //递归终止
  }

  Hanoi(n - 1, id, start, target, other);  //先将n-1个盘子从start移动到other
  int newId = id + n - 1;                  //计算最上层的盘子编号
  move(newId, start, target);              //把第n个盘子移动到target
  Hanoi(n - 1, id, other, start, target);  //最后将n-1个盘子从other移动到target
  return;
}

int main() {
  char a, b, c;
  int n;
  cin >> n >> a >> b >> c;  //输入盘子数目
  Hanoi(n, 1, a, b, c);
}
