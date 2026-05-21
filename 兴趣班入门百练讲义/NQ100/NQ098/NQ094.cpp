// NQ094 寻找林克的回忆(3)
#include <cmath>
#include <cstring>
#include <iostream>
using namespace std;
#define For(a, begin, end) for (register int a = begin; a < end; ++a)

//* 输入输出数据和全局变量
#define INF 0x7fffffff
#define BLANKCHAR '.'
const int N = 9;
const int MaxN = 1 << N;  //*1<<9 为512

int ones[MaxN], LOG2[MaxN];
int row[N], col[N], cell[3][3];
int Sudoku[N][N];
int maxScore = -1;  //记录最大值

inline int lowbit(int x) { return x & -x; }
void init() {
  For(i, 0, N) LOG2[1 << i] = i;  //*建表LOG2
  For(i, 0, MaxN)                 //*建表ones
      for (int j = i; j; j -= lowbit(j)) ones[i]++;
  //*初始化为111111111
  For(i, 0, 9) row[i] = col[i] = cell[i / 3][i % 3] = MaxN - 1;
}

//*返回x,y的权值 并且乘t
inline int get_score(int x, int y, int t) {
  return (min(min(x, 8 - x), min(y, 8 - y)) + 6) * t;
}
//*返回x,y的可用位置，用整数的二进制表示
inline int get(int x, int y) { return row[x] & col[y] & cell[x / 3][y / 3]; }
//把x,y位置二进制数的第n位取反
inline void flipbits(int x, int y, int n) {
  row[x] ^= 1 << n;
  col[y] ^= 1 << n;
  cell[x / 3][y / 3] ^= 1 << n;
}
//设置g[x][y]的值为t
inline void set(int x, int y, int t) { Sudoku[x][y] = t; }
//score参数记录当前dfs的累计权重
void dfs(int cellsLeft, int score) {
  if (!cellsLeft) {
    maxScore = max(maxScore, score);  //记录最大值
    return;
  }

  int minv = INF;  //*寻找最少空格的位置
  int x, y;
  For(i, 0, N) For(j, 0, N) if (!Sudoku[i][j]) {
    int t = ones[get(i, j)];
    if (t < minv) {
      minv = ones[get(i, j)];
      x = i, y = j;
    }
  }
  //*从最少空格的点x,y开始深搜
  for (int i = get(x, y); i; i -= lowbit(i)) {
    int t = LOG2[lowbit(i)];
    set(x, y, t + 1);   //! 0-8映射为1-9
    flipbits(x, y, t);  //*修改row,col,cell的状态位
    dfs(cellsLeft - 1, score + get_score(x, y, t + 1));
    flipbits(x, y, t);  //修改row,col,cell的状态位
    set(x, y, 0);       //*把当前点Sudoku[x][y]清0
  }
}

int main() {
  //*建表，初始化状态数组
  init();

  int cellsLeft = 0, score = 0;  //!初始数独的score
  For(i, 0, N) For(j, 0, N) {
    int t;
    cin >> t;  //输入数据为空格分隔的数字
    if (t) {
      set(i, j, t);  //记录Sudoku[x][y]为t
      if (t > 0) flipbits(i, j, t - 1);
      score += get_score(i, j, t);  //*计算初始score
    } else
      cellsLeft++;
  }

  dfs(cellsLeft, score);  //!不是从score=0开始！
  cout << maxScore << endl;
  return 0;
}
