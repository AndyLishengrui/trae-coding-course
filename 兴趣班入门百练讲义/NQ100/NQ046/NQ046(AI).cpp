#include <iostream>
using namespace std;

int main() {
    double top;
    while (cin >> top && top != 0) { // 读取顶部高度，直到输入为0
        double sum = 0.0; // 初始化砖块高度的累加和为0
        int blockCount = 0; // 初始化砖块数量为0

        // 循环计算砖块累加和，直到累加和达到或超过目标高度
        while (sum < top) {
            blockCount++; // 砖块数量加1
            sum += 1.0 / (2.0 * blockCount); // 计算当前砖块的高度并累加到总和中
        }

        // 输出砖块数量，根据数量决定输出“block”还是“blocks”
        cout << blockCount << (blockCount == 1 ? " block" : " blocks") << endl;
    }
    return 0;
}