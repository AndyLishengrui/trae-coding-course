#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

// 质数标记数组，p[i]为true表示i是质数
bool p[100];

// 标记数组，used[i]为true表示i已经被使用过
bool used[100];

// 存储当前质数环的元素
int a[100];

// 环的长度
int n;

// 当前测试用例编号
int now = 0;

// 深度优先搜索函数，deep表示当前要填充的位置
void dfs(int deep) {
    // 已经填充了n个元素，并且首尾元素之和是质数
    if (deep == n + 1 && p[a[1] + a[n]]) {
        // 打印当前的质数环
        for (int i = 1; i <= n; i++) {
            cout << a[i];
            if (i != n)
                cout << " ";
        }
        cout << endl;
        return;
    }
    // 尝试填充从2到n的每个数字
    for (int i = 2; i <= n; i++) {
        // 如果i未被使用，且与前一个数字的和是质数
        if (!used[i] && p[a[deep - 1] + i]) {
            // 标记i为已使用
            used[i] = true;
            // 将i加入质数环
            a[deep] = i;
            // 递归填充下一个位置
            dfs(deep + 1);
            // 回溯，标记i为未使用
            used[i] = false;
        }
    }
}

// 初始化质数标记数组
void init() {
    // 初始化p数组为true
    memset(p, true, sizeof(p));
    // 0和1不是质数
    p[0] = p[1] = false;
    // 筛法求质数
    for (int i = 2; i < 100; i++) {
        if (p[i]) {
            for (int j = i * 2; j < 100; j += i) {
                p[j] = false;
            }
        }
    }
}

int main() {
    // 初始化质数标记数组
    init();
    // 读取输入
    while (cin >> n) {
        // 测试用例编号递增
        now++;
        // 输出测试用例编号
        cout << "Case " << now << ":" << endl;
        // 第一个位置固定为1
        a[1] = 1;
        // 标记1为已使用
        used[1] = true;
        // 从第二个位置开始填充
        dfs(2);
        // 标记1为未使用
        used[1] = false;
        // 输出空行
        cout << endl;
    }
    return 0;
}