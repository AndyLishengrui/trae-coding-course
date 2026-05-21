// NQ097 寻找林克的回忆(2)
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
string str;               //存储输入的每一行字符串

int row[N], col[N], cell[3][3];  //?9×9的矩阵，用 行row 列col 3×3的Cell
int ones[MaxN];
int LOG2[MaxN];

void BuildLOG2() { For(i, 0, N) LOG2[1 << i] = i; }
//!取x二进制序列最后末一个1000模式的字串
inline int lowbit(int x) { return x & -x; }
inline int NumberOf1(int n) {
  int res = 0;
  while (n) {
    n -= lowbit(n);
    res += 1;
  }
  return res;
}
void Buildones() { For(i, 0, MaxN) ones[i] = NumberOf1(i); }
void init() {
  //二进制为1表示该位数字为空
  For(i, 0, N) row[i] = MaxN - 1;                   //!初始化为111111111
  For(i, 0, N) col[i] = MaxN - 1;                   //!初始化为111111111
  For(i, 0, 3) For(j, 0, 3) cell[i][j] = MaxN - 1;  //!初始化为111111111
}

//打印一行s
void printStr2line(string s) { cout << s << endl; }
//打印9*9矩阵
void printStr2Grid(string s) {
  For(i, 0, 9) cout << s.substr(i * 9, 9) << endl;
  cout << endl;
}

//把x,y位置二进制数的第n位取反
inline void flipbits(int x, int y, int n) {
  row[x] ^= 1 << n;
  col[y] ^= 1 << n;
  cell[x / 3][y / 3] ^= 1 << n;
}
//取交集的运算
inline int get(int x, int y)  //返回row[x],col[x]与cell[x][y]的可用集合
{
  return row[x] & col[y] & cell[x / 3][y / 3];  //同时为1的二进制位
}

bool dfs(int cnt) {
  if (cnt == 0) {
    //*输出可行解
    printStr2line(str);
    return true;
  }
  //找出可选方案数最小的格子
  int minv = INF;  //可以设置为10即可
  int x, y;
  For(i, 0, N) For(j, 0, N) if (str[i * 9 + j] == BLANKCHAR) {
    int t = ones[get(i, j)];  //*查表
    if (t < minv) {
      minv = t, x = i, y = j;  //*从空格最少的行列开始处理，记录x,y
    }
  }
  //从该方案[x,y,minV]开始枚举，指导找到cellstosolve-1方案为止
  //? get(x,y) 的返回值代表行，列，Cell中可选的二进制值
  for (int sk = get(x, y); sk; sk -= lowbit(sk)) {
    int t = LOG2[lowbit(sk)];  //得到1的最低位位置
    //修改状态row,col,cell
    flipbits(x, y, t);
    str[x * 9 + y] = '1' + t;  //修改str对应位置填上数(0-8映射到1-9)
    //继续深搜
    dfs(cnt - 1);
    //恢复状态
    str[x * 9 + y] = BLANKCHAR;
    flipbits(x, y, t);
  }
  return false;
}

int main() {
  //*初始化LOG2
  BuildLOG2();
  // i的二进制中有几个1
  Buildones();

  while (cin >> str, str[0] != 'e') {
    init();
    // * i,j是九宫格的行列坐标，k是字符串中的线性坐标
    int cnt = 0;
    for (int i = 0, k = 0; i < N; i++)
      for (int j = 0; j < N; j++, k++)
        if (str[k] != BLANKCHAR) {
          int t = str[k] - '1';  //*把题目的1-9映射成0-8
          flipbits(i, j, t);  //*初始化是1，这里取反设置为0，表示该位已占用
        } else
    cnt++;

    dfs(cnt);
  }
  return 0;
}