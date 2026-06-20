#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<int> nums;
    int x;
    while (cin >> x && x != -1) {
        nums.push_back(x);
    }
    for (int i = nums.size() - 1; i >= 0; i--) {
        cout << nums[i] << endl;
    }
    return 0;
}
