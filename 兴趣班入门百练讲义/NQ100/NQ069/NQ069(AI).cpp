#include <iostream>  // 引入输入输出流库
#include <vector>    // 引入向量库
#include <algorithm> // 引入算法库

using namespace std; // 使用标准命名空间

int main() {
    int N, M;
    cin >> N; // 输入整数N
    
    vector<int> q(N + 1); // 使用向量创建一个动态数组，大小为N+1
    // 循环读入N个整数到向量q中，注意下标从1开始
    for (int i = 1; i <= N; ++i) {
        cin >> q[i];
    }
    
    cin >> M; // 输入需要得到的和M
    
    // 对数组进行排序，以便使用二分查找
    sort(q.begin() + 1, q.begin() + N + 1);
    
    // 循环遍历数组q
    for (int i = 1; i <= N; ++i) {
        // 使用lower_bound查找第一个不小于M-q[i]的元素位置
        auto it = lower_bound(q.begin() + i + 1, q.begin() + N + 1, M - q[i]);
        
        // 检查是否找到了满足条件的数对
        if (it != q.begin() + N + 1 && *it == M - q[i]) {
            // 输出数对，并结束程序
            cout << q[i] << " " << M - q[i];
            return 0;
        }
    }
    
    // 如果没有找到满足条件的数对，输出"No"
    cout << "No";
    return 0;
}