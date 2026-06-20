#include <iostream>
using namespace std;

const int N = 10;  //最大值
int n;             //读入的n
int path[N];       //记录路径每个位的值
bool used[N];      //记录第i个数是否被用过

void dfs(int u) {
  if (u == n) {
    //输出排列
    for (int i = 0; i < n; i++) cout << path[i] << " ";
    cout << endl;
    return;
  }
  //枚举数字1--n
  for (int i = 1; i <= n; i++) {
    if (!used[i]) {
      path[u] = i;      //记录当前位path[u]的数字为i
      used[i] = true;   //标记数字i为已经使用郭
      dfs(u + 1);       //递归处理下一个位
      used[i] = false;  //恢复现场
    }
  }
}

int main() {
  cin >> n;
  dfs(0);
  return 0;
}