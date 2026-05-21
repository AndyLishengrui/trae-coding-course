#include <iostream>
#include <unordered_set>
#include <vector>
using namespace std;

int sumOfUnique(int a[], int size) {
    unordered_set<int> unique_values; // 存储唯一值的集合
    for (int i = 0; i < size; i++)
        unique_values.insert(a[i]); // 插入元素，自动去重
    return unique_values.size(); // 返回唯一值数量
}

int main() {
    int n, size;
    cin >> n >> size; // 读取数组长度和前缀大小
    vector<int> a(n);
    for (int i = 0; i < n; i++)
        cin >> a[i]; // 读取数组元素
    
    int unique_count = sumOfUnique(a.data(), size); // 计算前缀中唯一值数量
    cout << n - size + unique_count << endl; // 输出结果
    
    return 0;
}