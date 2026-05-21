#include <iostream>
#include <vector>
#include <string>
using namespace std;
using Grid = vector<vector<int>>;

// 初始数独盘面
const int initialGrid[9][9] = {
    {5, 3, 0, 0, 7, 0, 0, 0, 0},
    {6, 0, 0, 1, 9, 5, 0, 0, 0},
    {0, 9, 8, 0, 0, 0, 0, 6, 0},
    {8, 0, 0, 0, 6, 0, 0, 0, 3},
    {4, 0, 0, 8, 0, 3, 0, 0, 1},
    {7, 0, 0, 0, 2, 0, 0, 0, 6},
    {0, 6, 0, 0, 0, 0, 2, 8, 0},
    {0, 0, 0, 4, 1, 9, 0, 0, 5},
    {0, 0, 0, 0, 8, 0, 0, 7, 9}
};

bool isValid(const Grid& grid) {
    for (int i = 0; i < 9; ++i) {
        bool used[10] = {false};
        for (int j = 0; j < 9; ++j) {
            int num = grid[i][j];
            if (num < 1 || num > 9 || used[num]) return false;
            used[num] = true;
        }
    }
    for (int j = 0; j < 9; ++j) {
        bool used[10] = {false};
        for (int i = 0; i < 9; ++i) {
            int num = grid[i][j];
            if (used[num]) return false;
            used[num] = true;
        }
    }
    for (int br = 0; br < 9; br += 3) {
        for (int bc = 0; bc < 9; bc += 3) {
            bool used[10] = {false};
            for (int i = 0; i < 3; ++i) {
                for (int j = 0; j < 3; ++j) {
                    int num = grid[br + i][bc + j];
                    if (used[num]) return false;
                    used[num] = true;
                }
            }
        }
    }
    return true;
}

bool checkInitial(const Grid& grid) {
    for (int i = 0; i < 9; ++i) {
        for (int j = 0; j < 9; ++j) {
            if (initialGrid[i][j] != 0 && initialGrid[i][j] != grid[i][j]) {
                return false;
            }
        }
    }
    return true;
}

bool readGrid(Grid& grid) {
    grid.resize(9, vector<int>(9));
    for (int i = 0; i < 9; ++i) {
        string line;
        cin >> line;
        if (line.size() != 9) return false;
        for (int j = 0; j < 9; ++j) {
            char c = line[j];
            if (c < '1' || c > '9') return false;
            grid[i][j] = c - '0';
        }
    }
    return checkInitial(grid) && isValid(grid);
}

int main() {
    Grid grid;
    cout << (readGrid(grid) ? "Yes" : "No") << endl;
    return 0;
}