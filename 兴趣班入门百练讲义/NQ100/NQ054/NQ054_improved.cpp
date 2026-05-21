#include <iostream>
#include <vector>
#include <cstdlib>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int m, n;
    cin >> m >> n;
    
    if (m <= 0 || n <= 0) return 0;
    
    vector<vector<int>> scores(m, vector<int>(n));
    for (int i = 0; i < m; ++i)
        for (int j = 0; j < n; ++j)
            cin >> scores[i][j];
    
    int max_row = 1, max_col = 1;
    int max_abs_score = abs(scores[0][0]);
    
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            int current_abs = abs(scores[i][j]);
            if (current_abs > max_abs_score) {
                max_abs_score = current_abs;
                max_row = i + 1;
                max_col = j + 1;
            }
        }
    }
    
    cout << max_row << " " << max_col << " " << scores[max_row - 1][max_col - 1] << "\n";
    return 0;
}