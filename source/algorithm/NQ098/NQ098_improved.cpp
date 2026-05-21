#include <iostream>
#include <climits>
using namespace std;

const int N = 9;
const int MAXN = 1 << N;  // 512

int ones[MAXN], LOG2[MAXN];
int row[N], col[N], cell[3][3];
int sudoku[N][N];
int max_score = -1;

inline int lowbit(int x) { return x & -x; }

void init() {
    // 初始化LOG2和ones数组
    for (int i = 0; i < N; ++i) LOG2[1 << i] = i;
    for (int i = 0; i < MAXN; ++i) {
        ones[i] = 0;
        for (int j = i; j; j -= lowbit(j)) ones[i]++;
    }
    // 初始化状态数组
    for (int i = 0; i < N; ++i) row[i] = col[i] = MAXN - 1;
    for (int i = 0; i < 3; ++i) for (int j = 0; j < 3; ++j) cell[i][j] = MAXN - 1;
}

inline int get_score(int x, int y, int t) {
    int dist = min(min(x, 8 - x), min(y, 8 - y));
    return (dist + 6) * t;
}

inline int get_avail(int x, int y) {
    return row[x] & col[y] & cell[x/3][y/3];
}

inline void flip(int x, int y, int n) {
    row[x] ^= 1 << n;
    col[y] ^= 1 << n;
    cell[x/3][y/3] ^= 1 << n;
}

void dfs(int left, int score) {
    if (left == 0) {
        if (score > max_score) max_score = score;
        return;
    }
    
    // 找到可选数字最少的格子
    int min_opts = INT_MAX, x = -1, y = -1;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            if (sudoku[i][j] == 0) {
                int opts = ones[get_avail(i, j)];
                if (opts < min_opts) {
                    min_opts = opts;
                    x = i;
                    y = j;
                }
            }
        }
    }
    
    // 尝试填入每个可能的数字
    int avail = get_avail(x, y);
    for (int sk = avail; sk; sk -= lowbit(sk)) {
        int bit = lowbit(sk);
        int num = LOG2[bit];  // 0-8，对应数字1-9
        int val = num + 1;
        
        // 修改状态
        sudoku[x][y] = val;
        flip(x, y, num);
        int new_score = score + get_score(x, y, val);
        
        dfs(left-1, new_score);
        
        // 回溯
        sudoku[x][y] = 0;
        flip(x, y, num);
    }
}

int main() {
    init();
    
    int left = 0, initial_score = 0;
    
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            int t;
            cin >> t;
            sudoku[i][j] = t;
            if (t != 0) {
                int num = t - 1;
                flip(i, j, num);
                initial_score += get_score(i, j, t);
            } else {
                left++;
            }
        }
    }
    
    dfs(left, initial_score);
    cout << max_score << endl;
    
    return 0;
}