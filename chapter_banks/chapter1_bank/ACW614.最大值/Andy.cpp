#include <iostream>
#include <algorithm>
using namespace std;

/**
 * NQ1-14: 最大值
 * 输入三个整数，输出其中的最大值。
 * 时间: O(1) | 空间: O(1)
 */
int main() {
    int a, b, c;
    cin >> a >> b >> c;
    // max({...}) 是 C++11 的初始化列表用法
    cout << max({a, b, c}) << endl;
    return 0;
}
