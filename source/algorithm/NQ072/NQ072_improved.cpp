#include <iostream>
#include <vector>
using namespace std;
int N;
vector<int> positions;
bool isSafe(int row, int col) {
    for (int i = 0; i < row; ++i) {
        if (positions[i] == col) return false; // 检查列冲突
        if (abs(positions[i] - col) == abs(row - i)) return false; // 检查对角线冲突
    }
    return true;
}
void dfs(int row) {
    if (row == N) {
        for (int pos : positions) cout << pos;
        cout << endl;
        return;
    }
    for (int col = 1; col <= N; ++col) {
        if (isSafe(row, col)) {
            positions[row] = col;
            dfs(row + 1); // 递归搜索下一行
        }
    }
}
int main() {
    cin >> N;
    positions.resize(N);
    dfs(0);
    return 0;
}
