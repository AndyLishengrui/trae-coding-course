#include <cmath>
#include <cstring>
#include <iostream>
using namespace std;

// 数独相关常量定义
const int kSudokuSize = 9;
const int kMaxMask = 1 << kSudokuSize;  // 掩码最大值，二进制111111111（512）
const int kInitialMask = kMaxMask - 1;  // 初始掩码，表示所有数字1-9都可用
const int kInvalidScore = -1;           // 无解时的返回值

// 全局变量定义
int count_ones[kMaxMask];               // 存储每个掩码中1的个数（可选数字数量）
int log2_table[kMaxMask];               // 快速查找2^i对应的i值
int row_mask[kSudokuSize];              // 每行的可用数字掩码，1表示数字可用
int col_mask[kSudokuSize];              // 每列的可用数字掩码
int cell_mask[3][3];                    // 每个3x3单元格的可用数字掩码
int sudoku[kSudokuSize][kSudokuSize];   // 数独矩阵，0表示空格
int max_total_score = kInvalidScore;    // 记录最大总分，初始为无解状态

// 获取x的最低位1对应的数值
inline int LowBit(int x) {
    return x & -x;
}

// 计算(x,y)位置填入数字t后的得分
inline int CalculateScore(int x, int y, int t) {
    // 计算离中心的最小曼哈顿距离，距离越近分值越高
    int distance = min(min(x, 8 - x), min(y, 8 - y));
    // 分值规则：中心10分，每外减1分，最外层6分
    return (distance + 6) * t;
}

// 获取(x,y)位置的可用数字掩码
inline int GetAvailableMask(int x, int y) {
    return row_mask[x] & col_mask[y] & cell_mask[x / 3][y / 3];
}

// 翻转(x,y)位置对应数字的掩码状态（标记为已使用或未使用）
inline void FlipMask(int x, int y, int digit_idx) {
    int mask = 1 << digit_idx;
    row_mask[x] ^= mask;
    col_mask[y] ^= mask;
    cell_mask[x / 3][y / 3] ^= mask;
}

// 初始化全局变量：预计算辅助表，初始化掩码为全可用状态
void Initialize() {
    // 预计算log2_table：快速将2^i映射为i
    for (int i = 0; i < kSudokuSize; ++i) {
        log2_table[1 << i] = i;
    }

    // 预计算count_ones：统计每个掩码中1的个数
    for (int i = 0; i < kMaxMask; ++i) {
        count_ones[i] = 0;
        for (int j = i; j != 0; j -= LowBit(j)) {
            count_ones[i]++;
        }
    }

    // 初始化所有掩码为全1（所有数字1-9都可用）
    for (int i = 0; i < kSudokuSize; ++i) {
        row_mask[i] = kInitialMask;
        col_mask[i] = kInitialMask;
        cell_mask[i / 3][i % 3] = kInitialMask;
    }
}

// 回溯搜索数独的最优解（最大总分）
void Backtrack(int empty_cells, int current_score) {
    // 所有空格填充完成，更新最大总分
    if (empty_cells == 0) {
        if (current_score > max_total_score) {
            max_total_score = current_score;
        }
        return;
    }

    // 启发式剪枝：选择可选数字最少的空格优先填充，减少搜索分支
    int min_available = kSudokuSize + 1;
    int x = -1, y = -1;
    for (int i = 0; i < kSudokuSize; ++i) {
        for (int j = 0; j < kSudokuSize; ++j) {
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

    // 遍历当前位置的所有可选数字
    int available_mask = GetAvailableMask(x, y);
    for (int mask = available_mask; mask != 0; mask -= LowBit(mask)) {
        int digit_idx = log2_table[LowBit(mask)];  // 转换为0-8的索引
        int digit = digit_idx + 1;                 // 转换为1-9的实际数字

        // 填充数字并更新状态
        sudoku[x][y] = digit;
        FlipMask(x, y, digit_idx);

        // 递归搜索下一个空格
        Backtrack(empty_cells - 1, current_score + CalculateScore(x, y, digit));

        // 回溯：恢复状态
        FlipMask(x, y, digit_idx);
        sudoku[x][y] = 0;
    }
}

int main() {
    // 初始化辅助表和掩码
    Initialize();

    int empty_cells = 0;
    int initial_score = 0;

    // 读取数独输入
    for (int i = 0; i < kSudokuSize; ++i) {
        for (int j = 0; j < kSudokuSize; ++j) {
            int t;
            cin >> t;
            sudoku[i][j] = t;
            if (t != 0) {
                // 标记已填数字对应的掩码为不可用
                int digit_idx = t - 1;
                FlipMask(i, j, digit_idx);
                // 计算初始已填数字的得分
                initial_score += CalculateScore(i, j, t);
            } else {
                // 统计空格数量
                empty_cells++;
            }
        }
    }

    // 开始回溯搜索最大总分
    Backtrack(empty_cells, initial_score);

    // 输出结果
    cout << max_total_score << endl;

    return 0;
}
