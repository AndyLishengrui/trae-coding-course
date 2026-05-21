//NQ091 骑士林克的怜悯
#include <cstring>
#include <iostream>
#include <vector>
using namespace std;

struct Point {
  int r, c;
};
Point dir[8] = {{-2, -1}, {-2, 1}, {-1, -2}, {-1, 2},
                {1, -2},  {1, 2},  {2, -1},  {2, 1}};

Point path[30];
int p, q;
int f[30][30];
//从 (r,c)出发，此时已经走了step步，看能否成功
bool dfs(int r, int c, int step) {
  //?所有棋盘格子都走到
  if (step == p * q) return true;
  //?是否超过边界
  if (r < 0 || r >= q || c < 0 || c >= p) return false;
  //?r,c是否来过
  if (f[r][c]) return false;

  f[r][c] = 1;
  path[step].r = r;
  path[step].c = c;
  // todo 枚举8个方向，深搜
  for (int i = 0; i < 8; ++i) {
    if (dfs(r + dir[i].r, c + dir[i].c, step + 1)) return true;
  }
  f[r][c] = 0;  //回溯，取消这一步的走法，使得走其他步的时候，能绕回到这里
  return false;
}
int main() {
  int t;
  cin >> t;
  for (int tt = 1; tt <= t; ++tt) {
    cout << "#" << tt << ":" << endl;
    cin >> p >> q;  // p数字, q字母
    memset(f, 0, sizeof(f));
    //*复用变量i作为退出标记
    int i;
    for (i = 0; i < q; ++i)
      for (int j = 0; j < p; ++j) {
        if (dfs(i, j, 0)) {
          i = q + 77;  //*加上你喜欢的数
          for (int k = 0; k < p * q; ++k)
            cout << char(path[k].r + 'A') << (path[k].c + 1);
          break;
        }
      }
    if (i == q)  //*判断i的值是否被手动更改
      cout << "none";
    cout << endl;
  }
}