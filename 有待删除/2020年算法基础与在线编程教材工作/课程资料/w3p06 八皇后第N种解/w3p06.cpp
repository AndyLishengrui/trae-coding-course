// NQ074 求八皇后的第n种解
#include <cstring>
#include <iostream>
using namespace std;
//八皇后的解空间数组，每一行是一种皇后的摆法
int res[92][8];
// 存储皇后的一组解,res[0]存储皇后第0行的位置，res[i]存储皇后第i行的位置
int path[8];
int cnt = 0;  //可行解的计数器

void dfs(int n) {
  //递归出口，n从0开始到7全部遍历完毕
  if (n > 7) {
    for (int k = 0; k < 8; k++) 
      res[cnt][k] = path[k];
    cnt++;
    return;
  }
  //假定n-1个皇后已经全部摆好，现在准备摆第n个皇后
  //意味着solution[0]--solution[n-1]已经有值了
  for (int i = 1; i <= 8; i++)  //尝试0-7列位置，摆放第n个皇后
  {
    int k;
    for (k = 0; k < n; k++)
      if ((path[k] == i) ||                //发现同列，跳出
          abs(path[k] - i) == abs(n - k))  //对角线，跳出
        break;
    if (k == n) {
      path[n] = i;  //把当前第n个皇后放在第i个位置上
      dfs(n + 1);
    }
  }
}

int main() {
  int T, n;
  memset(path, 0, sizeof(path));
  //打表法，计算92组解并排序
  cnt = 0;
  dfs(0);  //深度优先搜索
  // T组测试数据
  cin >> T;
  while (T--) {
    cin >> n;
    for (int i = 0; i < 8; i++) cout << res[n - 1][i];
    cout << endl;
  }
  return 0;
}
