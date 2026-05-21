#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;
const int MAXN = 1007;
int a[MAXN];
int main() {
    int q;
    cin >> q;
    while (q--) {
        vector<int> diffs;
        int n, k;
        cin >> n >> k;
        for (int i = 0; i < n; ++i) {
            cin >> a[i];
        }
        for (int i = 0; i < n-1; ++i) {
            for (int j = i+1; j < n; ++j) {
                int diff = abs(a[i] - a[j]);
                diffs.push_back(diff);  // 计算所有可能的差
            }
        }
        sort(diffs.begin(), diffs.end(), greater<int>());  // 降序排序
        auto last = unique(diffs.begin(), diffs.end());
        diffs.erase(last, diffs.end());  // 去重
        if (k <= diffs.size()) {
            cout << diffs[k-1] << endl;  // 输出第K大的差
        } else {
            cout << "Invalid k value!" << endl;
        }
    }
    return 0;
}