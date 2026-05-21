#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int T;
    cin >> T;
    while (T--) {
        int n;
        cin >> n;
        vector<int> nums(n);
        // 读取n个数字
        for (int i = 0; i < n; i++) {
            cin >> nums[i];
        }
        sort(nums.begin(), nums.end()); // 对数组进行排序
        // 输出排序结果，注意最后一个元素后无空格
        for (int i = 0; i < n; i++) {
            if (i > 0) cout << " ";
            cout << nums[i];
        }
        cout << endl;
    }
    return 0;
}