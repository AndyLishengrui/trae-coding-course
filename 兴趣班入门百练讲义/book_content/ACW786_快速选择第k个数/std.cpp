#include <iostream>
#include <vector>
#include <algorithm>

/**
 * @brief 快速选择算法实现，寻找数组 a[l...r] 中的第 k 小的元素。
 * @param a 待排序数组的引用
 * @param l 数组左边界
 * @param r 数组右边界
 * @param k 目标元素的排名 (1-indexed)
 * @return 第 k 小的元素的值
 */
int quick_select(std::vector<int>& a, int l, int r, int k) {
    // 如果子数组只剩下一个元素，则直接返回该元素（这是递归终止条件）
    if (l >= r) {
        return a[l];
    }

    // 1. 选择基准值 (Pivot)
    // 使用三位指针法进行分区操作，选取中间元素作为基准，避免极端情况下的O(N^2)复杂度。
    int pivot_value = a[(l + r) / 2];

    // 2. 初始化分区指针
    // i 负责向右移动，寻找大于或等于 pivot 的元素。
    // j 负责向左移动，寻找小于或等于 pivot 的元素。
    int i = l - 1;
    int j = r + 1;

    // 3. 执行分区操作
    while (i < j) {
        // 找到第一个大于或等于 pivot_value 的元素
        do { i++; } while (a[i] < pivot_value);
        // 找到第一个小于或等于 pivot_value 的元素
        do { j--; } while (a[j] > pivot_value);

        // 如果指针没有交叉，则交换元素
        if (i < j) {
            std::swap(a[i], a[j]);
        }
    }

    // 经过循环，j 指向的是左侧分区 a[l...j] 的最右端。
    // 该分区包含了所有小于或等于 pivot_value 的元素。
    
    // 计算左侧分区的大小 S
    // 左侧分区 a[l...j] 的元素个数为 j - l + 1
    int left_segment_size = j - l + 1;

    // 4. 递归选择
    if (k <= left_segment_size) {
        // Case 1: k 在左侧分区 (包含基准值)。
        // 目标元素仍然是左侧分区 a[l...j] 中的第 k 小的元素。
        return quick_select(a, l, j, k);
    } else {
        // Case 2: k 在右侧分区 a[j+1...r] 中。
        // 我们已经排除了左侧的 left_segment_size 个元素，因此在右侧分区中，
        // 我们需要寻找第 (k - left_segment_size) 小的元素。
        return quick_select(a, j + 1, r, k - left_segment_size);
    }
}

int main() {
    // 优化输入输出速度
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int n, k;
    if (!(std::cin >> n >> k)) {
        return 0;
    }

    // 读取数列
    std::vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> a[i];
    }

    // 调用快速选择算法。由于 k 是 1-indexed，直接传入 k。
    int result = quick_select(a, 0, n - 1, k);

    std::cout << result << "\n";

    return 0;
}
