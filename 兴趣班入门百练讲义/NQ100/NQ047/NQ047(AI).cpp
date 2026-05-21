#include <iostream>
#include <unordered_set>
#include <vector>

int SumofUnique(int a[], int size) {
    // 创建一个无序集合用于存储唯一值
    std::unordered_set<int> unique_values;
    // 遍历数组
    for (int i = 0; i < size; ++i) {
        // 将数组中的元素插入到集合中，若元素已存在则不会插入
        unique_values.insert(a[i]);
    }
    // 返回集合中唯一值的个数
    return unique_values.size();
}

int main() {
    int n, size;
    std::cin >> n >> size; // 读取数组的长度和需要计算的前缀大小
    std::vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> a[i]; // 读取数组元素
    }
    int result = SumofUnique(a.data(), size); // 调用函数计算唯一值的数量
    std::cout <<  n-size+result << std::endl; // 输出结果
    return 0;
}