//NQ080 质数环
#include <algorithm>
#include <cstring>
#include <iostream>
#define For(i, a, b) for (int i = a; i <= b; i++)
using namespace std;
bool p[100], used[100];  //默认初始化为false
int n, a[100], now;
void dfs(int deep) {
  //结束条件抵达搜索个数n，并且头尾元素为质数
  if (deep == n + 1 && p[a[1] + a[n]]) {
    For(i, 1, n) {
      printf("%d", a[i]);
      if (i != n) printf(" ");  //打印空格
    }
    puts("");  //换行
    return;    //退出
  }
  For(i, 2, n) {  //深度优先搜索
    if (p[i + a[deep - 1]] && !used[i]) {
      used[i] = true;
      a[deep] = i;
      dfs(deep + 1);
      used[i] = false;
    }
  }
}
int main() {
  //打表法判断是否是质数，N<=20因此只需要打表到31即可。
  p[2] = p[3] = p[5] = p[7] = p[11] = p[13] =
      p[17] = p[19] = p[23] = p[29] = p[31] =
          true;  //每日打表心情好
  bool isf = false;
  while (~scanf("%d", &n)) {
    a[1] = 1;  //质数环首项为1
    if (isf) puts("");
    isf = true;
    printf("Case %d:\n", ++now);
    memset(used, false, sizeof(used));
    dfs(2);  //从第2项开始深搜
  }
  return 0;
}