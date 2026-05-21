#include <iostream>
using namespace std;

int main() {
    int x, candidate, count = 0;
    
    // 摩尔投票算法寻找多数元素
    while (cin >> x) {
        if (count == 0) {
            candidate = x; // 当计数器为0时，设置新的候选元素
            count = 1;
        } else if (candidate == x) {
            count++; // 当前元素与候选元素相同，计数器加1
        } else {
            count--; // 当前元素与候选元素不同，计数器减1
        }
    }
    
    // 输出多数元素
    cout << candidate << endl;
    return 0;
}