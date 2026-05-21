// NQ096 寻找林克的回忆1
#include <cmath>
#include <cstring>
#include <iostream>
using namespace std;
#define For(a, begin, end) for (register int a = begin; a < end; ++a)
#define blankchar '0'  //另外一题为'.'
//输入输出数据和全局变量
#define INF 0x7fffffff
const int N = 9;
const int maxArray = 1 << N;  //*1<<9 为512

int row[N], col[N], cell[3][3];  //?9×9的矩阵，用 行row 列col 3×3的Cell
int ones[maxArray], lowbit2pos[maxArray];
bool found = false;
string str;  //存储输入的每一行字符串

inline int lowbit(int x) { return x & -x; }
inline int clearbit(int &x, int n) { return x -= 1 << n; }
inline int resetbit(int &x, int n) { return x += 1 << n; }
//取交集的运算
inline int get(int x, int y)  //返回row[x],col[x]与cell[x][y]的可用集合
{
  return row[x] & col[y] & cell[x / 3][y / 3];
}

void init() {
  for (int i = 0; i < N; i++)
    row[i] = col[i] = maxArray - 1;  //每一个位都设置为1：511=1 11111111
  for (int i = 0; i < 3; i++)
    for (int j = 0; j < 3; j++)
      cell[i][j] = maxArray - 1;  //每一个位都设置为1：511=1 11111111
}
void printStr2line(string s) { cout << s << endl; }
void printStr2Grid(string s) {
  For(i, 0, 9) cout << s.substr(i * 9, 9) << endl;
}
string readGrid2str(int n) {
  string res;
  For(i, 0, n) {
    string s;
    cin >> s;
    res += s;
  }
  return res;
}

bool dfs(int cnt) {
  if (cnt == 0) return true;
  found = false;
  //找出可选方案数最小的格子
  int minv = INF;
  int x, y;
  for (int i = 0; i < N; i++)
    for (int j = 0; j < N; j++)
      if (str[i * 9 + j] == blankchar) {
        int t = ones[get(i, j)];  //打表得到有几个可选方案t
        if (t < minv) {
          minv = t, x = i, y = j;
        }
      }  //循环遍历，得到方案最小的x,y，以及最小方案数minv

  for (int sk = get(x, y); sk; sk -= lowbit(sk)) {
    // sk为某数独串(使用lowbit循环取出每一个要填的空，状态为1为要填的空)
    //得到需要填的数，从小到大，最小是0，最大是8
    int t = lowbit2pos[lowbit(sk)];
    //修改状态row,col,cell
    clearbit(row[x], t), clearbit(col[y], t);
    clearbit(cell[x / 3][y / 3], t);
    //修改str对应位置填上数(0-8映射到1-9)
    str[x * 9 + y] = '1' + t;
    //继续深搜
    found = dfs(cnt - 1);
    if (found) return true;  //找到一种方案
    //恢复状态
    str[x * 9 + y] = blankchar;
    resetbit(row[x], t), resetbit(col[y], t);
    resetbit(cell[x / 3][y / 3], t);
  }
  return false;
}

int main() {
  // 初始化lowbi2pos，只有离散的几个数字有值
  for (int i = 0; i < N; i++)
    lowbit2pos[1 << i] = i;  //*1<<8=256;...1<<1=2,1<<0=1
  for (int i = 0; i < maxArray; i++) {
    int s = 0;
    for (int j = i; j; j -= lowbit(j)) s++;
    ones[i] = s;  // i的二进制表示中有s个1
  }

  str = readGrid2str(9);  //读入9行
  init();
  // i,j是九宫格的行列坐标，k是字符串中的线性坐标
  int cnt = 0;
  for (int i = 0, k = 0; i < N; i++)
    for (int j = 0; j < N; j++, k++)  //*K的用法
      if (str[k] != blankchar) {
        //*把题目的1-9映射成0-8
        int t = str[k] - '1';
        //第t位设置为0
        clearbit(row[i], t), clearbit(col[j], t);
        clearbit(cell[i / 3][j / 3], t);
      } else
        cnt++;
  dfs(cnt);
  printStr2Grid(str);
  return 0;
}
