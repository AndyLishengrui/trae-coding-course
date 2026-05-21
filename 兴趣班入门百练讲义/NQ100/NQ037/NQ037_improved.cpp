// NQ037 按绝对值排序
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;
// 按绝对值从大到小排序
bool abs_greater(int a, int b) {return abs(a) > abs(b); }
int main() {
    int n; cin >> n;
    while (n--) {
        int m;cin >> m;
        vector<int> nums;
        nums.reserve(m);
        for (int i = 0; i < m; ++i) {
            int num;cin >> num;
            nums.push_back(num);
        }
        sort(nums.begin(), nums.end(), abs_greater);
        if (!nums.empty()) {
            cout << nums[0];
            for (size_t i = 1; i < nums.size(); ++i)
                cout << " " << nums[i];
        }
        cout << endl;
    }
    return 0;
}