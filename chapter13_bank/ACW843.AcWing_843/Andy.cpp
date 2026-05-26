#include <iostream>
using namespace std;

const int N = 20;  //最大值
int n;             //输入的n
char g[N][N];      //棋盘
//三个指示器列、对角线、反对角线,对角线以截距为编号
bool col[N], dg[N], udg[N];

void dfs(int u) {
  if (u == n) {
    //输出排列
    for (int i = 0; i < n; i++) puts(g[i]);
    puts("");
    return;
  }
  //枚举列0--n
  for (int i = 0; i < n; i++) {
    if (!col[i] && !dg[i + u] && !udg[i - u + n]) {
      g[u][i] = 'Q';  //当前位置设置为Q字符
      col[i] = dg[i + u] = udg[i - u + n] = true;  //标记数字i为已经使用郭
      dfs(u + 1);                                  //递归处理下一个位
      g[u][i] = '.';                               //恢复现场
      col[i] = dg[i + u] = udg[i - u + n] = false;  //恢复现场
    }
  }
}

int main() {
  cin >> n;
  //初始化图
  for (int i = 0; i < n; i++)
    for (int j = 0; j < n; j++) g[i][j] = '.';
  dfs(0);
  return 0;
}
