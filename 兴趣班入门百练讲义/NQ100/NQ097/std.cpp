// NQ097 寻找林克的回忆(2)
#include <iostream>
#include <string>
#include <cstring>
#include <climits>
using namespace std;

const int SUDOKU_SIZE = 9;
const int MAX_MASK = 1 << SUDOKU_SIZE;  // 2^9 = 512，二进制表示数字可用性
const char BLANK_CHAR = '.';

// 行、列、3x3单元格的可用状态：二进制位为1表示对应数字（0-8映射1-9）可用
int row[SUDOKU_SIZE];
int col[SUDOKU_SIZE];
int cell[3][3];

// log2_table[mask] = 最低位1的位置（0-8）
int log2_table[MAX_MASK];
// number_of_ones[mask] = mask中二进制1的个数
int number_of_ones[MAX_MASK];

// 获取二进制数最低位的1对应的数值
inline int lowbit(int x) {
    return x & -x;
}

// 计算二进制数中1的个数
int count_set_bits(int n) {
    int res = 0;
    while (n) {
        n -= lowbit(n);
        res++;
    }
    return res;
}

// 初始化log2映射表：log2_table[2^t] = t（t=0~8）
void build_log2() {
    for (int t = 0; t < SUDOKU_SIZE; ++t) {
        log2_table[1 << t] = t;
    }
}

// 初始化number_of_ones数组：存储每个数的二进制中1的个数
void build_number_of_ones() {
    for (int mask = 0; mask < MAX_MASK; ++mask) {
        number_of_ones[mask] = count_set_bits(mask);
    }
}

// 初始化行、列、单元格的可用状态为全1（所有数字可用）
void init_sudoku() {
    for (int i = 0; i < SUDOKU_SIZE; ++i) {
        row[i] = MAX_MASK - 1;  // 二进制9个1
        col[i] = MAX_MASK - 1;
    }
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            cell[i][j] = MAX_MASK - 1;
        }
    }
}

// 翻转x行y列位置的数字t的可用状态（0-8）
// 1->0表示该数字被占用，0->1表示释放
inline void flip_bits(int x, int y, int t) {
    row[x] ^= 1 << t;
    col[y] ^= 1 << t;
    cell[x / 3][y / 3] ^= 1 << t;
}

// 获取x行y列位置的可用数字集合（二进制表示）
inline int get_available(int x, int y) {
    return row[x] & col[y] & cell[x / 3][y / 3];
}

// 递归求解数独，cnt为剩余空白格数量
bool solve_sudoku(string& str, int cnt) {
    if (cnt == 0) {
        // 找到唯一解，输出结果
        cout << str << endl;
        return true;
    }

    // 选择可选数字最少的格子（MRV启发式，减少搜索分支）
    int min_options = INT_MAX;
    int x = -1, y = -1;
    for (int i = 0; i < SUDOKU_SIZE; ++i) {
        for (int j = 0; j < SUDOKU_SIZE; ++j) {
            if (str[i * SUDOKU_SIZE + j] == BLANK_CHAR) {
                int options = number_of_ones[get_available(i, j)];
                if (options < min_options) {
                    min_options = options;
                    x = i;
                    y = j;
                }
            }
        }
    }

    // 枚举该格子的所有可选数字
    int available = get_available(x, y);
    for (int sk = available; sk; sk -= lowbit(sk)) {
        int t = log2_table[lowbit(sk)];  // 转换为0-8的数字索引

        // 填入数字，更新状态
        flip_bits(x, y, t);
        str[x * SUDOKU_SIZE + y] = '1' + t;  // 转换为1-9的字符

        // 递归搜索剩余空白格
        if (solve_sudoku(str, cnt - 1)) {
            return true;  // 找到解后立即返回，无需继续回溯
        }

        // 回溯，恢复状态
        str[x * SUDOKU_SIZE + y] = BLANK_CHAR;
        flip_bits(x, y, t);
    }

    return false;  // 题目保证有唯一解，此分支不会被触发
}

int main() {
    // 初始化辅助表
    build_log2();
    build_number_of_ones();

    string str;
    while (cin >> str && str != "end") {
        init_sudoku();
        int blank_count = 0;

        // 初始化数独状态：填入已有的数字，统计空白格数量
        for (int i = 0, k = 0; i < SUDOKU_SIZE; ++i) {
            for (int j = 0; j < SUDOKU_SIZE; ++j, ++k) {
                if (str[k] != BLANK_CHAR) {
                    int t = str[k] - '1';  // 转换为0-8的索引
                    flip_bits(i, j, t);  // 标记该数字已被占用
                } else {
                    blank_count++;
                }
            }
        }

        // 求解数独
        solve_sudoku(str, blank_count);
    }

    return 0;
}