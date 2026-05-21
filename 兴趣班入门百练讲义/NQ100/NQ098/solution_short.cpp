#include < cmath >
#include < cstring >
#include < iostream >
using namespace std;
const int kSudokuSize = 9;
const int kMaxMask = 1 < < kSudokuSize;//掩码最大值，二进制111111111（512）
const int kInitialMask = kMaxMask-1;//初始掩码，表示所有数字1-9都可用
const int kInvalidScore =-1; //无解时的返回值
int count_ones[kMaxMask]; //存储每个掩码中1的个数（可选数字数量）
int log2_table[kMaxMask]; //快速查找2^i对应的i值
int row_mask[kSudokuSize]; //每行的可用数字掩码，1表示数字可用
int col_mask[kSudokuSize]; //每列的可用数字掩码
int cell_mask[3][3]; //每个3x3单元格的可用数字掩码
int sudoku[kSudokuSize][kSudokuSize]; //数独矩阵，0表示空格
int max_total_score = kInvalidScore; //记录最大总分，初始为无解状态
inline int LowBit(int x) {
 return x &-x;
}
inline int CalculateScore(int x, int y, int t) {
 int distance = min(min(x, 8-x), min(y, 8-y));
 return (distance+6)*t;
}
inline int GetAvailableMask(int x, int y) {
 return row_mask[x] & col_mask[y] & cell_mask[x/3][y/3];
}
inline void FlipMask(int x, int y, int digit_idx) {
 int mask = 1 < < digit_idx;
 row_mask[x] ^= mask;
 col_mask[y] ^= mask;
 cell_mask[x/3][y/3] ^= mask;
}
void Initialize() {
 for (int i = 0; i < kSudokuSize;++i) {
  log2_table[1 < < i] = i;
 }
 for (int i = 0; i < kMaxMask;++i) {
  count_ones[i] = 0;
  for (int j = i; j != 0; j-= LowBit(j)) {
   count_ones[i]++;
  }
 }
 for (int i = 0; i < kSudokuSize;++i) {
  row_mask[i] = kInitialMask;
  col_mask[i] = kInitialMask;
  cell_mask[i/3][i%3] = kInitialMask;
 }
}
void Backtrack(int empty_cells, int current_score) {
 if (empty_cells == 0) {
  if (current_score > max_total_score) {
   max_total_score = current_score;
  }
  return;
 }
 int min_available = kSudokuSize+1;
 int x =-1, y =-1;
 for (int i = 0; i < kSudokuSize;++i) {
  for (int j = 0; j < kSudokuSize;++j) {
   if (sudoku[i][j] == 0) {
    int available_mask = GetAvailableMask(i, j);
    int available_count = count_ones[available_mask];
    if (available_count < min_available) {
     min_available = available_count;
     x = i;
     y = j;
    }
   }
  }
 }
 int available_mask = GetAvailableMask(x, y);
 for (int mask = available_mask; mask != 0; mask-= LowBit(mask)) {
  int digit_idx = log2_table[LowBit(mask)];//转换为0-8的索引
  int digit = digit_idx+1; //转换为1-9的实际数字
  sudoku[x][y] = digit;
  FlipMask(x, y, digit_idx);
  // 递归搜索下一个空格
  Backtrack(empty_cells-1, current_score+CalculateScore(x, y, digit));
  FlipMask(x, y, digit_idx);
  sudoku[x][y] = 0;
 }
}
int main() {
 Initialize();
 int empty_cells = 0;
 int initial_score = 0;
 for (int i = 0; i < kSudokuSize;++i) {
  for (int j = 0; j < kSudokuSize;++j) {
   int t;
   cin > > t;
   sudoku[i][j] = t;
   if (t != 0) {
    int digit_idx = t-1;
    FlipMask(i, j, digit_idx);
    initial_score+= CalculateScore(i, j, t);
   } else {
    empty_cells++;
   }
  }
 }
 Backtrack(empty_cells, initial_score);
 cout < < max_total_score < < endl;
 return 0;
}